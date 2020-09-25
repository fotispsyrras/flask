import sqlite3

connection = sqlite3.connect('customers.sqlite3')
# connection = sqlite3.connect(':memory:')
c = connection.cursor()

# c.execute("""CREATE table customers (
#     firstname text,
#     lastname text,
#     balance int
# )""")

# connection.commit()

# c.execute("INSERT INTO customers (firstname, lastname, balance) VALUES ('Bill', 'Saltis', '1000')")
# connection.commit()

c.execute("SELECT * from customers WHERE balance > 2900")

# print(c.fetchall())

for customer in c.fetchall():
    print(f"Ο πελάτης {customer[1]} {customer[0]} χρωστάει {customer[2]}")

