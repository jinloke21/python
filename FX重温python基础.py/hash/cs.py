import cv2

cap = cv2.VideoCapture(0)
scaling_factor = 0.5
# 循环采集直到按下Esc键
while True:
# 采集当前画面
    ret, frame = cap.read()

