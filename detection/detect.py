import operator
from tkinter import Label, StringVar, Tk, messagebox
from tkinter.constants import HORIZONTAL
from tkinter.ttk import Progressbar

#Classe de détection

class Detect:
    #Entrainement de l'algo
    cascade = "detection/cascade-V0.1.xml"
    

    #Fonction de lecture d'image
    def imageRead (self, image):
        import cv2

        #Vérification de la validité de l'argument
        if(isinstance(image, str)):
                #Instanciation de l'entrainement      
                face_cascade=cv2.CascadeClassifier(self.cascade)
                #Lecture de l'image      
                img = cv2.imread(image, cv2.IMREAD_COLOR)

                while True:
                    
                    #Passage en niveau de gris
                    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    #Détection des objets 
                    face=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
                    for x, y, w, h in face:
                        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    if cv2.waitKey(1)&0xFF==ord('q'):
                        break
                    cv2.imshow("Title", img)
                cv2.destroyAllWindows()
        else:
            print("Erreur input")

    #Détecter toutes les images et vidéos d'un dossier
    def DetectAll (self, pathImport, pathResult):
        import os
        #Instanciation d'une fenêtre de chargement
        window = Loading()

        #Lecture de tous les fichiers
        entries = os.listdir(pathImport)

        frameCount = 1
        Savepour = 0
        length = len(entries)
        for entry in entries:

            #Détecter toutes les images et vidéos d'un dossier
            window.currentTask(entry)

            #lecture de l'extension du fichier
            extension = entry[-3]+entry[-2]+entry[-1]
            if((extension=="jpg")or(extension=="png")or(extension=="PNG")or(extension=="JPG")):
                print("detecting : "+entry)
                try:
                    #Utilisation de la détection sur une image
                    self.imageSave(entry,pathImport, pathResult)
                except:
                    #En cas d'erreur sur une image
                    messagebox.showerror(
                        title="Error", 
                        message="Error detect"
                    )

            if((extension=="mp4")or(extension=="MP4")):
                print("detecting : "+entry)
                try:

                    #Utilisation de la détection sur une vidéo
                    self.videoSave(entry, pathImport ,pathResult)
                except:

                    messagebox.showerror(
                        title="Error", 
                        message="Error detect"
                    )

            #Pourcentage de réalisation du programme
            pour = int((frameCount*100)/length)
            if(pour != Savepour):
                print("Analyse Total :"+str(pour)+"%")
                #Update pourcentage
                window.step(pour)
                Savepour=pour

            frameCount+=1

        messagebox.showinfo(
        title="Succès", 
        message="Détection finit"
        )
        window.destroy()
        
        print("Program ending")

    #Détecter toutes les images d'un dossier
    def DetectAllImage (self, pathImport, pathResult):
        import os

        entries = os.listdir(pathImport)
        frameCount = 1
        Savepour=0
        length=len(entries)
        window = Loading()

        for entry in entries:

            extension = entry[-3]+entry[-2]+entry[-1]
            if((extension=="jpg")or(extension=="png")or(extension=="PNG")or(extension=="JPG")):
                print("detecting : "+entry)
                self.imageSave(entry,pathImport, pathResult)

            pour = int((frameCount*100)/length)
            if(pour != Savepour):
                print("Analyse Total :"+str(pour)+"%")
                window.step(pour)
                Savepour=pour

            frameCount+=1

        messagebox.showinfo(
        title="Succès", 
        message="Détection finit"
        )
        window.destroy()
        print("Program ending")

