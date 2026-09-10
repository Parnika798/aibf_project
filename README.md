# Bilingual Financial Complaint Intelligence System

## FinTech Software Application with AI

The **Bilingual Financial Complaint Intelligence System** is a FinTech application that uses **Artificial Intelligence (AI) and Natural Language Processing (NLP)** to automatically classify financial complaints written in **English and Hindi**.

The application helps users process complaint datasets, obtain predicted complaint categories, view category-wise insights, and download the classified results.

---

## Key Features

- **Bilingual Complaint Classification** – Classifies financial complaints written in English and Hindi.
- **CSV / Excel Upload** – Accepts complaint datasets in `.csv` and `.xlsx` formats.
- **AI-Based Prediction** – Automatically assigns a predicted category to each complaint.
- **Insights Dashboard** – Displays complaint counts, category distribution, percentages, and interactive charts.
- **Download Results** – Allows users to download the processed dataset with predicted categories.
- **Batch Processing** – Processes multiple complaints from an uploaded dataset in a single workflow.

---

## Application Workflow

```text
User
  │
  ▼
Streamlit Interface
  │
  ▼
Upload CSV / Excel
  │
  ▼
Complaint Text
  │
  ▼
AI Classification Pipeline
  │
  ▼
Predicted Category
  │
  ├───────────────┐
  ▼               ▼
Insights        Download
Dashboard       Results
```

---

## AI Component

The application uses a **trained text classification pipeline** to predict the category of each financial complaint.

The trained model and label encoder are stored in the `model/` directory:

```text
model/
├── clf_pipeline1.pkl
└── label_encoder1.pkl
```

The model is loaded when the application starts, so **model training is not required during normal application use**.

The final classification model achieved **88.38% accuracy** during evaluation.

---

## Input Format

The uploaded file must contain a column named:

```text
complaint_text
```

Example:

| complaint_text |
|---|
| I have an issue with my credit card payment |
| मेरे क्रेडिट कार्ड से संबंधित समस्या है |

Supported formats:

```text
.csv
.xlsx
```

A sample bilingual dataset is available at:

```text
dataset/sample_bilingual_complaints.csv
```

---

## Application Modules

### 1. Upload Data

Upload a CSV or Excel file containing financial complaints.

### 2. Insights

View:

- Total complaints
- Number of categories
- Most common complaint category
- Category-wise counts
- Percentage distribution
- Interactive visualizations

### 3. Download

Download the processed dataset containing the original complaint information and the generated `predicted_category`.

---

## How to Use

### Option 1 — Live Application

**Streamlit Application:**  
https://fincomplaint-mfttwa3nnlsntdqchlkzzu.streamlit.app/

No local installation is required.

1. Open the application.
2. Select **Upload Data**.
3. Upload a CSV or Excel file containing `complaint_text`.
4. View the predicted categories.
5. Open **Insights** to analyze the results.
6. Use **Download** to save the classified dataset.

---

## Option 2 — Run Locally

### Clone the Repository

```bash
git clone https://github.com/Parnika798/aibf_project
cd aibf_project
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

The application will open in a web browser.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web application interface |
| Pandas | Data processing |
| Scikit-learn | Machine learning |
| NLP | Complaint text processing |
| Joblib | Model loading |
| Plotly | Interactive visualizations |

---

## Project Structure

```text
FinancialComplaintClassification/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── model/
│   ├── clf_pipeline1.pkl
│   └── label_encoder1.pkl
│
├── assets/
│   └── styles.css
│
├── dataset/
│   └── sample_bilingual_complaints.csv
│
├── src/
│   ├── config.py
│   ├── dataset_analysis_cleaning.py
│   ├── eda.py
│   └── preprocessing.py
│
├── notebooks/
│   ├── 50k-samples-baseline-models-with-tf-idf.ipynb
│   ├── Final_NLP_Project_Fine_Tuning.ipynb
│   ├── ensemble-model.ipynb
│   └── nlp-project-dataset-building-50k-samples.ipynb
│
├── docs/
├── config/
└── tests/
```

### Component Roles

- `app.py` – Main Streamlit application
- `model/` – Trained AI model and label encoder
- `dataset/` – Sample complaint data
- `src/` – Supporting data processing and analysis code
- `notebooks/` – Model development and experimentation
- `assets/` – Application styling
- `docs/` – Documentation and report
- `tests/` – Application tests
- `config/` – Configuration files

The **main executable file is `app.py`**. The notebooks and supporting files document the development process and are not required for normal application use.

---

## Scope

The current application focuses on **financial complaint classification and analysis**.

The system can potentially be extended to support:

- Additional languages
- More financial product categories
- Automated complaint routing
- Priority or severity prediction
- Complaint trend monitoring
- Integration with financial grievance-management systems

---

## Impact

The application demonstrates a practical integration of **AI, NLP, data processing, and interactive analytics** within the FinTech domain.

- **88.38% classification accuracy** during model evaluation
- **English and Hindi** complaint processing
- Automated classification reduces repetitive manual categorization
- Interactive analytics enables faster identification of common complaint categories
- Batch processing supports efficient handling of complaint datasets

---

## Authors

**Parnika Jain – 23070126087**  
**Srishti Tripathi – 23070126131**

### Bilingual Financial Complaint Intelligence System
**FinTech AI Application**
