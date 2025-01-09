import psycopg2
from contextlib import contextmanager

@contextmanager
def DbConnect():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="quduq",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    try:
        yield conn, cur  
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
    finally:
        cur.close()
        conn.commit()  
        conn.close()

with DbConnect() as (conn, cur):
    cur.execute("SELECT * FROM products;")
    result = cur.fetchall()
    print(result)
