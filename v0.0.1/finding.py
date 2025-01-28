import os


def finding(file_first=f"{os.path.abspath('..')}"):
    """
    显示当前目录(或指定目录)下的所有文件和文件夹(包括子文件夹下的)
    :param file_first: 开始的目录
    :return: list|None
    """
    files = os.listdir(file_first)
    files_ = [f"{file_first}\\{file}" for file in files]

    for file_sub in files:
        if os.path.isdir(f"{file_first}\\{file_sub}"):
            files_sub = finding(f"{file_first}\\{file_sub}")
            if files_sub:
                files_ = files_ + files_sub
    if files_:
        return files_
    else:
        return None


if __name__ == "__main__":
    for i in finding(r"D:\pan_Python"):
        print(i)
