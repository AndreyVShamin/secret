#!/usr/bin/python3
import sqlite3
 
def secret(application):
    conn = sqlite3.connect("/var/.secret.db3")
    cursor = conn.cursor()
    cursor.execute("SELECT secret FROM pass WHERE app LIKE '{}'".format(application))
    sec = cursor.fetchone()[0]
    conn.close()
    return sec

if __name__ == "__main__":
    print (secret("DJANGO01"))
