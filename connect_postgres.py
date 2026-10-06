import os
import psycopg

connection = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="data_engineering",
    user="postgres",
    password=os.getenv("POSTGRES_PASSWORD")
)

print("Connected to PostgreSQL successfully!")

connection.close()