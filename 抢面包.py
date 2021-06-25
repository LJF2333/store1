import threading
import time
baskets=0
cost = 2
class cooks(threading.Thread):
    username=""
    count = 0
    def run(self) -> None:
        global baskets
        while True:
            if baskets<500 :
                baskets=baskets+1
                self.count=self.count+1
                time.sleep(3)
                print(self.username,"在制作面包，现在篮子里有",baskets,"个面包")
            elif baskets ==500:
                time.sleep(0.1)
            else:
                print(self.username,"制作了",self.count,"个面包")
                break



class customer(threading.Thread):
    customerName=""
    count=0
    money=1000
    price=2
    def run(self) -> None:
        global baskets
        while True:
            if baskets==0:
                time.sleep(2)
                print("请稍等，厨师正在制作，您已购买", self.count, "个面包，您的余额为", self.money)
            elif self.money==0:
                break
            elif self.money>0:
                baskets=baskets-1
                self.count=self.count+1
                self.money=self.money-self.price
                print(self.customerName, "正在购买面包，买了",self.count,"个面包，还有" ,baskets, "个面包")







c1=cooks()
c2=cooks()
c3=cooks()

c1.username="张厨师"
c2.username="李厨师"
c3.username="王厨师"

c1.start()
c2.start()
c3.start()

p1=customer()
p2=customer()
p3=customer()
p4=customer()
p5=customer()

p1.customerName="顾一"
p2.customerName="顾二"
p3.customerName="顾三"
p4.customerName="顾四"
p5.customerName="顾五"

p1.start()
p2.start()
p3.start()
p4.start()
p5.start()