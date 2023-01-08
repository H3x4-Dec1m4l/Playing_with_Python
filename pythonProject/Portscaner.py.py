import socket
ip = str(input('digite um endereço ip:'))
for p in range(1,65536):
    sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if sok.connect_ex((ip, p)) == 0:
        print(f'Porta {p} aberta')
        sok.close()




