import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="quduq",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS products2 (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        description TEXT,
        price NUMERIC(10, 2),
        quantity INT
    );
    """
    cursor.execute(query)
    conn.commit()

def insert_product(name, description, price, quantity):
    query = """
    INSERT INTO products (name, description, price, quantity)
    VALUES (%s, %s, %s, %s);
    """
    cursor.execute(query, (name, description, price, quantity))
    conn.commit()

def select_all_products():
    query = "SELECT * FROM products;"
    cursor.execute(query)
    return cursor.fetchall()

def update_product(product_id, name, description, price, quantity):
    query = """
    UPDATE products
    SET name = %s, description = %s, price = %s, quantity = %s
    WHERE id = %s;
    """
    cursor.execute(query, (name, description, price, quantity, product_id))
    conn.commit()

def delete_product(product_id):
    query = "DELETE FROM products WHERE id = %s;"
    cursor.execute(query, (product_id,))
    conn.commit()

if __name__ == "__main__":

    create_table()

    print("Mahsulot qo'shilmoqda...")
    insert_product("Laptop", "High-performance laptop", 1200.50, 10)
    insert_product("Smartphone", "Latest model smartphone", 800.00, 25)
    
    print("\nBarcha mahsulotlar:")
    products = select_all_products()
    for product in products:
        print(product)

    print("\nMahsulot yangilanmoqda...")
    update_product(1, "Laptop Pro", "Upgraded laptop version", 1500.00, 8)
    
    print("\nYangilangan mahsulotlar:")
    products = select_all_products()
    for product in products:
        print(product)

    print("\nMahsulot o'chirilmoqda...")
    delete_product(2)
    
    print("\nQolgan mahsulotlar:")
    products = select_all_products()
    for product in products:
        print(product)

    
    cursor.close()
    conn.close()
