import os,sys,time,requests,json
from requests import post
def balik():
   f = input("\033[31mQuieres seguir ejecutando el script: (s/n): \033[31m")
   if f == "s":
      os.system("python3 spamcall-v6.0.py")
   elif f == "n":
        sys.exit("\033[31m")

m = '\033[1;31m' 
b = '\033[1;36m'       
k = '\033[1;33m' 
h = '\033[1;32m'
u = '\033[1;35m'
p = '\033[1;37m'
ut = '\033[1;34m'
     

os.system('clear')
def asw(b):
  for m in b + "\n":
      sys.stdout.write(m)
      sys.stdout.flush()
      time.sleep(3./100)

def lo(s):
  for c in s  + "\n":
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(3./100)

asw(f"{m}Entrando al script...................................................................................")
os.system("clear")

                                                       
asw(f"{m};;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
asw(f"{m}                             SPAM 6.0    ")	
asw(f"{m};;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
asw(f"{m} Creador: Juan Olmo Mendoza  ")
asw(f"{m} Github: Juan3817381  ")
asw(f"{m}----------------------------------------------------------------------------")
asw(f"{m}| Correo de Errores: Errorprograma2@gmail.com                              |")
asw(f"{m}----------------------------------------------------------------------------")
asw(f"{m}[1] Spam de Llamadas   ")
print()                  
asw(f"{m}[2] Spam de sms   ")
print()
asw(f"{m}[3] Salir   ")
print()
f = input("\033[31m")
if f == "1":
   os.system("python3 script.py")
if f == "2":
   os.system("python3 script2.py")
elif f == "3":
     sys.exit("\033[31m")


