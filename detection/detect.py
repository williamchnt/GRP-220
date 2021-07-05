from tkinter import Label, StringVar, Tk, messagebox
from tkinter.constants import HORIZONTAL
from tkinter.ttk import Progressbar

class Detect:
    cascade = "detection/cascade-V0.1.xml"
    
    def imageRead (self, image):
        import cv2

        if(isinstance(image, str)):         
                face_cascade=cv2.CascadeClassifier(self.cascade)
                img = cv2.imread(image, cv2.IMREAD_COLOR)

                while True:
                    
                    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    face=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
                    for x, y, w, h in face:
                        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    if cv2.waitKey(1)&0xFF==ord('q'):
                        break
                    cv2.imshow("Title", img)
                cv2.destroyAllWindows()
        else:
            print("Erreur input")

    
    def DetectAll (self, pathImport, pathResult):
        import os
        window = Loading()

        entries = os.listdir(pathImport)

        frameCount = 1
        Savepour=0
        length=len(entries)
        for entry in entries:

            window.currentTask(entry)
            extension = entry[-3]+entry[-2]+entry[-1]
            if((extension=="jpg")or(extension=="png")):
                print("detecting : "+entry)
                self.imageSave(entry,pathImport, pathResult)

            if((extension=="mp4")):
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

    def DetectAllImage (self, pathImport, pathResult):
        import os

        entries = os.listdir(pathImport)
        frameCount = 1
        Savepour=0
        length=len(entries)
        window = Loading()

        for entry in entries:

            extension = entry[-3]+entry[-2]+entry[-1]
            if((extension=="jpg")or(extension=="png")):
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

    def DetectAllVideo (self, pathImport, pathResult):
        import os

        entries = os.listdir(pathImport)
        frameCount = 1
        Savepour=0
        length=len(entries)
        window = Loading()

        for entry in entries:

            extension = entry[-3]+entry[-2]+entry[-1]

            if((extension=="mp4")):
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


    def imageSave (self, image,pathImport, pathResult):
        import cv2

        if(isinstance(image, str)):
                toDetect = pathImport+"/"+image
            
                face_cascade=cv2.CascadeClassifier(self.cascade)
                img = cv2.imread(toDetect, cv2.IMREAD_COLOR)

                gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                face=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
                for x, y, w, h in face:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                
                newTitle=pathResult+"/"+image
                cv2.imwrite(newTitle, img)
                del img

        else:

            print("Erreur input")

    def video(self, video):
        
            import cv2

            face_cascade=cv2.CascadeClassifier(self.cascade)
            cap=cv2.VideoCapture(video)

                # Check if camera opened successfully
            if (cap.isOpened()== False): 
                messagebox.showwarning(
                    title="Warning", 
                    message="Error opening video stream or file"
                )
                print("Error opening video stream or file")

            # Read until video is completed
            while(cap.isOpened()):
            # Capture frame-by-frame
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

                        # Display the resulting frame
                    cv2.imshow('Frame',frame)

                    # Press Q on keyboard to  exit
                    if cv2.waitKey(1)&0xFF==ord('q'):
                        break

                    # Break the loop
                else: 
                    break

            cap.release()
            cv2.destroyAllWindows()

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

            # Check if camera opened successfully
        if (cap.isOpened()== False): 
            messagebox.showwarning(
                    title="Warning", 
                    message="Error opening video stream or file"
                )
            print("Error opening video stream or file")

        frameCount = 1
        Savepour=0
        # Read until video is completed
        while(cap.isOpened()):
        # Capture frame-by-frame
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
                #cv2.imshow('out', frame)

                # Break the loop
                if cv2.waitKey(1) == ord('q'):
                    break
            else: 
                break

        cap.release()
        out.release()
        window.destroy()
        cv2.destroyAllWindows()

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
    
class Loading:

    def __init__(self):
        self.window = Tk()
        self.window.geometry("600x100")
        self.window.title("Detection")
        self.progress = Progressbar(self.window, orient = HORIZONTAL,length = 100, mode = 'determinate')
        self.progress.pack(pady=10)
        self.percent = StringVar()
        self.text = StringVar()
        self.taskLabel = Label(self.window,textvariable=self.text).pack()
        self.percentLabel = Label(self.window,textvariable=self.percent).pack()
        self.window.attributes("-topmost", True) 

    def step(self, value):
        self.progress['value'] = value
        self.percent.set(str(value)+"% completed")
        self.window.update()

    def currentTask(self, task):
        self.text.set("Detecting : "+task)

    def setTitle(self,title):
        self.window.title("Vidéo detection : "+title)

    def destroy(self):
        self.window.destroy()

#model = Detect()
#model.DetectAll("C:/Users/Utilisateur/Documents/efrei/L3/mastercamp/git/GRP-220-2/ressources/import/img", "C:/Users/Utilisateur/Documents/efrei/L3/mastercamp/git/GRP-220-2/ressources/result")
#model.videoSave("test2.mp4","C:/Users/Utilisateur/Documents/efrei/L3/mastercamp/git/GRP-220-2/ressources/import/img", "C:/Users/Utilisateur/Documents/efrei/L3/mastercamp/git/GRP-220-2/ressources/result")