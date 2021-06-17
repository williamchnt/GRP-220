import cv2
import operator

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_alt2.xml")
profile_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_profileface.xml")
img = cv2.imread("image compr.png", cv2.IMREAD_COLOR)
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