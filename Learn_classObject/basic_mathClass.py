# coding=utf-8

class mathOperation:
    num1 =1
    def plus(self,num):
        result = self.num1 + num
        return result
    def minus(self,num):
        result=self.num1 - num
        return result
    def multiply(self,num):
        result=self.num1 * num
        return result
    def divide(self,num):
        result = self.num1 // num
        return result
    def mod(self,num):
        result = self.num1 % num
        return result

mathInstance = mathOperation()

print'请输入要计算的两个整数：'
num1 = int(input())
mathInstance.num1 = num1
num2 = int(input())


plusResult = mathInstance.plus(num2)
minusResult = mathInstance.minus(num2)
multiplyResult = mathInstance.multiply(num2)
print'%d + %d = %d\n' %(num1,num2,plusResult)
print'%d - %d = %d\n' %(num1,num2,minusResult)
print'%d x %d = %d\n' %(num1,num2,multiplyResult)
try:
    divideResult = mathInstance.divide(num2)
    modResult = mathInstance.mod(num2)
    print'%d / %d = %d ...... %d\n' %(num1,num2,divideResult,modResult)
except:
    print'%d / %d = 除数不能为0\n' %(num1,num2)

