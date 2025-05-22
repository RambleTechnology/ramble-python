from wxauto import WeChat
import time
from PIL import ImageGrab
import os
from datetime import datetime
import ctypes
import subprocess
 
def get_function_list():
    return """当前支持的功能：
1. 截图 - 截取当前屏幕并发送
2. 锁屏 - 锁定电脑屏幕
3. 关机 - 关闭电脑
4. 重启 - 重启电脑
5. 功能 - 显示当前支持的功能列表"""
 
def system_shutdown():
    try:
        subprocess.run(['shutdown', '/s', '/t', '0'], check=True)
        return True
    except Exception as e:
        print(f"关机失败: {e}")
        return False
 
def system_restart():
    try:
        subprocess.run(['shutdown', '/r', '/t', '0'], check=True)
        return True
    except Exception as e:
        print(f"重启失败: {e}")
        return False
 
def lock_screen():
    try:
        ctypes.windll.user32.LockWorkStation()
        print("屏幕已锁定")
        return True
    except Exception as e:
        print(f"锁屏失败: {e}")
        return False
 
def take_screenshot():
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'screenshots/screenshot_{timestamp}.png'
    screenshot = ImageGrab.grab()
    screenshot.save(filename)
    return filename
 
def monitor_file_transfer():
    wx = WeChat()
    print("开始监测文件传输助手...")
     
    last_msgs = []
    try:
        last_msgs = wx.GetAllMessage()
    except Exception as e:
        print(f"获取初始消息失败: {e}")
     
    while True:
        try:
            current_msgs = wx.GetAllMessage()
             
            if len(current_msgs) > len(last_msgs):
                new_msgs = current_msgs[len(last_msgs):]
                 
                for msg in new_msgs:
                    print(f"收到新消息: {msg}")
                     
                    if "功能" in msg:
                        wx.SendMsg(get_function_list())
                     
                    elif "截图" in msg:
                        print("正在截图...")
                        screenshot_path = take_screenshot()
                        try:
                            wx.SendFiles(screenshot_path)
                            if os.path.exists(screenshot_path):
                                os.remove(screenshot_path)
                        except Exception as e:
                            print(f"发送截图失败: {e}")
                     
                    # elif "锁屏" in msg:
                    #     print("正在执行锁屏...")
                    #     wx.SendMsg("屏幕已锁定")
                    #     time.sleep(1)
                    #     if lock_screen():
                    #         pass
                    #     else:
                    #         wx.SendMsg("锁屏失败")
                     
                    # elif "关机" in msg:
                    #     print("正在执行关机...")
                    #     wx.SendMsg("正在执行关机操作...")
                    #     time.sleep(1)
                    #     if system_shutdown():
                    #         pass
                    #     else:
                    #         wx.SendMsg("关机失败")
                     
                    # elif "重启" in msg:
                    #     print("正在执行重启...")
                    #     wx.SendMsg("正在执行重启操作...")
                    #     time.sleep(1)
                    #     if system_restart():
                    #         pass
                    #     else:
                    #         wx.SendMsg("重启失败")
                 
                last_msgs = current_msgs
             
            time.sleep(1)
             
        except Exception as e:
            print(f"发生错误: {e}")
            time.sleep(5)
 
"""吾爱pojie 微信文件传输助手控制电脑 https://www.52pojie.cn/thread-2027985-1-1.html
"""
if __name__ == "__main__":
    monitor_file_transfer()