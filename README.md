# Banking Complaint Intelligence — AI-Powered Complaint Classification

An AI/NLP-based FinTech application that automatically classifies bank customer
complaints (bilingual text) into categories, so support teams can triage and
route them faster instead of reading each one manually.

Built for CA-2 (Unit 3 & 4 — AI in Banking & Finance).

## What it does

- **Classify**: A trained NLP text-classification pipeline (TF-IDF baseline +
  fine-tuned model, selected via an ensembling process — see `notebooks/`)
  predicts a category for each complaint, in either of the supported
  languages.
- **Batch process**: Upload a CSV/XLSX of complaints; every row gets an
  AI-predicted category in one pass.
- **Visualize**: Dashboard shows category distribution, top categories, and
  a breakdown table (Plotly charts).
- **Export**: Download the classified data as CSV for downstream use
  (e.g. routing to the right support queue).

## Repository structure

```
.
├── README.md
├── requirements.txt
├── config/
│   └── config.py            # paths & constants
├── src/
│   ├── predict.py           # AI library: model loading + inference (UI-agnostic)
│   ├── app.py                # Streamlit dashboard (uses src/predict.py)
│   ├── preprocessing.py      # text cleaning used before training/inference
│   ├── dataset_analysis_cleaning.py
│   └── eda.py
├── model/
│   ├── clf_pipeline1.pkl     # trained sklearn pipeline
│   └── label_encoder1.pkl
├── dataset/
│   └── sample_bilingual_complaints.csv
├── notebooks/                 # experimentation & model development history
│   ├── nlp-project-dataset-building-50k-samples.ipynb
│   ├── 50k-samples-baseline-models-with-tf-idf.ipynb
│   ├── Final_NLP_Project_Fine_Tuning.ipynb
│   └── ensemble-model.ipynb
├── examples/
│   └── example_usage.py      # using the AI library without the UI
├── tests/
│   └── test_predict.py
├── docs/
│   └── report.md
└── assets/
    └── styles.css
```

## Why the model logic lives in `src/predict.py`

The original app loaded and called the model directly inside the Streamlit
script. It's been extracted into `src/predict.py` as a small, reusable
`ComplaintClassifier` class + convenience functions, so the *same AI logic*
can be called from:
- the dashboard (`src/app.py`)
- a standalone script (`examples/example_usage.py`)
- automated tests (`tests/test_predict.py`)

without duplicating model-loading code anywhere.

## Setup

```bash
pip install -r requirements.txt
```

Place the trained model files in `model/`:
- `model/clf_pipeline1.pkl`
- `model/label_encoder1.pkl`

## Running the dashboard

```bash
streamlit run src/app.py
```

Upload a CSV/XLSX with a `complaint_text` column; the app adds a
`predicted_category` column and lets you view insights or download results.

## Running tests

```bash
pytest tests/
```

## Using the library directly (no UI)

```python
from src.predict import classify

classify("My debit card was charged twice for one transaction")
```

See `examples/example_usage.py` for more.

## Documentation

See [`docs/report.md`](docs/report.md) for the full report: need analysis,
technical functionality, architecture, usage/scope, and impact overview.
