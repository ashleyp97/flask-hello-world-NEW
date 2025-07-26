import psycopg
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def db_test():
    conn = psycopg.connect("postgresql://lab_10_qg0a_user:RLFv1qvFiD42BaJ4enaGrPxVYio9Ndna@dpg-d22cn8fgi27c73eqh7sg-a/lab_10_qg0a")
    conn.close()
    return 'db test working'

@app.route('/db_create')
def creating():
    conn = psycopg.connect("postgresql://lab_10_qg0a_user:RLFv1qvFiD42BaJ4enaGrPxVYio9Ndna@dpg-d22cn8fgi27c73eqh7sg-a/lab_10_qg0a")
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

@app.route('/db_insert')
def inserting():
    conn = psycopg.connect("postgresql://lab_10_qg0a_user:RLFv1qvFiD42BaJ4enaGrPxVYio9Ndna@dpg-d22cn8fgi27c73eqh7sg-a/lab_10_qg0a")
    cur = conn.cursor()
    cur.execute('''
                INSERT INTO Basketball (First, Last, City, Name, Number)
                Values
                ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
                ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
                ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
                ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
                ''')
    conn.commit()
    cur.close()
    return "Basketball Table Populated"

@app.route('/db_select')
def selecting():
    conn = psycopg.connect("postgresql://lab_10_qg0a_user:RLFv1qvFiD42BaJ4enaGrPxVYio9Ndna@dpg-d22cn8fgi27c73eqh7sg-a/lab_10_qg0a")
    cur = conn.cursor()
    cur.execute('''
                SELECT * FROM Basketball;
                ''')
    records = cur.fetchall()
    conn.close()
    response_string = ""
    response_string += "<table>"
    for player in records:
        response_string += "<tr>"
        for info in player:
            response_string += "<td>{}</td>".format(info)
        response_string += "</tr>"
    response_string += "</table>"
    return response_string