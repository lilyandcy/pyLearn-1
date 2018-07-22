sentence ='I am an English sentence'
string_List= sentence.split()
print string_List
sentence2 = ";I;am;an;English;sentence;"
string_List2=sentence2.split(';')
print string_List2

s=';'
li=['apple','pear','orange']
fruit=s.join(li)
print fruit

word ='hello world!'
for c in word:
    print c
print word[0]
print word[-2]

print word[5:7]
print word[:-5]
print word[:]