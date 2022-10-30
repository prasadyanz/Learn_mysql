import mysql.connector
''' 
 incase of of new user , do the below in terminal
 
2sudo mysql -u root -p
GRANT ALL PRIVILEGES ON *.* TO 'prasad_pi'@'localhost' WITH GRANT OPTION;
'''

def create_server_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host= "localhost",
            user= "prasad_pi",
            passwd= "dasarp_pi"
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    print("Database created successfully")


connection = create_server_connection()
create_database(connection,"CREATE DATABASE stock_data_log")

