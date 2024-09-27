import cv2

# 初始化摄像头
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        # 显示摄像头画面
        cv2.imshow('Camera', frame)

        # 按 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# 释放资源
cap.release()
cv2.destroyAllWindows()
