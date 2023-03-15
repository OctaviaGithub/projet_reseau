# Créé par Ordinateur, le 15/03/2023 en Python 3.7

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
