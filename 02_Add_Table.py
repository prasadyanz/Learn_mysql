import mysql.connector

def create_server_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host= "localhost",
            user= "prasad_pi",
            passwd= "dasarp_pi",
            database = "stock_data_log"
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection
connection = create_server_connection()
mycursor = connection.cursor()

################################       Create Big Table    ########################################
# stock,name,sector,subsector,product,moat,risk,remarks,mcap,status,Watch_list,\
# type,min_PE,nominal_PE,max_PE,why_yes,why_no

# mycursor.execute("CREATE TABLE STOCK_DATA(stock varchar(20) NOT NULL, name TEXT NOT NULL, sector varchar(20) NOT NULL,\
#  subsector varchar(30) NOT NULL,product TEXT,moat TEXT,risk TEXT ,remarks TEXT ,\
# mcap int UNSIGNED NOT NULL,status varchar(20) NOT NULL, Watch_list varchar(5),\
# type varchar(20), min_PE int, nominal_PE int, max_PE int, why_yes text, why_no text, stockID int PRIMARY KEY AUTO_INCREMENT)")

''' get the items in a table '''
table_name = 'MOAT'
mycursor.execute("DESCRIBE "+table_name )
for x in mycursor:
    print(x)

''' Create a table with column from given list '''
moat_list = ['High Govt Intervention', 'High Raw matrial import', 'fluctuating raw matrial cost',
             'Low Switching cost', 'High Competition', 'Cyclical', 'Too Diversified',
             'Unwanted Diversification', 'Change in Industrial Landscap', 'No Pricing power',
             'Expect Technology Changes', 'Others', 'To Check', 'Low Volume/ il-liquid']

# mycursor.execute("CREATE TABLE RISK (risk varchar(30) NOT NULL)")

for x in moat_list:
    vals = x
    sql = "INSERT INTO RISK ({}) VALUES (%s) ".format('risk')
    print(sql, (vals,))
    mycursor.execute(sql, (vals,))
    connection.commit()