# In src/config.py

from pathlib import Path

# This is the path to your main 'ComplaintClassification' folder
ROOT_DIR = Path(__file__).parent.parent

# This creates a path to your 'data' folder
DATA_DIR = ROOT_DIR / "data"

# You can now define paths to your specific files
RAW_DATA_FILE = DATA_DIR / "consumercomplaints.xlsx"
CLEANED_DATA_FILE = DATA_DIR / "cleaned_complaints.xlsx"

# --- ADD THIS NEW LINE for your translated file ---
TRANSLATED_DATA_FILE = DATA_DIR / "translated_complaints.xlsx" # Use your file's actual name