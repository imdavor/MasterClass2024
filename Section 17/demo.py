import psycopg2


conn = psycopg2.connect(
    dbname="test", user="postgres", password="admin123", host="localhost", port="5432"
)
print(conn)
