from datetime import datetime
#now=datetime.now()
#print (now.strftime("%I:%M:%S %p"))
#print (now.strftime("%H:%M"))
sd=datetime.strptime(input(),'%I:%M:%S%p')
print(sd.time())
