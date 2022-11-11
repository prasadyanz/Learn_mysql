import datetime

import Database

# Returns the current local date
today = datetime.today().isoformat()
# today = (datetime.datetime.now() - datetime.timedelta(days=7)).date()
print(type(today))
print(today)

# table_name = "STOCK_DATA"
# sql = "ALTER TABLE "+table_name+ " ADD (min_PE int , nominal_PE int, max_PE int)"
# Database.mycursor.execute(sql)
# sql = "ALTER TABLE "+ table_name+ " ADD (date DATE)"
# Database.mycursor.execute(sql)

vals = today
print(vals)
# Database.mycursor.execute("select * from stock_data")
# myresult = Database.mycursor.fetchall()
# for y in myresult:
#     stock_name = str(y[0])
#     sql = "UPDATE STOCK_DATA SET date = %s WHERE stock = %s"
#     Database.mycursor.execute(sql, (today, stock_name,))
#     Database.db.commit()
