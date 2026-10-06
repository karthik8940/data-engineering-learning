import pandas as pd

# EXTRACT
df = pd.read_csv("messy_employees.csv")

print("Original data:")
print(df)

# CHECK MISSING VALUES
print("\nMissing values:")
print(df.isnull().sum())

# REMOVE DUPLICATES
df = df.drop_duplicates()

# REMOVE INVALID AGES
df = df[df["age"].isna() | (df["age"] >= 0)]

# FILL MISSING AGE
df["age"] = df["age"].fillna(0)

# FILL MISSING SALARY
df["salary"] = df["salary"].fillna(0)

print("\nCleaned data:")
print(df)

# SAVE CLEAN DATA
df.to_csv("clean_employees.csv", index=False)

print("\nCleaning completed!")