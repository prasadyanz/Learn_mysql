import mysql.connector
import openpyxl
import csv

connection = mysql.connector.connect(
            host= "localhost",
            user= "prasad_pi",
            passwd= "dasarp_pi",
            database = "stock_data_log"
        )
mycursor = connection.cursor(buffered=True)

THIS_FOLDER = "/home/pi/Documents/Database_log_old.csv"
file = open(THIS_FOLDER)
csvreader = csv.reader(file)
rows = []
for row in csvreader:
    rows.append(row)
file.close()

for y in range(0, len(rows)):
    print(rows[y])

