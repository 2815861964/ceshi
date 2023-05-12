import pyperclip3
# pyperclip3.copy('Hello world!')
# pyperclip3.paste()
# waitForPaste当剪切板非空才返回，waitForNewPaste当剪切板内容更改返回,好像用不了
while(True):
    a = pyperclip3.waitForNewPaste(5)