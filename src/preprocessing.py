# preprocessing.py

import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK resources (first time only)
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')

# 1. Load cleaned dataset
file_path = r"C:\Users\parni\Downloads\ComplaintClassification\cleaned_complaints.csv"
df = pd.read_csv(file_path)

print("Dataset shape before preprocessing:", df.shape)

# 2. Initialize tools
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# 3. Text cleaning function
def preprocess_text(text):
    if pd.isnull(text):
        return ""
    text = text.lower()  # lowercase
    text = re.sub(r'[^a-z\s]', '', text)  # remove punctuation/numbers
    tokens = nltk.word_tokenize(text)  # tokenize
    tokens = [t for t in tokens if t not in stop_words]  # remove stopwords
    tokens = [lemmatizer.lemmatize(t) for t in tokens]  # lemmatize
    return " ".join(tokens)

# 4. Apply preprocessing
df['cleaned_text'] = df['complaint_text'].apply(preprocess_text)

# 5. Save preprocessed dataset
output_path = r"C:\Users\parni\Downloads\ComplaintClassification\preprocessed_complaints.csv"
df.to_csv(output_path, index=False)

print("Preprocessing complete.")
print("Dataset shape after preprocessing:", df.shape)
print(df[['complaint_text', 'cleaned_text', 'label']].head())


