import random
num=random.randint(0,500)
i=0
a=5000
c=0
while i<20:
    number=input("请输入您猜的数：  ")
    number=int(number)
    if number > num:
        a = a - 500
        c=c+1
        print("数字过大！继续加油。￥",a)
    elif number < num:
        a = a - 500
        c = c + 1
        print("数字过小！继续加油。￥",a)
    else:
        a = a + 3000
        print("恭喜您猜中了！本次数字为： ",num,"￥",a,i,c)
        c=0
        break
    if a==0:
        print("金币为0,暂停游戏，请及时充值！")
        break
    if c==15:
       print("超过输入次数，系统已锁定！")
       break
    i = i + 1
    print(i,a,c)



