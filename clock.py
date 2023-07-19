lockimport tkinter as tk
from tkinter import messagebox
from random import randrange
import time

# 设置时钟的基本参数
WIDTH = 500
HEIGHT = 450
FOREGROUND_COLOR = "#FF6600"
BACKGROUND_COLOR = "#DDDDDD"

# 创建一个窗口
root = tk.Tk()
root.title("专注时钟")
root.geometry("{0}x{1}".format(WIDTH, HEIGHT))

# 创建并设置表盘
hour_label = tk.Label(root, text="小时:", font=("Helvetica", 16, "bold"))
hour_label.pack(pady=10)

minute_label = tk.Label(root, text="分钟:", font=("Helvetica", 12, "bold"))
minute_label.pack(pady=10)

second_label = tk.Label(root, text="秒钟:", font=("Helvetica", 12, "bold"))
second_label.pack(pady=10)

# 设置时间显示的方法
def draw_hours():
    hour_text = tk.StringVar()
    hour_text.set("00")
    hour_label.config(text=hour_text)

    for _ in range(12):
        hour_text.set(f"{hour_text.get()}:00")
        hour_label.config(text=hour_text)

    hour_text.set("12")
    hour_label.config(text=":00")

def draw_minutes():
    minute_text = tk.StringVar()
    minute_text.set("00")
    minute_label.config(text=minute_text)

    for _ in range(60):
        minute_text.set(f"{minute_text.get()}:00")
        minute_label.config(text=minute_text)

    minute_text.set("00")
    minute_label.config(text=":00")

def draw_seconds():
    second_text = tk.StringVar()
    second_text.set("00")
    second_label.config(text=second_text)

    for _ in range(60):
        second_text.set(f"{second_text.get()}:00")
        second_label.config(text=second_text)

    second_text.set("00")
    second_label.config(text=":00")

    time.sleep(0.5)

# 主循环
root.mainloop()
