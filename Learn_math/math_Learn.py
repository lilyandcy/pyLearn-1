import math

def function_Complex(a,b,c):
    try:
        result1 = (-b + math.sqrt(b*b-4*a*c))/(2*a)
        result2 = (-b - math.sqrt(b*b-4*a*c))/(2*a)
        return (result1,result2)
    except:
        return 'No valid input'

print function_Complex(3,12,2)

