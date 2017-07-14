import urllib
url  = "site.com"
diretorios = ["adm", "painel", "admin", "administrador", "login","adminstrator"]
for i in diretorios:
       alvo = url +i
       res = urllib.request.urlopen(alvo) 
     
       if res.getcode() == 200:
          print (i)
          print  ("Encontrado: " + alvo)
          exit()

print ("Nao encontrado ")




