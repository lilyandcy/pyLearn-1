from random import randint

num = randint(1,100)

print 'What number do you guess?'
guessResult = False

while guessResult == False:
    answer = int(raw_input())
    if answer > num:
        print'Too big guess. Try again?'
    if answer < num:
        print'Too small guess. Try again?'
    if answer == num:
        print'You are absolutely right!'
        guessResult = True
