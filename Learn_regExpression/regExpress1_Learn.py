import re
text='Hi, I am Shirley Hilton. I am his wife.'
m = re.findall(r'\b[Hh]i\b', text)
if m:
    print m
else:
    print'not match'