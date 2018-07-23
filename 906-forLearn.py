inputResult = False
while inputResult == False:
    print'Please input a base number greater than 3:'
    startBase = int(raw_input())
    if startBase < 3:
        print'Input too small. Try again?'
    if startBase >= 3:
        inputResult = True

firstNum = 1
secondNum = 1
fResult = 0
print firstNum
print secondNum
for i in range(0,startBase-2):
    fResult = secondNum + firstNum
    print fResult
    firstNum = secondNum
    secondNum = fResult

