from copy import deepcopy
a =[3,4]
m =[1,2,a,[5,a]]
n = deepcopy(m)
n[3][1][0] = -1
print(n)