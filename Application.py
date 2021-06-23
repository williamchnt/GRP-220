from tkinter import *
from PIL import ImageTk, Image

#fenêtre principale
appli = Tk()
width = 950
height = 700

#creation des frames 
#detection_frame = Frame(appli, bg = "#16A8DB", bd = 1, relief = SUNKEN, padx = 15, pady = 15)
#import_frame = Frame(appli, bg = "#16A8DB", bd = 1, relief = SUNKEN, padx = 15, pady = 15)


#modification de la fenêtre principale
appli.title("Pr'eau'Pre")
#appli.geometry("900x600")
appli.minsize(width,height)
appli.maxsize(width,height)
#appli.config(background = "#4065A4")
appli.iconbitmap("logo_ocean_six.ico")

#application d'un background pour la fenêtre principale
bg_appli = PhotoImage(file = "backgroundAppli.png")
bg_label = Label(appli, image = bg_appli)
bg_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

#ajout des boutons

button_border_import = Frame(
    appli, 
    highlightbackground = "white", 
    highlightthickness = 2, 
    bd=0
)

button_border_photo = Frame(
    appli, 
    highlightbackground = "white", 
    highlightthickness = 2, 
    bd=0
)

button_border_video = Frame(
    appli, 
    highlightbackground = "white", 
    highlightthickness = 2, 
    bd=0
)

button_photo = Button(
    button_border_photo, 
    text = "Detection photo", 
    font = ("Ubisoft Sans Bold",20),
    bd = 5,
    bg = "#05afde",
    fg = "white",
    relief = "flat"  
)

button_video = Button(
    button_border_video, 
    text = "Detection video", 
    font = ("Ubisoft Sans Bold",20),
    bd = 5,
    bg = "#05afde",
    fg = "white",
    relief = "flat"
)

download_logo = Image.open("download_logo.png")
rendu = ImageTk.PhotoImage(download_logo)

button_import = Button(
    button_border_import, 
    text = "Importer photos/videos ", 
    font = ("Ubisoft Sans Bold",20), 
    image = rendu, 
    compound = RIGHT, 
    bd = 5,
    bg = "#05afde",
    fg = "white",
    relief = "flat"
)

#Placement des boutons sur l'appli

button_border_import.pack()
button_import.pack()
button_border_import.place(x = width/2 - 145, y = 435)

button_border_photo.pack()
button_photo.pack()
button_border_photo.place(x = width/2 - 100, y = 515)

button_border_video.pack()
button_video.pack()
button_border_video.place(x = width/2 - 100, y = 590)

#function des boutons
def changeOnHover(button):
      
    button.bind("<Enter>", func=lambda e: button.config(
        cursor = "hand2", bg = "white", fg = "black"))
    
    button.bind("<Leave>", func=lambda e: button.config(
        bg="#05afde", fg = "white"))
     
#affichage de la fenêtre + application des fonctions

changeOnHover(button_photo)
changeOnHover(button_video)
changeOnHover(button_import)
appli.mainloop()

