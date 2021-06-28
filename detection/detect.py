class Detect:
    cascade = "cascade-V0.1.xml"
    
    
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

    def DetectAllImages (self, path):
        import os

        entries = os.listdir('./ressources/import/img')

        for entry in entries:

            extension = entry[-3]+entry[-2]+entry[-1]
            if((extension=="jpg")or(extension=="png")):

                self.imageSave(entry, path)


    def imageSave (self, image, path):
        import cv2

        if(isinstance(image, str)):
                toDetect = "./ressourcesimport/img/"+image

            
                face_cascade=cv2.CascadeClassifier(self.cascade)
                img = cv2.imread(toDetect, cv2.IMREAD_COLOR)

                gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                face=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
                for x, y, w, h in face:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                
                newTitle=path+"/"+image+"-detect.jpg"
                print(newTitle)
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


model = Detect()
#model.imageRead("test-image.jpg")
#model.imageSave("plastique.jpg")
model.DetectAllImages("C:/Users/Utilisateur/Documents/efrei/L3/mastercamp/git/GRP-220-2/ressources/result")
#model.imageSave("test-image.jpg")
#model.detectLive()
#model.video("test.mp4")