import time
from PIL import Image, ImageDraw, ImageFont
import urllib.request
import matplotlib
import random

class Configuration :

    def __init__(self):
        self.__reseau = {}

    def nouveau_nom(self):
        '''Fonction permettant de donner un nom à votre réseau.'''
        new_name = input('#Console | Quel nom souhaiteriez-vous avoir ?')
        if self.__reseau.get("nom") == None :
            self.__reseau["nom"] = new_name
        else:
            del self.__reseau["nom"]
            self.__reseau["nom"] = new_name

    def __str__(self):
        print("Votre réseaux est composé de : " , self.__reseau)

    def get_reseau(self):
        '''Permet de donner le type de votre réseau.'''
        return self.__reseau["type"]

    def get_nom(self):
        '''Permet de donner le nom de votre réseau.'''
        return self.__reseau["nom"]

    def type_réseaux(self):
        '''Fonction permettant de déterminer le type de réseau que vous souhaitez faire.'''
        type = input("#Console | Veuillez choisir entre l'un des types de réseaux suivants : chating / posting")
        while type != "chating" and type != "posting":
            type = input("#Console | Veuillez choisir entre l'un des types de réseaux suivants : chating / posting")
        if self.__reseau.get(type) != None :
            del self.__reseau["type"]
            self.__reseau["type"] = type
        else:
            self.__reseau["type"] = type

    def création_serveur(self):
        '''Permet de créer votre serveur en une seule fonction.'''
        self.type_réseaux()
        self.nouveau_nom()

class chating:

    def __init__(self):
        self.__message = []
        self.__personnage = profil()

    def verif_age(self):
        '''Permettant de vérifier si vous êtes dans la limite d'âge.'''
        if self.__typechat.get_typechat() == "Majeur":
            if int(self.__profil.get_age()) < 18 :
                return "> Message Administration : Vous êtes interdit d'accéder à ce chat !"
        else :
            return "> Message Administration : Accès au chat accordé."

    def envoyer_message(self):
        '''Fonction permettant d'envoyer un message dans le chat.'''
        message = input("Veuillez entrer votre message : ")
        self.__message.append(message)

    def affichage(self):
        '''Fonction permettant d'afficher une discussion.'''
        print("> Message du ",time.ctime(), " de : ", self.__personnage.get_pseudonyme(), " : ")
        print("   >>> ", self.__message[len(self.__message)])

    def affichage_image(self):
        '''Ouvre l'image depuis l'internet grâce au module "urllib.request" ainsi qu'à l'url correspondant.'''
        lien = input("#Console | Veuillez mettre précisément votre lien internet :")
        urllib.request.urlretrieve(str(url),"emojis.png")
        img = Image.open("emojis.png")
        img.show()

    def conversation(self):
        '''Fonction permettant de mettre le début d'une conversation.'''
        self.__typechat.affichage_typechat()
        self.verif_age()
        while vérification != "Non" :
            self.envoyer_message()
            self.affichage()
            self.__message.pop(0)

