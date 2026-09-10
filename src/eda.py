import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    r"C:\Users\parni\Downloads\ComplaintClassification\consumercomplaints.csv",
    encoding="latin1",
    on_bad_lines="skip"
)


# Keep only needed columns
df = df[['Product', 'Consumer complaint narrative']]
df = df.rename(columns={'Consumer complaint narrative': 'complaint_text', 'Product': 'label'})
df = df.dropna()

# Class distribution
print(df['label'].value_counts())

# Bar plot of complaint counts
plt.figure(figsize=(10,6))
sns.countplot(y=df['label'], order=df['label'].value_counts().index)
plt.title("Distribution of Complaints by Product")
plt.show()

# Text length distribution
df['text_length'] = df['complaint_text'].apply(len)
plt.hist(df['text_length'], bins=50)
plt.title("Distribution of Complaint Lengths")
plt.show()
