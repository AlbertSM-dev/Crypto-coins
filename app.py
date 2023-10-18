#!/usr/bin/env python3
import requests
import sqlite3
import pandas as pd
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Crypto.sqlite3'

db = SQLAlchemy(app)

class Crypto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.String(50))

@app.route('/')    
def get_coins():
    response = requests.get("https://api.coincap.io/v2/assets")
    return response.json()["data"]

@app.route('/db') 
def db_connect():
    conn = sqlite3.connect('test_database') 
    c = conn.cursor()

    c.execute('''
            CREATE TABLE IF NOT EXISTS products
            ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT)
            ''')
            
    c.execute('''
            CREATE TABLE IF NOT EXISTS prices
            ([product_id] INTEGER PRIMARY KEY, [price] INTEGER)
            ''')
                        
    conn.commit()
    return "conn"

@app.route('/dbi') 
def db_insert():
    conn = sqlite3.connect('test_database') 
    c = conn.cursor()
                    
    c.execute('''
            INSERT or REPLACE INTO products (product_id, product_name)

                    VALUES
                    (1,'Computers'),
                    (2,'Printer'),
                    (3,'Tablet'),
                    (4,'Desk'),
                    (5,'Chair')
            ''')

    c.execute('''
            INSERT or REPLACE INTO prices (product_id, price)

                    VALUES
                    (1,800),
                    (2,200),
                    (3,300),
                    (4,450),
                    (5,150)
            ''')

    conn.commit()
    db_show()

@app.route('/dbs') 
def db_show():
    conn = sqlite3.connect('test_database') 
    c = conn.cursor()
                    
    c.execute('''
            SELECT
            a.product_name,
            b.price
            FROM products a
            LEFT JOIN prices b ON a.product_id = b.product_id
            ''')

    df = pd.DataFrame(c.fetchall(), columns=['product_name','price'])
    return df.to_string()

if __name__ == "__main__":
    current_price = get_coins()
    #new_entry = Crypto(price=current_price["priceUs"])
    #db.session.add(new_entry)
    #db.session.commit()