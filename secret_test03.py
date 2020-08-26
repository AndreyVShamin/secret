#!/usr/bin/python3
import sqlite3
 
conn = sqlite3.connect("/var/.secret.db3")
cursor = conn.cursor()
cursor.execute("SELECT secret FROM pass WHERE app LIKE 'DJANGO01'")
print (cursor.fetchone())

conn.close()