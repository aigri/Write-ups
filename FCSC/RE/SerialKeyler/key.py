import socket,time

HOSTNAME = "challenges2.france-cybersecurity-challenge.fr"
PORT = 3001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOSTNAME, PORT))
answer=''
i=0
msg = sock.recv(1024)
str = msg.decode().split(": ")[1].partition('\n')[0]
print(str)

for y in str:
        answer = answer[0:i] + chr(ord(y)^31)
        i+=1
print(answer[::-1])
sock.sendall(answer[::-1].encode() + b'\n')


for z in range(100):
        answer=''
        i=0
        msg = sock.recv(1024)
        print("Message reçu : " + msg.decode())
        str = msg.decode().split(": ")[1].partition('\n')[0]
        for y in str:
                answer = answer[0:i] + chr(ord(y)^31)
                i+=1
        print("Réponse : " + answer[::-1])
        sock.sendall(answer[::-1].encode() + b'\n')
        time.sleep(1)
sock.close() 