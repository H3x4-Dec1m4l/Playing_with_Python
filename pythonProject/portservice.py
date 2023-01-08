import socket
ip = input('Digite o endereço de ip: ')
porta = int(input('Digite a porta: '))
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect_ex((ip, porta))
banner = soc.recv(1024)
print(banner)

