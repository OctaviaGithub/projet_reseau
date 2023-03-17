# Créé par Ordinateur, le 15/03/2023 en Python 3.7
import time
from PIL import Image, ImageDraw, ImageFont
import urllib.request
import matplotlib
import random

class profil :

    def __init__(self):
        self.__prenom = None
        self.__age = None
        self.__description = None
        self.__profil = None
        self.__url = None
        self.__couleur_pseudo = None
        self.__pseudonyme = None
        self.__role = "User"
        self.__liste_user=["BasicUser","Moderator","Administrator","Owner"]
        self.création_compte()

    def création_compte(self):
        '''Fonction permettant de vous créer un compte.'''
        if self.__prenom == None:
            self.__prenom = input("#Console | Quel pseudonyme voudriez vous choisir ?")
        if self.__age == None :
            self.__age = input ("#Console | Entrez votre âge : ")
            while not self.__age.isdigit():
                self.__age = input ("#Console | Entrez votre âge : ")
        if self.__description == None :
            self.new_description()
        if self.__pseudonyme == None :
            self.new_pseudonyme()
        print("#Console | Compte créé avec succés !")

    def change_role(self,new_role):
        '''Permet de changer le rôle de l'utilisateur.'''
        for i in self.__liste_user :
            if new_role == i :
                self.__role = new_role

    def get_pseudonyme(self):
        '''Permet de return le pseudonyme de l'utilisateur.'''
        return self.__prenom

    def get_role(self):
        '''Permet de return le role de l'User.'''
        return self.__role

    def get_age(self):
        '''Permet de return l'âge de l'utilisateur.'''
        return self.__age

    def new_pseudonyme(self):
        '''Fonction permettant de mettre à jour votre pseudonyme.'''
        pseudonyme = input("#Console | Quel nouveau pseudonyme souhaiteriez vous utiliser ?")
        self.__prenom = pseudonyme
        return "#Console | Votre pseudonyme a bien été changé en : " , self.__prenom

    def affichage_profil(self):
        '''Permet d'afficher les informations de votre profil.'''
        self.création_compte()
        print("Console > Voici votre profil : ")
        print("     > Pseudonyme : ", self.__pseudonyme)
        print("     > Votre âge : ", self.__age)
        if self.__description == None:
            print("     > Votre description est vide.")
        else:
            print("     > Profil : ", self.__description)
        self.affichage_total()

    def new_profil(self):
        '''Fonction permettant de vous mettre une nouvelle biographie.'''
        profil = input("#Console | Veuillez écrire une mini-biographie de ce que vous voulez ! ")
        self.__description = profil

    def test_url_image(self):
        '''Fonction permettant de tester votre url pour votre image de profil.'''
        self.__url = input("#Console | Veuillez entrer l'adresse précise de l'image :")
        urllib.request.urlretrieve(str(self.__url),"Emojis.jpg")
        print("#Console | Picture Download Succesfull")

    def affichage_total(self):
        '''Ouvre l'image depuis l'internet grâce au module "urllib.request" ainsi qu'à l'url correspondant tout en casant votre pseudonyme dessus.'''
        self.test_url_image()
        urllib.request.urlretrieve(str(self.__url),"emojis.png")
        img = Image.open("emojis.png")
        x,y = img.size
        if x!=y:
            raise ValueError("#Console | Veuillez mettre une image carré !")
        d1 =  ImageDraw.Draw(img)
        myFont = ImageFont.truetype("/Users/Ordinateur/Desktop/Cours/Projets réseau social/16020_FUTURAM.ttf",x//15) ##Proposer à la personne de mettre le style de police qu'elle souhaite.
        self.new_couleur_pseudo()
        liste_couleur = {}
        for cname, hex in matplotlib.colors.cnames.items():
            liste_couleur[cname] = hex
        hexa_couleur = liste_couleur.get(self.__couleur_pseudo)
        rouge = int(hexa_couleur[1]+hexa_couleur[2],16)
        vert = int(hexa_couleur[3]+hexa_couleur[4],16)
        bleu = int(hexa_couleur[5]+hexa_couleur[6],16)
        d1.text((0,y//10*9), self.__prenom, fill =(rouge, vert, bleu), font=myFont) ##Proposer à la personne de mettre la couleur qu'elle veut.
        img.show()

    def new_description(self):
        '''Fonction permettant de mettre une nouvelle description.'''
        self.__description = input("#Console | Veuillez vous donner une description : ")

    def new_couleur_pseudo(self):
        '''Fonction permettant de mettre une nouvelle couleur à votre pseudo.'''
        if self.__couleur_pseudo == None:
            self.__couleur_pseudo = input("#Console | Veuillez donner la couleur de votre pseudo : ")

    def new_pseudonyme(self):
        '''Fonction permettant de mettre votre pseudo avec un #xxxx comme Discord.'''
        self.__pseudonyme = str(self.__prenom) + "#"
        for i in range(4):
            self.__pseudonyme = self.__pseudonyme + str(random.randint(0,9))

