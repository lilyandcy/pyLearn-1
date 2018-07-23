print'Please input a number to want to add from 1 to it.'
maxNum = int(raw_input())
startNum = 1
result = 0
while startNum <= maxNum:
    result = result + startNum
    startNum = startNum + 1
print result