import mysql.connector
from datetime import datetime



def insert_valor(thing, t, h):
	conn = mysql.connector.connect(user='santi', password='santi',
                              host='127.0.0.1', database="ejercicio2",
                              auth_plugin='mysql_native_password')
	cursor = conn.cursor()
	insert_stmt = ("INSERT INTO valores(service, fecha, temperature, humidity) VALUES (%s, %s, %s, %s)")
	data = (thing, datetime.now(), t,h)
	try:
	   cursor.execute(insert_stmt, data)
	   conn.commit()
	except Exception as e:
	   conn.rollback()
	   print(e)
	conn.close()
	print("Valor inserted..")

def get_all():
	res = []
	try:
		connection = mysql.connector.connect(user='santi', password='santi',
                              host='127.0.0.1', database="ejercicio2",
                              auth_plugin='mysql_native_password')
		sql_select_Query = "select fecha, temperature, humidity from valores"
		cursor = connection.cursor()
		cursor.execute(sql_select_Query)
		records = cursor.fetchall()
		for row in records:
			r = {"fecha":row[0].strftime("%m/%d/%Y, %H:%M:%S"),"temperature": row[1], "humidity":row[2]}
			res.append(r)
	except mysql.connector.Error as e:
		print("Error reading data from MySQL table", e)
	finally:
		if connection.is_connected():
			connection.close()
			cursor.close()
			print("MySQL connection is closed")
	return res