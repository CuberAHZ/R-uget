import win32api
import win32con

win32api.SetFileAttributes("D:\\git_\\R-uget", win32con.FILE_ATTRIBUTE_HIDDEN)