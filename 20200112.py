import matplotlib.pyplot as plt
import numpy as np
import cv2
import csv
from datetime import datetime 

f=open("shujvlast.txt")
data=f.read()
sdata=data.split("\n")
flr=[]
N=len(sdata)-1 
for x in range(N):
    flr.append(sdata[x].split(","))


for x in range(N):
        if float(flr[x][2])<0.22 and float(flr[x][2])>0.16:
                flr[x][3]=500
        else:
                flr[x][3]=0

asd1=[]
asd6=[]
asd11=[]
asd12=[]
asd13=[]

for x in range(N):
    rate1=flr[x][0]
    frate1=datetime.strptime(rate1,'%Y%m%d%H%M%S')
    asd1.append(frate1)
    rate6=flr[x][5] 
    frate6=500-float(rate6) 
    if frate6<0:
            frate6=0
    else:
            frate6=500-float(rate6)
    asd6.append(frate6)
    rate13=flr[x][0]
    frate13=datetime.strptime(rate13,'%Y%m%d%H%M%S')
    asd13.append(frate13)
    rate11=flr[x][2]
    rate12=flr[x][3]
    frate11=float(rate11)*800
    frate12=float(rate12)
    asd11.append(frate11)
    asd12.append(frate12)
x0=asd1
y5=asd6

x11=asd13 
y11=asd11
x12=asd13 
y12=asd12 
#plt.plot(x11,y11, label='bw')
#plt.plot(x12,y12, label='bh')




f=open("exp.txt")
edata=f.read()
esdata=edata.split("\n")
eflr=[]
M=len(esdata)-1 
for x in range(M):
    eflr.append(esdata[x].split(","))

asd20=[]
asd21=[]
for x in range(M):
    rate20=eflr[x][0]
    frate20=datetime.strptime(rate20,'%Y%m%d%H%M%S')
    asd20.append(frate20)
    rate21=eflr[x][1] 
    frate21=float(rate21) 
    asd21.append(frate21)
x10=asd20
y10=asd21
#plt.plot(x10,y10, label='record


#fgdjklsgfjldskfjkdsl;fjdxlzjcvlxzvjzxkl;vjkxlz;cvjxkzlcvjkzxl;Jcvkxlz;cjlzx:Jcklz:Jcklz:cjkl;ZJcklz;JcklzJCkl;zJCL
asdy5=[]
asdy5m=[]
asdy5mn=1000
moven=15
asdy5v=[]
asd46=[]
eyeslplen=2000
eyesmall=[]
for x in range(N):

    rate46=flr[x][5] 
    frate46=500-float(rate46) 
    asdy5.append(float(rate46))
    if x>asdy5mn:
        asdy5m.append(sum(asdy5[(x-asdy5mn):x])/asdy5mn)
    else:
        asdy5m.append(sum(asdy5[0:x])/(x+1))
    
    if asdy5m[x]<moven:
            asdy5v.append(500)
    else:
            asdy5v.append(0)
     
    if y11[x]>0.16*800 and y11[x]<0.22*800:
            eyesmall.append(500) 
     
    else:
            eyesmall.append(0)  



enddone=[]
for x in range(N):
        if x > eyeslplen:
                if 500 in eyesmall[x-eyeslplen:x] and asdy5v[x]==500:
                        enddone.append(550)
                else:
                        enddone.append(0)
        else: 
                if 500 in eyesmall[0:x] and asdy5v[x]==500:
                        enddone.append(550)
                else:
                        enddone.append(0)







print(asdy5m)
print(y10)
print("jkl;jkljklj;")
print(x10)
#plt.plot_date(x0, asdy5v,'-', label='asdy5v')
#plt.plot_date(x0, y11,'-', label='y11')
plt.plot(x10,y10, '-',label='record')
plt.plot(x0,enddone, '-',label='enddone')
plt.plot_date(x0, eyesmall,'-', label='eyesmall')
#plt.plot_date(x0, asd46,'-', label='asd46')

#plt.plot(x0,y1000, label='event')


plt.xlabel('time')
plt.ylabel('length')
plt.title('homework_data')
plt.legend()
plt.show()

