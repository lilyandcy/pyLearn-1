from random import randint
setNum = randint(1,100)
print'What number do you want to guess?'
resultGuess = False
while resultGuess == False:
    resultNum = int(raw_input())
    if resultNum > setNum:
        print'%d is bigger number. Try again?' %resultNum
    if resultNum < setNum:
        print'%d is smaller number. Try again?' %resultNum
    if resultNum == setNum:
        print 'Great, %d is the correct number!' %resultNum
        resultGuess = True

