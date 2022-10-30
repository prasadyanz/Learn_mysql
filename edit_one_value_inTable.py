import Database
Database.mycursor.execute("select * from stock_data")
myresult = Database.mycursor.fetchall()
for y in myresult:
    stock_name = str(y[0])
    if stock_name[:3] == "NSE":
        print(stock_name[4:])
        new_stock_name = stock_name[4:]
        sql = "UPDATE STOCK_DATA SET STOCK = %s WHERE stock = %s "
        # print(sql, (new_stock_name,stock_name,))
        Database.mycursor.execute(sql, (new_stock_name,stock_name,))
        Database.db.commit()