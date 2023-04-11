import mysql.connector
from Product import Product
class Store:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def add_product(self, product):
        sql = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"
        values = (product.name, product.price, product.quantity)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def remove_product(self, product):
        sql = "DELETE FROM products WHERE id = %s"
        values = (product.id,)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def search_product(self, name):
        sql = "SELECT id, name, price, quantity FROM products WHERE name = %s"
        values = (name,)
        self.cursor.execute(sql, values)
        row = self.cursor.fetchone()
        if row:
            return Product(*row)
        else:
            return None

    def display_products(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        if len(rows) == 0:
            print("No products found.")
        else:
            print("ID\tName\tPrice\tQuantity")
            print("--\t----\t-----\t--------")
            for row in rows:
                product = Product(row[1], row[2], row[3],row[0])
                print(product.id, "\t", product.name, "\t", product.price, "\t", product.quantity)
            print("-------------------------------")
    def get_product(self, id):
        query = "SELECT * FROM products WHERE id = %s"
        self.cursor.execute(query, (id,))
        row = self.cursor.fetchone()
        if row is not None:
            return Product(*row)
        else:
            return None