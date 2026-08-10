# ML-Based Network Intrusion Detection System (NIDS) with Threshold Calibration

## 📌 Project Overview
This project aims to develop a practical Network Intrusion Detection System (NIDS) using the **UNSW-NB15 dataset**. Our primary focus is to keep the **False Positive Rate (FPR) below 3%** through ROC Probability Threshold Calibration, ensuring the system is reliable for real-world security operations.

This project addresses a **public safety / societal issue** — unreliable intrusion detection systems that generate too many false alarms are impractical for real-world security operations, so this project also serves as a comparative study of multiple ML algorithms for this problem.

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

## 🤖 Models Used (minimum 3, per assignment requirement)

| # | Model | Purpose |
|---|---|---|
| 1 | Random Forest | Primary/baseline model |
| 2 | XGBoost | Stronger tree-based ensemble, compared against Random Forest |
| 3 | Logistic Regression | Simple linear baseline, shows performance gap vs. ensemble models |

All three models are evaluated and compared using **Accuracy, Precision, Recall, F1-score, and FPR** — FPR is prioritized since minimizing false alarms is the core requirement.

---

## 📁 Project Structure

```
nids_project/
├── data/           <- dataset CSV files go here (not tracked by git)
├── notebooks/      <- Jupyter notebooks for EDA, preprocessing, training, evaluation
├── models/         <- saved trained models, scaler, threshold (.pkl files)
├── app/            <- Streamlit demo app
└── README.md
```

---

## 📊 Dataset

This project uses the **UNSW-NB15** dataset.

- **Download from Kaggle:** search `UNSW_NB15` by Mr Wells David, or use this link: `<paste your Kaggle dataset link here>`
- **Files needed** (place these inside the `data/` folder):
  - `UNSW_NB15_training-set.csv`
  - `UNSW_NB15_testing-set.csv`
  - `UNSW-NB15_features.csv` (feature name/description reference)
- Dataset files are **not** committed to this repository (see `.gitignore`) due to size — every team member must download them individually.

### Citation
This dataset is for academic use. Please cite the original authors in the report's References section:
> Moustafa, Nour, and Jill Slay. "UNSW-NB15: a comprehensive data set for network intrusion detection systems (UNSW-NB15 network data set)." Military Communications and Information Systems Conference (MilCIS), 2015. IEEE, 2015.

---

## 🛠️ Environment Setup & Installation

To maintain consistency, all team members must use the following setup:

### 1. Prerequisites
- **Python:** 3.14.x
- **Editor:** VS Code (with Python and Jupyter extensions)

### 2. Installation Steps

Clone the repository and run the following commands in your terminal:

```bash
# Clone the repo
git clone <repo-url>
cd nids_project

# Create a virtual environment
python -m venv venv

# Activate virtual environment (Windows)
.\venv\Scripts\activate
# Activate virtual environment (Mac/Linux)
source venv/bin/activate

# Install required libraries
pip install -r requirements.txt
```

### 3. Download the dataset
Download the 3 required CSV files (see **Dataset** section above) and place them inside the `data/` folder.

### 4. Select the correct kernel in VS Code
Open any notebook in `notebooks/`, then select the `venv` Python interpreter as the kernel (`Ctrl+Shift+P` → `Python: Select Interpreter`).

---

## ▶️ Usage

### Run the notebooks
Open `notebooks/` in VS Code and run cells in order: data exploration → preprocessing → feature selection → model training (all 3 models) → threshold calibration → evaluation.

### Run the demo app
```bash
streamlit run app/app.py
```

---

## 👥 Team & Task Division

| Member | Responsibility |
|---|---|
| Member 1 | Data preprocessing & EDA |
| Member 2 | Feature selection & training all 3 models (Random Forest, XGBoost, Logistic Regression) |
| Member 3 | Threshold calibration (ROC), evaluation (confusion matrix, per-category recall, k-fold check), model comparison |
| Member 4 | Streamlit demo app & presentation slides |

Report sections (Literature Review, Sustainability & Societal Impact, Ethical Considerations, etc.) should be divided among all members alongside the coding tasks — see **Assignment Requirements** below.

---

## 📈 Evaluation Metrics
We prioritize **Precision, Recall, and FPR** over plain Accuracy, since minimizing false alarms (FPR < 3%) is the core requirement of this project.

---

## 📋 Assignment Requirements Checklist

**Part 1 — Coding Implementation**
- [ ] Dataset collected & preprocessed
- [ ] At least 3 ML algorithms implemented (Random Forest, XGBoost, Logistic Regression)
- [ ] Models evaluated & compared with appropriate metrics
- [ ] Code well-commented and organized

**Part 2 — Report**
- [ ] Introduction
- [ ] Literature Review
- [ ] Data Analysis (dataset description, preprocessing, EDA)
- [ ] Methodology (algorithms used, rationale, parameter tuning)
- [ ] Result Analysis (model comparison)
- [ ] Sustainability & Societal Impact Analysis
- [ ] Ethical Considerations (privacy, bias, fairness, transparency)
- [ ] Conclusion & future work
- [ ] References

**Part 3 — Presentation**
- [ ] Slides: problem intro, data/methodology, key results, conclusion
- [ ] Ready for Q&A discussion

**Deadlines**
- Topic approval: by 3rd Lab
- Final submission (code + report + presentation): before 7th Lab