from flask import Flask, request
import mysql.connector

# Main program
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )

app = Flask(__name__)
@app.route('/airport/<code>')
def echo(code):
    sql = f"SELECT ident, name, municipality FROM airport WHERE ident=" + "'" + str(code) + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return '{"ICAO":"' + result[0][0] + '", "Name":"' + result[0][1] + '", "Location":"' + result[0][2] + '"}'

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)