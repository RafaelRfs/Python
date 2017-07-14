import subprocess
import os
import sys

n1 = int(sys.argv[1])
m2 = int(sys.argv[2])

with open(os.devnull,"wb") as limbo:

 print("Devices Online:")

 for n in xrange(n1,m2):
  ip = "192.168.0.{0}".format(n)
  result = subprocess.Popen(["ping","-c","1","-n","-W","2",ip],
                               stdout=limbo, stderr=limbo).wait()
  
  if result == 0:
      print ip, "online"
  
     
