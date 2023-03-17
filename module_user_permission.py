##Fichier pour les fonctions d'administrateurs.

import module_chat,module_profil,module_serveur,projet_réseau_principal

class User_Permission():

    def __init__(self):
        self.__profil = projet_réseau_principal.Configuration()
        self.__liste_user=["BasicUser","Moderator","Administrator","Owner"]
        self.__perm = {"Owner,add_salon" : True, "Administrator,add_salon" : False, "Moderator,add_salon" : False, "User,add_salon" : False,\
                       "Owner,change_salon" : True, "Administrator,change_salon" : False, "Moderator,change_salon" : False, "User,change_salon" : False,\
                       "Owner,change_role" : True, "Administrator,change_role": False, "Moderator,change_role" : False, "User,change_role" : False,\
                       "Owner,suppr_message" : True, "Administrator,suppr_message" : False, "Moderator,suppr_message" : False, "User,suppr_message": False}
        ##self.__perm = permission de base des quatre membres principaux du réseau.

    def get_liste_perm(self):
        print(self.__perm)

    def change_permission_add_salon(self,nom_role:str):
        if self.__profil.get_role(self.__profil.get_role) == self.__liste_user[3]:
            print("#Console | Permission Accordée")
            for i in self.__perm:
                print(i)
                test = (nom_role+",add_salon")
                print(test)
                if self.__perm[str(i)] == test :
                    if self.__perm[nom_role,",add_salon"] == True:
                        self.__perm[nom_role,",add_salon"] = False
                    else:
                        self.__perm[nom_role,",add_salon"] = True
                else:
                    print("Rien n'a été trouvé.")
        else:
            print("#Console | Permission non Accordée. Vous n'êtes pas l'Owner.")









