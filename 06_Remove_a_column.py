import Database

table_name = "AARTIIND_findata"
column_name = "date"
sql = "ALTER TABLE "+ table_name+ " DROP "+ column_name
Database.mycursor.execute(sql)
