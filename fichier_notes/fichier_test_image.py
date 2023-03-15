# Créé par Ordinateur, le 04/06/2022 en Python 3.7
from PIL import Image, ImageDraw,ImageFont
import urllib.request
import matplotlib

def couleur(nom_couleur : str):
    liste_couleur = {}
    for cname, hex in matplotlib.colors.cnames.items():
        liste_couleur[cname] = hex
    hexa_couleur = liste_couleur.get(nom_couleur)
    rouge = int(hexa_couleur[1]+hexa_couleur[2],16)
    vert = int(hexa_couleur[3]+hexa_couleur[4],16)
    bleu = int(hexa_couleur[5]+hexa_couleur[6],16)
    print("Rouge : ", rouge," | Vert : ",vert," | Bleu : ",bleu)


def image_affichage(url):
        '''Ouvre l'image depuis l'internet grâce au module "urllib.request" ainsi qu'à l'url correspondant.'''
        print(">>> Couleur du pseudo : Rouge / Vert / Bleu")
        urllib.request.urlretrieve(str(url),"emojis.png")
        img = Image.open("emojis.png")
        x,y = img.size
        if x!=y:
            raise ValueError("Veuillez mettre une image carré !")
        d1 =  ImageDraw.Draw(img)
        myFont = ImageFont.truetype("/Users/Ordinateur/Desktop/Cours/Projets réseau social/16020_FUTURAM.ttf",x//15)
        d1.text((0,y//10*9), "fhlezjqhbfezqhfeozqu", fill =(36, 191, 108), font=myFont)
        img.show()
