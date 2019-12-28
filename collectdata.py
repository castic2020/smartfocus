#20191228从文件读视频 
#人眼比例
#笔头识别
#数据统一文件
import numpy as np
import cv2
import datetime
f=open('shujv.csv','w')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
N=0
cx0=0
cy0=0
mdis=0




input_movie = cv2.VideoCapture("作业素材1.avi")
length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))
while True:
    ret, frame = input_movie.read()
    if not ret:
        break
    cv2.imshow("frame",frame)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red=np.array([170,50,60])
    upper_red=np.array([340,255,255])
    mask=cv2.inRange(hsv,lower_red,upper_red)
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    areas=[]
    
    bw=-1
    bh=-1
    goodeye=0
    goodpen=0
    N+=1
    
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color =frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        bw=0
        bh=0
        goodeye=0
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            bw=ew/w
            bh=eh/h
            goodeye=1

    for cnt in contours:
        area = cv2.contourArea(cnt)
        areas.append(area)
        goodpen=0
    if areas !=[]:
        ai=areas.index(max(areas))
        cnt=contours[ai]
        frame = cv2.drawContours(frame, contours, ai, (0,255,0),3)
        M = cv2.moments(cnt)
        goodpen=0
        if M['m00'] !=0:
            goodpen=1
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame,(cx,cy), 5 , (255,0,0),-1)
            mdis=((cx-cx0)**2+(cy-cy0)**2)**0.5
        cx0=cx
        cy0=cy
        print(mdis)
    
    nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    shujvbwbhtime=str(nowTime)+','+str(N)+','+str(bw)+','+str(bh)+','+str(goodeye)+','+str(mdis)+','+str(goodpen)+'\n'
    f.write(shujvbwbhtime)
    cv2.imshow('frame',frame)
    key = cv2.waitKey(10) & 0xFF
    if key&0xff==27:
        print("Quit Process ")
        break
f.close()
cv2.destroyAllWindows()
input_movie.release()
        
            

