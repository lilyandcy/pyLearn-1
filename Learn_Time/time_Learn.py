import time
starttime=time.time()
print 'start:%f' % starttime
total=0
for i in range(10):
    print i
    total=total+i
print total
endtime=time.time()
print 'end:%f' % endtime
print 'total time:%f' %(endtime-starttime)
