import psycopg2


conn = psycopg2.connect(
    dbname="studentdb",
    user="postgres",
    password="admin123",
    host="localhost",
    port="5432",
)
cur = conn.cursor()  # moraš kreirati kursor
cur.execute(
    "CREATE TABLE students(students_id SERIAL PRIMARY KEY, name TEXT, address TEXT, age INT, number TEXT);"
)
print("Table created successfully")
conn.commit()
conn.close()
