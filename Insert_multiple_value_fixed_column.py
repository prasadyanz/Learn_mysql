'''    insert mutiple values to fixed columns     '''
import Database
get_sectors = Database.get_sectors
for x in get_sectors:
    print(x)
# type_list = ["Sensitive","Cyclical","Defensive" ]
sql = "UPDATE STOCK_DATA SET type = 'Sensitive' WHERE sector = 'Engineering'"
print(sql)
Database.mycursor.execute(sql)
Database.db.commit()

# for y in range(0, len(rows)):
#     sql = """INSERT INTO Current_PF (stock ,buy_price ,qty ) VALUES (%s,%s,%s)"""
#     mycursor.execute(sql, (rows[y][0],rows[y][1],rows[y][2]))
#     db.commit()