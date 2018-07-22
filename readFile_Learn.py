f = open('data.txt')
f_data=f.read()
f.seek(0)
f_dataline=f.readline()
f.seek(0)
f_datalineList=f.readlines()
print f_data
print f_dataline
print f_datalineList
f.close()