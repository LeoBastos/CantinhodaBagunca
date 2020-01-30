import socket


ip = input("Digite o IP ou endereco: ")

ports = []
count = 0

while count < 2:
    ports.append(int(input("Digite a porta: ")))
    count += 1


for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)
    code = client.connect_ex((ip, port))

    if code == 0:
        print (str(port) + " -> Porta aberta")
    else:
        print (str(port) + " -> Porta fechada")

print ("Scan Finalizado")


####netstat -a ######