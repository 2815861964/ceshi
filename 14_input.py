# BMI = 体重 / (身高 ** 2)
try:
    user_weight = float(input("请输入您的体重（单位：kg）："))
    user_height = float(input("请输入您的身高（单位：m）："))
    user_BMI = user_weight / (user_height) ** 2

except ValueError:
    print("输入类型错误")
except ZeroDivisionError:
    print("身高不能为零")
else:
    print("您的BMI值为：" + str(user_BMI))
finally:
    print("程序执行结束")