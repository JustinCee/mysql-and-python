import mysql.connector

Hospital = mysql.connector.connect(user='justin', password='@Lifechoices1234', host='127.0.0.1', database='Hospital',
                                   auth_plugin='mysql_native_password')
mycursor = Hospital.cursor()
xy = mycursor.execute('Select * from Logins')
for i in mycursor:
    print(i)
