#!/usr/bin/python

import serial 
import MySQLdb
from datetime import datetime

#establish connection to MySQL (change parameters as it fits your database)
dbConn = MySQLdb.connect("localhost","user","password","DATABASE_NAME") or die ("could not connect to database")

cursor = dbConn.cursor()

device = '/dev/ttyUSB0' #Adjust device name
date = datetime.now().strftime("%Y-%m-%d %H:%M")

try:
  print "Trying...",device 
  arduino = serial.Serial(device, 9600) 
except: 
  print "Failed to connect on",device
 
data = arduino.readline()  #read the data from the arduino
pieces = data.split("\t")  #split the data by the tab
 
# Insert data into database (change names as it fits designed table structure) 
try:
        cursor.execute("INSERT INTO temp (temp_date,temp_humid,temp_temp) VALUES (%s,%s,%s)", (date,pieces[0],pieces[1]))
        dbConn.commit() 
        cursor.execute("INSERT INTO humid (humid_date,humid_humid) VALUES (%s,%s)", (date,pieces[2]))
        dbConn.commit()
        cursor.close()  

except MySQLdb.IntegrityError:
  print "failed to insert data"
finally:
  cursor.close()
