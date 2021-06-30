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

        entries = os.listdir(pathImport)

        for entry in entries:

            extension = entry[-3]+entry[-2]+entry[-1]
            if((extension=="jpg")or(extension=="png")):
                print("detecting : "+entry)
                self.imageSave(entry,pathImport, pathResult)

            if((extension=="mp4")):
                print("detecting : "+entry)
                self.videoSave(entry, pathImport ,pathResult)

        print("Program ending")

    def DetectAllImage (self, pathImport, pathResult):
        import os

        entries = os.listdir(pathImport)

        for entry in entries:

            extension = entry[-3]+entry[-2]+entry[-1]
            if((extension=="jpg")or(extension=="png")):
                print("detecting : "+entry)
                self.imageSave(entry,pathImport, pathResult)

        print("Program ending")

    def DetectAllVideo (self, pathImport, pathResult):
        import os

        entries = os.listdir(pathImport)

        for entry in entries:

            extension = entry[-3]+entry[-2]+entry[-1]

            if((extension=="mp4")):
                print("detecting : "+entry)
                self.videoSave(entry, pathImport ,pathResult)

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

        toDetect = pathImport+"/"+video
        cap=cv2.VideoCapture(toDetect)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        fourcc=cv2.VideoWriter_fourcc(*'MP4V')
        outputTitle=pathResult+"/"+video
        out=cv2.VideoWriter(outputTitle,fourcc,20.0, (height,  width))

            # Check if camera opened successfully
        if (cap.isOpened()== False): 
            print("Error opening video stream or file")

        frameCount = 1
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
                print("Analyse "+video+" : "+str(pour)+"%")
                frameCount+=1
                #cv2.imshow('out', frame)

                # Break the loop
                if cv2.waitKey(1) == ord('q'):
                    break
            else: 
                break

        cap.release()
        out.release()
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
model.DetectAll("C:/Users/Utilisateur/Documents/efrei/L3/mastercamp/git/GRP-220-2/ressources/import/img", "C:/Users/Utilisateur/Documents/efrei/L3/mastercamp/git/GRP-220-2/ressources/result")
#model.videoSave("test2.mp4","C:/Users/Utilisateur/Documents/efrei/L3/mastercamp/git/GRP-220-2/ressources/import/img", "C:/Users/Utilisateur/Documents/efrei/L3/mastercamp/git/GRP-220-2/ressources/result")