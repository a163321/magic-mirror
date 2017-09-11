import cv2
import numpy as np

# 模式参数
filename = "data/haarcascades/haarcascade_frontalface_default.xml"  # 识别模式文件

# 人脸识别


def gface(image):
    # 创建 classifier
    clf = cv2.CascadeClassifier(filename)
    # 设定灰度
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 人脸框的颜色
    color = (0, 255, 0)

    # 识别面部

    faces = clf.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # 画方框

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)

    return image


cap = cv2.VideoCapture(0)  # 从摄像头中取得视频

while(cap.isOpened()):
    # 读取帧摄像头
    ret, frame = cap.read()
    if ret == True:
        # 输出当前帧
        frame = gface(frame)

        cv2.imshow('My Camera', frame)

        # 键盘按 Q 退出
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
    else:
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
