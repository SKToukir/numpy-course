import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("res/output.avi",fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == True:
        out.write(frame)
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        cv2.imshow('frame', gray)
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()