score ={
    'Yan':95,
    'Lily':97,
    'Emily':89
}

score['Emily'] = 90
score['Charles'] = 93

for key in score:
    print key, score.get(key)