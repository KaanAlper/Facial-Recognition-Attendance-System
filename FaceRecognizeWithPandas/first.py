import mysql.connector as mysql
from mysql.connector import Error
import os

def setup():
    try:
        conn = mysql.connect(host='localhost', user='root', password='')
        if conn.is_connected():
            print("MySql'e Baglanildi")
            cursor = conn.cursor()
    #---------------------------------------------
            try:
                cursor.execute("CREATE DATABASE yoklamasistemi;")
            except:
                print("Database zaten mevcut!!!")
            else:
                print("DATABASE Olusturuldu")

    #---------------------------------------------
            path = "C:\\xampp\\mysql\\data\\yoklamasistemi\\Attendance"

    #---------------------------------------------
            try:
                os.mkdir(path)
            except:
                print("Yoklama Klasoru Zaten Olusturulmus")
            else:
                print("Yoklama Klasoru Olusturuldu")
    #---------------------------------------------
            try:
                os.remove("key.lock")
            except:
                print("Sistem Klidi Zaten Acik")
            else:
                print("Sistem Klidi Acildi")
    #---------------------------------------------

            os.system('cmd /c pip install -r requirements.txt')


    except Error as e:
        print("MySQL'e Baglanirkan hata oldu -->", e)

