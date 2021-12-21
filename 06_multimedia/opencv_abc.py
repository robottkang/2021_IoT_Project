import cv2
import time

body_cascade = cv2.CascadeClassifier('./xml/haarcascade_fullbody.xml')

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    body = body_cascade.detectMultiScale(gray, 1.3, 5)
    print(body)

    for (x, y, w, h) in body:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()