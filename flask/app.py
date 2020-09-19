from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello,world!'

@app.route('/todolist')
def todolist():
    return 'to do list here'


# if __name__ =='__name__':
#     app.run(debug=True)