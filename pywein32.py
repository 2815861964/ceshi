import win32con

import win32gui

import time

import random

QQWin= win32gui.FindWindow("TXGuiFoundation","王晨")
class_name = win32gui.GetClassName(QQWin)
title = win32gui.GetWindowText(QQWin)
rect = win32gui.GetWindowRect(QQWin)
print(rect)