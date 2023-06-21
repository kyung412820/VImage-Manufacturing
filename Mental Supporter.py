# Mental Supporter1

import numpy as np
import os
import cv2 as cv
import cv2 
from PIL import Image
import glob
import subprocess

print("\n[ 카테고리를 선택해 주십시오]\n")
print("Enter. 기본 카테고리 \n")
print("0. video 데이터 생성 + 기본 카테고리\n")
print("1. 업스케일+프레임보간 \n")
print("2. 프레임보간\n")
category=input("어느 카테고리를 택하시겠습니까?:")

if category=="0":
    os.popen("C:\"[ScrewThisNoise] Koikatsu BetterRepack RX17\[ScrewThisNoise] Koikatsu BetterRepack RX17\CharaStudio.exe")
    os.startfile('C:/Users/user/Videos')
    os.startfile('D:\Webuianimating\opencv')
    input("생성한 Video를 추출 폴더로 옮기십시오")
elif category=="1":
    os.system("C:\\realesrgan-ncnn-vulkan-20220424-windows\\realesrgan-ncnn-vulkan.exe -i D:\Webuianimating\\tmp_image -o D:\Webuianimating\out_image -n realesr-animevideov3 -s 4 -f png")
    os.system("ffmpeg -f image2 -r 15 -i D:\Webuianimating\out_image\%07d.png -vcodec libx264 D:\Webuianimating\out_image\Final_Video.mp4")
    print("\n업스케일을 완료했습니다\n\n")
    input("프레임 보간을 바로 진행하시겠습니까?:")
    os.startfile('D:\Webuianimating\out_image')
    print("\n\n프레임 보간 프로그램과 필요한 폴더를 실행했습니다.")
    print("프레임 보간을 진행해 주십시오")
    subprocess.run("C:/Users/user/AppData/Local/Flowframes/Flowframes.exe")
    exit()
elif category=="2":
    os.startfile('D:\Webuianimating\out_image')
    print("\n\n프레임 보간 프로그램과 필요한 폴더를 실행했습니다.")
    print("프레임 보간을 진행해 주십시오")
    subprocess.run("C:/Users/user/AppData/Local/Flowframes/Flowframes.exe")
    exit()

path = "D:\Webuianimating\opencv\input"#인풋데이터 위치(폴더명 data)
os.chdir(path) #프로그램 자체에서 연결된 폴더 지정

MP4_filepath = os.listdir('D:\Webuianimating\opencv')
MP4_file = [file for file in MP4_filepath if file.endswith(".mp4")]
if MP4_file!=[]:
    video = cv2.VideoCapture('D:\Webuianimating\opencv\\'+ str(MP4_file[0]))

    if not video.isOpened():
        print("Could not Open :", MP4_file)
        exit(0)

    length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    """
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)
    """

    count = 0
    while(video.isOpened() and count<length):
        ret, image = video.read()
        if(int(video.get(1)) % 1 == 0): #앞서 불러온 fps 값을 사용하여 1프레임마다 추출
            if int(video.get(1))<=10: #각 번호별 파일명 적용
                cv2.imwrite(path + "/000000%d.png" % count, image)
            elif int(video.get(1))<100:
                cv2.imwrite(path + "/00000%d.png" % count, image)
            elif int(video.get(1))<1000:
                cv2.imwrite(path + "/0000%d.png" % count, image)
            elif int(video.get(1))<10000:
                cv2.imwrite(path + "/000%d.png" % count, image)
            count += 1
        
    video.release()
    print("\ncomplete : 비디오를 input 데이터로 활용합니다\n")
else:
    print("비디오가 해당 파일에 없습니다. 인풋데이터의 자료를 바탕으로 프로그램을 계속합니다\n")

def get_files_count(folder_path):
	dirListing = os.listdir(folder_path)
	return len(dirListing)

file_lst = os.listdir(path)
img_count = get_files_count("D:\Webuianimating\opencv\input")#인풋데이터 숫자

png_img = []
jpg_img = []
count=0


for file in file_lst: #인풋데이터 폴더에서 png파일, jpg파일만 인식
    if '.png' in file: 
        f = cv2.imread(file)
        png_img.append(f)
    if '.jpg' in file: 
        f = cv2.imread(file)
        jpg_img.append(f)
    #아웃풋 폴더 설정 (폴더명 complete)
    
    
    #아웃풋 폴더 설정 (폴더명 complete)

