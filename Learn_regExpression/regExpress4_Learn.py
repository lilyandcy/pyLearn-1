import re
phoneContent='(021)88776543 010-55667890 02584453362 057166345673'
p0=re.findall(r'\(?0\d{2,3}[) -]?\d{7,8}', phoneContent)
p1=re.findall(r'\(0\d{2,3}\)\d{7,8}|0\d{2,3}[ -]?\d{7,8}', phoneContent)
print p0
print p1
