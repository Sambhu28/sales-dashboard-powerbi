import pandas as pd

#data lode

df = pd.read_csv("samplesuperstore.csv")
print(df.shape)

# chack for missind value

print(df.isnull().sum())

# If you find missing values, fix them like this:
#
#df = df.dropna()  # removes rows with missing values

#fix data

# Fix Order Date
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month"] = df["Order Date"].dt.month
df["Year"] = df["Order Date"].dt.year
df["Month Name"] = df["Order Date"].dt.strftime("%B")

# Fix Ship Date also
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Create Profit Margin column
df["Profit Margin"] = (df["Profit"] / df["Sales"]) * 100
df["Profit Margin"] = df["Profit Margin"].round(2)

# Save cleaned file
df.to_csv("cleaned_superstore.csv", index=False)

print("File saved successfully!")