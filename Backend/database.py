import mysql.connector

def get_connection():
    try:
        connection=mysql.connector.connect(
            user="root",
            password="root",
            database="Project_Product",
            host="localhost"
        )
        cursor =connection.cursor()
        print('connection successful')
        return connection,cursor
    
    except mysql.connector.Error as e:
        print(f'database failed to connect:{e}')
        return None,None