import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://lab_10_qg0a_user:RLFv1qvFiD42BaJ4enaGrPxVYio9Ndna@dpg-d22cn8fgi27c73eqh7sg-a/lab_10_qg0a")
    conn.close()
    return 'db_test working'