import os,sys,strftime
import re,time
import requests
import colorama

from colorama import Fore, Stlye, init, Back
init(autoreset=True)

merah = (Fore.RED + Style.BRIGHT)
biru =(Fore.CYAN + Style.BRIGHT)
ungu = (Fore.MAGENTA + Style.BRIGHT)
kuning = (Fore.YELLOW + Style.BRIGHT)
hijau = (Fore.GREEN + Style.BRIGHT)

from time import sleep
def logo():
	os.system('clear')
	   x=(biru+'========================================================================')
	print(x)
	print(hijau+'                    Script Python INSTALL EHCP')
	print(' \nVersi   : 1.0 ')
	print(ungu+' Creator : Muhaminudin')
	print(kuning+' \nScript Untuk Memudahkan Dalam Menginstall EHCP')
	print(x)
	print('\n\n')

#Main
c= requests.Session()
url = c.get.text('https://raw.githubusercontent.com/udinartstar/debian/master/repo.udin')
if not os.path.exists('./bahan'):
	os.makedirs('./bahan')
f1=open('./bahan/repo','w')
f1.write(url)
f1.close()
