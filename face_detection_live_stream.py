import cv2
face_cascade = cv2.CascadeClassifier("raw.githubusercontent.com_opencv_opencv_4.x_data_haarcascades_haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
while(True):
    ret,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
    cv2.imshow("image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
