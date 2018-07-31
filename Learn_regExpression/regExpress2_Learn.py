import re

textContent='site sea sue sweet see case sse ssee loses'
m = re.findall(r'\bs\S*e\b',textContent)
print m

textPhone ='I alike a 13876853981 and go to 18621906610 and :18616870959'
p = re.findall(r'1[0-9]{10}', textPhone)
print p
