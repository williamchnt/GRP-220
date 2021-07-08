from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter import filedialog, messagebox
import detection.detect as detect

#--Fenêtre principale--
appli = Tk()
width = 950
height = 700
importDataPath = ""
detectionResultsPath = ""

#--Modification de la fenêtre principale--
appli.title("Pr'eau'Pre")
appli.minsize(width,height)
appli.maxsize(width,height)
appli.iconbitmap("ressources/logo_ocean_six.ico")

#--Application d'un background pour la fenêtre principale--
bg_appli = PhotoImage(file = "ressources/backgroundAppli.png")
bg_label = Label(appli, image = bg_appli)
bg_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

#--Fonctions des boutons--

# Fonction d'importation des images
def importData():
    global importDataPath 

    messagebox.showwarning(
        title = "Warning", 
        message = "Penser à vérifier le nom de chacun de vos fichiers.\nCertains caractères spéciaux ne sont pas pris en compte (accent, espace et apostophe)."
    )

    importDataPath = filedialog.askdirectory()
    
    messagebox.showinfo(
        title = "Information", 
        message = "Seuls les fichiers suivants (jpeg, png, mp4) seront analysés."
    )

# Fonction de d'appel du programme de détection 
def detectData():
    global importDataPath
    global detectionResultsPath

    if not importDataPath == "":
        messagebox.showinfo(
            title = "Information", 
            message = "Veuillez sélectionner un dossier \noù les résulats de la détection seront stockés."
        )

        detectionResultsPath = filedialog.askdirectory()

        if not detectionResultsPath == "":
            if (len(os.listdir(detectionResultsPath)) == 0):
                model = detect.Detect()
                model.DetectAll(importDataPath, detectionResultsPath)
            else:
                messagebox.showerror(
                    title = "Error", 
                    message = "Le dossier sélectionné n'est pas vide."
                )
        else:
            messagebox.showerror(
                title = "Error", 
                message = "Aucun dossier n'a été sélectionné."
            )
    else:
        messagebox.showerror(
                title = "Error", 
                message = "Aucune donnée n'a été importé."
            )

#--Frames des boutons--
button_border_import = Frame(
    appli, 
    highlightbackground = "white", 
    highlightthickness = 2, 
    bd = 0,
)

button_border_detection = Frame(
    appli, 
    highlightbackground = "white", 
    highlightthickness = 2, 
    bd = 0,
)

#--Boutons--
button_detection = Button(
    button_border_detection, 
    text = "Commencer la détection", 
    font = ("Ubisoft Sans Bold",27),
    bd = 5,
    bg = "#05afde",
    fg = "white",
    relief = "flat",
    command = detectData
)

download_logo = Image.open("ressources/download_logo.png")
rendu = ImageTk.PhotoImage(download_logo)

button_import = Button(
    button_border_import, 
    text = "Importer photos/videos ", 
    font = ("Ubisoft Sans Bold",27), 
    image = rendu, 
    compound = RIGHT, 
    bd = 5,
    bg = "#05afde",
    fg = "white",
    relief = "flat",
    command = importData
)

#--Placement des boutons sur l'appli--
button_border_import.pack()
button_import.pack()
button_border_import.place(x = width/2 - 205, y = 445)

button_border_detection.pack()
button_detection.pack()
button_border_detection.place(x = width/2 - 212, y = 545)


#--Fonction d'animation des boutons--
def changeOnHover(button):
      
    button.bind("<Enter>", func = lambda e: button.config(
        cursor = "hand2", bg = "white", fg = "black"))
    
    button.bind("<Leave>", func = lambda e: button.config(
        bg = "#05afde", fg = "white"))

#--Affichage de la fenêtre + application des fonctions--
changeOnHover(button_detection)
changeOnHover(button_import)
appli.mainloop()