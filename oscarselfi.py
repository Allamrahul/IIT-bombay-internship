import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img=cv2.imread("oscarSelfie.jpg")#reading the image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#RGB to gray image
faces = face_cascade.detectMultiScale(gray, 1.3, 8)#Detects faces
count=0
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)#Bounding rectangle around face
    roi_gray = gray[y:y+h, x:x+w]#Selecting the face part in gray image
    eyes = eye_cascade.detectMultiScale(roi_gray)#Detecting eyes
    count+=1
    if count==4:#Ellens face is being detected in the last
        [x1,y1,w1,h1]=eyes[1]#Either right or left eye could be choosen.I choose left
        [x0,y0,w0,h0]=eyes[0]
[x1,y1]=[x1+faces[3][0],y1+faces[3][1]]
[x0,y0]=[x0+faces[3][0],y0+faces[3][1]]
print "(x1,y1,w1,h1)=(%s,%s,%s,%s)"%(x1,y1,w1,h1)#eyes of ellen
[c,b]=[x0+(w0/2-5),y0+31]#coordinates of centroid
cv2.putText(img, "x", (c, b),#displaying  "x"
cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)#For varying the properties of "x"
[b,g,r]=img[c,b]
print "RGB value at centroid of ellens eye [R,G,B]=[%s,%s,%s]"%(r,g,b)#gives rgb of pupil
cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(0,0,255),2)
cv2.rectangle(img,(x0,y0),(x0+w0,y0+h0),(0,0,255),2)#Bounding rectangle around the required area
cv2.imshow('img',img)
cv2.waitKey(0) & 0xFF






