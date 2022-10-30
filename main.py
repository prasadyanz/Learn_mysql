import mysql.connector
import csv

import Database

db = mysql.connector.connect(
    host= "localhost",
    user = "Prasad",
    passwd = "dasarp",
    database="my_stock_data"

)

mycursor = db.cursor()
# mycursor.execute("CREATE DATABASE my_stock_data")


#  stock, name, sector, subsector, product, moat, risk, remarks, Mcap, status

###############################     Create a Table       #########################################
# mycursor.execute("CREATE TABLE STOCK_DATA(stock varchar(20) NOT NULL, name varchar(50) NOT NULL,\
# sector varchar(20) NOT NULL, subsector varchar(30) NOT NULL,product TEXT,\
# moat TEXT,risk TEXT ,remarks TEXT ,\
# mcap int UNSIGNED NOT NULL,status varchar(20) NOT NULL,stockID int PRIMARY KEY AUTO_INCREMENT)")

