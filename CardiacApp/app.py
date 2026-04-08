from flask import Flask, render_template, request, send_file
import joblib
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import io

# Step 1: Flask App Setup
app = Flask(__name__)

# Step 2: Load Trained ML Model
model = joblib.load("random_forest_model.pkl")

# Step 3: Home + Prediction Route
@app.route("/", methods=["GET", "POST"])
@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        name = request.form["name"]
        hr = float(request.form["hr"])
        map_val = float(request.form["map"])
        sbp = float(request.form["sbp"])

        features = [[hr, map_val, sbp]]
        prediction = model.predict(features)[0]
        result = "🚨 At Risk of Cardiac Arrest" if prediction == 1 else "✅ No Risk Detected"

        return render_template("index.html", result=result, name=name, hr=hr, map=map_val, sbp=sbp)

    return render_template("index.html", result=None)

# Step 4: Download PDF Report
@app.route("/download", methods=["POST"])
def download():
    name = request.form["name"]
    hr = request.form["hr"]
    map_val = request.form["map"]
    sbp = request.form["sbp"]

    # Predict again (for PDF)
    data = pd.DataFrame([[float(hr), float(map_val), float(sbp)]], columns=["heart_rate", "map", "systolic_bp"])
    prediction = model.predict(data)[0]
    result = "✅ No Risk Detected" if prediction == 0 else "🚨 At Risk of Cardiac Arrest"

    # Create the PDF
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Logo and Header
    p.setFont("Helvetica-Bold", 18)
    p.drawString(50, height - 50, "🏥 VitalCare AI - ICU Report")
    p.line(45, height - 55, 560, height - 55)  # horizontal line

    # Timestamp
    p.setFont("Helvetica", 10)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    p.drawRightString(width - 50, height - 70, f"Generated on: {timestamp}")

    # Patient Information Box
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, height - 110, "Patient Information:")
    p.rect(45, height - 200, 520, 80, stroke=1, fill=0)  # box around vitals

    p.setFont("Helvetica", 11)
    p.drawString(70, height - 130, f"Name: {name}")
    p.drawString(70, height - 150, f"Heart Rate (HR): {hr} bpm")
    p.drawString(70, height - 170, f"Mean Arterial Pressure (MAP): {map_val} mmHg")
    p.drawString(70, height - 190, f"Systolic Blood Pressure (SBP): {sbp} mmHg")

    # Prediction Result
    p.setFont("Helvetica-Bold", 12)
    p.setFillColorRGB(0.2, 0.2, 0.8)
    p.drawString(50, height - 230, "Prediction Result:")
    p.setFillColorRGB(0, 0, 0)
    p.setFont("Helvetica-Bold", 14)
    p.drawString(60, height - 250, result)

    # Footer
    p.setFont("Helvetica-Oblique", 10)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(50, 80, "Doctor Reviewed By: _________________________")
    p.drawString(50, 60, "Note: This report is auto-generated using machine learning models.")

    p.showPage()
    p.save()
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name=f"{name}_Cardiac_Report.pdf")

# Step 5: Run App
if __name__ == "__main__":
    print("🔥 Flask app is starting...")
    # ❌ Remove or comment this line below
    # app.run(debug=True)

    # ✅ Keep only this:
    app.run(host="0.0.0.0", port=5050, debug=True)
