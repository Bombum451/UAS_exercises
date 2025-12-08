import mysql.connector

def getcode(code):
    sql = f"SELECT name, municipality FROM airport WHERE ident=" + str(code)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    return

# Main program
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )

code = input("Enter code ")
getcode(code)