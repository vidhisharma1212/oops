class Number:
    def __init__(self, num):
        self.num= num

    def __add__(self, num2, num3 ):
        print("Let's add")
        return self.num + num2.num + num3.num
    def __mul__(self, num2 ):
        print("Let's multiply")
        return self.num * num2.num
    
n1= Number(4)
n2= Number(6)
n3= Number(1)
# n4= Number(2)
sum = n1+n2+n3
# mul= n1*n2
print(sum)
# print(mul)