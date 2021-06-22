from tkinter import *
from PIL import ImageTk, Image

#fenêtre principale
appli = Tk()

#creation des frames 
detection_frame = Frame(appli, bg = "#16A8DB", bd = 1, relief = SUNKEN, padx = 15, pady = 15)
import_frame = Frame(appli, bg = "#16A8DB", bd = 1, relief = SUNKEN, padx = 15, pady = 15)


#modification de la fenêtre principale
appli.title("Pr'eau'Pre")
#appli.geometry("900x600")
#appli.minsize(700,400)
appli.config(background = "#4065A4")
appli.iconbitmap("logo_ocean_six.ico")

#contenu de la fenêtre
title = Label(appli, text = "Bienvenue sur Pr'eau'Pre", font = ("Ubisoft Sans Bold",40), bg = "#16A8DB", fg = "black")

#ajout des boutons
button1 = Button(detection_frame, text = "Detection photo", font = ("Ubisoft Sans Bold",20))
button2 = Button(detection_frame, text = "Detection video", font = ("Ubisoft Sans Bold",20))


#ajout des images
height = 220
width = 300

logo = Image.open("logo_ocean_six_with_text.png")
resized = logo.resize((300,225), Image.ANTIALIAS)
final_logo = ImageTk.PhotoImage(resized)
download_logo = Image.open("download_logo.png")
rendu = ImageTk.PhotoImage(download_logo)

button_import = Button(import_frame, text = "Importer photos/videos ", font = ("Ubisoft Sans Bold",20), image = rendu, compound = RIGHT)

canvas = Canvas(appli, width = width, height = height, bg = "white", bd = 0, highlightthickness = 0)
canvas.create_image(width/2, height/2, image = final_logo)

#placement des éléments
title.grid(row = 0, column = 0, padx = 100)

canvas.grid(row = 1, column = 0, pady = 30)

import_frame.grid(row = 2, column = 0, sticky = W, padx = 40)
button_import.pack()

detection_frame.grid(row = 2, column = 0, sticky = E, padx = 80, pady = 30)
button1.pack(pady = 10)
button2.pack(pady = 10)

#affichage de la fenêtre
appli.mainloop()

