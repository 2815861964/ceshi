import time

from pykeyboard import *
from pymouse import *

m = PyMouse() #建立鼠标对象
k = PyKeyboard() #建立键盘对象

time.sleep(2)
location1=m.position()
print("获得")
time.sleep(4)
location2=m.position()


m.click(location1[0],location1[1])
k.type_string('111')
m.click(location2[0],location2[1])