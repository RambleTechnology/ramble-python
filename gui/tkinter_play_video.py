import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk

# 视频窗口设置
window_width = 2048
window_height = 1440
image_width = int(window_width * 0.5)
image_height = int(window_height * 0.5)

# 读取视频文件
vc1 = cv2.VideoCapture("1.mp4")  # 请确保1.mp4在你的工作目录中

# 图像转换函数
def tkImage(vc):
    ref, frame = vc.read()
    if not ref:
        return None  # 如果视频结束，返回None
    cvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pilImage = Image.fromarray(cvimage)
    pilImage = pilImage.resize((image_width, image_height), Image.Resampling.LANCZOS)  # 使用LANCZOS代替ANTIALIAS
    tkImage = ImageTk.PhotoImage(image=pilImage)
    return tkImage

# 更新视频帧的函数
def update_video():
    picture = tkImage(vc1)
    if picture:  # 如果成功读取到视频帧
        canvas.create_image(0, 0, anchor="nw", image=picture)
        canvas.image = picture  # 保存图像引用，以防被垃圾回收
        win.after(30, update_video)  # 每30毫秒更新一次
    else:
        vc1.set(cv2.CAP_PROP_POS_FRAMES, 0)  # 如果视频结束，重新开始
        update_video()

# 创建Tkinter窗口
win = tk.Tk()
win.geometry(f"{window_width}x{window_height}")

# 创建Canvas用于显示视频
canvas = Canvas(win, bg="black", width=image_width, height=image_height)
canvas.pack()

# 启动视频播放
update_video()

# 运行Tkinter事件循环
win.mainloop()

# 释放视频资源
vc1.release()
cv2.destroyAllWindows()