for i in range(0, img_count):
    if len(png_img) == 0:
        pil_image=Image.fromarray(jpg_img[i])
        img_color = jpg_img[i] # 이미지 파일을 컬러로 불러옴
    if len(jpg_img) == 0:
        pil_image=Image.fromarray(png_img[i])
        img_color = png_img[i]
    else:
        print("input 데이터가 없습니다\n")

    if len(glob.glob('D:\Webuianimating\opencv\Background\*jpg')) != 0:
        img_background_jpg = glob.glob('D:\Webuianimating\opencv\Background\*jpg')
        img_background = cv.imread(img_background_jpg[0])
    elif len(glob.glob('D:\Webuianimating\opencv\Background\*png')) != 0:
        img_background_png = glob.glob('D:\Webuianimating\opencv\Background\*png')
        img_background = cv.imread(img_background_png[0])
    else:
        img_background=0

    height, width = img_color.shape[:2] # 이미지의 높이와 너비 불러옴, 가로 [0], 세로[1]
    img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV) # cvtColor 함수를 이용하여 hsv 색공간으로 변환

    if img_color[100][20][1]==0:
        lower_blue = (0,0,10 ) # hsv 이미지에서 바이너리 이미지로 생성 , 적당한 값 30 #검은색 이외값 추출
        upper_blue = (180, 255, 255) #검은색 이외값 추출 
        img_mask = cv2.inRange(img_hsv, lower_blue, upper_blue) # 범위내의 픽셀들은 흰색, 나머지 검은색
    else:
        lower_blue = (0,220,150 ) # 녹색 추출 
        upper_blue = (90, 255, 255) # 녹색 추출 
        img_mask = cv2.inRange(img_hsv, lower_blue, upper_blue) # 범위내의 픽셀들은 흰색, 나머지 검은색
        img_mask = 255-img_mask #녹색이나 특정 색을 검은색으로 추출할 경우 필요한 색 반전
    
    if ((width/2)-round(height*9/32)>0):
        img_color=img_color[0:height,int((width/2)-round(height*9/32)):int((width/2)+round(height*9/32))]
        img_mask=img_mask[0:height,int((width/2)-round(height*9/32)):int((width/2)+round(height*9/32))]

    img_mask = cv2.medianBlur(img_mask, 3)
# 바이너리 이미지를 마스크로 사용하여 원본이미지에서 범위값에 해당하는 영상부분을 획득
    if count==0:
        print("img_color: ", img_color.shape, "img_mask: ", img_mask.shape, "img_background: ", img_background.shape)
        if((img_background.shape[0]==img_color.shape[0]==img_mask.shape[0])and(img_background.shape[1]==img_color.shape[1]==img_mask.shape[1])):
            print("\n배경을 포함한 이미지를 생성합니다\n")
            count=1
    img_result = cv2.copyTo(img_color, img_mask, img_background)

    if i<10: #각 번호별 파일명 적용
         output_name="000000"+str(i)+".png"
    elif i<100:
          output_name="00000"+str(i)+".png"
    elif i<1000:
          output_name="0000"+str(i)+".png"
    elif i<10000:
          output_name="000"+str(i)+".png"
    os.chdir("D:\Webuianimating\\ai_input") 
    cv2.imwrite(output_name,img_color) #이미지 저장
    
    os.chdir("D:\Webuianimating\\ai_mask") 
    cv2.imwrite(output_name,img_mask) 

    os.chdir("D:\Webuianimating\opencv\Background_output")
    if (count==1):
        cv2.imwrite(output_name,img_result)

    if(count==0):
        print("배경이 합쳐진 이미지는 생성되지 않았습니다\n")
        count=1

os.startfile('D:\Webuianimating\\ai_input')

print("이 이후는 업스케일을 시작합니다. 완성된 이미지를 한번 더 가공/확인 해보시길 바랍니다")
print("작업이 완료되셨다면 정해진 업스케일용 input폴더에 이미지를 넣고 Enter를 눌러주시길 바랍니다\n")
contin_upftp=input("진행하시겠습니까?:")

if contin_upftp=="":
    os.system("C:\\realesrgan-ncnn-vulkan-20220424-windows\\realesrgan-ncnn-vulkan.exe -i D:\Webuianimating\\tmp_image -o D:\Webuianimating\out_image -n realesr-animevideov3 -s 4 -f png")
    os.system("ffmpeg -f image2 -r 15 -i D:\Webuianimating\out_image\%07d.png -vcodec libx264 D:\Webuianimating\out_image\Final_Video.mp4")
    print("\n업스케일을 완료했습니다\n\n")

    input("프레임 보간을 바로 진행하시겠습니까?:")
    os.startfile('D:\Webuianimating\out_image')
    print("\n\n프레임 보간 프로그램과 필요한 폴더를 실행했습니다.")
    print("프레임 보간을 진행해 주십시오")
    subprocess.run("C:/Users/user/AppData/Local/Flowframes/Flowframes.exe")
"""
cv2.imshow('img_origin', img_color)
cv2.imshow('img_mask', img_mask)
cv2.imshow('img_color', img_result)
"""

