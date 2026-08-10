# ML-Based Network Intrusion Detection System (NIDS) with Threshold Calibration

## 📌 Project Overview
This project aims to develop a practical Network Intrusion Detection System (NIDS) using the **UNSW-NB15 dataset**. Our primary focus is to keep the **False Positive Rate (FPR) below 3%** through ROC Probability Threshold Calibration, ensuring the system is reliable for real-world security operations.

---

## 🚀 Current Status (Baseline Completed)
We have successfully implemented the baseline model.
- **Model:** Random Forest
- **Data Preprocessing:** Categorical encoding (LabelEncoder) and Scaling (StandardScaler) applied.
- **Current Result:** 
  - **FPR:** < 3%
  - **Optimal Threshold:** 0.4771
  - **Detection Rate (TPR):** 87.77%

---

## 🛠️ Environment Setup & Installation

To maintain consistency, all team members must use the following setup:

### 1. Prerequisites
- **Python:** 3.12.x (Recommended for stability)
- **Editor:** VS Code

### 2. Installation Steps
Clone the repository and run the following commands in your terminal:

```bash
# Create a virtual environment
python -m venv venv

# Activate virtual environment (Windows)
.\venv\Scripts\activate

# Install required libraries
pip install pandas numpy scikit-learn matplotlib seaborn xgboost streamlit joblib jupyter ipykernel