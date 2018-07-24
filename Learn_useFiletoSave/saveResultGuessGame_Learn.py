import random

f = open('game.txt')
score = f.read().split()
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
if game_times >0:
    avg_times = float(total_times) / game_times
else:
    avg_times = 0
print'You have played %d times, minimun %d to guess the right answer, average %.2f to get the right answer' %(game_times,min_times,avg_times)

num = random.randint(1,100)
print'Guess what I think?'
bingo = False
while bingo == False:
    answer = int(raw_input())
    if answer < 0:
        print 'Exit the Game'
        break
    if answer > num:
        print'too big'
    if answer < num:
        print'too small'
    if answer == num:
        print'Bingo'
        bingo = True
