from multiping import MultiPing
from psycopg2 import Error

import psycopg2
import os
import datetime

address = [
    {"nama": "REMALA STR", "ip": "101.255.54.22"},
    {"nama": "PRESENSI", "ip": "101.255.54.22"},
    {"nama": "FIRSTMEDIA STR", "ip": "a11.now.im"},
    {"nama": "VM DB 7.5", "ip": "192.168.7.5"},
    {"nama": "WINSERVER 7.2", "ip": "192.168.7.2"},
    {"nama": "ESX5.5 7.3", "ip": "192.168.7.3"},
    {"nama": "HADOOP-1", "ip": "192.168.7.91"},
    {"nama": "HADOOP-2", "ip": "192.168.7.92"},
    {"nama": "HADOOP-3", "ip": "192.168.7.93"},
    {"nama": "HADOOP-4", "ip": "192.168.7.94"},
    {"nama": "INDIHOME WS", "ip": "k44.qc.to"},
    {"nama": "ROUTER LA", "ip": "183.91.67.214"},
    {"nama": "ROUTER LA111", "ip": "192.168.1.1"},
    {"nama": "ROUTER LA212", "ip": "192.168.1.2"},
    {"nama": "VM WAKALAH 1.20", "ip": "192.168.1.20"},
    {"nama": "VM HOSTING2 1.238", "ip": "192.168.1.238"},
    {"nama": "VMMX JALADAR 1.237", "ip": "192.168.1.237"},
    {"nama": "VM NS1-NX 1.235", "ip": "192.168.1.235"},
    {"nama": "VM SMARTMEDIA 1.211", "ip": "192.168.1.211"},
    {"nama": "VM WHBS 1.139", "ip": "192.168.1.139"},
    {"nama": "VM HOSTING1 1.81", "ip": "192.168.1.81"},
    {"nama": "VM LCT 1.29", "ip": "192.168.1.29"},
    {"nama": "VM YMCOM 1.36", "ip": "192.168.1.36"},
    {"nama": "VM IPDBR 1.42", "ip": "192.168.1.42"},
    {"nama": "VM MONSTRACK 1.52", "ip": "192.168.1.52"},
    {"nama": "VM Q4000 1.51", "ip": "192.168.1.51"},
    {"nama": "VM JALADARA 1.61", "ip": "192.168.1.61"},
    {"nama": "VM AMS 1.32", "ip": "192.168.1.32"},
    {"nama": "VM YMDB 1.35", "ip": "192.168.1.35"},
    {"nama": "VM ERC 1.25", "ip": "192.168.1.25"},
    {"nama": "VM SMARTMEDIA 1.28", "ip": "192.168.1.28"},
    {"nama": "VM MULE 1.21", "ip": "192.168.1.21"},
    {"nama": "VM MIP 1.22", "ip": "192.168.1.22"},
    {"nama": "VM ERC 1.24", "ip": "192.168.1.24"},
    {"nama": "GOOGLE CLOUD ADDPOINT", "ip": "35.240.227.30"},
    {"nama": "DAXA SERVER", "ip": "111.221.43.144"},
    {"nama": "GEOSERVER", "ip": "192.168.7.8"},
    {"nama": "PRIMASAVER", "ip": "202.152.24.149"},
    {"nama": "VPN PELINDO", "ip": "10.0.127.45"},
    {"nama": "VPN KAI", "ip": "10.50.1.1"},
    {"nama": "VASA PROD 96", "ip": "10.0.127.96"},
    {"nama": "VASA PROD 95", "ip": "10.0.127.95"},
    {"nama": "VASA PROD 98", "ip": "10.0.127.98"},
    {"nama": "VASA PROD 99", "ip": "10.0.127.99"},
    {"nama": "VASA DEV 12", "ip": "10.0.130.12"},
    {"nama": "VASA DEV 19", "ip": "10.0.130.19"},
    {"nama": "KATRACK KAI", "ip": "10.6.0.220"},
    {"nama": "KATRACKING ALPHA", "ip": "10.6.0.130"},
    {"nama": "LCT WEBSERVICES", "ip": "172.16.8.66"}
]
tgl = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
for add in address:
    try:
        insert_nama = add['nama']
        insert_ip   = add['ip']
        mp          = MultiPing([add['ip']])
        mp.send()
        responses, no_responses = mp.receive(1)
        if len(responses) > 0:
            connection = psycopg2.connect(
                user="monitoring", password="imaniprima11", host="127.0.0.1", port="5432", database="monitoring")
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
                user="monitoring", password="imaniprima11", host="127.0.0.1", port="5432", database="monitoring")
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
        print("Error prosessing " + insert_nama )
    
