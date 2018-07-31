import re
textContent='123 4839 9039 ab89 98 afbac3d'
t0=re.findall(r'\b\d{4}\b', textContent)
t1=re.findall(r'\b\d+\b', textContent)
t2=re.findall(r'\b\d\b', textContent)
t3=re.findall(r'\b\d*\b', textContent)
t4=re.findall(r'[^0-9\s]+', textContent)
print t0
print t1
print t2
print t3
print t4