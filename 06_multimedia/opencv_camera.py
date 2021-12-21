import cv2
'''
cap = cv2.VideoCapture('output.avi')

if not cap.isOpened():
    print('Camera open failed')
    exit()

ret, frame = cap.read()
cv2.imwrite('output.jpg', frame)

cap.release()
cv2.destroyAllWindows()
'''
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

fourcc = cv2.VideoWriter_fourcc(*'DIVX')

out = cv2.VideoWriter('output.avi', fourcc, 30, (160, 100))


while True:
    ret, frame = cap.read()
    if not ret:
        break
    edge = cv2.Canny(frame, 40, 30)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)
    cv2.imshow('gray', gray)
    out.write(frame)
    out.write(edge)
    out.write(gray)


    if cv2.waitKey(10) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()