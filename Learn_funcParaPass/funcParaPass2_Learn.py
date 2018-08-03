def calcSum(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum

print calcSum(1,2,3)
print calcSum(123,456)
print calcSum()