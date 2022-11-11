import csv
import Database
mycursor = Database.mycursor
db = Database.db

""" From a csv into a table """
mycursor.execute("CREATE TABLE Current_PF(stock varchar(20) NOT NULL, buy_price float UNSIGNED NOT NULL, qty int UNSIGNED NOT NULL)")

mycursor.execute("DESCRIBE Current_PF")
for x in mycursor:
    print(x)

THIS_FOLDER = r"D:\Finance\PF\PF.csv"
file = open(THIS_FOLDER)
csvreader = csv.reader(file)
rows = []
for row in csvreader:
    rows.append(row)
file.close()

for y in range(0, len(rows)):
    sql = """INSERT INTO Current_PF (stock ,buy_price ,qty ) VALUES (%s,%s,%s)"""
    mycursor.execute(sql, (rows[y][0],rows[y][1],rows[y][2]))
    db.commit()
