# Banking Complaint Intelligence — Project Report

*CA-2: AI in Banking & Finance*

## 1. Need Analysis / Statement of Need

Banks and FinTech platforms receive a high volume of customer complaints
daily across channels (app, email, call transcripts, forms), often in more
than one language. Manually reading and routing each complaint to the
correct department (e.g. card fraud, loan servicing, account access) is
slow, inconsistent, and doesn't scale with complaint volume.

This creates a need for an **automated, AI-based triage layer** that can:
- Read a complaint's free text and predict which category/department it
  belongs to, without manual tagging.
- Handle complaints in more than one language.
- Process complaints in bulk (not one at a time).
- Give staff a quick, visual summary of what customers are complaining
  about, to spot trends (e.g. a spike in a specific fraud category).

The application addresses this directly: it's a bilingual NLP
classification system, packaged as a batch-upload dashboard, so a bank's
operations team can drop in a day's complaints and immediately see them
categorized and summarized.

## 2. Technical Functionality

**Core AI component**: A supervised text-classification pipeline trained on
a bilingual banking-complaint dataset (~50k samples — see `notebooks/`).
Development went through the following stages, documented in the notebooks:

1. **Dataset construction** (`nlp-project-dataset-building-50k-samples.ipynb`)
   — building/labelling a 50k-sample bilingual complaint dataset.
2. **Baseline modeling** (`50k-samples-baseline-models-with-tf-idf.ipynb`)
   — TF-IDF + classical ML baselines to establish a performance floor.
3. **Fine-tuning** (`Final_NLP_Project_Fine_Tuning.ipynb`) — fine-tuning a
   stronger model on the labelled data.
4. **Ensembling** (`ensemble-model.ipynb`) — combining models to improve
   robustness, before selecting the final pipeline shipped as
   `model/clf_pipeline1.pkl` + `model/label_encoder1.pkl`.

**Application features**:
| Feature | Description |
|---|---|
| Bulk upload | CSV/XLSX upload of complaints with a `complaint_text` column |
| AI classification | Every row is classified via `src/predict.py`'s `ComplaintClassifier` |
| Insights dashboard | KPI cards, bar chart, pie chart, and a percentage breakdown table of predicted categories |
| Export | Download the classified dataset as CSV |
| Reusable library | The same classifier can be called from scripts/tests, not just the UI (`examples/example_usage.py`) |

*(Fill in: final model type, accuracy/F1 on the held-out set, number of
categories, and dataset source — pull these from your notebooks.)*

## 3. Architecture

```
                 ┌───────────────────────┐
                 │   Training pipeline     │
                 │ (notebooks/, offline)   │
                 │ dataset → preprocessing │
                 │ → TF-IDF/fine-tune      │
                 │ → ensemble → export     │
                 └───────────┬─────────────┘
                             │ produces
                             ▼
                 model/clf_pipeline1.pkl
                 model/label_encoder1.pkl
                             │ loaded by
                             ▼
              ┌───────────────────────────┐
              │      src/predict.py         │
              │  ComplaintClassifier         │
              │  (predict / predict_batch /  │
              │   predict_with_confidence)   │
              └─────────────┬─────────────┘
                             │ used by
              ┌──────────────┼───────────────┐
              ▼                              ▼
     src/app.py (Streamlit UI)     examples/, tests/
     upload → classify → chart      direct programmatic use
     → export
```

The design separates **training** (offline, notebooks), **inference**
(`src/predict.py`, a small library), and **presentation** (`src/app.py`).
This means the AI logic isn't locked inside the UI — it can be reused,
tested, or exposed through a different interface later (e.g. an API) with
no changes to the model layer.

## 4. Usage / Scope

**Intended users**: Bank/FinTech support-operations teams who receive
written complaints and need to route them.

**In scope**:
- Text-based complaint classification (bilingual).
- Batch processing via file upload.
- Descriptive analytics on classified complaints.

**Out of scope (possible future extensions)**:
- Real-time streaming ingestion from a live complaint channel.
- Automatic routing/ticket creation in a downstream system.
- Sentiment/urgency scoring as a second model layer.
- Multi-tenant/bank deployment with authentication.

## 5. Impact Overview

- **Efficiency**: Removes manual reading/tagging for bulk complaints —
  turns an hours-long manual sort into a single batch upload.
- **Consistency**: Categories are assigned by a single trained model rather
  than varying by which staff member reviews a complaint.
- **Visibility**: The insights dashboard surfaces category trends
  immediately, which can flag emerging issues (e.g. a surge in a specific
  fraud type) faster than manual aggregation would.
- **Accessibility**: Bilingual support means complaints don't need to be
  translated or pre-filtered by language before processing.

*(Fill in with any measured before/after numbers, e.g. manual triage time
vs. batch processing time, if available.)*

---

## How to Run

See the main [README.md](../README.md) for setup, running the dashboard,
Docker instructions, and running tests.
