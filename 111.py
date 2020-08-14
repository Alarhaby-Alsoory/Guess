import socket
import sys

print ('Inter Your Target >> ')

hostname = input ()
ip = socket.gethostbyname (hostname)
print ('Your Host Name Is: ' , hostname , '\n' , 'Your Target Ip Is: ' , ip)