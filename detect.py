class Detect:
    
    
    def imageRead (self, image):
        import cv2
        import operator

        if(isinstance(image, str)):

            
                face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_alt2.xml")
                profile_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_profileface.xml")
                img = cv2.imread(image, cv2.IMREAD_COLOR)
                width=img.shape[1]
                marge=70

                

                while True:
                    
                    tab_face=[]
                    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    face=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4, minSize=(5, 5))
                    for x, y, w, h in face:
                        tab_face.append([x, y, x+w, y+h])
                    face=profile_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4)
                    for x, y, w, h in face:
                        tab_face.append([x, y, x+w, y+h])
                    gray2=cv2.flip(gray, 1)
                    face=profile_cascade.detectMultiScale(gray2, scaleFactor=1.2, minNeighbors=4)
                    for x, y, w, h in face:
                        tab_face.append([width-x, y, width-(x+w), y+h])
                    tab_face=sorted(tab_face, key=operator.itemgetter(0, 1))
                    index=0
                    for x, y, x2, y2 in tab_face:
                        if not index or (x-tab_face[index-1][0]>marge or y-tab_face[index-1][1]>marge):
                            cv2.rectangle(img, (x, y), (x2, y2), (0, 0, 255), 2)
                        index+=1
                    if cv2.waitKey(1)&0xFF==ord('q'):
                        break
                    cv2.imshow("Title", img)
                cv2.destroyAllWindows()
        else:
            print("Erreur input")

    def imageSave (self, image):
        import cv2
        import operator

        if(isinstance(image, str)):

            
                face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_alt2.xml")
                profile_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_profileface.xml")
                img = cv2.imread(image, cv2.IMREAD_COLOR)
                width=img.shape[1]
                marge=70

                tab_face=[]
                gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                face=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4, minSize=(5, 5))
                for x, y, w, h in face:
                    tab_face.append([x, y, x+w, y+h])
                face=profile_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4)
                for x, y, w, h in face:
                    tab_face.append([x, y, x+w, y+h])
                gray2=cv2.flip(gray, 1)
                face=profile_cascade.detectMultiScale(gray2, scaleFactor=1.2, minNeighbors=4)
                for x, y, w, h in face:
                    tab_face.append([width-x, y, width-(x+w), y+h])
                tab_face=sorted(tab_face, key=operator.itemgetter(0, 1))
                index=0
                for x, y, x2, y2 in tab_face:
                    if not index or (x-tab_face[index-1][0]>marge or y-tab_face[index-1][1]>marge):
                        cv2.rectangle(img, (x, y), (x2, y2), (0, 0, 255), 2)
                    index+=1

                newTitle=image+"-detect.jpg"
                cv2.imwrite(newTitle, img)

        else:
            print("Erreur input")



    def video(self, cap):

        import cv2
        import operator

        face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_alt2.xml")
        profile_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_profileface.xml")
        cap=cv2.VideoCapture(cap)
        width=int(cap.get(3))
        marge=70

            # Check if camera opened successfully
        if (cap.isOpened()== False): 
            print("Error opening video stream or file")

        # Read until video is completed
        while(cap.isOpened()):
        # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:
                tab_face=[]
                tickmark=cv2.getTickCount()
                gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                face=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4, minSize=(5, 5))
                for x, y, w, h in face:
                    tab_face.append([x, y, x+w, y+h])
                face=profile_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4)
                for x, y, w, h in face:
                    tab_face.append([x, y, x+w, y+h])
                gray2=cv2.flip(gray, 1)
                face=profile_cascade.detectMultiScale(gray2, scaleFactor=1.2, minNeighbors=4)
                for x, y, w, h in face:
                    tab_face.append([width-x, y, width-(x+w), y+h])
                tab_face=sorted(tab_face, key=operator.itemgetter(0, 1))
                index=0
                for x, y, x2, y2 in tab_face:
                    if not index or (x-tab_face[index-1][0]>marge or y-tab_face[index-1][1]>marge):
                        cv2.rectangle(frame, (x, y), (x2, y2), (0, 0, 255), 2)
                    index+=1

                fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
                cv2.putText(frame, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)  

                # Display the resulting frame
                cv2.imshow('Frame',frame)

                # Press Q on keyboard to  exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            # Break the loop
            else: 
                break

        cap.release()
        cv2.destroyAllWindows()

    def detectLive(self):
        import cv2
        import operator

        face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_alt2.xml")
        profile_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_profileface.xml")
        cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
        width=int(cap.get(3))
        marge=70

        while True:
            ret, frame=cap.read()
            tab_face=[]
            tickmark=cv2.getTickCount()
            gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4, minSize=(5, 5))
            for x, y, w, h in face:
                tab_face.append([x, y, x+w, y+h])
            face=profile_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4)
            for x, y, w, h in face:
                tab_face.append([x, y, x+w, y+h])
            gray2=cv2.flip(gray, 1)
            face=profile_cascade.detectMultiScale(gray2, scaleFactor=1.2, minNeighbors=4)
            for x, y, w, h in face:
                tab_face.append([width-x, y, width-(x+w), y+h])
            tab_face=sorted(tab_face, key=operator.itemgetter(0, 1))
            index=0
            for x, y, x2, y2 in tab_face:
                if not index or (x-tab_face[index-1][0]>marge or y-tab_face[index-1][1]>marge):
                    cv2.rectangle(frame, (x, y), (x2, y2), (0, 0, 255), 2)
                index+=1
            if cv2.waitKey(1)&0xFF==ord('q'):
                break
            fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
            cv2.putText(frame, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
            cv2.imshow('video', frame)
        cap.release()
        cv2.destroyAllWindows()


model = Detect()
#model.imageRead("image compr.png")
#model.imageSave("image compr.png")
model.detectLive()