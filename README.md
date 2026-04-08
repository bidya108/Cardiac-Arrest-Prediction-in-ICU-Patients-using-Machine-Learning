# Cardiac Arrest Prediction in ICU Patients

## 📌 Overview
This project builds a machine learning-based system to predict the risk of cardiac arrest in ICU patients using clinical data from the MIMIC-IV dataset. The goal is to assist early detection and improve clinical decision-making.

---

## 🚀 Features
- 📊 Uses 40+ clinical features (vital signs, lab values)
- 🤖 Machine Learning Models:
  - Random Forest (Primary Model)
  - Logistic Regression (Baseline)
- 🎯 Optimized for high recall (critical in healthcare)
- 🌐 Flask-based web application for real-time prediction
- 📄 Automated PDF report generation
- ⚡ Instant patient risk prediction

---

## 🧠 Model Performance

### 🔹 Random Forest
- Accuracy: 1.00  
- Precision: 1.00  
- Recall: 1.00  
- F1-Score: 1.00  
- ROC-AUC: 1.00  

### 🔹 Logistic Regression
- Accuracy: 0.99  
- Precision: 0.99  
- Recall: 0.99  
- F1-Score: 0.99  

---

## 📊 Project Visualizations

### 🔹 Confusion Matrix
![Confusion Matrix](images/confusion_matrix.png)

### 🔹 Correlation Heatmap
![Correlation Heatmap](images/correlation_heatmap.png)

### 🔹 Feature Importance
![Feature Importance](images/feature_importance.png)

### 🔹 ROC Curve
![ROC Curve](images/roc_curve.png)

### 🔹 Model Performance Comparison
![Model Performance](images/model_performance_comparison.png)

### 🔹 Heart Rate Analysis
![Heart Rate](images/heart_rate.png)

### 🔹 Systolic Blood Pressure
![Systolic BP](images/systolic_bp.png)

### 🔹 Map Visualization
![Map](images/map.png)

---

## ⚙️ Tech Stack
- Python 🐍  
- Scikit-learn  
- Pandas & NumPy  
- Matplotlib & Seaborn  
- Flask (Web App)  
- ReportLab (PDF Generation)  

---

## 🚀 How to Run

```bash
git clone https://github.com/Sahildas2003/Prediction-Of-Cardiac-Arrest.git
cd Prediction-Of-Cardiac-Arrest
pip install -r requirements.txt
python CardiacApp/app.py
