import pandas as pd
import psycopg

# EXTRACT
df = pd.read_csv("clean_employees.csv")

print("Clean data:")
print(df)

# CONNECT TO POSTGRESQL
connection = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="data_engineering",
    user="postgres",
    password="sama1234"
)

cursor = connection.cursor()

# LOAD DATA INTO POSTGRESQL
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

print("\nClean data loaded into PostgreSQL successfully!")

cursor.close()
connection.close()