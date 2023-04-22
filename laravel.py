# -*- coding: utf-8 -*-
import requests
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

def main(url):
 if "://" in url:
      url = url
 else:
	  url = "http://"+url
 if url.endswith('/'):
	  url = url[:-1]
 try:
		headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
		#gols3 = 'Chitoge kirisaki'
		get_soe = requests.get(url+"/sites/all/libraries/elfinder/php/connector.php",headers=headers, timeout=3, verify=False, allow_redirects=False).text
		if "errUnknownCmd" in get_soe:
		   print ('[OK!]' + url+'/c.php')
		   se = open('content.txt', 'a')
		   se.write(url+'/sites/all/libraries/elfinder/php/connector.php\n')
		   se.close()
		else:
		 get_soe = requests.get(url+"/elFinder/php/connector.php",headers=headers, timeout=3, verify=False, allow_redirects=False).text
		 if "errUnknownCmd" in get_soe:
		   print ('[OK!]' + url+'/wso.php')
		   se = open('content.txt', 'a')
		   se.write(url+'/elFinder/php/connector.php\n')
		   se.close()
		 else:
		  get_soe = requests.get(url+"/js/plugins/elfinder/php/connector.php",headers=headers, timeout=3, verify=False, allow_redirects=False).text
		  if "errUnknownCmd" in get_soe:
		   print ('[OK!]' + url+'/js/plugins/elfinder/php/connector.php')
		   se = open('content.txt', 'a')
		   se.write(url+'/js/plugins/elfinder/php/connector.php\n')
		   se.close()
		  else:
		   get_soe = requests.get(url+"/vendor/studio-42/elfinder/php/connector.php",headers=headers, timeout=3, verify=False, allow_redirects=False).text
		   if "errUnknownCmd" in get_soe:
		     print ('[OK!]' + url+'/Chitoge.php?Chitoge')
		     se = open('content.txt', 'a')
		     se.write(url+'/vendor/studio-42/elfinder/php/connector.php\n')
		     se.close()
		   else:
		    get_soe = requests.get(url+"/jscripts/elfinder/php/connector.php",headers=headers, timeout=3, verify=False, allow_redirects=False).text
		    if "errUnknownCmd" in get_soe:
		     print ('[OK!]' + url+'/marijuana.php')
		     se = open('content.txt', 'a')
		     se.write(url+'/jscripts/elfinder/php/connector.php\n')
		     se.close()
		    else:
		       get_soe = requests.get(url+"/plugin/elfinder/php/connector.php",headers=headers, timeout=3, verify=False, allow_redirects=False).text
		       if "errUnknownCmd" in get_soe:
		        print('[OK!]' + url+'/shell.php')
		        se = open('content.txt', 'a') 
		        se.write(url+'/plugin/elfinder/php/connector.php\n') 
		        se.close()
		       else:
		          get_soe = requests.get(url+"/timthumb.php",headers=headers, timeout=3, verify=False, allow_redirects=False).text
		          if "TimThumb version : 1." in get_soe:
		           print('[OK!]' + url+'/shell.php')
		           se = open('content.txt', 'a') 
		           se.write(url+'/timthumb.php\n') 
		           se.close()
		          else:
		           get_soe = requests.get(url+"/elfinder/php/connector.php",headers=headers, timeout=3, verify=False, allow_redirects=False).text
		           if "errUnknownCmd" in get_soe:
		            print ('[OK!]' + url+'/elFinder')
		            se = open('content.txt', 'a')
		            se.write(url+'/elfinder/php/connector.php\n')
		            se.close()
		           else:
		              get_soe = requests.get(url+"/_file-manager/php/connector.php",headers=headers, timeout=3, verify=False, allow_redirects=False).text
		              if "errUnknownCmd" in get_soe:
		                print ('[OK!]' + url+'/shell.php')
		                se = open('content.txt', 'a')
		                se.write(url+'/_file-manager/php/connector.php\n')
		                se.close()
		              else:
		               get_soe = requests.get(url+"/jquery-file-upload/server/php/",headers=headers, timeout=3, verify=False, allow_redirects=False).text
		               if '"files":' in get_soe:
		                print ('[OK!]' + url+'/jquery-file-upload/server/php/')
		                se = open('content.txt', 'a')
		                se.write(url+'/jquery-file-upload/server/php/\n')
		                se.close()
		               else:
		                get_soe = requests.get(url+"/server/php/",headers=headers, timeout=3, verify=False, allow_redirects=False).text
		                if '"files":' in get_soe:
		                    print ('[OK!]' + url+'/server/php/')
		                    se = open('content.txt', 'a')
		                    se.write(url+'/server/php/\n')
		                    se.close()
		                else:
		                 get_soe = requests.get(url+"/file-upload/server/php/",headers=headers, timeout=3, verify=False, allow_redirects=False).text
		                 if '"files":' in get_soe:
		                  print ('[OK!]' + url+'/file-upload/server/php/')
		                  se = open('content.txt', 'a')
		                  se.write(url+'/file-upload/server/php/\n')
		                  se.close()
		                 else:
		                   get_soe = requests.get(url+"/kcfinder/upload.php",headers=headers, timeout=3, verify=False, allow_redirects=False).text
		                   if 'alert("Unknown error");' in get_soe:
		                    print ('[OK!]' + url+'/kcfinder/upload.php')
		                    se = open('content.txt', 'a')
		                    se.write(url+'/kcfinder/upload.php\n')
		                    se.close()
		                   else:
		                    print ("[BAD]" + url)
 except:
		pass

print("""
         coco

""")
readsplit = open(raw_input("Ips List .txt: "), 'r').read().splitlines()
numthread = raw_input("Thread: ")
pool = ThreadPool(int(numthread))
for url in readsplit:
 
 pool.add_task(main, url)


pool.wait_completion()
