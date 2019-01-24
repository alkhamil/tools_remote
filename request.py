import requests
from psycopg2 import Error

import psycopg2
import os
import datetime

ipaddress = [
    {"nama": "FACEBOOK", "ip": "https://www.facebook.com/"},
    {"nama": "TWITTER", "ip": "https://twitter.com/"}
]

tgl = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
for ip in ipaddress:
    try:
        insert_nama = ip['nama']
        insert_ip = ip['ip']
        req = requests.get(ip['ip'])
        if req.status_code == 200:
            connection = psycopg2.connect(
                user="musername", password="password", host="127.0.0.1", port="5432", database="dbname")
            cursor = connection.cursor()
            sql = "INSERT INTO table (field1, field2) VALUES (%s, %s)"
            val = ("NORMAL", tgl)

            cursor.execute(sql, val)

            connection.commit()
            connection.close()
            print(cursor.rowcount, "baris berhasil masuk database.")
        else:
            connection = psycopg2.connect(
                user="username", password="password", host="127.0.0.1", port="5432", database="dbname")
            cursor = connection.cursor()
            sql = "INSERT INTO table (field1, field2) VALUES (%s, %s)"
            val = ("ABNORMAL", tgl)

            cursor.execute(sql, val)

            connection.commit()
            connection.close()
            print(cursor.rowcount, "baris berhasil masuk database.")
    except:
        print("Error prosessing " + insert_nama)
