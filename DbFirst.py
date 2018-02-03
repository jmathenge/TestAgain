import sqlite3 as db

file = "testSQLDB"
con = db.connect(file)
pos = con.cursor()

def createTable():
    pos.execute('CREATE TABLE IF NOT EXISTS equipment(id integer, name text, price integer)')
    con.commit()
    con.close()
    print("Table create fine..")

#createTable()
def addData():
    pos.execute('INSERT INTO equipment values (1,"Arduino", 30)' )
    pos.execute('INSERT INTO equipment values (3,"Rasp Pi", 50)' )
    pos.execute('INSERT INTO equipment values (4,"Laptop", 80)' )
    pos.execute('INSERT INTO equipment values (6,"IBM Pro", 90)' )
    pos.execute('INSERT INTO equipment values(7,"Toshiba", 100)' )
    
    con.commit()

#addData()

def retrieve():
    pos.execute('select * from equipment')
    for row in pos:
       print(row) 
    

retrieve()




