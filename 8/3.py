import mysql.connector
from geopy.distance import geodesic

def loc(code1, code2):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident=" + str(code1) + " LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    
    if cursor.rowcount >0 :
        for row in result:
            lat1 = row[0]
            lon1 = row[1]

    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident=" + str(code2) + " LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    
    if cursor.rowcount >0 :
        for row in result:
            lat2 = row[0]
            lon2 = row[1]
    
    coord1 = (lat1, lon1)
    coord2 = (lat2, lon2)
    
    print(geodesic(coord1, coord2).km)

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

code1 = input("Enter code1 ")
code2 = input("Enter code2 ")
loc(code1, code2)