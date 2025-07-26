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
    return 'db test working'

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgresql://lab_10_qg0a_user:RLFv1qvFiD42BaJ4enaGrPxVYio9Ndna@dpg-d22cn8fgi27c73eqh7sg-a/lab_10_qg0a")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    cur.close()
    return "basketball table created"