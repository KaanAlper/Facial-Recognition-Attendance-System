import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd
import datetime
import time

def kaydet():
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    sqldate=datetime.datetime.fromtimestamp(ts).strftime('%d_%m_%Y')
    empdata = pd.read_csv('C:\\xampp\\mysql\\data\\yoklamasistemi\\Attendance\\Attendance_'+date+'.csv')

    try:
        conn = mysql.connect(host='localhost', database='yoklamasistemi', user='root', password='')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("DataBase'e Baglanildi: ", record)
            cursor.execute("CREATE TABLE IF NOT EXISTS yoklama_bilgileri_"+sqldate+"(OgrenciNumara int(255),Isim varchar(255),Tarih varchar(255),Saat varchar(255));")
            print("Table Olusturuldu....")
            for i,row in empdata.iterrows():
                sql = "INSERT INTO yoklamasistemi.yoklama_bilgileri_"+sqldate+"(OgrenciNumara,Isim,Tarih,Saat) VALUES (%s,%s,%s,%s);"
                cursor.execute(sql, tuple(row))
                print("Kayit Depolandi")
                conn.commit()
    except Error as e:
                print("MySQL'e Baglanirkan hata oldu -->", e)
