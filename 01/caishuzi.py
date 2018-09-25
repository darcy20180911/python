import random
print ("*******猜字谜******")
xdd=int(input("请输入一个两位数的整数"))
shu=random.randint(10,99)
while xdd!=shu:
    if  xdd>=100 or xdd<10:
        print("范围不对")
        xdd = int(input("请输入一个两位数的整数"))
    elif xdd>shu:
        print("da")
        xdd = int(input("请输入一个两位数的整数"))
    elif xdd<shu:
        print("xiao")
        xdd = int(input("请输入一个两位数的整数"))
print("right")



