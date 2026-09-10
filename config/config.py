"""
config.py
---------
Central configuration: file paths and constants used across the app.
Keeping these in one place avoids hard-coded paths scattered through
app.py / predict.py / scripts, and makes the project portable
(e.g. for Docker, where paths may differ).
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_DIR = BASE_DIR / "model"
MODEL_PATH = MODEL_DIR / "clf_pipeline1.pkl"
LABEL_ENCODER_PATH = MODEL_DIR / "label_encoder1.pkl"

DATASET_DIR = BASE_DIR / "dataset"
SAMPLE_DATASET_PATH = DATASET_DIR / "sample_bilingual_complaints.csv"

REQUIRED_INPUT_COLUMN = "complaint_text"
PREDICTED_COLUMN = "predicted_category"

SUPPORTED_UPLOAD_TYPES = ["csv", "xlsx"]
