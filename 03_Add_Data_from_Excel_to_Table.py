import openpyxl
import csv
import SQL_Connect_PI as DB



# Table_Name = "STOCK_DATA"


# THIS_FOLDER = "/home/pi/Documents/Database_log_old.csv"
# file = open(THIS_FOLDER)
# csvreader = csv.reader(file)
# rows = []
# for row in csvreader:
#     rows.append(row)
# file.close()
#
# for y in range(1, len(rows)):
#     sql = """INSERT INTO STOCK_DATA (stock,name,sector,subsector,product,moat,risk,remarks,mcap,status,Watch_list,
#     type,min_PE,nominal_PE,max_PE,why_yes,why_no ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
#     mycursor.execute(sql, (rows[y][0],rows[y][1],rows[y][2],rows[y][3],rows[y][4],rows[y][5]
#                                ,rows[y][6],rows[y][7],rows[y][8],rows[y][9],rows[y][10],rows[y][11],
#                            rows[y][12],rows[y][13],rows[y][14],rows[y][15],rows[y][16]))
#     connection.commit()


#   Check the Table
table_name = "MOAT"
DB.mycursor.execute("SELECT * FROM "+ table_name)
myresult = DB.mycursor.fetchall()
# num_fields = len(mycursor.description)
# field_names = [i[0] for i in mycursor.description]
# print(field_names)
for x in myresult:
    print(x)
