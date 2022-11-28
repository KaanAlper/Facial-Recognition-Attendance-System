import mysql.connector as mysql
from mysql.connector import Error
import os
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False
    
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
               
            cursor.execute("CREATE DATABASE admin;")
            cursor.execute("USE admin;")
            cursor.execute("CREATE TABLE IF NOT EXISTS giris(kullanici_adi varchar(15),sifre varchar(15));")
            

            kullanici_adi=input("Bir Kullanici Adi Olusturunuz --> ")
            sifre=input("Bir Sifre Olusturuldu --> ")
           
            sql = "INSERT INTO giris (kullanici_adi,sifre) VALUES (%s,%s);"
            row = [kullanici_adi, sifre]
            cursor.execute(sql, tuple(row))
            print("Giris Bilgileri Depolandi")
            conn.commit()
        #---------------------------------------------
                
            os.remove("key.lock")
            print("Sistem Klidi Acildi")
        #---------------------------------------------
            os.system('cmd /c pip install -r requirements.txt')


    except Error as e:
        print("MySQL'e Baglanirkan hata oldu -->", e)

