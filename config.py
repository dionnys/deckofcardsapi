#!/usr/bin/python
#-*- coding: utf-8 -*-
import mysql.connector as mysql
from mysql.connector import errorcode
from tabulate import tabulate


host = 'localhost'
user = 'deck_cards'
user_pwd = 'D3$k#C4Rd$'
database = 'deck_cards'

try:
    cnx = mysql.connect(user=user,password=user_pwd,host=host,database=database)
    cursor = cnx.cursor()
except mysql.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Algo está mal con su nombre de usuario o contraseña")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de datos no existe")
    else:
        print(err)
else:

    def insert(data_shuffle):
        add_shuffle =("INSERT INTO shuffle_card " "(deck_id, shuffled,remaining,url_card_img,value,suit,fecha) " "VALUES (%(deck_id)s, %(shuffled)s, %(remaining)s,%(url_card_img)s,%(value)s,%(suit)s, %(fecha)s) " )
        #data_shuffle={'deck_id': deck_id, 'shuffled': shuffled, 'remaining': remaining, 'url_card_img': url_card_img, 'fecha':fecha}
        cursor.execute(add_shuffle,data_shuffle)
        cnx.commit()
        cnx.close()

    def select():
        query =("SELECT deck_id,value,suit,shuffled,url_card_img,fecha FROM shuffle_card ORDER BY fecha DESC LIMIT 10")
        cursor.execute(query)
        results=cursor.fetchall()
        #print(data)
        #if len(data)>=1:
         #   print(data)
          #  cnx.close()
        print(tabulate(results, headers=['deck_id', 'value', 'suit', 'shuffled', 'url_card_img','fecha'], tablefmt='psql'))



if __name__ == '__main__':
    select()
