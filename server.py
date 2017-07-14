import socket,sys

def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 7000
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: "+str(msg))


def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: "+str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error: "+str(msg)+"\n"+" Retrying...")
        socket_bind()

def socket_accept():
    conn,address = s.accept()
    print("Connection has been estabilished | IP: "+address[0]+" | PORT "+str(address[1]))
    send_commands(conn)
    conn.close()

def  send_commands(conn):
    while True:
        cmd = raw_input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024))
            end = ""
            print(client_response,end)


def main():
    socket_create()
    socket_bind()
    socket_accept()

main()


















            













            

            




        
            


