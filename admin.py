# StaY MaD
# Reverse IP Mass Admin finder v2
# Kyubi referrence : #http://img1.wikia.nocookie.net/__cb20120730083419/powerlisting/images/1/1a/Kyuubi-fire-chakra.jpg
# http://naruto.wikia.com/wiki/Kurama
# Have fun     :::: MaDLeeTs.com ::::
# x
import urllib2, urllib, socket, argparse, sys, os, threading, Queue, re, httplib, itertools
import json

# list of admins , Extend it if you want more results results

getx = ['/admin/', '/administrator/', '/admin-cp/', '/webways-admin/', '/admin_login/']

found = []
# Queue

q = Queue.Queue()
useragent = "Mozilla/5.0 (Windows NT 5.1; rv:24.0) Gecko/20100101 Firefox/24.0"
# parser
parser = argparse.ArgumentParser(__file__, description="Reverse IP admin finder ./VIRkid @MaDLeeTs")
parser.add_argument("--timeout", "-t", help="Custom connection timeout", type=float, default=2.0)
parser.add_argument("--target", "-u", help="Specify the target URL/IP")
parser.add_argument("--proxy", "-p", help="Proxy e.g 127.0.0.1:8080 ")
parser.add_argument("--thrd", "-w", help="Number of threads", type=int, default=2)
parser.add_argument("--src", "-s", help="Source of Reverse IP (yougetsignal / viewdns ) default : yougetsignal", type=str, default="youget")

args = parser.parse_args()
# cleaner
if sys.platform == "linux" or sys.platform == "linux2":
    cl = "clear"
else:
    cl = "cls"
os.system(cl)

def banner():
    print "\t\t*********************************************"
    print "\t\t*                                           *"
    print "\t\t*        Kyuubi R-admin Buster              *"
    print "\t\t*             .:VIRkid:.                    *"
    print "\t\t*       Usage: python script.py -help       *"
    print "\t\t*     ali ahmady , pHaNtOm_X ,Ch3rn0by1     *"
    print "\t\t*********************************************"

banner()

def fetchYouget(target):
    url = "http://domains.yougetsignal.com/domains.php"

    postdata = {'remoteAddress': target, 'key': ''}
    postdata = urllib.urlencode(postdata)

    request = urllib2.Request(url, postdata)

    request.add_header("User-Agent", useragent)
    yougetJson = urllib2.urlopen(request).read()

    results = [i[0] for i in json.loads(yougetJson)['domainArray']]
    return results


def fetchViewDns(target):
    url = "http://viewdns.info/reverseip/?t=1&host=" + target
    request = urllib2.Request(url)
    request.add_header("User-Agent", useragent)
    data=urllib2.urlopen(request).read()
    results = re.findall('<td>(.+?\..+?)</td>', data)
    return results


def stormer(q):
    try:
        log = open('sites.txt', 'w')
        while not q.empty():
            site = q.get(block=True, timeout=2)
            cn = urllib.urlopen(site)

            if cn.getcode() == 404:
                pass
            else:

                rsp = cn.read()
                rx = re.findall('type="Password"', rsp, re.I)

                if len(rx) == 1:
                    if "wp-admin" in rsp:
                        print '[w] %s' % site
                        found.append('[w] http://%s' % site)
                    else:

                        print '[+] %s' % site
                        found.append('[+] http://%s' % site)
                else:
                    pass

            q.task_done()


    except(socket.error, IOError, httplib.BadStatusLine):
        pass
    finally:
        for uri in found:
            uri.replace("\n", "")
            log.write(uri + '\n')
        log.close()


def killa(nom):
    for i in xrange(nom):
        thread = threading.Thread(target=stormer, args=(q,))
        thread.daemon = True
        thread.start()
    thread.join()


# target filter
try:
    target = args.target
    if target[-1] == '/':
        target = target.replace(target[-1], "")
        target = target.replace("http://", "")

    yg = open('list.txt', 'w')
    target = socket.gethostbyname(target)
    print "\n" + "-" * 25
    print 'Target : %s' % target
    print "-" * 25
    # proxy
    proxy = args.proxy
    if proxy:
        opener = urllib2.build_opener(
            urllib2.HTTPHandler(),
            urllib2.HTTPSHandler(),
            urllib2.ProxyHandler({'http': 'http://' + proxy}))
        urllib2.install_opener(opener)
        # request
    if 'youget' in args.src.lower():

        result = fetchYouget(args.target)
    # reading youget response
    elif 'viewdns' in args.src.lower():
        result = fetchViewDns(args.target)
    l = len(result)
    while l:
        if l == 0:
            print "[-]Reverse IP limit reached"
            break
        print "-" * 25
        print "[+] Domain list fetch complete \n[+] Domain count : %s" % l
        print "-" * 25
        # writer
        with open('list.txt', 'w') as yg:
            for each in result:
                yg.write(each + '\n')
                # REverse IP COmplete
        if proxy:
            print "-" * 25 + '\n' + 'Proxy : %s' % proxy + '\n' + "-" * 25
        if args.thrd:
            print "-" * 25 + '\n' + 'Threads: %s' % args.thrd + '\n' + "-" * 25
        if args.timeout:
            print "-" * 25 + '\n' + 'Timeout: %s Seconds' % args.timeout + '\n' + "-" * 25
            # Start of Admin buster

        lstx = open('list.txt', 'r')
        sites = lstx.readlines()
        print"\n" + "-" * 25
        print ' Rsp | \tURL'
        print '-' * 25
        socket.setdefaulttimeout(args.timeout)
        flist = []
        for each in sites:
            each = each.replace("\n", "").replace("\r", "")
            if each:
                flist.append(each)
            #			q.put(each)
        product = itertools.product(flist, getx)
        for site in product:
            site = ''.join(site)
            site = 'http://' + site
            q.put(site)
        break

    while not q.empty():
        killa(args.thrd)
except TypeError, e:
    print "[-] NO target specified"
    print e
except socket.gaierror:
    print "[-]NOPE WRONG URL"
except KeyboardInterrupt:
    print "[-] Abort signal Detected"
except httplib.BadStatusLine:
    print "[-] Something went wrong try again or let it go"
