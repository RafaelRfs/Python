import urllib,os

print("#########################################################")
print("\n \n \n RFS File Downloader \n \n \n")
print("#########################################################\n")
try:
 url = str(raw_input('Digite a url: '))
 t =  urllib.urlopen(url)
 source = str(raw_input('Digite o source HTML:'))
 content = str(t.read())
 find = "<"+source+" src="
 mp4 = "."+str(raw_input("Digite o tipo de arquivo : "))
 posicao = content.index(find)+len(find)
 posicaoMp4 = content.index(mp4)+len(mp4)
 dif = posicaoMp4 - posicao
 arquivo = content[posicao + 1: posicao + dif]

 if(len(arquivo) > 0):
     print("[+] Arquivo encontrado: \n %s   "%arquivo)
     if(urllib.urlretrieve ( arquivo)):
         print("[+] Download feito com sucesso do arquivo "+mp4)
     else:
         print("[+] Erro ao fazer download do arquivo")



except:
    print("[-] Erro ao encontrar o arquivo ")


    
print("\n######################################################### \n")

