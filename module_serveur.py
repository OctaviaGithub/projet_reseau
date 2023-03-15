# Créé par Ordinateur, le 15/03/2023 en Python 3.7

import projet_réseau_principal
import module_profil

class serveur_chating :
    '''Classe permettant la construction d'un serveur de type "chating" avec des chats, des descriptions et un affichage complet.'''

    def __init__(self):
        '''Initialisation de la classe serveur_chating'''
        self.__message = []
        self.__id_chat = None
        self.__typechat = None
        self.__typechat2 = None
        self.__nom = None
        self.__serveur = projet_réseau_principal.Configuration()
        self.__liste_chat = []
        self.__serveur.création_serveur()
        self.__personnage = module_profil.profil()
        ##Lignes permettant de vérifier si votre réseau est bien du type chating.
        if self.__serveur.get_reseau() == "chating":
            print(">>> Réseau créé avec réussite.")
        else:
            raise ValueError("#Console | Votre réseau n'est pas du type chating.")

    def get_typechat(self):
        '''Permet de donner le type de votre chat.'''
        return self.__typechat

    def get_typechat2(self):
        '''Permet de donner le type d'âge requis pour le chat.'''
        return self.__typechat2

    def get_nomchat(self):
        '''Permet de donner le nom du chat demandé.'''
        return self.__nom

    def get_listechat(self):
        '''Permet de renvoyer la liste des chats de votre serveur sous forme de liste de dictionnaires.'''
        return self.__liste_chat

    def get_profil(self):
        '''Permet de vous donner l'affichage total de votre profil.'''
        self.__personnage.affichage_profil()

    def get_id_chat(self):
        '''Permet de prendre l'ID d'un chat.'''
        chat_demande = input("#Console | Mettez le nom du chat dans lequel vous souhaitez rentrer")
        for i in range(len(self.__liste_chat)):
            if self.__liste_chat[i].get("nom") == chat_demande:
                return self.__liste_chat[i].get("id_chat")
            else :
                raise ValueError("#Console | Votre chat demandé n'existe pas !")
        if self.__liste_chat[i].get("âge") == "Majeur":
            if int(self.__profil.get_age()) < 18 :
                return "> Message Administration : Vous êtes interdit d'accéder à ce chat !"
        else :
            return "> Message Administration : Accès au chat accordé."

    def créer_chat(self):
        '''Fonction permettant de créer un chat sous forme de dictionnaire contenant les informations 'nom' / 'type' / 'âge' .'''
        chat = {}
        type_chat = input("#Console | Veuillez choisir entre l'un des types de chats suivants : public / privé")
        while type_chat != "public" and type_chat != "privé":
            type_chat = input("#Console | Veuillez choisir entre l'un des types de chats suivants : public / privé")
        chat["typechat"] = type_chat
        if type_chat == "public":
            type_chat2 = input("#Console | Veuillez choisir entre l'un des types de chats suivants : tout age / majeur")
            while type_chat2 != "tout age" and type_chat2 != "majeur":
                type_chat2 = input("#Console | Veuillez choisir entre l'un des types de chats suivants : tout age / majeur")
            chat["âge"] = type_chat2
        else:
            chat["âge"] = "privé"
        nom = input("#Console | Choisissez un nom pour votre chat : ")
        if self.__nom != None :
            self.__nom = nom
        else :
            self.__nom = nom
        serveur_chating.création_id_chat(self)
        chat["id_chat"] = self.__id_chat
        chat["nom"] = nom
        self.__liste_chat.append(chat)
        bio = input("# Console | Mettez une description à votre chat : ")
        chat["description"] = bio

    def affichage_typechat(self):
        '''Fonction d'affichage des informations du chat créé.'''
        if self.__typechat=="privé":
            print("Votre chat se nomme ",self.__nom," . Il est privé.")
        else:
            print("Votre chat se nomme ",self.__nom," . Il est public et ",self.__typechat2,".")

    def supprimer_chat(self,nomchat):
        '''Fonction permettant de supprimer un chat de la liste_chat.'''
        for i in range(len(self.__liste_chat)):
            if self.__liste_chat[i].get("nom") == nomchat:
                return self.__liste_chat.pop(i)

    def création_id_chat(self):
        '''Création de l'ID du chat en question.'''
        self.__id_chat = str("#")
        for i in range(8):
            id = random.randint(0,9)
            self.__id_chat = self.__id_chat + str(id)

    def description_chat(self):
        '''Fonction permettant de rajouter une description à votre chat.'''
        nomchat = input("#Console | Sur quel chat souhaitez vous mettre une description ? ")
        bio = input("#Console | Mettez une description à votre chat : ")
        for i in range(len(self.__liste_chat)):
            if self.__liste_chat[i].get("nom") == nomchat:
                self.__liste_chat[i]["description"] = bio

    def affichage_serveur(self):
        '''Fonction d'Administrateur permettant l'affichage des informations du serveur.'''
        print("         > Informations Serveur :")
        print("     >>> Nom : ", self.__serveur.get_nom())
        print("     >>> Type du réseau :", self.__serveur.get_reseau())
        compteur = 1
        for i in range(len(self.__liste_chat)):
            print("Votre chat N°",compteur," se nomme : ",self.__liste_chat[i].get("nom"), ". Il est : ", self.__liste_chat[i].get("typechat"), ". Et il est : ", self.__liste_chat[i].get("âge"))
            print("     > La description de ce chat : ", self.__liste_chat[i].get("description"), self.__liste_chat[i].get("id_chat"))
            time.sleep(2)
            compteur += 1

    def rentrer_chat(self):
        '''fonction permettant de discuter dans le chat demandé.'''
        self.get_id_chat()
        print("#Console | Accès autorisé !")
        print("#Console | Un nouveau membre est arrivé dans le chat : ", self.__personnage.get_pseudonyme())
        self.conversation()

    def envoyer_message(self):
        '''Fonction permettant d'envoyer un message dans le chat.'''
        message = input("#Console | Veuillez entrer votre message : ")
        self.__message.append(message)

    def affichage(self):
        '''Fonction permettant d'afficher une discussion.'''
        print("> Message du ",time.ctime(), " de : ", self.__personnage.get_pseudonyme(), " : ")
        print("   >>> ", self.__message[0])

    def affichage_image(self):
        '''Ouvre l'image depuis l'internet grâce au module "urllib.request" ainsi qu'à l'url correspondant.'''
        lien = input("#Console | Veuillez mettre précisément votre lien internet :")
        urllib.request.urlretrieve(str(url),"emojis.png")
        img = Image.open("emojis.png")
        img.show()

    def conversation(self):
        '''Fonction permettant de mettre le début d'une conversation.'''
        vérification = input("#Console | Souhaitez vous continuer la conversation ? Mettez Non pour sortir")
        while vérification != "Non" :
            self.envoyer_message()
            self.affichage()
            self.__message.pop(0)
            vérification = input("#Console | Souhaitez vous continuer la conversation ? Mettez Non pour sortir")
        print("#Console | Vous avez quitté la conversation !")
