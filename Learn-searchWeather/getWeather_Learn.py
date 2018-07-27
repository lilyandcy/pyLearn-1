# coding=utf-8
import urllib2
import json
from city import city

cityname=raw_input('Which city\'s weather do you want to search?\n')
citycode = city.get(cityname)
if citycode:
    try:
        url =('http://www.weather.com.cn/data/cityinfo/%s.html' %citycode)
        content=urllib2.urlopen(url).read()
        data = json.loads(content)
        result = data['weatherinfo']
        str_temp = ('%s\n%s ~ %s') %(
            result['weather'],
            result['temp1'],
            result['temp2']
        )
        print str_temp
    except:
        print 'Search failure'
else:
    print 'City not found'