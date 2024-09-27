import socket as s

server_tcp_address = ("10.210.0.49", 12345)

client_tcp = s.socket(s.AF_INET, s.SOCK_STREAM)

try:
    
    client_tcp.connect(server_tcp_address)
    
    print("""in questo programma gestirai la posizione virtuale di un robot,
    per gestirla devi utilizzare le funzioni:
    1 - forward
    2 - backward
    3 - right
    4 - left
    per uscire dalla connessione scrivi 'end'""")
    
    messaggio=input("Inserisci il numero della funzione e la potenza tra 0-100(num, power):  ")   
   
    while messaggio!="end":
        client_tcp.send(messaggio.encode('utf-8'))
        messaggio = client_tcp.recv(4096).decode('utf-8')
        print(f"Il server dice: {messaggio}")
        messaggio=input("Inserisci il numero della funzione e la potenza tra 0-100(num, power):  ")

except KeyboardInterrupt:
    print("\nProgramma interrotto da CTRL + C")

print("Chiusura della connessione...")
client_tcp.close()
