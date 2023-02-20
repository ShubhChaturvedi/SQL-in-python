import sqlite3

connect = sqlite3.connect('data.db')

# connect.execute('''CREATE TABLE CUSTOMER 
#                 (ID INT PRIMARY KEY NOT NULL,
#                  NAME TEXT NOT NULL,
#                  AGE INT NOT NULL);''')


connect.execute('''INSERT INTO CUSTOMER (ID, NAME, AGE) VALUES (1, "SHUBH" , 19)''')

connect.execute('''INSERT INTO CUSTOMER (ID, NAME, AGE) VALUES (2, "TANISHKA" , 17)''')

data = connect.execute('''SELECT * FROM CUSTOMER''')
for row in data:
    print(row)



connect.close()