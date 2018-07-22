f=open('output.txt','w')
f.write('a string you want to write')
f.close()

data='I will be in a file.\nSo cool!'
out=open('output.txt','a')
out.write(data)
out.close()