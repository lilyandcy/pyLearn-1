from random import randint
def isEqual(num1, num2):
    if num1<num2:
        print 'too small'
        return False
    elif num1>num2:
        print 'too big'
        return False
    else:
        print 'bingo!'
        return True

num = randint(1,100)
print 'Guess what I think?'
guessResult = False
while guessResult == False:
    inputResult = input()
    guessResult=isEqual(inputResult,num)



