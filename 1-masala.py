import psycopg2

try:
    connection = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="quduq",
        host="localhost",
        port="5432"
    )

    cursor = connection.cursor()

    create_table_query = '''
    CREATE TABLE Product (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        price NUMERIC(10, 2) NOT NULL,
        color VARCHAR(50),
        image TEXT
    );
    '''

    cursor.execute(create_table_query)
    connection.commit()

    print("Product table saccesfully created.")

except (Exception, psycopg2.Error) as error:
    print("error", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL bilan aloqa yopildi.")
