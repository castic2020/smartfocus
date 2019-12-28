#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 11:43
# @Author  : HaoWANG
# @Site    : 
# @File    : VideoWrite.py
# @Software: PyCharm
 
# 加载包
import math
import sys
import cv2
import datetime 
def main():
	# 初始化摄像头
	keep_processing = True;
	camera_to_use = 1;  # 0 if you have one camera, 1 or > 1 otherwise
	cap = cv2.VideoCapture(0)  # 定义视频捕获类cap
	windowName = "Live Video Capture and Write"  # 窗口名
	
	# opencv中视频录制需要借助VideoWriter对象， 将从VideoCapture 中读入图片，不断地写入到VideoWrite的数据流中。
	# 指定视频编解码方式为MJPG
	codec = cv2.VideoWriter_fourcc(*'MJPG')
	fps = 25.0  # 指定写入帧率为25
	frameSize = (640, 480)  # 指定窗口大小
	# # 创建 VideoWriter对象
	nowTime=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
	vfilename="VideoRecord"+str(nowTime)+'.avi'
	
	print(vfilename)

	output = cv2.VideoWriter(vfilename, codec, fps, frameSize)
	
	# 摄像头开启检测
	# error detection #
	'''if not (((len(sys.argv) == 2) and (cap.open(str(sys.argv[1]))))
	        or (cap.open(camera_to_use))):
		print("ERROR：No video file specified or camera connected.")
		return -1'''
	
	# Camera Is Open
	# create window by name (note flags for resizable or not)
	cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
	print("按键Q-结束视频录制")
	
	while (cap.isOpened()):
		
		# 00 if video file successfully open then read frame from video
		if (keep_processing):
			
			ret, frame = cap.read()  # 定义read对象ret和frame帧
			# start a timer (to see how long processing and display takes)
			start_t = cv2.getTickCount()
			
			# 不断的从VideoCapture 中读入图片，然后写入到VideoWrite的数据流中。
			output.write(frame)
			
			cv2.imshow(windowName, frame)  # display image
			
			# stop the timer and convert to ms. (to see how long processing and display takes)
			stop_t = ((cv2.getTickCount() - start_t) / cv2.getTickFrequency()) * 1000
			
			# 接收键盘停止指令
			# start the event loop - essential
			# wait 40ms or less depending on processing time taken (i.e. 1000ms / 25 fps = 40 ms)
			
			key = cv2.waitKey(max(2, 40 - int(math.ceil(stop_t)))) & 0xFF
			
			# It can also be set to detect specific key strokes by recording which key is pressed
			# e.g. if user presses "q" then exit
			
			if (key == ord('q')):
				print("Quit Process ")
				keep_processing = False
		else:
			break
	
	print("The display and video write tasks take {} ms".format(stop_t))
	
	# release the camera and close all windows
	# 资源释放,在录制结束后，我们要释放资源：
	# # 释放资源
	cap.release()
	output.release()
	cv2.destroyAllWindows()
# end main()
 
if __name__ == "__main__":
	main()
