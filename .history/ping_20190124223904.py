from multiping import MultiPing
from psycopg2 import Error

import psycopg2
import os
import datetime

address = [
    {"nama": "LOCALHOST", "ip": "127.0.0.1"},
    {"nama": "GOOGLE", "ip": "8.8.8.8"}
]
tgl = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
for add in address:
    try:
        insert_nama = add['nama']
        insert_ip = add['ip']
        mp = MultiPing([add['ip']])
        mp.send()
        responses, no_responses = mp.receive(1)
        if len(responses) > 0:
            connection = psycopg2.connect(
                user="username", password="password", host="127.0.0.1", port="5432", database="dbname")
            cursor = connection.cursor()
            sql = "INSERT INTO ip_pantau (nama_ip, ip_ip, status_ip, tanggal_ip) VALUES (%s, %s, %s, %s)"
            val = (insert_nama, insert_ip, 'NORMAL', tgl)

            cursor.execute(sql, val)

            connection.commit()
            connection.close()
            print(cursor.rowcount, "baris berhasil masuk database.")
            print(" " + insert_nama + " / " + insert_ip +
                  " \n ==================================== \n " + "NETWORK NORMAL " + tgl + "\n")
        else:
            connection = psycopg2.connect(
                user="username", password="password", host="127.0.0.1", port="5432", database="dbname")
            cursor = connection.cursor()
            sql = "INSERT INTO ip_pantau (nama_ip, ip_ip, status_ip, tanggal_ip) VALUES (%s, %s, %s, %s)"
            val = (insert_nama, insert_ip, 'ABNORMAL', tgl)

            cursor.execute(sql, val)

            connection.commit()
            connection.close()
            print(cursor.rowcount, "baris berhasil masuk database.")
            print(" " + insert_nama + " / " + insert_ip +
                  " \n ==================================== \n " + "NETWORK ABNORMAL " + tgl + "\n")
    except:
        print("Error prosessing " + insert_nama)
