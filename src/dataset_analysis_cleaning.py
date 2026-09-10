# dataset_analysis.py

import pandas as pd

# 1. Load dataset
file_path = r"C:\Users\parni\Downloads\ComplaintClassification\consumercomplaints.csv"
df = pd.read_csv(
    r"C:\Users\parni\Downloads\ComplaintClassification\consumercomplaints.csv",
    encoding="latin1",
    on_bad_lines="skip"
)


# 2. View dataset shape
print("Dataset shape:", df.shape)

# 3. Display first 5 rows
print("\nSample rows:")
print(df.head())

# 4. Dataset info (column types, null counts)
print("\nDataset Info:")
print(df.info())

# 5. Check missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# 6. Unique value counts for categorical columns
print("\nUnique values per column:")
for col in ["Product", "Sub-product", "Issue", "Sub-issue"]:
    if col in df.columns:
        print(f"{col}: {df[col].nunique()} unique values")

# 7. Distribution of target variable (Product)
print("\nComplaint distribution by Product:")
print(df["Product"].value_counts())


# Drop irrelevant columns
df_clean = df.drop(columns=[
    'Unnamed: 0',
    'Date received',
    'Sub-product',
    'Issue',
    'Sub-issue'
])

# Rename for clarity
df_clean = df_clean.rename(columns={
    'Consumer complaint narrative': 'complaint_text',
    'Product': 'label'
})

# Drop rows with missing values in key columns
df_clean = df_clean.dropna(subset=['complaint_text', 'label'])

print("Cleaned dataset shape:", df_clean.shape)
print(df_clean)

df_clean.to_csv("cleaned_complaints.csv", index=False)

