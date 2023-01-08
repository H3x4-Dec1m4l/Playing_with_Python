import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("whois.iana.org",43))
site = input('digite o nome do site:')
s.re
res = s.recv(1024).split()
whois = res[19]
s.close()
#print whois

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((whois,43))
s1.send(sys.argv[1]+"\r\n")
resp = s1.recv(1024)
print (resp)