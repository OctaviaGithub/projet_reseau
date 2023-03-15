# Créé par Ordinateur, le 06/06/2022 en Python 3.7
#importing library
from tkinter import *
#creating window
window = Tk()
#Title
window.title('Grand Canyon')
#display attributes
canvas = Canvas(window, width = 500, height = 500)
canvas.pack()
#GIF in my_image variable
#Give the entire file address along with the file name and gif extension
#Use \\ in the address
#The image given by me is C:\\UserAdmin\\Device\\Desktop2\\canyon.gif
my_image = PhotoImage(file='/Users/Ordinateur/Desktop/Cours/Projets réseau social/minion.gif')
canvas.create_image(0, 0, anchor = NW, image-my_image)
