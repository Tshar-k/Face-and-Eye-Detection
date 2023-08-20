import cv2
face_cascade = cv2.CascadeClassifier("raw.githubusercontent.com_opencv_opencv_4.x_data_haarcascades_haarcascade_frontalface_default.xml")
img = cv2.imread("test_face_detectimg2.jpg")
img = cv2.resize(img,(512,512))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.1,5)
for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
        cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllwindow()