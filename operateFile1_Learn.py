file = open('scores.txt','w')
line1 ='Sam 23 35 44 47\n'
line2 ='Yan 60 77 68\n'
line3 ='Lily 97 99 89 91\n'
line4 ='Liang 100\n'
lines =[line1,line2,line3,line4]
file.writelines(lines)
file.close()

operateFile = open('scores.txt')
fileLines = operateFile.readlines()
operateFile.close()
results=[]

for fileLine in fileLines:
    data = fileLine.split()
    scoreSum = 0
    for score in data[1:]:
        scoreSum=scoreSum + int(score)
    result = '%s\t: %d\n' %(data[0], scoreSum)
    results.append(result)

output = open('result.txt','w')
output.writelines(results)
output.close()