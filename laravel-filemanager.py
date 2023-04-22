# -*- coding: utf-8 -*-
import requests,socket
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
		get_soe = requests.get(url+"/laravel-filemanager",headers=headers, timeout=3, verify=False, allow_redirects=False).text
		if "<title>File Manager</title>" in get_soe or "/vendor/laravel-filemanager/" in get_soe:
		   print '[OK!]' + url+''
		   se = open('filemanager.txt', 'a')
		   se.write(url+'/laravel-filemanager\n')
		   se.close()
		else:
		 get_soe = requests.get(url+"/laravel-filemanager",headers=headers, timeout=3, verify=False, allow_redirects=False).status_code
		 #print url + "" +get_soe
   		 if get_soe == 302:
		   print '[OK!]' + url+''
		   se = open('filemanager2.txt', 'a')
		   se.write(url+'\n')
		   se.close()
		 else:
		  
		  get_soe = requests.get(url+"/filemanager",headers=headers, timeout=3, verify=False, allow_redirects=False).text
		  if "<title>File Manager</title>" in get_soe or "/vendor/laravel-filemanager/" in get_soe or "/vendor/laravel-filemanager/" in get_soe:
		      print '[OK!]' + url+''
		      se = open('filemanager.txt', 'a')
		      se.write(url+'/laravel-filemanager\n')
		      se.close()
		  else:
		      get_soe = requests.get(url+"/filemanager",headers=headers, timeout=3, verify=False, allow_redirects=False).status_code
		      #print url + "" +get_soe
		      if get_soe == 302:
		          print '[OK!]' + url+''
		          se = open('filemanager2.txt', 'a')
		          se.write(url+'\n')
		          se.close()
		      else:
		          print '\033[91m[BAD]' + url + '\033[00m'
 except:
		pass

print("""
         filemanager

""")
readsplit = open(raw_input("Ips List .txt: "), 'r').read().splitlines()
numthread = raw_input("Thread: ")
pool = ThreadPool(int(numthread))
for url in readsplit:
 
 pool.add_task(main, url)


pool.wait_completion()
