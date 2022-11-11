# import mysql.connector
#
# connection = mysql.connector.connect(
#             host='localhost',
#             user= "prasad_pi",
#             passwd= "dasarp_pi",
#             database = "stock_data_log"
#         )
# mycursor = connection.cursor(buffered=True)

import mysql.connector
connection = mysql.connector.connect(
            host='192.168.1.69',
            user= "prasad_pi",
            passwd= "dasarp_pi",
            database = "stock_data_log"
        )
mycursor = connection.cursor(buffered=True)