import time
from PIL import Image, ImageDraw, ImageFont
import urllib.request
import matplotlib
import random
import module_profil
import module_user_permission, module_profil

class Configuration :

    def __init__(self):
        self.__reseau = {}
        self.création_serveur()
        self.__role = module_profil.profil()
        self.__role.change_role("Owner")

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

    def get_role(self,nom_role):
        return self.__role.get_role()

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

