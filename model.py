import psycopg2
import json
from random import seed
from random import randint


class Model(object):
    def __init__(self):
        config = json.loads(open("server_config.json", "r").read())
        self.con = psycopg2.connect(database=config["database"],
                                    user=config["user"],
                                    password=config["password"],
                                    host=config["host"],
                                    port=config["port"])
        self.cursor = self.con.cursor()
        print("Database opened successfully")

    def insert_purchase(self, code):
        try:
            self.cursor.execute("INSERT INTO sales (product_code, date) "
                                "VALUES ({}, NOW())".format(code))
            self.con.commit()
            return True
        except Exception:
            return False

    def insert_random_purchases(self, n):
        products = self.get_codes_array()
        seed(1)
        for i in range(0, n, 1):
            self.cursor.execute("INSERT INTO sales (product_code, date) "
                                "VALUES ({}, NOW() - (random() * "
                                "(NOW() + '1 year' - NOW())))".format(products[randint(0, len(products) - 1)]))
        self.con.commit()

    def update_price(self, code, new_price):
        self.cursor.execute("UPDATE products SET price = '{}' WHERE code = {}".format(new_price, code))
        self.con.commit()

    def delete_purchase(self, purchase_id):
        self.cursor.execute("DELETE FROM sales WHERE id = {}".format(purchase_id))
        self.con.commit()

    def search_product(self, search_string):
        self.cursor.execute("SELECT code, description, price, quantity FROM products CROSS JOIN storage "
                            "WHERE code = product_code AND description LIKE '%{}%'".format(search_string))
        tuples_array = self.cursor.fetchall()
        results = []
        for single in tuples_array:
            results.append(single)
        return results

    def get_codes_array(self):
        self.cursor.execute("SELECT code FROM products")
        tuples_array = self.cursor.fetchall()
        codes = []
        for single in tuples_array:
            codes.append(single[0])
        return codes

    # def update_storage(self):
    #     self.cursor.execute("UPDATE storage SET ")

    def clear_tables(self):
        # self.cursor.execute("DELETE FROM storage")
        self.cursor.execute("DELETE FROM sales")
        # self.cursor.execute("DELETE FROM products")
        self.con.commit()