#Détecter toutes les images et vidéos d'un dossier
    def DetectAllVideo (self, pathImport, pathResult):
        import os

        entries = os.listdir(pathImport)
        frameCount = 1
        Savepour=0
        length=len(entries)
        window = Loading()

        for entry in entries:

            extension = entry[-3]+entry[-2]+entry[-1]

            if((extension=="mp4")or(extension=="MP4")):
                print("detecting : "+entry)
                self.videoSave(entry, pathImport ,pathResult)

            pour = int((frameCount*100)/length)
            if(pour != Savepour):
                print("Analyse Total :"+str(pour)+"%")
                window.step(pour)
                Savepour=pour

            frameCount+=1

        messagebox.showinfo(
        title="Succès", 
        message="Détection finit"
        )
        window.destroy()
        print("Program ending")

    #Sauvegarder une image détecter dans un fichier
    def imageSave (self, image,pathImport, pathResult):
        import cv2

        if(isinstance(image, str)):
                #Chemin vers l'image
                toDetect = pathImport+"/"+image

                face_cascade=cv2.CascadeClassifier(self.cascade)
 
                img = cv2.imread(toDetect, cv2.IMREAD_COLOR)
                width=img.shape[1]
                gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                face=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4)
                tab_face=[]
                index=0
                marge=50
                for x, y, w, h in face:
                    
                    if w >50:
                        #tab_face.append([width-x, y, width-(x+w), y+h])
                        cv2.rectangle(img, (x, y),  (x+w, y+h), (255, 0, 0), 2)
                
                #tab_face=sorted(tab_face, key=operator.itemgetter(0, 1))
                #for x, y, x2, y2 in tab_face:
                #    if not index or (x-tab_face[index-1][0]>marge or y-tab_face[index-1][1]>marge):
                #        cv2.rectangle(img, (x, y), (x2, y2), (0, 0, 255), 2)
                #    index+=1

                
                newTitle=pathResult+"/"+image
                cv2.imwrite(newTitle, img)
                del img

        else:

            print("Erreur input")

    #Détecter une vidéo
    def video(self, video):
        
            import cv2

            face_cascade=cv2.CascadeClassifier(self.cascade)
            cap=cv2.VideoCapture(video)

                #Vérifiction vidéo ouverte
            if (cap.isOpened()== False): 
                messagebox.showwarning(
                    title="Warning", 
                    message="Error opening video stream or file"
                )
                print("Error opening video stream or file")

            # Lecture de la vidéo jusqu'à la fin
            while(cap.isOpened()):
            # Découpage frame par frame
                ret, frame=cap.read()
                if ret == True:
                    tickmark=cv2.getTickCount()
                    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    face=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
                    for x, y, w, h in face:
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    if cv2.waitKey(1)&0xFF==ord('q'):
                        break
                    fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
                    cv2.putText(frame, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

                        # Afficher le résultat
                    cv2.imshow('Frame',frame)

                    # Q pour arreter
                    if cv2.waitKey(1)&0xFF==ord('q'):
                        break

                else: 
                    break

            cap.release()
            cv2.destroyAllWindows()

    #Détecter et sauvegarder une vidéo
    def videoSave(self, video,pathImport, pathResult):

        import cv2

        face_cascade=cv2.CascadeClassifier(self.cascade)
        window = Loading()
        window.currentTask(video)
        window.setTitle(video)
        toDetect = pathImport+"/"+video
        cap=cv2.VideoCapture(toDetect)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        fourcc=cv2.VideoWriter_fourcc(*'MJPG')
        newtitle = video[:-4]
        outputTitle=pathResult+"/"+newtitle+".avi"
        out=cv2.VideoWriter(outputTitle,fourcc,30.0, (width,height))

        if (cap.isOpened()== False): 
            messagebox.showwarning(
                    title="Warning", 
                    message="Error opening video stream or file"
                )
            print("Error opening video stream or file")

        frameCount = 1
        Savepour=0

        while(cap.isOpened()):

            ret, frame=cap.read()
            if ret == True:
                gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                face=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
                for x, y, w, h in face:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    # Display the resulting frame
                out.write(frame)
                pour = int((frameCount*100)/length)
                if(pour != Savepour):
                    print("Analyse "+video+" : "+str(pour)+"%")
                    window.step(pour)
                    Savepour=pour

                frameCount+=1

                if cv2.waitKey(1) == ord('q'):
                    break
            else: 
                break

        cap.release()
        out.release()
        window.destroy()
        cv2.destroyAllWindows()


    #Détecter en direct
    def detectLive(self):
        import cv2


        face_cascade=cv2.CascadeClassifier(self.cascade)
        cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

        while True:
            ret, frame=cap.read()
            tickmark=cv2.getTickCount()
            gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
            for x, y, w, h in face:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            if cv2.waitKey(1)&0xFF==ord('q'):
                break
            fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
            cv2.putText(frame, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
            cv2.imshow('video', frame)
        cap.release()
        cv2.destroyAllWindows()
    

#Fenêtre de chargement
class Loading:

    def __init__(self):
        #initialisation de la fenêtre
        self.window = Tk()
        self.window.geometry("600x100")
        self.window.title("Detection")
        self.progress = Progressbar(self.window, orient = HORIZONTAL,length = 100, mode = 'determinate')
        self.progress.pack(pady=10)
        self.percent = StringVar(self.window)
        self.text = StringVar(self.window)
        self.taskLabel = Label(self.window,textvariable=self.text).pack()
        self.percentLabel = Label(self.window,textvariable=self.percent).pack()
        self.window.attributes("-topmost", True) 

    #Update de la barre de chargement
    def step(self, value):
        self.progress['value'] = value
        self.percent.set(str(value)+"% completed")
        self.window.update()

    #Affichage du fichier detecter
    def currentTask(self, task):
        self.text.set("Detecting : "+task)

    #Modification du titre de la fenêtre
    def setTitle(self,title):
        self.window.title("Vidéo detection : "+title)

    #Destruction de le fenêtre
    def destroy(self):
        self.window.destroy()

#model = Detect()
#model.imageSave("roumanie_14306c4d855f2d66d7431f3f87127c593ea077fa.jpg","C:/Users/Utilisateur/Downloads/Test images","C:/Users/Utilisateur/Downloads/testOral")