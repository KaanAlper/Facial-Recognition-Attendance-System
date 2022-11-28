import mysql.connector as mysql
from mysql.connector import Error
import os

def range_char(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))

def setup():
    try:
        conn = mysql.connect(host='localhost', user='root', password='')
        if conn.is_connected():
            print("MySql'e Baglanildi")
            cursor = conn.cursor()
    #---------------------------------------------
            for character in range_char("A", "K"):
                for i in range(9, 13):
                    if(character=='J')or(character=='K'):
                        if(i==11):
                            cursor.execute("CREATE DATABASE "+str(i)+character+";")
                            
                        else:
                            continue
                    else:
                        cursor.execute("CREATE DATABASE "+str(i)+character+";")
                
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

