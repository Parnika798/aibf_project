# Bilingual Financial Complaint Intelligence System

## FinTech Software Application with AI

The **Bilingual Financial Complaint Intelligence System** is a FinTech application that uses Artificial Intelligence and Natural Language Processing to automatically classify financial complaints written in **English and Hindi**.

The application is designed to help organize large volumes of financial complaints, automatically assign them to relevant categories, and provide interactive insights into complaint patterns.

The system provides a simple web-based interface through which users can upload complaint data, obtain AI-generated classifications, analyze the results, and download the processed data.

---

# 1. Statement of Need

Financial institutions receive a large number of consumer complaints related to different financial products and services.

Manually reviewing and categorizing every complaint can be time-consuming and may result in inconsistent classification. The problem becomes more challenging when complaints are submitted in multiple languages.

This application addresses this problem by providing an AI-assisted system that can:

- Automatically classify financial complaints
- Process complaints written in both English and Hindi
- Organize large numbers of complaints into meaningful categories
- Provide category-wise complaint insights
- Reduce the amount of manual classification required
- Support faster analysis of financial grievance data

The application demonstrates how AI can be integrated into a practical FinTech workflow rather than requiring users to interact directly with machine learning models or notebooks.

---

# 2. Application Functionality

The application provides the following core functionalities.

## 2.1 Complaint Data Upload

Users can upload financial complaint data in:

- CSV format
- Excel (`.xlsx`) format

The uploaded file must contain a column named:

```text
complaint_text
```

Example:

| complaint_text |
|---|
| I have an issue with my credit card payment |
| मेरे क्रेडिट कार्ड से संबंधित समस्या है |

---

## 2.2 AI-Based Complaint Classification

Once the complaint data is uploaded, the application automatically processes the complaint text using the trained AI classification pipeline.

For every complaint, the system generates a predicted category.

A new column is added to the uploaded dataset:

```text
predicted_category
```

This allows a large collection of complaints to be classified automatically rather than requiring each complaint to be manually categorized.

---

## 2.3 Bilingual Processing

The system is designed for financial complaints written in:

- English
- Hindi

This enables the application to handle multilingual complaint data within the same workflow.

---

## 2.4 Complaint Insights Dashboard

After classification, users can navigate to the **Insights** section of the application.

The dashboard provides:

- Total number of complaints
- Number of complaint categories
- Most frequent complaint category
- Category-wise complaint counts
- Complaint distribution
- Percentage breakdown of categories
- Interactive visualizations

This converts the classification output into information that can be used for analysis and decision-making.

---

## 2.5 Download Classified Data

After the complaints have been classified, users can download the processed dataset.

The downloaded file contains the original complaint information along with the AI-generated:

```text
predicted_category
```

This allows the classification results to be reused for further analysis or reporting.

---

# 3. Technical Functionality

The application consists of the following major components:

```text
User
  │
  ▼
Streamlit Web Interface
  │
  ├── Upload Complaint Data
  │
  ▼
Complaint Text Processing
  │
  ▼
Trained AI Classification Pipeline
  │
  ▼
Predicted Complaint Category
  │
  ├───────────────┐
  ▼               ▼
Insights       Download
Dashboard      Classified Data
```

The trained model is stored in the repository and loaded when the application starts.

```text
model/
├── clf_pipeline1.pkl
└── label_encoder1.pkl
```

Therefore, users do not need to train the model before using the application.

---

# 4. System Architecture

The project follows a simple application-oriented architecture.

### Presentation Layer

The Streamlit interface provides:

- Data upload
- Classification interaction
- Insights dashboard
- Download functionality

### AI / Processing Layer

The trained classification pipeline processes complaint text and generates the predicted complaint category.

### Data Layer

The system works with:

- Uploaded complaint datasets
- Sample bilingual complaint data
- Trained model files
- Label encoding information

### Analytics Layer

The classified data is analyzed to generate:

- Category counts
- Complaint distribution
- Percentages
- Interactive charts

---

# 5. Technology Stack

### Application

- Python
- Streamlit

### Data Processing

- Pandas
- NumPy

### AI / Machine Learning

- Scikit-learn
- Natural Language Processing
- Joblib
- Trained text classification pipeline

### Visualization

- Plotly

### Development

- Git
- GitHub
- Visual Studio Code

---

# 6. AI Component

Artificial Intelligence is the core functionality of the application.

The system uses a pre-trained text classification model to automatically determine the category of a financial complaint.

During development, different machine learning and NLP approaches were investigated to select an effective classification approach. The resulting trained model is integrated into the final application.

The application itself does not require users to understand the underlying algorithms. Users interact with the system through the application interface and receive classification results automatically.

