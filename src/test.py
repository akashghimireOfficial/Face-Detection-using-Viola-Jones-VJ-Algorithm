import cv2

## loading haar cascade classifier
haar_cascade = cv2.CascadeClassifier('../cascade.xml')

## Detection of face from live camera

### test on camera
cap=cv2.VideoCapture(0)
while cap.isOpened(0):
    sucess,img=cap.read()
    if not sucess:
        break
    gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=9)
    for (x, y, w, h) in faces_rect:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('Detected Faces',img)
    if cv2.waitKey(1)==27:
        break
    cap.release()
    cv2.destroyAllWindows()