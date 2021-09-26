#!/usr/bin/python
#-*- coding: utf-8 -*-
from config  import * #bases de datos
import requests,os,json,datetime
from  tkinter import * 
import tkinter as tk


fecha=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(fecha)

class deck_cards():
    def __init__(self):

            self.deck_count=1

            self.url="https://deckofcardsapi.com/api/deck/new/shuffle/"

            self.params={'deck_count' :self.deck_count} #if deck_count else{}

            self.response_1 = requests.get(self.url, params=self.params)

            if self.response_1.status_code == 200: 
                self.data = self.response_1.json()
                print (self.data)
                #barajamos las cartas 
                self.deck_id=self.data['deck_id']
                self.card_remaining= self.data['remaining']
                print ("ID del Mazo: ", self.deck_id)
                print ("Cartas Restantes: ",self.card_remaining,)
                #tomamos una carta

                self.next = input("¿Desea tomar una carta? [Y/N]").lower()

                if self.next =='y': 

                    self.draw_card=("https://deckofcardsapi.com/api/deck/"+self.deck_id+"/draw/?count=1")
                    print ("draw_card: ",self.draw_card)
                    self.response_2=requests.get(self.draw_card)
                    self.data_2= self.response_2.json()
                    self.card_remaining_2= self.data_2['remaining']
                    print(self.data_2['remaining'])
                    self.results = self.data_2.get('cards',[])
                    if self.results: 
                        for cards in self.results: 
                            url_card_img=cards['image']
                            value=cards['value']
                            suit=cards['suit']
                            print(url_card_img)
                            data_shuffle={'deck_id': self.deck_id, 'shuffled': self.draw_card, 'remaining': self.card_remaining, 'url_card_img': url_card_img, 'value':value,'suit':suit,'fecha':fecha}
                            insert(data_shuffle)
                            tempcards = requests.get(url_card_img)
                            open('.carta', 'wb').write(tempcards.content)
                            #abre una ventana para dibujar la carta
                            ventana=tk.Tk()
                            ventana.geometry("230x400")
                            ventana.config(bg="white")
                            ventana.title("DECK CARDS")
                            imagen_name=".carta"
                            imagen=PhotoImage(file=imagen_name)
                            fondo=Label(ventana,image=imagen).place(x=0,y=0)
                            etiqueta_1=tk.Label(text=("Cards:",value.capitalize(),'of', suit.lower()),bg="white")#valor de la carta
                            etiqueta_1.pack(side=BOTTOM, padx=0, pady=10,fill='x')
                            ventana.mainloop()
                    


                else:
                    self.next = input("¿Desea ver el registro de las ultimas cartas tomadas? [Y/N]").lower()
                    if self.next =='y': 
                        select()
                    
                    else: 
                        print("Barajar cartas")
                        deck_cards()
                        
            else:
                print ("Error al establecer una conexión con la Api:",self.url, "codigó:", self.response_1.status_code)





class  get_pokemons():
    def __init__(self,offset=0):
        url = 'https://pokeapi.co/api/v2/pokemon-form/'

        params={'offset' : offset} if offset else{}

        response = requests.get(url, params=params)

        if response.status_code == 200:

            data = response.json()
            results = data.get('results',[])
            if results: 
                for pokemon in results: 
                        name_pokemon=pokemon['name']
                        pokemon_url=pokemon['url']
                        pokemon_details=requests.get(pokemon_url)
                        imagen_url=pokemon_details.json()
                        imagen=imagen_url.get('sprites',[])
                        url_imagen=imagen['back_default']
                        print("Nombre: ", name_pokemon, "URL Imagen: ",url_imagen)

            next = input("¿Continuar listando? [Y/N]").lower()
            if next =='y': 
                get_pokemons(offset=offset+20)


        else:

            print ("Error al establecer una conexión con la Api:",url, "codigó:", response.status_code)


if __name__ == '__main__':
  #get_pokemons()
  app=deck_cards()
