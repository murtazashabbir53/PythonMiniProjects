
import cv2



cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"MURT")
output = cv2.VideoWriter("output.mp4",fourcc,20.0,(640,480))
print(cap.isOpened())
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        output.write(frame)
        #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",frame)


        if cv2.waitKey(1) & 0xFF == ord("q"):
            break




cap.release()
output.release()
cv2.destroyAllWindows()
