import cv2

c=cv2.VideoCapture(-1)

while c.isOpened():
    s,f=c.read()
    if not s:
        break
    cv2.imshow("test",f)
    key=cv2.waitKey(13)
    if key in (32,27):
        cv2.destroyAllWindows()
        c.release()
        break