import os
import sqlite3
import win32crypt
from os import getenv

try:
   username = getenv("username")
   print('#######################################################################################################\n\n')
   print('RFS Chrome DB v2')
   print('#######################################################################################################\n\n')
   arq = str(raw_input('Digite o nome do arquivo do banco de Dados: '))
   db = str(raw_input('Digite o nome do banco de Dados: '))
   tab = raw_input('Digite o nome da tabela:')

   os.system('copy "C:\\Users\\'+getenv("username")+'\\Appdata\\Local\\Google\\Chrome\\User Data\\Default\\'+arq+'" .')
   
   print('\n\n************************************************************************************************************')
   print('[+]Informacoes encontradas: \n\n')
   con = sqlite3.connect(db)
   cursor = con.cursor()
   sql = "SELECT * FROM "+tab
   data = cursor.execute(sql)
   for i in data:
      print(i)
      print('\n')
   con.close()

except Exception,e:
   print('\n [-] Banco de Dados nao encontrado, \n Erro: \n %s '%e)

