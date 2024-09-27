import socket as s

server_tcp=s.socket(s.AF_INET, s.SOCK_STREAM) 

server_tcp_address = ("10.210.0.164", 12345)

server_tcp.bind(server_tcp_address)

server_tcp.listen(1)

try:
    while True:

        client,address=server_tcp.accept()
        messaggio=server_tcp.recv(4096).decode('utf-8')

        while messaggio != "end":

            
            print(f"Connessione da {address}")
            messaggio=client.recv(4096).decode('utf-8')  
            messaggio = messaggio.split(sep=",")
            func =int(messaggio[0])
            power = int(messaggio[1])
            if func == 1:
                messaggio="forwrd"
            elif func==2:
                messaggio="backword"
            elif func == 3:
                messaggio="right"
            elif func == 4:
                messaggio = "left"
            else:
                print("error")
            
            client.send(messaggio.encode('utf-8'))
            messaggio=server_tcp.recv(4096).decode('utf-8')

except KeyboardInterrupt:
    print("\nProgramma interrotto da CTRL + C")


print("Chiusura della connessione...")
server_tcp.close()
