from flask import Flask, request, render_template
import sqlite3
import json

conn = sqlite3.connect('citizens.sqlite3', check_same_thread=False)

cur = conn.cursor()

# cur.execute("""CREATE table citizens (
#     id int,
#     firsname text,
#     lastname text,
#     area text,
#     descriptions text
#     )""")
# conn.commit()

app = Flask(__name__)

@app.route('/')
def hello():
    return "hi"

# @app.route('/citizen/<id>')
# def citizen(id):
#     id=int(id)
#     # lastname = request.values['lastname'] if 'lastname' in request.values else " "
#     # limit = request.values['limit'] if 'limit' in request.values else 20
#     # offset = request.values['offset'] if 'offset' in request.values else 0
#     cur.execute(f"select * from citizens where id {id} ")
#     return render_template('citizen.html', citizens=cur.fetchall(), )


@app.route('/citizens')
def citizens():
    lastname = request.values['lastname'] if 'lastname' in request.values else ""
    limit = request.values['limit'] if 'limit' in request.values else 20
    offset = request.values['offset'] if 'offset' in request.values else 0
    if lastname == "" :  
        cur.execute(f"select * from citizens limit {limit} offset {offset}")
    else:
        cur.execute(f"select * from citizens where lastname like '{lastname}' limit {limit} offset {offset}")
    return render_template('citizens.html', citizens=cur.fetchall(),lastname=lastname ,  limit=limit, nextpage=int(offset) + int(limit))


if __name__ == '__main__':
  app.run(debug=True)