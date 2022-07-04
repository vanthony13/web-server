from socket import *
import requests

# serverName = '192.168.1.50'
serverPort = 3000

def verifyCmd(cmd):
    cmd = cmd.split(" ")
    if len(cmd) < 4:
        return None
    else:
        return cmd
count = 0

print("Commands examples: ")
print("Ex1: whit response conde: ")
print("Server -> localhost 3000 -h ArqRedes.html")
print("Ex2: whit html file display: ")
print("Server -> localhost 3000 -b ArqRedes.html\n\n")

print("____________________client___________________________\n")

while True:
    # the cmd variable is to receive an string like this: localhost 3000 -h Facebook.html
    while True:
        cmd = input("Server: ")
        verfcmd = verifyCmd(cmd)
        if verfcmd != None:
            serverName = verfcmd[0]
            serverPort = int(verfcmd[1])
            opc = verfcmd[2]
            site = verfcmd[3]

            if opc == "-h":
                try:
                    clientSocket = socket(AF_INET, SOCK_STREAM)
                    clientSocket.connect((serverName, serverPort))
                    clientSocket.send(f'''Get /{site} HTTP/1.1
Host: localhost:{serverPort}
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0
Accept: image/webp,*/*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Referer: http://{serverName}:{serverPort}/{site}
Upgrade-Insecure-Requests: {count}'''.encode())
                    modifiedSentence = clientSocket.recv(1024).decode()
                    print('From Server: ', modifiedSentence[:1000])
                    clientSocket.close()
                    count += 1
                except OSError:
                    print("File not found")
            elif opc == "-b":
                res = requests.get(f'http://{serverName}:{serverPort}/{site}')

                print("Your Request: \n---------------------------------------------------------------\n")
                print(res.text[:1000])
                print("\n---------------------------------------------------------------\n")
            else:
                print("OSCommand: [Erro]")
        else:
            print("OSCommand: [Erro]")
        