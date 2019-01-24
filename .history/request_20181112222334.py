import requests
from psycopg2 import Error

import psycopg2
import os
import datetime

ipaddress = [
    {"nama": "IMANI.CO.ID", "ip": "https://imaniprima.co.id/"},
    {"nama": "AISSAT.COM", "ip": "https://www.aissat.com/"},
    {"nama": "M2M.ID", "ip": "https://m2m.id/"},
    {"nama": "ADPOINT.ID", "ip": "https://adpoint.id/"},
    {"nama": "DEV.ADPOINT.ID", "ip": "https://adpoint.id/"},
    {"nama": "ORBCOMM.COM", "ip": "https://www.orbcomm.com/"},
    {"nama": "JALADARA.ID", "ip": "http://jaladara.id/#/"},
    {"nama": "JALADARA.COM", "ip": "http://jaladara.com/#/"},
    {"nama": "JALADARA.CO", "ip": "http://jaladara.co/#/"},
    {"nama": "JALADARA.CO.ID", "ip": "http://jaladara.co.id/#/"},
    {"nama": "MONSTRACK.ID", "ip": "http://monstrack.id/"},
    {"nama": "TSR.CO.ID", "ip": "http://tsr.co.id/"},
    {"nama": "ATLAS.CO.ID", "ip": "https://atlas.co.id/"},
    {"nama": "BERITA.MARITIM.ID", "ip": "http://berita.maritim.id/"},
    {"nama": "MARITIMENEWS.ID", "ip": "https://maritimenews.id/"},
    {"nama": "YUSUFMANSUR.COM", "ip": "http://yusufmansur.com/"},
    {"nama": "WHBS.OR.ID", "ip": "http://whbs.or.id/"},
    {"nama": "PRIMASAVER.COM", "ip": "https://primasaver.com/home"}
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
