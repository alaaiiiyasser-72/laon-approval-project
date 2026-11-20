# 💳 Loan Approval Prediction Project

An end-to-end **Machine Learning** project for predicting loan approval decisions based on applicant and loan-related data.

The project follows a structured workflow covering exploratory data analysis, configuration management, preprocessing, model training, and pipeline execution.

---

## 📌 Project Overview

This project aims to build a structured machine learning workflow for loan approval prediction.

The codebase is organized into modular components to separate data, exploratory analysis, configuration, preprocessing, model training, and utility functions, making the project easier to maintain and extend.

---

## 🏗️ Project Structure

```text
loan-approval-project/
│
├── Data/
│   └── Loan_approval_data_2025.csv
│
├── Notebooks/
│   ├── eda.ipynb
│   └── notebook.ipynb
│
├── config/
│   └── config.yaml
│
├── src/
│   ├── preprocessing/
│   ├── training/
│   ├── utills/
│   └── xgb
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🔄 Workflow Overview

### 1. Exploratory Data Analysis (EDA)
**Location:** `Notebooks/`

- Explore the dataset and its structure.
- Analyze data distributions and patterns.
- Investigate missing values and feature relationships.
- Identify potential preprocessing requirements.

### 2. Configuration Management
**Location:** `config/config.yaml`

- Manage project configurations.
- Organize dataset paths.
- Configure model and pipeline settings.

### 3. Data Preprocessing & Model Development
**Location:** `src/`

- Prepare and preprocess input features.
- Organize the machine learning training workflow.
- Develop and train machine learning models, including XGBoost.
- Structure reusable components for preprocessing and training.

### 4. Pipeline Execution
**Entry Point:** `main.py`

- Serve as the main entry point for the project.
- Orchestrate the end-to-end machine learning workflow.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/alaiiiyasser-72/laon-approval-project.git
cd laon-approval-project
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Project

```bash
python main.py
```

---

## 🛠️ Tools & Technologies

- **Python** – Project implementation.
- **Pandas** – Data manipulation and processing.
- **Scikit-learn** – Machine learning and preprocessing tools.
- **XGBoost** – Gradient boosting model development.
- **Jupyter Notebook** – Exploratory data analysis and experimentation.
- **YAML** – Configuration management.

---

## 📌 Notes

- Ensure the dataset path in `config/config.yaml` matches the actual dataset location.
- Install the required dependencies before running the pipeline.
- Model evaluation metrics and additional implementation details can be added as the project documentation evolves.

---

## 👩‍💻 Author

**Alaa yasser**

Computer Science Student | Artificial Intelligence

Interested in Machine Learning, Data Analytics, AI Applications, and AI Agents.
