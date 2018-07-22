num = 10
guessResult = False
print'Please guess the number:'
while guessResult == False:
    answer = int(raw_input())
    if answer < num:
        print 'Too small'
    if answer > num:
        print 'Too big'
    if answer == num:
        print 'Bingo'
        guessResult = True