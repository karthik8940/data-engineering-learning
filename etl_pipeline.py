import pandas as pd
import psycopg

# EXTRACT
df = pd.read_csv("employees.csv")

print("CSV data:")
print(df)

# TRANSFORM
df["salary"] = df["salary"].astype(int)

print("\nTransformed data:")
print(df)

# LOAD
connection = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="data_engineering",
    user="postgres",
    password="sama1234"
)

cursor = connection.cursor()

for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO employees
        (employee_id, name, age, department, salary)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            int(row["employee_id"]),
            row["name"],
            int(row["age"]),
            row["department"],
            int(row["salary"])
        )
    )

connection.commit()

print("\nData loaded successfully!")

cursor.close()
connection.close()