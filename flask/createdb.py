import sqlite3
import requests

from random import randint,choice

connection = sqlite3.connect('fotis.db')
cur = connection.cursor()

# cur.execute("""CREATE table citizens (
#     id integer primary key autoincrement,
#     firstname text,
#     lastname text,
#     area text,
#     discription text  
# )""")


# connection.commit()
areas=['kriti','thessalia','attiki','makedonia','thraki']


url = 'https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain'

r = requests.get(url)
text = r.text
individual_words = text.split()

for x in range(1,10000001):
    random_number = randint(0,len(individual_words))
    random_number2 = randint(0, len(individual_words))
    area= choice(areas)
    discription =choice(individual_words).replace("'", '')
    firstname=individual_words[random_number].replace("'", '')
    lastname= individual_words[random_number2].replace("'", '')
    sql = f"INSERT INTO citizens ('firstname', 'lastname', 'area', 'discription') VALUES ('{firstname}','{lastname}','{area}','{discription}')"
    # print(x, sql)
    cur.execute(sql)
    connection.commit()