import nmap

N = nmap.PortScanner()
alvo = str(raw_input(' Alvo: '))
porta = str(raw_input(' Porta: '))

N.scan(alvo, porta)

for host in N.all_hosts():
 print('#############################')
 print('[+]Host: %s(%s)'%(host,N[host].hostname()))
 print('[+]State: %s'%N[host].state())
 for proto in N[host].all_protocols():
  print('################################')
  print('[+]Protocolo: %s'%proto)

  lport = N[host][proto].keys()
  lport = list(lport)
  lport.sort()

  for port in lport:
    print('[+]porta: %s\testado: %s'%(port, N[host][proto][port]['state']))