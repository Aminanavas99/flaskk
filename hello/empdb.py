
import sqlite3
con=sqlite3.connect('emp.db')
con.execute('''create table Employee(id integer primary key autoincrement,
            name varchar(20),
            email varchar(20),
            phone bigint)''')

con.close()


