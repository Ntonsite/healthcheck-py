from __future__ import print_function
import psutil


a = psutil.cpu_times()

b = psutil.virtual_memory()[2]

print ('*********************************************************************')
print('memory % used:', psutil.virtual_memory()[2])

print (a);

print ('*********************************************************************')

if b > 50:
	print ("Status is Bad")
else:
	print("Status is OK")