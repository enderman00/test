import tkinter as tk
from tkinter import messagebox

def show_hello():
    messagebox.showinfo("提示", "Hello World!")

# 创建主窗口
root = tk.Tk()
root.title("Hello World 程序")
root.title("Hello World 程序")
# 设置窗口大小
root.geometry("300x200")  # 设置窗口大小
# 创建标签
label = tk.Label(root, text="Hello World!", font=("Arial", 16))

# 创建按钮
button = tk.Button(root, text="点击我", command=show_hello)
button.pack(pady=20)  # 添加一些内边距使按钮位置更美观

# 启动主循环//
root.mainloop()
#dfghdfhdf