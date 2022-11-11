# import SQL_Connect_PI as SQ
import SQL_Connect_PC as SQ
db = SQ.connection
mycursor = SQ.mycursor



'''     Show all tables in a database   '''
# mycursor.execute("Show tables;")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

'''      Delete a table     '''
# mycursor = db.cursor()
# sql = "DROP TABLE IF EXISTS cams_findata"
# mycursor.execute(sql)


import Database
# table_name = 'STOCK_DATA'
table_name ="SUPREMEIND_findata"
''' get the items in a table '''
Database.mycursor.execute("DESCRIBE "+table_name )
for x in Database.mycursor:
    print(x)

sql = "SELECT * FROM " + table_name
Database.mycursor.execute(sql)
myresult = Database.mycursor.fetchall()
for y in myresult:
    y = list(y)
    print(len(y), y)