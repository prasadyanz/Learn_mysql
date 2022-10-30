import Database
for x in Database.get_sectors:
    table_name = "sector_"+x
    sql = "SELECT * FROM " + table_name
    Database.mycursor.execute(sql)
    myresult = Database.mycursor.fetchall()
    for y in myresult:
        y = list(y)
        if y[0] == x or y[0] == "" or y[0] == " ":
            pass
        else:
            sql = "UPDATE STOCK_DATA SET min_PE = 10, nominal_PE = 15, max_PE = 20;"
            print(sql)
            Database.mycursor.execute(sql)
            Database.db.commit()
