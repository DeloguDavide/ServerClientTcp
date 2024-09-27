import socket as s

server_tcp = s.socket(s.AF_INET, s.SOCK_STREAM)

server_tcp_address = ("10.210.0.164", 12345)

server_tcp.bind(server_tcp_address)

server_tcp.listen(1)
try:
    while True:
        client, address = server_tcp.accept()
        
        messaggio = client.recv(4096).decode('utf-8')
        while messaggio != "end":
            messaggio = messaggio.split(sep=",")
            func = int(messaggio[0])
            power = int(messaggio[1])
            if func == 1:
                messaggio = f"forward, con potenza {power}"
            elif func == 2:
                messaggio = f"backward, con potenza {power}"
            elif func == 3:
                messaggio = f"right, con potenza {power}"
            elif func == 4:
                messaggio = f"left, con potenza {power}"
            else:
                messaggio = "error"
            client.send(messaggio.encode('utf-8'))
            messaggio = client.recv(4096).decode('utf-8')
except KeyboardInterrupt:
    print("Chiusura del socket...")

server_tcp.close()