import psycopg2

conn = None

try:
    conn = psycopg2.connect(
        host="localhost",
        database="snake",
        user="postgres",
        password="1845"
    )

    cur = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE
);

    CREATE TABLE IF NOT EXISTS user_score (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        score INTEGER,
        level INTEGER,
        saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
    """

    cur.execute(create_table_query)
    conn.commit()
    print("Table created successfully")

except Exception as e:
    print("Error:", e)

finally:
    if conn:
        cur.close()
        conn.close()
