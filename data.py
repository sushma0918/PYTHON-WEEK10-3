import pandas as pd
df = pd.read_csv("C:\\Users\\91798\\PycharmProjects\\.venv\\Lib\\site-packages\\numpy\\_core\\tests\\data\\umath-validation-set-tanh.csv")
df["new_column"] = df[df.columns[0]] * 2
df["cleaned_column"] = df[df.columns[0]].fillna(0)
df = df.dropna()
df = df.drop_duplicates()
df = df.rename(columns={df.columns[0]: "new_name"})
print(df.head())
