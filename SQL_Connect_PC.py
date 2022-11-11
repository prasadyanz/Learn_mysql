import mysql.connector

connection = mysql.connector.connect(
    host= "localhost",
    user = "Prasad",
    passwd = "dasarp",
    database="my_stock_data"

)

mycursor = connection.cursor()