#Needed for postgres
#import psycopg2 

#Use sqllite
import sqlite3
import pickle

from tools.logging import logger

def get_db():
    #Postgres
    #return psycopg2.connect(host="localhost", dbname="authme" , user="loki", password="4prez")
    return sqlite3.connect("local_data_base")

def get_db_instance():  
    db  = get_db()
    cur  = db.cursor( )

    return db, cur 



if __name__ == "__main__":
    db, cur = get_db_instance()

    cur.execute("select * from users")
    for r in cur.fetchall():
        print(r)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS brain (
            id INTEGER PRIMARY KEY,
            movieID TEXT(255),
            data TEXT
        );
    """)    
    
    db.commit()




