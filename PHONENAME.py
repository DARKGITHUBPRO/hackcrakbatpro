import socket 
hostName= socket.gethostname()
ipAdd=socket.gethostbyname(hostName)
#Phone=gethostNumber()
##print ('Phone : '+hostNumber)
print ('     PC Name or Phone Name : '+hostName)
print ('     IP-Address : '+ ipAdd)
