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
                user="monitoring", password="imaniprima11", host="127.0.0.1", port="5432", database="monitoring")
            cursor = connection.cursor()
            sql = "INSERT INTO request_pantau (web_request, code_request, status_request, tanggal_request) VALUES (%s, %s, %s, %s)"
            val = (insert_nama, req.status_code, "NORMAL", tgl)

            cursor.execute(sql, val)

            connection.commit()
            connection.close()
            print(cursor.rowcount, "baris berhasil masuk database.")
        else:
            connection = psycopg2.connect(
                user="monitoring", password="imaniprima11", host="127.0.0.1", port="5432", database="monitoring")
            cursor = connection.cursor()
            sql = "INSERT INTO request_pantau (web_request, code_request, status_request, tanggal_request) VALUES (%s, %s, %s, %s)"
            val = (insert_nama, req.status_code, "ABNORMAL", tgl)

            cursor.execute(sql, val)

            connection.commit()
            connection.close()
            print(cursor.rowcount, "baris berhasil masuk database.")
    except:
        print("Error prosessing " + insert_nama)
