import Database
##################################   Alter  colum or row  ############################################################
# mycursor.execute("ALTER TABLE STOCK_DATA MODIFY name TEXT")
# Database.mycursor.execute("ALTER TABLE STOCK_DATA ADD COLUMN why_no TEXT AFTER why_yes")
# Database.db.commit()

# Database.mycursor.execute("UPDATE STOCK_DATA SET why_no = 'fill up' ")
# Database.db.commit()

# mycursor.execute("UPDATE STOCK_DATA SET sector = 'None' WHERE sector = ''")
# db.commit()

"""     Delete rows from a table  """
#
Database.mycursor.execute("DELETE FROM stock_data WHERE stock = 'x' ")
Database.db.commit()

# Database.mycursor.execute("select * from yahoo_fin_table")
# myresult = Database.mycursor.fetchall()
# for y in myresult:
#     stock_name = str(y[0])
#     if stock_name[:3] == "NSE":
#         print(stock_name[4:])
#         sql = "DELETE FROM yahoo_fin_table WHERE stock = %s "
#         print(sql, (stock_name,))
        # Database.mycursor.execute(sql, (stock_name,))
        # Database.db.commit()



'''    Delete full table from DB   '''
# table_name = "APCOTEXIND_findata"
# sql = "DROP TABLE "+table_name
# Database.mycursor.execute(sql)

'''     Add a column to the table       '''
# Database.mycursor.execute("ALTER TABLE yahoo_fin_table ADD Short_Term_Investments int(2) AFTER Long_Term_Debt")

# Database.mycursor.execute("ALTER TABLE yahoo_fin_table DROP Good_Will")