import python-nmap,sys
N = nmap.PortScanner()
N.scan(sys.argv[1],sys.argv[2])
