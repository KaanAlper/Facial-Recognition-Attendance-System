import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd

def kaydet():
    empdata = pd.read_csv('C:\\xampp\\mysql\\data\\yoklamasistemi\\StudentDetails.csv')
    try:
        conn = mysql.connect(host='localhost', database='yoklamasistemi', user='root', password='')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("DataBase'e Baglanildi: ", record)
            cursor.execute("CREATE TABLE IF NOT EXISTS ogrenci_data(OgrenciNumara int(255),Isim varchar(255));")
            print("Table Olusturuldu....")
            for i,row in empdata.iterrows():
                sql = "INSERT INTO yoklamasistemi.ogrenci_data (OgrenciNumara,Isim) VALUES (%s,%s);"
                cursor.execute(sql, tuple(row))
                print("Kayit Depolandi")
                conn.commit()
    except Error as e:
                print("MySQL'e Baglanirkan hata oldu -->", e)
