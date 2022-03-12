import numpy as np 
import cv2

#dim = 1280cols by 720 rows

cap = cv2.VideoCapture('rtsp://username:password@your_rtsp_ip_address')
b = True
while True:
    ret, frame = cap.read()
    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH )
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT )
    belt = frame[200:700, 100: 900]
    gray_belt = cv2.cvtColor(belt, cv2.COLOR_BGR2GRAY)  
      
    _, thresh_img = cv2.threshold(gray_belt, 80, 255, cv2.THRESH_BINARY)
    #cv2.imshow('thresh_img',thresh_img)
    #DETECT COINS:
    contours, _ = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        area = cv2.contourArea(cnt)
        #if 200 < x+w < 400 and area > 1000: 
        if area > 1000 and 200 < x+w < 400:
            cv2.rectangle(belt, (x, y), (x + w, y + h), (0, 255,0), 5)
            coin_type = "Unknown "
            if 30000 < area < 39000:
                coin_type = "quarter "
            if 17500 < area < 19000:
                coin_type = "dime "
            if 19000 < area < 22000:
                coin_type = "penny "
            if 23000 < area < 28000:
                coin_type = "nickel "

            cv2.putText(belt, coin_type, (x, y-7), 1, 1, (0, 255, 0))    
    cv2.imshow('section',belt)
    key = cv2.waitKey(30)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()










