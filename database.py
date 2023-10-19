import sqlite3
import pandas as pd

def db_connect():
    conn = sqlite3.connect('test_database.sqlite') 
    c = conn.cursor()

    c.execute('''
            CREATE TABLE IF NOT EXISTS COINS
            ([name] TEXT PRIMARY KEY, [price] TEXT)
            ''')
                        
    conn.commit()

def db_insert(rate):
    conn = sqlite3.connect('test_database.sqlite') 
    c = conn.cursor()
    name="Bitcoin" 

    c.execute("INSERT OR REPLACE INTO COINS (name,price) VALUES(?,?)", (name,rate))

    conn.commit()
    conn.close()

def db_show():
    conn = sqlite3.connect('test_database.sqlite') 
    c = conn.cursor()
                    
    c.execute('''
            SELECT
            a.name, 
            a.price
            FROM COINS a
            ''')

    df = pd.DataFrame(c.fetchall(), columns=['name','price'])
