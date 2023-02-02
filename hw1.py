import cv2 as cv
import numpy as np

def mouse_callback(event, x, y, flags, param):
    if event == 1:
        print('B: ', param[y][x][0], '\nG: ', param[y][x][1], '\nR: ', param[y][x][2])
        print('=================================')


Path = 'Data/'
Name = 'rabong2.jpg'
FullName = Path + Name

# 이미지 읽기
img = cv.imread(FullName)

#
#
# 여기에 소스코드 작성

area = [0, 0, 0, 0] #사분면

for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        if img[y, x, 2] > 70 and img[y, x, 1] > 41:
            img[y, x, 2] = 255
            img[y, x, 1] = 0
            img[y, x, 0] = 0

            if y < 256:
                if x >= 256:
                    area[0] += 1
                else:
                    area[1] += 1
            else:
                if x < 256:
                    area[2] += 1
                else:
                    area[3] += 1

#선
for x in range(img.shape[1]):
    img[256, x, 2] = 0
    img[256, x, 1] = 0
    img[256, x, 0] = 255

for y in range(img.shape[0]):
    img[y, 256, 2] = 0
    img[y, 256, 1] = 0
    img[y, 256, 0] = 255

#위치
location = max(area)

if location == area[0]:
    print("위치: 제1사분면")

elif location == area[1]:
    print("위치: 제2사분면")

elif location == area[2]:
    print("위치: 제3사분면")

elif location == area[3]:
    print("위치: 제4사분면")

print("크기", img.shape)

# 이미지 출력
cv.imshow('img', img)
#cv.imshow('gray1', gray1)
#cv.imshow('gray', gray)
#cv.imshow('blur', blur)


while cv.waitKey(33) <= 0:
    cv.setMouseCallback('img', mouse_callback, img)

cv.waitKey(0)
