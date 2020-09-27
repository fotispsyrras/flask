import sqlite3
import requests

from random import randint,choice

connection = sqlite3.connect('citizens.sqlite3')
cur = connection.cursor()

cur.execute("""CREATE table citizens (
    id integer primary key autoincrement,
    firstname text,
    lastname text,
    area text,
    discription text  
)""")


connection.commit()
areas=['kriti','thessalia','attiki','makedonia','thraki']


url = 'https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
r = requests.get(url,headers=headers)
text = r.text
individual_words = text.split()
print(r,text,individual_words)




for x in range(1,10000001):
    random_number = randint(1,len(individual_words))
    random_number2 = randint(1, len(individual_words))
    random_number=random_number - 1
    random_number2=random_number2 - 1
    area= choice(areas)
    discription =choice(individual_words).replace("'", '')
    firstname=individual_words[random_number].replace("'", '')
    lastname= individual_words[random_number2].replace("'", '')
    sql = f"INSERT INTO citizens ('firstname', 'lastname', 'area', 'discription') VALUES ('{firstname}','{lastname}','{area}','{discription}')"
    print(x, sql)
    cur.execute(sql)
    connection.commit()