import os
import random
import string
import secrets
import tkinter as tk
from tkinter import simpledialog, messagebox

end_name = ''

root = tk.Tk()
root1 = tk.Toplevel(root)
root1.withdraw()

window_width = 280
window_height = 170

# 处理难度
def get_user_input(entry):
    user_input = entry.get()
    try:
        # 转换为整数
        user_input = int(user_input)
        # 验证输入是否大于0
        if user_input > 0:
            root.withdraw()
            generate_files(user_input)
        else:
            tk.messagebox.showwarning("错误", "请输入大于0的整数")
    except ValueError:
        # 如果无法转换为整数，弹出错误提示
        tk.messagebox.showerror("错误", "请输入有效的整数")


# 自定义难度
def choose():
    root.deiconify()
    root.title("Cyber_box难度选择")
    root.geometry(f"{window_width}x{window_height}")
    # 创建说明标签
    label = tk.Label(root, text="自定义难度，1最简单，无上限")
    label.pack()
    # 创建输入框
    entry = tk.Entry(root)
    entry.pack()
    # 创建按钮，点击按钮时调用 get_user_input 函数
    button = tk.Button(root, text="确认", command=lambda:get_user_input(entry))
    button.pack()
    # 启动主循环
    root.mainloop()


# 生成指定长度的随机字符串
def generate_random_string(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


# 在指定文件夹folder_path内创建大小在[min_size_kb, max_size_kb]范围内的无后缀文件
def create_random_file(folder_path, min_size_kb=5, max_size_kb=30):
    file_name = generate_random_string()
    file_path = os.path.join(folder_path, file_name)
    # 随机生成文件大小
    file_size = random.randint(min_size_kb * 1024, max_size_kb * 1024)
    # 写入随机数据到文件
    with open(file_path, 'wb') as file:
        file.write(os.urandom(file_size))

# 读取文件并修改文件
def insert_success(folder_path):
    all_files=[]
    # 遍历所有文件夹里的文件
    for roots, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(roots, file)
            # 插入数组中
            all_files.append(file_path)
    if len(all_files)>0:
        # 随机选择文件
        random_file=random.choice(all_files)
        # 目标文件新名字和原始路径
        suc_name=secrets.token_urlsafe(2)
        suc_file=os.path.join(os.path.dirname(random_file),suc_name)
        # 修改文件名
        os.rename(random_file,suc_file)
        global end_name
        end_name = suc_name
        # print(f"已将文件 {random_file} 重命名为 {suc_name}")


# 检查答案
def check_user_input(entry1):
    user_input1 = entry1.get()

    if user_input1 == end_name:
        tk.messagebox.showinfo("Success", "恭喜！你成功找到了Ta！请期待下次更新~")
        root1.destroy()
    else:
        tk.messagebox.showwarning("Error", "不对哦，继续加油")


# 创建主窗口
def windows():
    # 显示窗口
    root1.deiconify()
    root1.title("提交答案")
    # 创建文本框
    entry1 = tk.Entry(root1)
    entry1.pack(pady=10)
    root1.geometry(f"{window_width}x{window_height}")
    # 创建按钮，点击时检查用户输入
    button1 = tk.Button(root1, text="输入Ta的文件名", command=lambda:check_user_input(entry1))
    button1.pack()
    # 运行主循环
    root1.mainloop()

# 创建文件夹
def generate_files(user_times):
    # 获取桌面路径
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    # 新建父文件夹
    folder1_path = os.path.join(desktop_path, 'Cyber_box')
    os.makedirs(folder1_path, exist_ok=True)
    print(f"正在初始化赛博盲盒...请稍等...")
    print("--" * 30)
    # 循环变量定义（一层一个变量）
    i = 1
    x = 1
    u = 1
    # 开始创建
    while i <= user_times:
        # 建立第一层子文件夹
        folder2_path = os.path.join(folder1_path, 'Welcome' + str(i))
        os.makedirs(folder2_path, exist_ok=True)
        # 建立第二层子文件夹(数量*2，注意大小)
        while x <= user_times * 2:
            folder3_path = os.path.join(folder2_path, 'Search' + str(x))
            os.makedirs(folder3_path, exist_ok=True)
            # 在该层中插入文件
            while u <= user_times:
                # 创建大小在30KB到120KB之间的无后缀文件
                create_random_file(folder3_path)
                u += 1
            # 重置变量继续循环
            x += 1
            u = 0
        # 重置变量继续循环
        x = 0
        i += 1

    # 读取所有文件并修改随机文件名字
    path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Cyber_box')
    insert_success(path)
    # 游戏说明，隐藏窗口
    tk.messagebox.showinfo(title="Cyber_box说明",
                           message="初始化成功！\n在电脑桌面进入Cyber_box文件夹\n在一堆的随机字符串文件中，找到那个与众不同的，你就成功啦\n现在开始游戏叭")
    windows()

if __name__ == "__main__":
    choose()
