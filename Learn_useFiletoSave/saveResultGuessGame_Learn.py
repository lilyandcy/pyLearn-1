import random
name = raw_input('Please input your name: ')
f = open('game.txt')
lines = f.readlines()
f.close()

scores={}
for l in lines:
    s=l.split()
    scores[s[0]]=s[1:]
score = scores.get(name)
if score is None:
    score =[0,0,0]
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
if game_times >0:
    avg_times = float(total_times) / game_times
else:
    avg_times = 0
print'%s have played %d times, minimun %d to guess the right answer, average %.2f to get the right answer' %(name, game_times,min_times,avg_times)

num = random.randint(1,100)
times = 0
print'Guess what I think?'
bingo = False
while bingo == False:
    answer = int(raw_input())
    times = times + 1
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

if game_times == 0 or times < min_times:
    min_times = times
total_times = total_times + times
game_times = game_times +1

scores[name]= [str(game_times), str(min_times), str(avg_times)]
result = ''
for n in scores:
    line = n+' '+' '.join(scores[n]) + '\n'
    result = result + line
f = open('game.txt','w')
f.write(result)
f.close()