---

# 7. How to Access the Application

There are two ways to execute the project.

## Method 1 — Streamlit Application

The easiest way to use the system is through the deployed Streamlit application.

**[Open the Live Streamlit Application](https://fincomplaint-mfttwa3nnlsntdqchlkzzu.streamlit.app/)**

No local installation is required.

### Steps

1. Open the Streamlit application.
2. Navigate to **Upload Data**.
3. Upload a CSV or Excel file containing the `complaint_text` column.
4. Allow the system to classify the complaints.
5. Open **Insights** to analyze the results.
6. Open **Download** to obtain the classified dataset.

---

# 8. Local Execution Using GitHub and VS Code

The complete project source code is available in this repository.

## Step 1 — Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/Parnika798/aibf_project
```

Navigate to the project:

```bash
cd FinancialComplaintClassification
```

## Step 2 — Open in VS Code

Open the `FinancialComplaintClassification` folder in Visual Studio Code.

## Step 3 — Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

## Step 4 — Start the Application

Run:

```bash
streamlit run app.py
```

The application will open in a web browser.

---

# 9. Input Requirements

The application accepts:

```text
.csv
.xlsx
```

The uploaded file must contain:

```text
complaint_text
```

### Sample Dataset

A sample dataset is provided in:

```text
dataset/sample_bilingual_complaints.csv
```

This file can be used to test the application.

---

# 10. Application Usage

The application consists of three main sections.

## Upload Data

Users upload their financial complaint dataset.

The system validates the uploaded data and applies the trained classification model to the complaint text.

## Insights

The classified complaints are summarized through an interactive dashboard.

Users can view:

- Total complaints
- Category counts
- Top complaint category
- Category distribution
- Percentage distribution
- Interactive charts

## Download

Users can download the processed complaint dataset containing the AI-generated predictions.

---

# 11. Project Structure

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
│
├── config/
│
└── tests/
```

---

# 12. Role of Project Components

| Component | Purpose |
|---|---|
| `app.py` | Main FinTech application |
| `model/` | Stores the trained AI model and label encoder |
| `assets/` | Application styling |
| `dataset/` | Sample complaint data |
| `src/` | Supporting data processing and analysis code |
| `notebooks/` | Model development and experimentation |
| `tests/` | Application testing |
| `docs/` | Project documentation and report |
| `config/` | Configuration files |
| `requirements.txt` | Required Python dependencies |

The **main executable component is `app.py`**. The notebooks and supporting source files document the development of the AI system but are not required for normal application execution.

---

# 13. Usage and Scope

The application can be used for:

- Financial complaint categorization
- Complaint data analysis
- Bilingual complaint processing
- Identifying frequently occurring complaint categories
- Organizing large complaint datasets
- Supporting financial grievance analysis

The current application focuses on complaint classification and analytics.

The same architecture can be extended in the future to support:

- Additional Indian languages
- More financial product categories
- Automated complaint routing
- Priority or severity prediction
- Complaint trend monitoring
- Integration with financial institution grievance-management systems

---

# 14. Impact Overview

The application demonstrates the potential of AI in FinTech for improving the handling of financial complaints.

### Operational Impact

Automated classification can reduce repetitive manual categorization work and help organize complaint data more efficiently.

### Analytical Impact

The insights dashboard provides a quick overview of complaint patterns and category distributions.

### Accessibility

Bilingual support allows complaints in English and Hindi to be processed within the same application.

### Decision Support

Structured complaint categories and analytics can help organizations identify frequently occurring complaint types and understand areas requiring attention.

### Scalability

The application is designed to process uploaded datasets rather than requiring complaints to be entered individually, making the workflow suitable for larger collections of complaint records.

---

# 15. Key Outcome

The project combines:

```text
FinTech Domain
      +
Artificial Intelligence
      +
Bilingual NLP
      +
Interactive Software Application
      +
Data Analytics
```

to provide an end-to-end financial complaint intelligence application.

The final system allows a user to move from:

```text
Raw Complaint Data
        ↓
AI Classification
        ↓
Structured Complaint Categories
        ↓
Interactive Insights
        ↓
Downloadable Results
```

without requiring the user to interact directly with the underlying machine learning development process.

---

# 16. Local Requirements

For local execution:

- Python 3.x
- Git
- Visual Studio Code (recommended)

Install dependencies using:

```bash
pip install -r requirements.txt
```

Then run:

```bash
streamlit run app.py
```

---

# Author

**Parnika Jain**

**Srishti Tripathi**

### Bilingual Financial Complaint Intelligence System

**FinTech AI Application**
