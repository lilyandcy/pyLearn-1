from random import choice

score_you =0
score_com =0
direction =['left','center','right']

def unit_Kick(turn):
    print '==== Round %d - You Kick! ====' %(turn)
    print 'Choose one side to shoot:'
    print 'left, center, right'
    you = raw_input()
    print 'You kicked ' + you
    com = choice(direction)
    print 'Computer saved '+ com
    if you!=com:
        return True
    else:
        return False
def unit_Save(turn):
    print '==== Round %d - You Save! ====' %(turn)
    print 'Choose one side to save:'
    print 'left, center, right'
    you =raw_input()
    print 'You saved ' + you
    com = choice(direction)
    print'Computer kicked ' + com
    if you == com:
        return True
    else:
        return False

for i in range(1,6):
    kick_Result = unit_Kick(i)
    if kick_Result == True:
        print 'Goal!'
        score_you+=1
    else:
        print 'Oops...'
    print 'Score: %d(you) - %d(com)\n' %(score_you,score_com)
    save_Result = unit_Save(i)
    if save_Result == True:
        print 'You saved!'
    else:
        print 'Oops...'
        score_com+=1
    print 'Score: %d(you) - %d(com)\n' % (score_you, score_com)
if score_you > score_com:
    print'You win!'
elif score_you < score_com:
    print'You lose!'
else:
    print'You tied!'