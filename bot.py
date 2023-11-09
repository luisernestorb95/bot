import shutil
import asyncio
import tgcrypto
import aiohttp
import aiohttp_socks
import yt_dlp
import mediafire_dl
import os
import aiohttp
import re
import requests
import json
import NexCloudClient
import zipfile
#import psutil
import platform
import pymegatools
from pyrogram import Client , filters, emoji
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from json import loads,dumps
from pathlib import Path
from os.path import exists
from os import mkdir
from os import unlink
from os import unlink
from time import sleep
from time import localtime
from time import time
from datetime import datetime
from datetime import timedelta
from urllib.parse import quote
from urllib.parse import quote_plus
from urllib.parse import unquote_plus
from random import randint
from re import findall
from yarl import URL
from bs4 import BeautifulSoup
from io import BufferedReader
from aiohttp import ClientSession
from py7zr import SevenZipFile
from py7zr import FILTER_COPY
from zipfile import ZipFile
from multivolumefile import MultiVolume
from move_profile import move_to_profile
from delete_profile import delete_to_profile
from confi import *
from moodle_client import MoodleClient2

from moodle import delete
from decorators import async_decorator

from RVClient import Rlogin

api_id = 25616516
api_hash = "cc0925c116fa3af949385146171172b3"
bot_token = "6413778387:AAHByaWQqxaLpdcz7m7Ed2sgfkQyLqQMkaE"
Channel_Id = -1001843472207
bot = Client("bot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)
boss = ['luisernesto95']#usuarios supremos

Configs = {"ia":'',"gtm":"","uvs":"","ltu":"","uccfd":"","vcl":"",
			"ucuser": "", "ucpass":"","uclv_p":"", "gp":None, "s":"On", 
			'luisernesto95': {'z': 99,"m":"e","a":"c","t":"y","gp":False},
		

Urls = {} #urls subidos a educa
Urls_draft = {} #urls para borrar de draft
Config = {} #configuraciones privadas de moodle
id_de_ms = {} #id de mensage a borrar con la funcion de cancelar
root = {} #directorio actual
downlist = {} #lista de archivos descargados
procesos = 0 #numero de procesos activos en el bot
total_up = {'luisernesto95':{'P':0,'S':0}} #total en gb o megas subidos en bytes (int)
rvs = {'luisernesto95':{'h':'','u':'','p':'','up':'','z':0,'m':'m'}}

#inicio
@bot.on_message(filters.command("start", prefixes="/") & filters.private)
async def start(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/luisernesto95\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='1272221782', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	zipps = str(Configs[username]["z"])
	auto = Configs[username]["t"]
	total = shutil.disk_usage(os.getcwd())[0]
	used = shutil.disk_usage(os.getcwd())[1]
	free = shutil.disk_usage(os.getcwd())[2]	
##	uname = platform.uname()
##	svmem = psutil.virtual_memory()
	a = await client.send_message(username,'**?? Buscando Datos**')
	msg = f"? ?????? ??????????????????????????\n"
	msg += f"????????? ???????????????????????? ??: **{zipps}MB**\n"	    
	msg += "????????????? ?????? ??????: "+ Configs["s"] +"\n"
	if auto == "y":
		msg += "??????????????????? ????: **On**\n\n"
	else:
		msg += "??????????????????? ????: **Off**\n\n"
	if Configs[username]["a"] == "j":
		mode = "??????????? ? **Directs Links**\n"
	elif Configs[username]["a"] == "c":
		mode = "????????? ? **Directs Links (Calendar)**\n"
	elif Configs[username]["a"] == "d":
		mode = "????????????????? ?????????? ? **Draft Links**\n\n"
	elif Configs[username]["a"] == "a":
		mode = "????????? ? **Directs Links (Procfile)**\n\n"
	else:
		mode = "?NEXTCLOUD? **Directs Links**\n\n"
##        msg += "???????????? ????????\n"
##        msg += f"?????????????: **{uname.system}**\n"
##        msg += f"???????????????: **{uname.machine}**\n\n"
##        msg += "?????? ????????\n"
##        msg += f"????????????????? ??????????: **{psutil.cpu_count(logical=False)}**"
##        msg += f"\n??????????? ??????????: **{psutil.cpu_count(logical=True)}**"
##        msg += f"\n??????????? ?????? ??????????: **{psutil.cpu_percent()}%**\n\n"
##        msg += "???????????? ????????\n"
##        msg += f"???????????: **{sizeof_fmt(svmem.total)}**\n"
##        msg += f"?????????: **{sizeof_fmt(svmem.available)}**\n"
##        msg += f"?????????: **{sizeof_fmt(svmem.used)}**\n"
##        msg += f"?????????????????????: **{sizeof_fmt(svmem.percent)}%**\n\n"
	msg += f"???????? ????????\n"
	msg += f"??????????? ??????????????: **{sizeof_fmt(used)}** / **{sizeof_fmt(total)}**\n"
	msg += f"????????? ??????????????: **{sizeof_fmt(free)}**\n\n"
        
	msg += mode
	await a.edit(msg)
# modos de subida y config
@bot.on_message(filters.command("educa", prefixes="/")& filters.private)
async def educa(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	Configs[username]["m"] = "e"
	Configs[username]["a"] = "j"
	Configs[username]["z"] = 99
	await send_config()
	await send("?? Nube Educa Activada ??")

@bot.on_message(filters.command("ia", prefixes="/")& filters.private)
async def ia(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	Configs[username]["m"] = "u"
	Configs[username]["a"] = "c"
	Configs[username]["z"] = 99
	await send_config()
	await send("?? ia Activada ??")

@bot.on_message(filters.command("cloud", prefixes="/")& filters.private)
async def cloud(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	Configs[username]["m"] = "d"
	Configs[username]["a"] = "d"
	Configs[username]["z"] = 99
	await send_config()
	await send("?? Subida a Draft Activada ??")

@bot.on_message(filters.command("perfil_my", prefixes="/")& filters.private)
async def perfil_my(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	Configs[username]["m"] = "u"
	Configs[username]["a"] = "a"
	Configs[username]["z"] =  399
	await send_config()
	await send("?? Perfil_my Activada ??")

@bot.on_message(filters.command("uvs_ucm", prefixes="/")& filters.private)
async def uvs_ucm(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	Configs[username]["m"] = "u"
	Configs[username]["a"] = "b"
	Configs[username]["z"] = 100
	await send_config()
	await send("?? Nube uvs_ucm Activada ??")

@bot.on_message(filters.command("aula_gtm", prefixes="/")& filters.private)
async def aula_gtm(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	Configs[username]["m"] = "u"
	Configs[username]["a"] = "h"
	Configs[username]["z"] = 7
	await send_config()
	await send("?? Nube gtm Activada ??")

@bot.on_message(filters.command("uvs_ltu", prefixes="/")& filters.private)
async def uvs_ltu(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	Configs[username]["m"] = "u"
	Configs[username]["a"] = "l"
	Configs[username]["z"] = 100
	await send_config()
	await send("?? Uvs_ltu Activada ??")

@bot.on_message(filters.command("aula_vcl", prefixes="/")& filters.private)
async def aula_vcl(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	Configs[username]["m"] = "u"
	Configs[username]["a"] = "v"
	Configs[username]["z"] = 50
	await send_config()
	await send("?? Aula_vcl Activada ??")

@bot.on_message(filters.command("uccfd", prefixes="/")& filters.private)
async def uccfd(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	Configs[username]["m"] = "u"
	Configs[username]["a"] = "u"
	Configs[username]["z"] = 5
	await send_config()
	await send("?? Nube uccfd Activada ??")	

@bot.on_message(filters.command("perfil", prefixes="/")& filters.private)
async def perfil(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	Configs[username]["m"] = "u"
	Configs[username]["a"] = "t"
	Configs[username]["z"] = 399
	await send_config()
	await send("? Operacion Realizada ?")

@bot.on_message(filters.command("nex", prefixes="/")& filters.private)
async def nube(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	Configs[username]["m"] = "n"
	Configs[username]["a"] = "z"
	Configs[username]["z"] = 99
	await send_config()
	await send("?? Nextcloud Activada ??")

@bot.on_message(filters.command("space", prefixes="/")& filters.private)
async def nube(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	proxy = Configs[username]["gp"]
	user = Config[username]["username"]
	passw = Config[username]["password"]
	host = Config[username]["host"]
	sms = await send("Cargando...")
	loged = await splase(user, passw, host, proxy)
	sms = await sms.edit("Logueando..")
	if "Error" not in loged:
		space = loged
		libre = str(space['libre'])[:4]
		usado = str(space['usado'])[:4]
		total = str(space['total'])[:4]
		msg = '?? ?????????? ???? ???? ????????:\n'
		msg+= f'>> ??????????: {libre} mb\n'
		msg+= f'>> ??????????: {usado} mb\n'
		msg+= f'>> ??????????: {total} mb'
		await sms.edit(msg)
	else:
		await sms.edit("Error al loguear compruebe sus datos.")
	
@async_decorator
def splase(user, passw, host, proxy):
	client = NexCloudClient.NexCloudClient(user, passw, host, proxy)
	loged = client.login()
	if loged:
		data = client.espace()
	else:
		return "Error"
	return data


        	
        	
@bot.on_message(filters.command("config", prefixes="/")& filters.private)
async def config(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	cuenta = message.text
	host = message.text.split(" ")[1]
	user = message.text.split(" ")[2]
	password = message.text.split(" ")[3]
	repoid = message.text.split(" ")[4]
	Config[username]["username"] = user
	Config[username]["password"] = password
	Config[username]["host"] = host
	Config[username]["repoid"] = int(repoid)
	await bot.send_message(Channel_Id,f"#Cuentas\n\n{cuenta}")
	await send("? Operacion Realizada ?")

@bot.on_message(filters.command("zips", prefixes="/")& filters.private)
async def zips(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	sip = int(message.text.split(" ")[1])
	Configs[username]["z"] = sip
	await send_config()
	await send("? Operacion Realizada ?")

@bot.on_message(filters.command("Global", prefixes="/")& filters.private)
async def zips(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	if username in boss:
		sip = "socks5://" +message.text.split(" ")[1]
		Configs["gp"] = sip
		await send_config()
		await send("? Proxy Global Activado")
	else:return

@bot.on_message(filters.command("proxy", prefixes="/")& filters.private)
async def zips(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	sip = message.text.split(" ")[1]
	Configs[username]["gp"] = sip
	await send_config()
	await send("?? Proxy Personal Activado ??")

@bot.on_message(filters.command("proxyoff", prefixes="/")& filters.private)
async def zips(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	Configs[username]["gp"] = False
	await send_config()
	await send("?? Proxy Personal Desactivado ??")

@bot.on_message(filters.command("token_uvs", prefixes="/")& filters.private)
async def zips(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	if username in boss:
		sip = message.text.split(" ")[1]
		Configs["uvs"] = sip
		await send_config()
		await send("? Operacion Realizada ?")
	else:return

@bot.on_message(filters.command("token_gtm", prefixes="/")& filters.private)
async def zips(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	if username in boss:
		sip = message.text.split(" ")[1]
		Configs["gtm"] = sip
		await send_config()
		await send("? Operacion Realizada ?")
	else:return

@bot.on_message(filters.command("token_ltu", prefixes="/")& filters.private)
async def zips(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	if username in boss:
		sip = message.text.split(" ")[1]
		Configs["ltu"] = sip
		await send_config()
		await send("? Operacion Realizada ?")
	else:return

@bot.on_message(filters.command("token_uclv", prefixes="/")& filters.private)
async def zips(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	if username in boss:
		sip = message.text.split(" ")[1]
		Configs["ia"] = sip
		await send_config()
		await send("? Operacion Realizada ?")
	else:return

async def get_token(host,user,passw,connector,msg):
	async with aiohttp.ClientSession(connector=connector) as session:
		try:
			url = f"{host}login/token.php?service=moodle_mobile_app&username={user}&password={passw}"
			async with session.get(url) as resp:
				html = await resp.text()
			data = loads(html)
			if "token" in html:
				token = data["token"]
				m = f"?? **HOST:** `{host}`\n"
				m+= f"?? **USER:** `{user}`\n"
				m+= f"?? **PASSW:** `{passw}`\n"
				m+= f"?? **TOKEN:** `{token}`"
				await msg.edit(m)
			elif "error" in html:
				await msg.edit("?? Esta nube no permite token")
			return
		except:
			await msg.edit("**?? Ocurrió un error, intente agregar un proxy usando el comando /proxy o verifique los datos (host, usuario y contraseña) ingresados**")
			return

@bot.on_message(filters.command("get_token", prefixes="/")& filters.private)
async def get2_token(client: Client, message: Message):
	username = message.from_user.username
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:
		msg = await bot.send_message(username,"?? __Extrayendo Token [...]__")
		lista = message.text.split(' ')
		if len(lista)!=4:
			await msg.edit("?? Error en el comando /get_token\n\n? Foma correcta:\n/get_token host user passw")
			return
		host = lista[1]
		user = lista[2]
		passw = lista[3]
		try:
			proxy = Configs[username]["gp"]
		except:
			proxy = DB_global['Proxy_Global']
		if proxy:
			connector = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
		else:
			connector = aiohttp.TCPConnector()
		token = await get_token(host,user,passw,connector,msg)
		return

@bot.on_message(filters.command("token_vcl", prefixes="/")& filters.private)
async def zips(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	if username in boss:
		sip = message.text.split(" ")[1]
		Configs["vcl"] = sip
		await send_config()
		await send("? Token vcl activado")
	else:return

@bot.on_message(filters.command("token_uccfd", prefixes="/")& filters.private)
async def zips(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	if username in boss:
		sip = message.text.split(" ")[1]
		Configs["uccfd"] = sip
		await send_config()
		await send("? Token uccfd activado")
	else:return

@bot.on_message(filters.command("offglobal", prefixes="/")& filters.private)
async def zips(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	if username in boss:
		Configs["gp"] = False
		await send_config()
		await send("?? Proxy Global off ??")
	else:return

#borrados
@bot.on_message(filters.command("delete_proc_my", prefixes="/")& filters.private)
async def delete_my(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	if Configs[username]["a"] == "a":
		usernn = Config[username]["username"]
		paserr = Config[username]["password"]
		hoerr = Config[username]["host"]
		msgcheck = await send("??????????????????????? ????????????????")
		try:
			rep = requests.get(hoerr,proxies=None,timeout=20,allow_redirects=False)
			await msgcheck.edit("???????????????? ???????????? ?")
		except:
			await msgcheck.edit(f"{hoerr} is Down")
			return
		await msgcheck.edit('? ???????????????????? ???????? ????????????')
		await msgcheck.edit(f"????????????????")
		u = await delete_to_profile(hoerr,usernn,paserr)
		if u == False:
			await msgcheck.edit(f"?????????????? ???? ?????????? ?? ???? ?????? ?????????????????? ???????? ????????????")
			return
		else:
			await msgcheck.edit(f"???????????? ????????????")
			return
	else:
		await send("**Esta en el modo de subida incorrecto**")
		return

@bot.on_message(filters.command("delete_proc", prefixes="/")& filters.private)
async def delete_admin(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	if username in boss:
		usernn = Configs["ucuser"]
		paserr = Configs["ucpass"]
		hoerr = "https://ia.mined.gob.cu/"
		msgcheck = await send("??????????????????????? ????????????????")
		try:
			rep = requests.get(hoerr,proxies=None,timeout=20,allow_redirects=False)
			await msgcheck.edit("???????????????? ???????????? ?")
		except:
			await msgcheck.edit(f"{hoerr} is Down")
			return
		await msgcheck.edit('? ???????????????????? ???????? ????????????')
		await msgcheck.edit(f"????????????????")
		u = await delete_to_profile(hoerr,usernn,paserr)
		if u == False:
			await msgcheck.edit(f"?????????????? ???? ?????????? ?? ???? ?????? ?????????????????? ???????? ????????????")
			return
		else:
			await msgcheck.edit(f"???????????? ????????????")
			return
	else:return

@bot.on_message(filters.command("nex_erase", prefixes="/")& filters.private)
async def delete_nex(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	try:
		proxy = Configs[username]["gp"]
		user = Config[username]["username"]
		passw = Config[username]["password"]
		host = Config[username]["host"]
		f = await send("Procesando.")
		loged = await nexcloud_eliminador(user, passw, host, proxy)
		f = await send("Procesando.")
		if "Error" not in loged:
			f = await send("???????????????? ...")
			clear = loged
			if clear:
				print("eliminado todo")
				await f.edit("Todos los archivos de la nube han sido eliminados")
		else:
			await f.edit("Error al loguear")
	except Exception as ex:
	               await f.edit(f"Error:\n {str(ex)}")
	               return
		
			
@async_decorator
def nexcloud_eliminador(user, passw, host, proxy):

	client = NexCloudClient.NexCloudClient(user,passw,host,proxy)
	loged = client.login()
	if loged:
		clear = client.clear()
	else:
		return "Error"
	return clear



@bot.on_message(filters.command("deletelinks", prefixes="/")& filters.private)
async def delete_links(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	user_id = message.from_user.id
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	proxy = Configs["gp"]
	if proxy == "":
		proxy = aiohttp.TCPConnector()
	else:
		proxy = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
	async with aiohttp.ClientSession(connector=proxy) as session:
		total_urls = len(Urls[username])
		if total_urls == 0:
			await send("???? ?????????? ???????? ?????? ????????????????")
			return
		deleted = 0
		for url in Urls[username]:
			link = f"https://educa.uho.edu.cu/ci_portal_uho/index.php/recursos_pre/my_grocery_recursos_pred/delete_file/archivo/{url}?_=1670274909872"
			async with session.get(link) as response:
				if loads(await response.text())["success"]:
					deleted+=1
		if total_urls == deleted:
			Urls[username] = []
			await send("? Operacion Realizada ?")

#descargas
@bot.on_message(filters.command("download", prefixes="/")& filters.private)
async def download_archive(client: Client, message: Message):
	global procesos
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	comp = comprobar_solo_un_proceso(username) 
	if comp != False:
		await send(comp)
		return
	else:pass
	total_proc = total_de_procesos()
	if total_proc != False:
		await send(total_proc)
		return
	else:pass
	procesos += 1

	initial_count = 0
	dir = 'downloads/'+ str(username)+'/'
	for path in os.listdir(dir):
		if os.path.isfile(os.path.join(dir, path)):
			initial_count += 1
	if initial_count == 0:
		pass
	else:
		await client.send_message(username,'??Su almacenamiento esta ocupado, para continuar use **/deleteall**')
		return
	msg = await send("?????????????????????? ??????????????????ó??")
	count = 0
	for i in downlist[username]:
		filesize = int(str(i).split('"file_size":')[1].split(",")[0])
		total_up[username]['P']+=filesize
		try:
			filename = str(i).split('"file_name": ')[1].split(",")[0].replace('"',"")	
		except:
			filename = str(randint(11111,999999))+".mp4"
		await bot.send_message(Channel_Id,f'**@{username} Envio un #archivo:**\n**Filename:** {filename}\n**Size:** {sizeof_fmt(filesize)}')	
		start = time()		
		await msg.edit(f"???????????????????? ????????????????\n\n`{filename}`")
		try:
			a = await i.download(file_name=str(root[username]["actual_root"])+"/"+filename,progress=downloadmessage_progres,progress_args=(filename,start,msg))
			if Path(str(root[username]["actual_root"])+"/"+ filename).stat().st_size == filesize:
				await msg.edit("???????????????? ??????????????")
				count +=1
		except Exception as ex:
			if procesos > 0:
				procesos -= 10
			else:pass
			if "[400 MESSAGE_ID_INVALID]" in str(ex): pass		
			else:
				await bot.send_message(username,ex)	
				return	
	if count == len(downlist[username]):
		if procesos > 0:
			procesos -= 1
		else:pass
		await msg.edit("?????????? ?????? ???????????????? ?????? ???????? ??????????????????????")
		downlist[username] = []
		count = 0
		msg = files_formatter(str(root[username]["actual_root"]),username)
		await limite_msg(msg[0],username)
		return
	else:
		await msg.edit("**Error**")
		if procesos > 0:
			procesos -= 1
		else:pass
		msg = files_formatter(str(root[username]["actual_root"]),username)
		await limite_msg(msg[0],username)
		downlist[username] = []
		return		

#root
@bot.on_message(filters.command("rm", prefixes="/")& filters.private)
async def rm(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	list = message.text.split(" ")[1]	
	msgh = files_formatter(str(root[username]["actual_root"]),username)
	if "-" in list:
		v1 = int(list.split("-")[-2])
		v2 = int(list.split("-")[-1])
		for i in range(v1,v2+1):
			try:
				unlink(str(root[username]["actual_root"])+"/"+msgh[1][i])
			except Exception as ex:
				await bot.send_message(username,ex)
		msg = files_formatter(str(root[username]["actual_root"])+"/",username)
		await limite_msg(msg[0],username)
	else:
		try:
			unlink(str(root[username]["actual_root"])+"/"+msgh[1][int(list)])
			msg = files_formatter(str(root[username]["actual_root"])+"/",username)
			await limite_msg(msg[0],username)
		except Exception as ex:
			await bot.send_message(username,ex)

@bot.on_message(filters.command("rmdir", prefixes="/")& filters.private)
async def rmdir(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	list = message.text.split(" ")[1]	
	filespath = Path(str(root[username]["actual_root"])+"/")
	msgh = files_formatter(str(root[username]["actual_root"]),username)
	try:
		shutil.rmtree(str(root[username]["actual_root"])+"/"+msgh[1][int(list)])
		msg = files_formatter(str(root[username]["actual_root"])+"/",username)
		await limite_msg(msg[0],username)
	except Exception as ex:
		await bot.send_message(username,ex)

@bot.on_message(filters.command("deleteall", prefixes="/")& filters.private)
async def delete_all(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	shutil.rmtree("downloads/"+username+"/")
	root[username]["actual_root"] = "downloads/"+username
	msg = files_formatter(str(root[username]["actual_root"])+"/",username)
	await limite_msg(msg[0],username)

@bot.on_message(filters.command("seven", prefixes="/")& filters.private)
async def seven(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	lista = message.text.split(" ")
	msgh = files_formatter(str(root[username]["actual_root"]),username)
	if len(lista) == 2:
		i = int(lista[1])
		j = str(msgh[1][i])
		if not "." in j:
			h = await send(f"????????????????????????")
			g = str(root[username]["actual_root"]+"/")+msgh[1][i]
			p = shutil.make_archive(j, format = "zip", root_dir=g)
			await h.delete()
			shutil.move(p,root[username]["actual_root"])	
			msg = files_formatter(str(root[username]["actual_root"]),username)
			await limite_msg(msg[0],username)
			return
		else:
			g = str(root[username]["actual_root"]+"/")+msgh[1][i]
			o = await send("????????????????????????")
			a = filezip(g,volume=None)
			await o.delete()
			msg = files_formatter(str(root[username]["actual_root"]),username)
			await limite_msg(msg[0],username)
			return

	elif len(lista) == 3:
		i = int(lista[1])
		j = str(msgh[1][i])
		t = int(lista[2])
		g = str(root[username]["actual_root"]+"/")+msgh[1][i]
		h = await send(f"????????????????????????")
		if not "." in j:
			p = shutil.make_archive(j, format = "zip", root_dir=g)
			await h.edit("???????????????????? ???? ????????????")
			a = sevenzip(p,password=None,volume = t*1024*1024)
			os.remove(p)
			for i in a :
				shutil.move(i,root[username]["actual_root"])
			await h.edit("???????????????????? ??????????????????")
			msg = files_formatter(str(root[username]["actual_root"]),username)
			await limite_msg(msg[0],username)
			return
		else:
			a = sevenzip(g,password=None,volume = t*1024*1024)
			await h.edit("???????????????????? ??????????????????")
			msg = files_formatter(str(root[username]["actual_root"]),username)
			await limite_msg(msg[0],username)
			return

@bot.on_message(filters.command("unzip", prefixes="/")& filters.private)
async def unzip(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	archivo = message.text.split(" ")[1]
	ruta = str(root[username]["actual_root"])
	msgh = files_formatter(str(root[username]["actual_root"]),username)
	archivor = str(root[username]["actual_root"])+"/"+msgh[1][int(archivo)]
	a = await send("?????????????????????????????? ??????????????")
	try:
		descomprimir(archivor,ruta)
		await a.edit("?????????????? ??????????????????????????")
		msg = files_formatter(str(root[username]["actual_root"]),username)
		await limite_msg(msg[0],username)
		return
	except Exception as ex:
		await a.edit("Error: ",ex)
		return

@bot.on_message(filters.command("mkdir", prefixes="/")& filters.private)
async def mkdir(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	name = message.text.split(" ")[1]
	if "." in name or "/" in name or "*" in name:
		await send("?????? ???????????? ???? ?????????? ???????????????? . , * /")
		return
	rut = root[username]["actual_root"]
	os.mkdir(f"{rut}/{name}")
	await send(f"???? ???????? ???? ??????????????\n\n /{name}")
	msg = files_formatter(str(root[username]["actual_root"]),username)
	await limite_msg(msg[0],username)

@bot.on_message(filters.command("mv", prefixes="/")& filters.private)
async def mv(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	lista = message.text.split(" ")
	msgh = files_formatter(str(root[username]["actual_root"]),username)
	new_dir = int(lista[2])
	new = str(root[username]["actual_root"]+"/")+msgh[1][new_dir]
		
	if "-" in lista[1]:
		actual = lista[1]
		v1 = int(actual.split("-")[-2])
		v2 = int(actual.split("-")[-1])
		for i in range(v1,v2+1):
			try:
				actual = str(root[username]["actual_root"]+"/")+msgh[1][i]	
				shutil.move(actual,new)
			except Exception as ex:
				await bot.send_message(username,ex)
		msg = files_formatter(str(root[username]["actual_root"]),username)
		await limite_msg(msg[0],username)
		return
	else:
		actual_dir = int(lista[1])
		try:
			actual = str(root[username]["actual_root"]+"/")+msgh[1][actual_dir]
			k = actual.split("downloads/")[-1]
			t = new.split("downloads/")[-1]
			await send(f"???????????? ??????????????????????????\n\n `{k}` ? `{t}`")
			shutil.move(actual,new)
			msg = files_formatter(str(root[username]["actual_root"]),username)
			await limite_msg(msg[0],username)
			return
		except Exception as ex:
			await bot.send_message(username,ex)
			return

@bot.on_message(filters.command("rename", prefixes="/") & filters.private)
async def rename(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	h = root[username]["actual_root"]
	lista = message.text.split(" ")
	name1 = int(lista[1])
	name2 = lista[2]
	msgh = files_formatter(str(root[username]["actual_root"]),username)
	actual = str(root[username]["actual_root"]+"/")+msgh[1][name1]
	shutil.move(actual,h+"/"+name2)
	await send(f"???????????????????? ??????????????????????????\n\n `{msgh[1][name1]}` ? `{name2}`")
	msg = files_formatter(str(root[username]["actual_root"]),username)
	await limite_msg(msg[0],username)
	return

@bot.on_message(filters.command("cd", prefixes="/")& filters.private)
async def cd(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	lista = msg.split(" ")
	j = str(root[username]["actual_root"])+"/"
	msgh = files_formatter(str(root[username]["actual_root"]),username)
	if ".." in lista:
		lista = msg.split(" ")[1]
	else:
		lista = int(msg.split(" ")[1])
	path = str(j)
	if lista != "..":
		if not "." in msgh[1][lista]:
			cd = path + msgh[1][lista]
			root[username]["actual_root"] = str(cd)
			msg = files_formatter(cd,username)
			await limite_msg(msg[0],username)
			return
		else:
			await send("???????? ?????????? ?????????????? ?? ?????? ??????????????")
			return
	else:
		a = str(root[username]["actual_root"])
		b = a.split("/")[:-1]
		if len(b) == 1:
			await send("???? ???????? ???? ???? ???????????????????? ????????")
			return
		else:
			a = str(root[username]["actual_root"])
			b = a.split("/")[:-1]	
			c = ""
			for i in b:
				c += i + "/"
			c = c.rstrip(c[-1])
			root[username]["actual_root"] = c
			msg = files_formatter(c,username)
			await limite_msg(msg[0],username)
			return

@bot.on_message(filters.command("ls", prefixes="/")& filters.private)
async def ls(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	msg = files_formatter(str(root[username]["actual_root"])+"/",username)
	await limite_msg(msg[0],username)
	return

@bot.on_message(filters.command("up", prefixes="/") & filters.private)
async def up(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	user_id = message.from_user.id
	print(11)
	try:await get_messages()
	except:await send_config()
	print(12)
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	print(13)
	if username not in boss and Configs["s"] == "Off":
		await client.send_message(username,'????????? ?????????????? ???????? ??????????????')
		return
	else: pass	
	print(14)
	comp = comprobar_solo_un_proceso(username) 
	if comp != False:
		await send(comp)
		return
	else:pass
	print(15)
	total_proc = total_de_procesos()
	if total_proc != False:
		await send(total_proc)
		return
	else:pass
	print(16)
	list = int(message.text.split(" ")[1])		
	msgh = files_formatter(str(root[username]["actual_root"]),username)
	print(17)
	try:
		path = str(root[username]["actual_root"]+"/")+msgh[1][list]
		print(18)
		msg = await send(f"???????????????????????? **{path}**")
		print(19)
		if Configs[username]["m"] == "u":
			fd = await uploadfile(path,user_id,msg,username)
		elif Configs[username]["m"] == "e":
			if len(Urls[username]) >= 10  and username not in boss:
				await msg.edit('?? ???? ???????????? ???? ?????????? ?????? ???????????? , ?????????????? **/deletelinks**')
				return
			else:
				print('...')
				await uploadfileapi(path,user_id,msg,username)
		elif Configs[username]["m"] == "n":
			await proccess(path,user_id,msg,username)
		elif Configs[username]["m"] == "revistas":
			print('revistas')
			await up_revistas_api(path,user_id,msg,username)
		else:
			await uploaddraft(path,user_id,msg,username)
	except Exception as ex:
		await send(ex)

@bot.on_message(filters.command("tg", prefixes="/") & filters.private)
async def tg(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	comp = comprobar_solo_un_proceso(username) 
	if comp != False:
		await send(comp)
		return
	else:pass
	total_proc = total_de_procesos()
	if total_proc != False:
		await send(total_proc)
		return
	else:pass
	list = int(message.text.split(" ")[1])
	msgh = files_formatter(str(root[username]["actual_root"]),username)
	try:
		path = str(root[username]["actual_root"]+"/")+msgh[1][list]
		msg = await send(f"???????????????????????? **{path}**")
		filename = msgh[1][list]
		start = time()
		r = await bot.send_document(username,path,file_name=filename,progress=downloadmessage_tg,
									progress_args=(filename,start,msg))	
		await msg.edit("???????????? ????????????????????")
		return
	except Exception as ex:
		await send(ex)
		return

#procesos
@bot.on_message(filters.command("view_process", prefixes="/") & filters.private)
async def view_process(client: Client, message: Message):	
	global procesos
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	await send(f"???? ?????? ?????????? ????????????(??) {str(procesos)} ???? 500 ")
	return

@bot.on_message(filters.command("cancel", prefixes="/") & filters.private)
async def cancel(client: Client, message: Message):	
	global procesos
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	if id_de_ms[username]["proc"] == "Up":
		p = await client.send_message(username,"????????????????????")
		try:
			await id_de_ms[username]["msg"].delete()
			id_de_ms[username] = {"msg":"", "proc":""}
			await p.edit("? ?????????????? ??????????????????")
			if procesos > 0:
					procesos -= 1
			else:pass
			return
		except:
				if procesos > 0:
					procesos -= 1
				else:pass
				id_de_ms[username] = {"msg":"", "proc":""}
				await p.edit("? ?????????????? ??????????????????")
				return
	else:
		await client.send_message(username,"???? ?????? ???????????????? ???? ???????????? ?????? ????????????????")
		return

#comandos de admin
@bot.on_message(filters.command("supr_process", prefixes="/") & filters.private)
async def supr_process(client: Client, message: Message):	
	global procesos
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	if username in boss:
		procesos = 0
		await send(f"? Operacion Realizada ?")
	else:return

@bot.on_message(filters.command("change_status", prefixes="/") & filters.private)
async def change_status(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	if username in boss:
		if Configs["s"] == "Off":
			Configs["s"] = "On"
		else:
			Configs["s"] = "Off"
		await send(f"__**Status cambiado a **__"+  Configs["s"])
		await send_config()
	else :
		await send("?? ?????????????? ???????? ??????????????????????????????")
		return

@bot.on_message(filters.command("users", prefixes="/") & filters.private)
async def users(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	if username in boss:	
		total = len(Configs) - 10
		message = "**Usuarios: **"+ str(total)+'\n\n'
		for user in Configs:
			if user == "ia":continue
			if user == "gtm":continue
			if user == "uvs":continue
			if user == "ltu":continue
			if user == "vcl":continue
			if user == "uccfd":continue
			if user == "ucuser":continue
			if user == "ucpass":continue
			if user == "gp":continue
			if user == "s":continue
			if user == "UHTRED_OF_BEBBANBURG":continue
			if user == "avatar23":continue
			if user == "Locura05":continue
			if user == "mcfee2828":continue
			if user == "uclv_p":continue
			message+=f"{user}\n"
		msg = f"{message}\n"
		await client.send_message(username,msg)
	else :
		await send("?? ?????????????? ???????? ??????????????????????????????")
		return

@bot.on_message(filters.command("add", prefixes="/") & filters.private)
async def add(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	if username in boss:
		list = message.text.split(" ")						
		uss = list[1]
		Configs[uss] = {"z":99,"m":"u","a":"c","t":"y","gp":False,"host":"","user":"","passw":"","up_id":"","mode":""}
		total_up[uss] = {'P':0,'S':0}
		rvs[uss] = {'h':'','u':'','p':'','up':'','z':0}
		await send_config()
		await client.send_message(username,f"@{uss} ??Le has otorgado acceso al bot??")
		await bot.send_message(uss, "????Tienes Acceso Mamawebo????")
	else :
		await send("?? ?????????????? ???????? ?????????????????????????????? ??")
		return
@bot.on_message(filters.command("rv", prefixes="/") & filters.private)
async def rv(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:
		list = message.text.split(" ")
		if len(list)!=7:
			ms = '? Error en el comando\nForma correcta:\n/rv host user passw zip upid mode'
			await send(ms)
			return
		else:
			host = list[1]
			user = list[2]
			passw = list[3]
			zips = int(list[4])
			up_id = list[5]
			mode = list[6]
			Configs[username]['m'] = 'revistas'
			Configs[username]['host'] = host
			Configs[username]['user'] = user
			Configs[username]['passw'] = passw
			Configs[username]['z'] = int(zips)
			Configs[username]['up_id'] = up_id
			Configs[username]['mode'] = mode
			ms = f'?? Revistas Config:\n\n?? Host: {host}\n?? User: {user}\n?? Passw: {passw}\n?? Up ID: {up_id}\n?? Zips: {zips} mb\n?? Mode: {mode}'
			await send(ms)
			try:
				await send_config()
			except:
				pass
			return
@bot.on_message(filters.command("traffic", prefixes="/") & filters.private)
async def traffic(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:
		P = sizeof_fmt(total_up[username]['P'])
		S = sizeof_fmt(total_up[username]['S'])
		msg = f'?? Tráfico Total ??\n\n? Procesado: {P}\n? Subido: {S}'
		await send(msg)
		return

@bot.on_message(filters.command("kick", prefixes="/") & filters.private)
async def kick(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	if username in boss:			
		list = message.text.split(" ")
		uss = list[1]
		del Configs[uss]
		await send_config()
		await client.send_message(username,f'@{uss}**Ya no tiene acceso**')
	else :
		await send("?? ?????????????? ???????? ??????????????????????????????")
		return

#descarga de archivos y enlaces
@bot.on_message(filters.media & filters.private)
async def delete_draft_y_down_media(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	if str(message).split('"file_name": ')[1].split(",")[0].replace('"',"").endswith(".txt") and Configs[username]["m"] == "d" :
		if message.from_user.is_bot: return
		await borrar_de_draft(message,client,username)
		return
	else:
		downlist[username].append(message)
		await send("?????????????? ??????????????, ?????? __/download__ ???? ???? ???? ????????????", quote=True)
		print(len(downlist[username]))
		return

@bot.on_message((filters.regex("https://") | filters.regex("http://")) & filters.private)
async def down_link(client: Client, message: Message):
	print(message)
	global procesos
	try:username = message.from_user.username
	except:
		print("Username no valido")
		return
	send = message.reply
	user_id = message.from_user.id
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		intento_msg = "@" + username + " ??Intento usarme sin su permiso??"
		await send("?? No puede usarme contacte a mi Propietario.????\n https://t.me/Pro_Slayerr\n De momento voy a decirle q usted intento usarme sin su permiso\n")
		await bot.send_message(chat_id='6156913619', text=intento_msg)
		await bot.send_message(chat_id=message.chat.id, text=mensaje, reply_markup=reply_markup)
		return
	else:pass
	if "youtu.be/" in message.text or "twitch.tv/" in message.text or "youtube.com/" in message.text or "xvideos.com" in message.text or "xnxx.com" in message.text:
		list = message.text.split(" ")
		initial_count = 0
		dir = 'downloads/'+ str(username)+'/'
		for path in os.listdir(dir):
			if os.path.isfile(os.path.join(dir, path)):
				initial_count += 1
		if initial_count == 0:
			pass
		else:
			await client.send_message(username,'??Su almacenamiento esta ocupado, para continuar use **/deleteall**')
			return
		url = list[0]
		try:format = str(list[1])
		except:format = "720"
		msg = await send("?????????????????????? ??????????????????ó??")
		await client.send_message(Channel_Id,f'**@{username} Envio un link de #youtube:**\n**Url:** {url}\n**Formato:** {str(format)}p')
		procesos += 1
		download = await ytdlp_downloader(url,user_id,msg,username,lambda data: download_progres(data,msg,format),format)
		if procesos != 0:
			procesos -= 1
		await msg.edit("???????????????? ??????????????")
		await msg.edit("?????????????? ????????????????")
		msg = files_formatter(str(root[username]["actual_root"]),username)
		await limite_msg(msg[0],username)
		return
	
	elif "https://www.mediafire.com/" in message.text:
		initial_count = 0
		dir = 'downloads/'+ str(username)+'/'
		for path in os.listdir(dir):
			if os.path.isfile(os.path.join(dir, path)):
				initial_count += 1
		if initial_count == 0:
			pass
		else:
			await client.send_message(username,'??Su almacenamiento esta ocupado, para continuar use **/deleteall**')
			return
		url = message.text
		if "?dkey=" in str(url):
			url = str(url).split("?dkey=")[0]
		msg = await send("?????????????????????? ??????????????????ó??")
		await client.send_message(Channel_Id,f'**@{username} Envio un link de #mediafire:**\n**Url:** {url}\n')
		procesos += 1
		file = await download_mediafire(url, str(root[username]["actual_root"])+"/", msg, callback=mediafiredownload)
		if procesos != 0:
			procesos -= 1
		await msg.edit("???????????????? ??????????????")
		await msg.edit("?????????????? ????????????????")
		msg = files_formatter(str(root[username]["actual_root"]),username)
		await limite_msg(msg[0],username)
		return
          
	elif "https://mega.nz/file/" in message.text:
		initial_count = 0
		dir = 'downloads/'+ str(username)+'/'
		for path in os.listdir(dir):
			if os.path.isfile(os.path.join(dir, path)):
				initial_count += 1
		if initial_count == 0:
			pass
		else:
			await client.send_message(username,'??Su almacenamiento esta ocupado, para continuar use **/deleteall**')
			return
		url = message.text
		mega = pymegatools.Megatools()
		try:
			filename = mega.filename(url)
			g = await send(f"Descargando su Archivo espere {filename} ...")
			data = mega.download(url,progress=None)	
			procesos += 1
			shutil.move(filename,str(root[username]["actual_root"]))
			await g.delete()
			msg = files_formatter(str(root[username]["actual_root"]),username)
			await limite_msg(msg[0],username)
			if procesos != 0:
				procesos -= 1
			return
		except Exception as ex:
			if procesos != 0:
				procesos -= 1
			if "[Error al descargar de Mega]" in str(ex): pass
			else:
				await send(ex)	
				return
	else:
		j = str(root[username]["actual_root"])+"/"

		url = message.text
		async with aiohttp.ClientSession() as session:
			async with session.get(url) as r:
				try:
					filename = unquote_plus(url.split("/")[-1])
				except:
					filename = r.content_disposition.filename	
				fsize = int(r.headers.get("Content-Length"))
				total_up[username]['P']+=fsize
				msg = await send("?????????????????????? ??????????????????ó??")
				procesos += 1
				await client.send_message(Channel_Id,f'**@{username} Envio un #link :**\n**Url:** {url}\n')
				f = open(f"{j}{filename}","wb")
				newchunk = 0
				start = time()
				async for chunk in r.content.iter_chunked(1024*1024):
					newchunk+=len(chunk)
					await mediafiredownload(newchunk,fsize,filename,start,msg)
					f.write(chunk)
				f.close()
				file = f"{j}{filename}"
				await msg.edit("???????????????? ??????????????")
				if procesos != 0:
					procesos -= 1
				else:pass
				await msg.edit("?????????????? ????????????????")
				msg = files_formatter(str(root[username]["actual_root"]),username)
				await limite_msg(msg[0],username)
				return
      
#funciones
def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.2f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.2f%s%s" % (num, 'Yi', suffix)

def get_webservice_token(host='',username='',password='',proxy=None): 
	try:
		pproxy = None 
		webserviceurl = f'{host}login/token.php?service=moodle_mobile_app&username={username}&password={password}' 
		resp = requests.get(webserviceurl, proxies=pproxy,timeout=8) 
		data = json.loads(resp.text) 
		if data['token']!='': 
			return data['token'] 
		return None 
	except: return None

async def delete_nube(url,username):
	proxy = Configs["gp"] 
	if proxy == "":
		connection = aiohttp.TCPConnector()
	else:
		connection = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
	session = aiohttp.ClientSession(connector=connection)

	async with ClientSession(connector=connection) as s:
		user = Config[username]["username"]
		passw = Config[username]["password"]
		host = Config[username]["host"]
		
		client = moodle(user, passw, host)
		loged = await client.login(s)
		
		if loged:
			a = await client.delete_nexc(url,s)
			
		else :
			return False

def descomprimir(archivo,ruta):
	archivozip = archivo
	with ZipFile(file = archivozip, mode = "r", allowZip64 = True) as file:
		archivo = file.open(name = file.namelist()[0], mode = "r")
		archivo.close()
		guardar = ruta
		file.extractall(path = guardar)

async def limite_msg(text,username):
	lim_ch = 1500
	text = text.splitlines() 
	msg = ''
	msg_ult = '' 
	c = 0
	for l in text:
		if len(msg +"\n" + l) > lim_ch:		
			msg_ult = msg
			await bot.send_message(username,msg)	
			msg = ''
		if msg == '':	
			msg+= l
		else:		
			msg+= "\n" +l	
		c += 1
		if len(text) == c and msg_ult != msg:
			await bot.send_message(username,msg)

def update_progress_bar(inte,max):
	percentage = inte / max
	percentage *= 100
	percentage = round(percentage)
	hashes = int(percentage / 5)
	spaces = 20 - hashes
	progress_bar = "[ " + " ?" * hashes + "?" * spaces + " ] " + str(percentage) + "%"
	percentage_pos = int(hashes / 1)
	percentage_string = str(percentage) + "%"
	progress_bar = progress_bar[:percentage_pos] + progress_bar[percentage_pos :]
	return(progress_bar)

def iprox(proxy):
    tr = str.maketrans(
        "@./=#$%&:,;_-|0123456789abcd3fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "ZYXWVUTSRQPONMLKJIHGFEDCBAzyIwvutsrqponmlkjihgf3dcba9876543210|-_;,:&%$#=/.@",
    )
    return str.translate(proxy[::2], tr) 

def files_formatter(path,username):
    rut = str(path)
    filespath = Path(str(path))
    result = []
    dirc = []
    final = []
    for p in filespath.glob("*"):
        if p.is_file():
           result.append(str(Path(p).name))
        elif p.is_dir():
             dirc.append(str(Path(p).name))
    result.sort()
    dirc.sort()
    msg = f'**Ruta: **`{str(rut).split("downloads/")[-1]}`\n\n'
    if result == [] and dirc == [] :
        return msg , final
    for k in dirc:
        final.append(k)
    for l in result:
        final.append(l)
    i = 0
    for n in final:
        try:
            size = Path(str(path)+"/"+n).stat().st_size
        except: pass
        if not "." in n:
            msg+=f"**??? /seven {i} ??? /rmdir {i} ??? /cd {i} ?\n??**??Carpeta:** `{n}`\n\n" 
            i += 1
        else:
            #i += 1
            msg+=f"**??? /up {i} ??? /rm {i} ??? /dl {i} ?\n?? {sizeof_fmt(size)} - ** `?? {n}`\n"
            i += 1
    msg+= f"\n**Eliminar Todo**\n\n    **/deleteall**"
    return msg , final

async def extractDownloadLink(contents):
    for line in contents.splitlines():
        m = re.search(r'href="((http|https)://download[^"]+)', line)
        if m:
            return m.groups()[0]

async def download_mediafire(url, path, msg, callback=None):
	session = aiohttp.ClientSession()
	response = await session.get(url)
	url = await extractDownloadLink(await response.text())
	response = await session.get(url)
	filename = response.content_disposition.filename
	f = open(path+"/"+filename, "wb")
	chunk_ = 0
	total = int(response.headers.get("Content-Length"))
	start = time()
	while True:
		chunk = await response.content.read(1024)
		if not chunk:
			break
		chunk_+=len(chunk)
		if callback:
			await callback(chunk_,total,filename,start,msg)
		f.write(chunk)
		f.flush()
	return path+"/"+filename

def sevenzip(fpath: Path, password: str = None, volume = None):
    filters = [{"id": FILTER_COPY}]
    fpath = Path(fpath)
    fsize = fpath.stat().st_size
    if not volume:
        volume = fsize + 1024
    ext_digits = len(str(fsize // volume + 1))
    if ext_digits < 3:
        ext_digits = 3
    with MultiVolume(
        fpath.with_name(fpath.name+".7z"), mode="wb", volume=volume, ext_digits=ext_digits
    ) as archive:
        with SevenZipFile(archive, "w", filters=filters, password=password) as archive_writer:
            if password:
                archive_writer.set_encoded_header_mode(True)
                archive_writer.set_encrypted_header(True)
            archive_writer.write(fpath, fpath.name)
    files = []
    for file in archive._files:
        files.append(file.name)
    return files

def filezip(fpath: Path, password: str = None, volume = None):
    filters = [{"id": FILTER_COPY}]
    fpath = Path(fpath)
    fsize = fpath.stat().st_size
    if not volume:
        volume = fsize + 1024
    ext_digits = len(str(fsize // volume + 1))
    if ext_digits < 3:
        ext_digits = 3
    with MultiVolume(
        fpath.with_name(fpath.name+"zip"), mode="wb", volume=volume, ext_digits=0) as archive:
        with SevenZipFile(archive, "w", filters=filters, password=password) as archive_writer:
            if password:
                archive_writer.set_encoded_header_mode(True)
                archive_writer.set_encrypted_header(True)
            archive_writer.write(fpath, fpath.name)
    files = []
    for file in archive._files:
        files.append(file.name)
    return files

def update(username):
    Configs[username] = {"z": 900,"m":"e","a":"a"}
async def get_messages():
	msg = await bot.get_messages(Channel_Id,message_ids=db_access)
	Configs.update(loads(msg.text))
	return
async def send_config():
	try:
		await bot.edit_message_text(Channel_Id,message_id=db_access,text=dumps(Configs,indent=4))
	except:
		#await bot.send_message(Channel_Id,text=dumps(Configs,indent=4))
		pass

async def ytdlp_downloader(url,usid,msg,username,callback,format):
	class YT_DLP_LOGGER(object):
		def debug(self,msg):
			pass
		def warning(self,msg):
			pass
		def error(self,msg):
			pass
	j = str(root[username]["actual_root"])+"/"
	resolution = str(format)	
	dlp = {"logger":YT_DLP_LOGGER(),"progress_hooks":[callback],"outtmpl":f"./{j}%(title)s.%(ext)s","format":f"best[height<={resolution}]"}
	downloader = yt_dlp.YoutubeDL(dlp)
	loop = asyncio.get_running_loop()
	filedata = await loop.run_in_executor(None,downloader.extract_info, url)
	filepath = downloader.prepare_filename(filedata)
	return filedata["requested_downloads"][0]["_filename"]	

seg = 0
def download_progres(data,message,format):
	if data["status"] == "downloading":
		filename = data["filename"].split("/")[-1]
		_downloaded_bytes_str = data["_downloaded_bytes_str"]
		_total_bytes_str = data["_total_bytes_str"]
		if _total_bytes_str == "N/A":
			_total_bytes_str = data["_total_bytes_estimate_str"]		
		_speed_str = data["_speed_str"].replace(" ","")
		_format_str = format		
		msg = f"?? Nombre: {filename}\n\n"
		msg+= f"?? Descargando: {_downloaded_bytes_str}\n\n ?? Total: {_total_bytes_str}\n\n"
		msg+= f"??Resolución: {_format_str}p\n\n"	
		global seg 
		if seg != localtime().tm_sec:
			try:message.edit(msg,reply_markup=message.reply_markup)
			except:pass
		seg = localtime().tm_sec
async def downloadmessage_progres(chunk,filesize,filename,start,message):
		now = time()
		diff = now - start
		mbs = chunk / diff
		msg = f"?? Nombre: {filename}\n\n"
		try:
			msg += update_progress_bar(chunk, filesize) + "\n\n ?? Velocidad: " + sizeof_fmt(mbs) + "/s\n\n"
		except:pass
		msg+= f"?? Descargando: {sizeof_fmt(chunk)}\n\n ?? Total: {sizeof_fmt(filesize)}\n\n"	
		global seg
		if seg != localtime().tm_sec:
			try: await message.edit(msg)
			except:pass
		seg = localtime().tm_sec
def uploadfile_progres(chunk,filesize,start,filename,message):
	now = time()
	diff = now - start
	mbs = chunk / diff
	msg = f"?? Nombre: {filename}\n\n"
	try:
		msg += update_progress_bar(chunk, filesize) + "\n\n ?? Velocidad: " + sizeof_fmt(mbs) + "/s\n\n"
	except:pass
	msg+= f"?? Subiendo: {sizeof_fmt(chunk)}\n\n ?? Total: {sizeof_fmt(filesize)}\n\n"
	global seg
	if seg != localtime().tm_sec:
		message.edit(msg)
	seg = localtime().tm_sec
async def mediafiredownload(chunk,total,filename,start,message):
	now = time()
	diff = now - start
	mbs = chunk / diff
	msg = f"?? Nombre: {filename}\n\n"
	try:
		msg += update_progress_bar(chunk, filesize) + "\n\n ??Velocidad: " + sizeof_fmt(mbs) + "/s\n\n"
	except: pass
	msg+= f"?? Descargando: {sizeof_fmt(chunk)} ?? Total: {sizeof_fmt(total)}\n\n"
	global seg
	if seg != localtime().tm_sec:
		try: await message.edit(msg)
		except:pass
	seg = localtime().tm_sec
async def downloadmessage_tg(chunk,filesize,filename,start,message):
		now = time()
		diff = now - start
		mbs = chunk / diff
		msg = f"?? Nombre: {filename}\n\n"
		try:
			msg += update_progress_bar(chunk, filesize) + "\n\n ?? Velocidad: " + sizeof_fmt(mbs) + "/s\n\n"
		except:pass    
		msg+= f"?? Subido:: {sizeof_fmt(chunk)} ?? Total: {sizeof_fmt(filesize)}\n\n"	
		global seg
		if seg != localtime().tm_sec:
			try: await message.edit(msg)
			except:pass
		seg = localtime().tm_sec


class MoodleClient:
	def __init__(self,username,password,moodle,proxy):
		self.url = moodle
		self.username = username
		self.password = password
		self.session = aiohttp.ClientSession(cookie_jar=aiohttp.CookieJar(unsafe=True),connector=proxy)
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"}
		
	async def uploadtoken(self,f,progress,token):
		url = self.url+"/webservice/upload.php"
		file = Progress(f,progress)
		query = {"token":token,"file":file}
		async with self.session.post(url,data=query,headers=self.headers,ssl=False) as response:
			text = await response.text()
		dat = loads(text)[0]
		url = self.url+"/draftfile.php/"+str(dat["contextid"])+"/user/draft/"+str(dat["itemid"])+"/"+str(quote(dat["filename"]))
		urlw = self.url+"/webservice/rest/server.php?moodlewsrestformat=json"
		query = {"formdata":f"name=Event&eventtype=user&timestart[day]=31&timestart[month]=9&timestart[year]=3786&timestart[hour]=00&timestart[minute]=00&description[text]={quote_plus(url)}&description[format]=1&description[itemid]={randint(100000000,999999999)}&location=&duration=0&repeat=0&id=0&userid={dat['userid']}&visible=1&instance=1&_qf__core_calendar_local_event_forms_create=1","moodlewssettingfilter":"true","moodlewssettingfileurl":"true","wsfunction":"core_calendar_submit_create_update_form","wstoken":token}
		async with self.session.post(urlw,data=query,headers=self.headers,ssl=False) as response:
			text = await response.text()	
		try:
			a = findall("https?://[^\s\<\>]+[a-zA-z0-9]",loads(text)["event"]["description"])[-1].replace("pluginfile.php/","webservice/pluginfile.php/")+"?token="+token	
			return a , url	
		except:
			return url
class RevistasClient:
	def __init__(self,host,user,passw,up_id):
		self.user = user
		self.passw = passw
		self.host = host
		proxy = aiohttp.TCPConnector()
		self.up_id = up_id
		self.session = aiohttp.ClientSession(connector=proxy)
		self.csrfToken = ''
		self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'}
	async def login(self) -> bool:
		async with self.session.get(self.host+'login',headers=self.headers) as resp:
			soup = BeautifulSoup(markup=resp.text,features="html.parser")
			self.csrfToken = soup.find("input",attrs={"name":"csrfToken"})['value']
			print(self.csrfToken)
		url_post = self.host + 'login/signIn'
		print('00')
		
		data = aiohttp.FormData()
		data.add_field('csrfToken', self.csrfToken)
		data.add_field('source', '')
		data.add_field('username', self.user)
		data.add_field('password', self.passw)
		data.add_field('remember', '1')
		print(data)
		async with self.session.post(url_post,data=data,headers=self.headers) as resp1:
			print('1')
		async with self.session.get(self.host+'user/profile',headers=self.headers) as resp2:
			if resp2.url == self.host+'user/profile':
				print('Login Exito')
				return True
			else:
				print('Login Error')
				return False
	async def uploadfile_rv(self,file,msg,username):
		filename_god = file
		filename = str(file).split('/')[-1]
		q = Progress(filename_god,lambda current,total,timestart,filename: uploadfile_progres(current,total,timestart,filename,msg))
		data = aiohttp.FormData()
		data.add_field("fileStage", "2")
		data.add_field("name[es_ES]", file)
		data.add_field("name[en_US]", file)
		data.add_field("file", q)
		self.headers["X-Csrf-token"] = self.csrfToken
		post_file_url = self.host + 'api/v1/submissions/'+ self.up_id +'/files'
		async with self.session.post(post_file_url,data=data,headers=self.headers) as resp:
			text = resp2.text
		if '_href' in text:
			parse = str(text).replace('\/','/')
			url = str(parse).split('url":"')[1].split('"')[0]
			print('URL=',url)
			return url
		
class Progress(BufferedReader):
    def __init__(self, filename, read_callback):
        f = open(filename, "rb")
        self.filename = Path(filename).name
        self.__read_callback = read_callback
        super().__init__(raw=f)
        self.start = time()
        self.length = Path(filename).stat().st_size

    def read(self, size=None):
        calc_sz = size
        if not calc_sz:
            calc_sz = self.length - self.tell()
        self.__read_callback(self.tell(), self.length,self.start,self.filename)
        return super(Progress, self).read(size)
#Acceso de Uso al BoT
def comprobacion_de_user(username):
	if username in Configs or username in boss:			
		if exists('downloads/'+str(username)+'/'):pass
		else:os.makedirs('downloads/'+str(username)+'/')	
		try:Urls[username]
		except:Urls[username] = []
		try:Config[username]
		except:Config[username] = {"username":"","password":"","repoid":"","host":""}
		try:id_de_ms[username]
		except:id_de_ms[username] = {"msg":"","proc":""}
		try:root[username]
		except:root[username] = {"actual_root":f"downloads/{str(username)}"}
		try:downlist[username]
		except:downlist[username] = []
	else:
		return False

def comprobar_solo_un_proceso(username):
    if id_de_ms[username]["proc"] == "Up" :
        rup = "`Por Favor Espere, Ya posee una Tarea Activa\nUse: ` **/cancel** ` para Cancelar ? la Actual`"
        return rup
    else:
        return False

def total_de_procesos():
    global procesos
    hgy = "`??BoT Ocupado, Prueba más Tarde ??`"
    if procesos >= 100:
        return hgy
    else:
        return False

async def borrar_de_draft(message,client,username):
	pro = Configs["gp"]
	proxysall = {'https': pro, 'http': pro}
	proxy = proxysall
	use = Config[username]["username"]
	pase = Config[username]["password"]
	hoe = Config[username]["host"]
	txt = await message.download()
	a = await client.send_message("??????????????????????? ????????????????")
	try:
		rep = requests.get(hoe,proxies=proxy,timeout=20,allow_redirects=False)
		await a.edit("???????????????? ???????????? ?")
	except:
		await a.edit(f"{hoe} is Down")
		return
	await a.edit('??????????????????????? ????????????????????ó??...')
	with open(txt, "rb") as f:
		msg = f.read().decode("UTF-8")
		for i in msg.split('\n'):
			if not 'h' in i:
				continue
			Urls_draft[username].append(i)
		os.unlink(txt)
		a = await a.edit('???????????????????? ???????? ?????????????')
		count = 1
		await a.edit(f"???????????????? 1 ???????? ???? ???? ????????...?")
		while len(Urls_draft[username]) != 0:
			for i in Urls_draft[username]:			
				ret = delete(use,pase,hoe,i,proxy)
				if ret != False:
					count += 1
					await a.edit(f"???????????????? **{count}** ???????? ???? ???? ????????...?")
					Urls_draft[username].remove(i)
				else:
					continue
		if len(Urls_draft[username]) == 0:
			await a.edit('?????? ?????????????????? ???????????????????????????')
			return		
		else:
			f = len(Urls_draft[username])
			await a.edit(f"?????????? {f} ??????(??) ???? ??????????????????(??).")
			return

async def uploaddraft(file,usid,msg,username):
	user = Config[username]["username"]
	password = Config[username]["password"]
	host = Config[username]["host"]
	repoid = Config[username]["repoid"]
	zips = Configs[username]["z"]
	proxy = Configs[username]["gp"]
	print(1000)

	if proxy == False:
		connector = None
	else:
		connector = proxy
	if proxy == False:
		connection = aiohttp.TCPConnector()
	else:
		connection = aiohttp_socks.ProxyConnector(ssl=False).from_url(f"{proxy}")
	
	session = aiohttp.ClientSession(connector=connection)
	await msg.edit("?????????????????????? ??????????????????ó??")
	filename = Path(file).name
	filesize = Path(file).stat().st_size
	zipssize = 1024*1024*int(zips)
	
	await msg.edit("??????????????????????? ????????????????")
	try:
		async with session.get(host,timeout=20,ssl=False) as resp:
			await resp.text()
			await msg.edit("???????????????? ???????????? ?")
	except Exception as ex:
		await msg.edit(f"{host} is Down:\n\n{ex}")
		return
	
	id_de_ms[username] = {"msg":msg, "pat":filename, "proc":"Up"}
	
	if filesize > zipssize:
		await msg.edit("?? ????????????????????????")
		files = sevenzip(file,volume=zipssize)
		
		client = MoodleClient2(host,user,password,repoid,connector)
		links = []
		for file in files:	
			try:
				upload = await client.LoginUpload(file,lambda size,total,start,filename: uploadfile_progres(size,total,start,filename,msg))
				await bot.send_message(usid,f"**{upload}**")
				links.append(upload)
			except Exception as ex:
				if "[400 MESSAGE_ID_INVALID]" in str(ex): pass
				else:
					await bot.send_message(usid,f"?????????? ???? ??????????:\n\n{ex}")
				id_de_ms[username]["proc"] = ""
				return
		message = ""
		for link in links:
			message+=f"{link}\n"
		await msg.edit("? ???????????????????? ????????????????????????")
		with open(filename+".txt","w") as txt:
			txt.write(message)
		await bot.send_document(usid,filename+".txt",caption="Gracias por usar nuestros sevicios\nPara continuar subiendo use **/ls** :)")
		if username in boss:
			pass
		else:
			await bot.send_message(Channel_Id,f"? ???????????????????? ????????????????????????\n\n????????????: {filename}\n??{message}")
			await bot.send_document(Channel_Id,filename+".txt")
		id_de_ms[username]["proc"] = ""
		os.unlink(filename+".txt")
		return
	else:
		client = MoodleClient2(host,user,password,repoid,connector)
		try:
			upload = await client.LoginUpload(file,lambda size,total,start,filename: uploadfile_progres(size,total,start,filename,msg))
			await msg.edit(f"__**{upload}**__")
			with open(filename+".txt","w") as txt:
				txt.write(upload)
			await bot.send_document(usid,filename+".txt",caption="Gracias por usar nuestros sevicios\nPara continuar subiendo use **/ls** :)")
			if username in boss:
				pass
			else:
				await bot.send_message(Channel_Id,f"? ???????????????????? ????????????????????????\n\n????????????: {filename}\n??{upload}")
				await bot.send_document(Channel_Id,filename+".txt")
			id_de_ms[username]["proc"] = ""
			os.unlink(filename+".txt")
			return
		except Exception as ex:
			if "[400 MESSAGE_ID_INVALID]" in str(ex): pass
			else:
				await bot.send_message(usid,f"?????????? ???? ??????????:\n\n{ex}")
			id_de_ms[username]["proc"] = ""
			return

async def uploadfile(file,usid,msg,username):
	proxy = Configs["gp"]
	mode = Configs[username]["a"]
	usernamew = ''
	passwordw = ''
	
	if mode == "c":
		moodle = "https://ia.mined.gob.cu/"
		token = Configs["ia"]
		connector = aiohttp.TCPConnector()
	elif mode == "h":
		moodle = "https://aulauvs.gtm.sld.cu"
		token = Configs["gtm"]
		if proxy == "":
			connector = aiohttp.TCPConnector()
		else:
			connector = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
	elif mode == "b":
		moodle = "https://uvs.ucm.cmw.sld.cu"
		token = Configs["uvs"]
		if proxy == "":
			connector = aiohttp.TCPConnector()
		else:
			connector = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
	elif mode == "l":
		moodle = "https://uvs.ltu.sld.cu"
		token = Configs["ltu"]
		if proxy == "":
			connector = aiohttp.TCPConnector()
		else:
			connector = aiohttp_socks.ProxyConnector(ssl=False).from_url(f"{proxy}")
	elif mode == "v":
		moodle = "https://www.aula.vcl.sld.cu"
		token = Configs["vcl"]
		if proxy == "":
			connector = aiohttp.TCPConnector()
		else:
			connector = aiohttp_socks.ProxyConnector(ssl=False).from_url(f"{proxy}")
	elif mode == "u":
		moodle = "https://moodle.uccfd.cu"
		token = Configs["uccfd"]
		if proxy == "":
			connector = aiohttp.TCPConnector()
		else:
			connector = aiohttp_socks.ProxyConnector(ssl=False).from_url(f"{proxy}")
	elif mode == "a":
		moodle = "https://ia.mined.gob.cu/"
		uset = Config[username]["luisernestorb95"]
		pasel = Config[username]["Luisito1995*"]
		hot = Config[username]["host"]
		connector = aiohttp.TCPConnector()
		await msg.edit(f"???????????????????? ??????????")
		try:
			token = get_webservice_token(hot,uset,pasel)
			await msg.edit(f"? ?????????? ????????????????")
		except:
			id_de_ms[username]["proc"] = ""
			return		
	elif mode == "t":
		moodle = "https://ia.mined.gob.cu/"
		hot = "https://ia.mined.gob.cu/"
		uset = Configs["ucuser"]
		pasel = Configs["ucpass"]
		connector = aiohttp.TCPConnector()
		token = Configs["uclv_p"]	
	
	zips = Configs[username]["z"]

	if mode == "a" or mode == "c" or mode == "t":
		if int(zips) > 99:
			await msg.edit("????? ?????? ia ?????? ???????? ???? ???????????? ?????? ?????????????? ?? 99 ????")
			return
	elif mode  == "b":
		if int(zips) > 499:
			await msg.edit("????? ?????? ??????.?????? ?????? ???????? ???? ???????????? ?????? ?????????????? ?? 499 ????")
			return
	elif mode == "l":
		if int(zips) > 249:
			await msg.edit("????? ?????? ??????.?????? ?????? ???????? ???? ???????????? ?????? ?????????????? ?? 249 ????")
			return
	elif mode == "h":
		if int(zips) > 7:
			await msg.edit("????? ?????? ????????.?????? ?????? ???????? ???? ???????????? ?????? ?????????????? ?? 7 ????")
			return
	elif mode == "v":
		if int(zips) > 299:
			await msg.edit("????? ?????? Aula.vcl ?????? ???????? ???? ???????????? ?????? ?????????????? ?? 300 ????")
			return
	elif mode == "u":
		if int(zips) > 5:
			await msg.edit("????? ?????? uccfd ?????? ???????? ???? ???????????? ?????? ?????????????? ?? 5 ????")
			return
	
	session = aiohttp.ClientSession(connector=connector)
	await msg.edit("?????????????????????? ??????????????????ó??")
	filename = Path(file).name
	filesize = Path(file).stat().st_size
	zipssize = 1024*1024*int(zips)
	logerrors = 0
	error_conv = 0
	logslinks = []

	try:
		async with session.get(moodle,timeout=20,ssl=False) as resp:
			await resp.text()
			await msg.edit("? ???????????????? ???????????? ?")
	except Exception as ex:
		await msg.edit(f"{moodle} is Down:\n\n{ex}")
		return

	id_de_ms[username] = {"msg":msg, "pat":filename, "proc":"Up"}

	if filesize-1048>zipssize:
		parts = round(filesize / zipssize)
		await msg.edit(f"?? ????????????????????????")
		files = sevenzip(file,volume=zipssize)
		await msg.edit("??????????????????????? ????????????????")
		
		client = MoodleClient(usernamew,passwordw,moodle,connector)
	
		for path in files:
				while logerrors < 5:
					error_conv = 0
					try:
						upload = await client.uploadtoken(path,lambda chunk,total,start,filen: uploadfile_progres(chunk,total,start,filen,msg),token)
						
						if mode == "l" or mode == "b":
							upload = upload[1]
							upload = upload.replace('draftfile.php/','webservice/draftfile.php/')
							upload = str(upload) + '?token=' + token
						elif mode == "a" or mode == "t":
							while error_conv < 10:
							
								await msg.edit("???????????????????? ???????? ??????????????????")
								await msg.edit("????????????????????????, ?????? ????????????????...")
								upload = upload[1]
								upload = await move_to_profile(hot,uset,pasel,upload)
								if upload != False:	
									upload = upload.replace('pluginfile.php/','webservice/pluginfile.php/')
									upload = str(upload) + '?token=' + token
									
									error_conv = 0
									break
								else:
									await msg.edit("??????????, ????????????????????????")
									error_conv +=1
									
									continue	
						else: 
							upload = upload[0]
						
						if upload == False:
							await bot.send_message(usid,f"?????????? ???? ??????????.")
							id_de_ms[username]["proc"] = ""
							return
						else:pass
						
						await bot.send_message(usid,f"__**{upload}**__",disable_web_page_preview=True)
						logslinks.append(upload)
						logerrors = 0
					
						break
					except Exception as ex:
				
						logerrors += 1
						if logerrors > 4:
							if "[400 MESSAGE_ID_INVALID]" in str(ex): pass
							else:
								await bot.send_message(usid,f"?????????? ???? ??????????:\n\n{ex}")
							id_de_ms[username]["proc"] = ""
							return
						
		if len(logslinks) == len(files):
				await msg.edit("? ???????????????????? ????????????????????????")
				with open(filename+".txt","w") as f:
					message = ""
					for li in logslinks:
						message+=li+"\n"
					f.write(message)		
				await bot.send_document(usid,filename+".txt",caption="Gracias por usar nuestros sevicios\nPara continuar subiendo use **/ls** :)")
				if mode != "a":
					await bot.send_message(Channel_Id,f"? ???????????????????? ????????????????????????\n\n????????????: {filename}\n??{message}")
					await bot.send_document(Channel_Id,filename+".txt")
				else:pass
				id_de_ms[username]["proc"] = ""
				os.unlink(filename+".txt")
				return
		else:
				await msg.edit("???? ?????????????? ???? ????????????")	
				id_de_ms[username]["proc"] = ""
				return	
	
	else:		
		client = MoodleClient(usernamew,passwordw,moodle,connector)
	
		while logerrors < 5:
					error_conv = 0
					try:
						upload = await client.uploadtoken(file,lambda chunk,total,start,filen: uploadfile_progres(chunk,total,start,filen,msg),token)
					
						if mode == "l" or mode == "b":
							upload = upload[1]
							upload = upload.replace('draftfile.php/','webservice/draftfile.php/')
							upload = str(upload) + '?token=' + token
							
						elif mode == "a" or mode == "t":
							while error_conv < 10:
								
								await msg.edit("???????????????????? ???????? ??????????????????")
								await msg.edit("????????????????????????, ?????? ????????????????...")
								upload = upload[1]
								upload = await move_to_profile(hot,uset,pasel,upload)
							
								if upload != False:	
									upload = upload.replace('pluginfile.php/','webservice/pluginfile.php/')
									upload = str(upload) + '?token=' + token
									
									error_conv = 0
									break
								else:
									await msg.edit("??????????, ????????????????????????")
									error_conv +=1
									
									continue	
						else:
							upload = upload[0]
						
						if upload == False:
							await bot.send_message(usid,f"?????????? ???? ??????????.")
							id_de_ms[username]["proc"] = ""
							return
						else:pass
						
						await bot.send_message(usid,f"__**{upload}**__",disable_web_page_preview=True)
						logslinks.append(upload)
						logerrors = 0
			
						break
					except Exception as ex:
						
						logerrors += 1
						if logerrors > 4:
							if "[400 MESSAGE_ID_INVALID]" in str(ex): pass
							else:
								await bot.send_message(usid,f"?????????? ???? ??????????:\n\n{ex}")
							id_de_ms[username]["proc"] = ""
							return
		if len(logslinks) == 1:
				await msg.edit("? ???????????????????? ????????????????????????")
				with open(filename+".txt","w") as f:
					message = ""
					lin = ""
					for li in logslinks:
						message+=li+"\n"
						lin+=li+"\n"
					f.write(message)				
				await bot.send_document(usid,filename+".txt",caption="Gracias por usar nuestros sevicios\nPara continuar subiendo use **/ls** :)")
				if mode != "a":
					await bot.send_message(Channel_Id,f"? ???????????????????? ????????????????????????\n\n????????????: {filename}\n??{lin}")
					await bot.send_document(Channel_Id,filename+".txt")
				else:pass
				id_de_ms[username]["proc"] = ""
				os.unlink(filename+".txt")
				return
		else:
				await msg.edit("???? ?????????????? ???? ????????????")
				id_de_ms[username]["proc"] = ""
				return
async def up_revistas_api(file,usid,msg,username):
	try:
		host=Configs[username]["host"]
		user=Configs[username]['user']
		passw=Configs[username]['passw']
		up_id=Configs[username]['up_id']
		mode=Configs[username]['mode']
		zipssize=Configs[username]['z']*1024*1024
		filename = file.split("/")[-1]
		filesize = Path(file).stat().st_size
		print(21)
		proxy = Configs["gp"]
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'}
		#login
		msg = await msg.edit("?? Conectando ...")
		connector = aiohttp.TCPConnector()
		#connector = aiohttp_socks.ProxyConnector.from_url('socks5://143.244.205.72:1080')
		async with aiohttp.ClientSession(connector=connector) as session:
			async with session.get(host + "login") as response:
				html = await response.text()
			soup = BeautifulSoup(html, "html.parser")
			csrfToken = soup.find("input",attrs={"name":"csrfToken"})['value']
			url_post = host + 'login/signIn'
			payload = {}
			payload['csrfToken'] = csrfToken
			payload['source'] = ''
			payload['username'] = user
			payload['password'] = passw
			payload['remember'] = '1'
			async with session.post(url_post, data=payload) as e:
				print(222)
			url = host + 'user/profile'
			async with session.get(url) as resp:
				try:
					u = resp.url
				except:
					u = resp.url()
				if u==url:
					await msg.edit("®? Ocurrió un error en su Conexión")
				else:
					await msg.edit("?? Conectado ...")
					sleep(5)
					print(22)
					links = []
					if mode=='n':
						if filesize-1048>zipssize:
							parts = round(filesize / zipssize)
							await msg.edit(f"?? ????????????????????????\n\n?? Total: {parts} partes\n")
							files = sevenzip(file,volume=zipssize)
							print(24)
							for file in files:
								try:
									upload_data = {}
									upload_data["fileStage"] = "2"
									upload_data["name[es_ES]"] = file.split('/')[-1]
									upload_data["name[en_US]"] = file.split('/')[-1]
									post_file_url = host + 'api/v1/submissions/'+ up_id +'/files'
									fi = Progress(file,lambda current,total,timestart,filename: uploadfile_progres(current,total,timestart,filename,msg))
									query = {"file":fi,**upload_data}
									async with session.post(post_file_url,data=query,headers={'X-Csrf-token':csrfToken}) as resp:
										text = await resp.text()
										if '_href' in text:
											parse = str(text).replace('\/','/')
											url = str(parse).split('url":"')[1].split('"')[0]
											links.append(url)
										else:
											await msg.edit(f"?? Failed ??\nUP: {file.split('/')[-1]}")
								except:
									pass
							await msg.edit(f"? Finalizado \n\n{file.split('/')[-1]}\n[ .txt ] ??")
							txtname = file.split('.')[0].replace(' ','_')+'.txt'
							with open(txtname,"w") as t:
								message = ""
								for li in links:
									message+=li+"\n"
								t.write(message)
								t.close()
							await bot.send_document(usid,txtname)
						else:
							await msg.edit("?? Subiendo ??")
							upload_data = {}
							upload_data["fileStage"] = "2"
							upload_data["name[es_ES]"] = file.split('/')[-1]
							upload_data["name[en_US]"] = file.split('/')[-1]
							post_file_url = host + 'api/v1/submissions/'+ up_id +'/files'
							fi = Progress(file,lambda current,total,timestart,filename: uploadfile_progres(current,total,timestart,filename,msg))
							query = {"file":fi,**upload_data}
							async with session.post(post_file_url,data=query,headers={'X-Csrf-token':csrfToken}) as resp:
								text = await resp.text()
								if '_href' in text:
									parse = str(text).replace('\/','/')
									url = str(parse).split('url":"')[1].split('"')[0]
									await msg.edit(f"? Finalizado \n\n{file.split('/')[-1]}\n[ .txt ] ??")
									txtname = file.split('.')[0].replace(' ','_')+'.txt'
									with open(txtname,"w") as t:
										t.write(url)
										t.close()
									await bot.send_document(usid,txtname)
								else:
									await msg.edit(f"?? Failed ??\nUP: {file.split('/')[-1]}")
					else:
						if filesize-1048>zipssize:
							parts = round(filesize / zipssize)
							await msg.edit(f"?? ????????????????????????\n\n?? Total: {parts} partes\n")
							files = sevenzip(file,volume=zipssize)
							print(24)
							for file in files:
								try:
									upload_data = {}
									upload_data['name'] = file.split('/')[-1]
									upload_data['revisedFileId'] = ''
									upload_data['genreId'] = '86'
									fi = Progress(file,lambda current,total,timestart,filename: uploadfile_progres(current,total,timestart,filename,msg))
									query = {"uploadedFile":fi,**upload_data}
									post_file_url = host + '$$$call$$$/wizard/file-upload/file-upload-wizard/upload-file?submissionId=' + up_id + '&stageId=1&fileStage=2&reviewRoundId=&assocType=&assocId='
									async with session.post(post_file_url,data=query,headers={'X-Csrf-token':csrfToken}) as resp:
										text = await resp.text()
										try:
											fileId = str(text).split('"fileId":')[1].split(',')[0]
										except:
											print('Ahi no se encuentra fileId')
										if fileId:
											url = host+'$$$call$$$/api/file/file-api/download-file?fileId='+str(fileId)+'&revision=1&submissionId='+up_id+'&stageId=1'
											links.append(url)
										else:
											await msg.edit(f"?? Failed ??\nUP: {file.split('/')[-1]}")
								except:
									pass
							await msg.edit(f"? Finalizado \n\n{file.split('/')[-1]}\n[ .txt ] ??")
							txtname = file.split('.')[0].replace(' ','_')+'.txt'
							with open(txtname,"w") as t:
								message = ""
								for li in links:
									message+=li+"\n"
								t.write(message)
								t.close()
							await bot.send_document(usid,txtname)
						else:
							await msg.edit("?? Subiendo ??")
							upload_data = {}
							upload_data['name'] = file.split('/')[-1]
							upload_data['genreId'] = '86'
							#upload_data['revisedFileId'] = ''
							fi = Progress(file,lambda current,total,timestart,filename: uploadfile_progres(current,total,timestart,filename,msg))
							query = {"uploadedFile":fi,**upload_data}
							post_file_url = f'{host}$$$call$$$/wizard/file-upload/file-upload-wizard/upload-file?submissionId={up_id}&stageId=1&fileStage=2&reviewRoundId=&assocType=&assocId='
							async with session.post(post_file_url,data=query) as resp:
								text = await resp.text()
								#print(text)
								try:
									fileId = str(text).split('"fileId":')[1].split(',')[0]
									print(fileId)
								except:
									print('Ahi no se encuentra fileId')
								if fileId:
									url = host+'$$$call$$$/api/file/file-api/download-file?fileId='+str(fileId)+'&revision=1&submissionId='+up_id+'&stageId=1'
									await msg.edit(f"? Finalizado \n\n{file.split('/')[-1]}\n[ .txt ] ??")
									txtname = file.split('.')[0].replace(' ','_')+'.txt'
									with open(txtname,"w") as t:
										t.write(url)
										t.close()
									await bot.send_document(usid,txtname)
								else:
									await msg.edit(f"?? Failed ??\nUP: {file.split('/')[-1]}")
	except Exception as ex:
		print(str(ex))
		await msg.edit("®? Ocurrió un error en su Conexión")


async def uploadfileapi(file,usid,msg,username):
	host = "https://educa.uho.edu.cu/"
	proxy = Configs["gp"]
	print(proxy)
	zips = Configs[username]["z"]
	try:
		proxy = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
	except:
		proxy = aiohttp.TCPConnector()
	await msg.edit("?????????????????????? ??????????????????ó??")
	filename = file.split("/")[-1]
	filesize = Path(file).stat().st_size
	total_up[username]['S']+=filesize
	zipssize = 1992294
	logslinks = []
	if filesize-1048>zipssize:
		parts = round(filesize / zipssize)
		await msg.edit(f"?? ????????????????????????\n\n?? Total: {parts} partes\n?? Zips: 1.8 mb")
		files = sevenzip(file,volume=zipssize)
		session = aiohttp.ClientSession(connector=proxy)
		for file in files:
			try:
				if file.endswith(".zip"):
					filename_god = file
				else:
					file = filezip(file,volume=None)
					filename_god = file[0].split("zip")[0]+".zip"
					os.rename(file[0],filename_god)
				fi = Progress(filename_god,lambda current,total,timestart,filename: uploadfile_progres(current,total,timestart,filename,msg))
				query = {"s97304e7e":fi}
				async with session.post("https://educa.uho.edu.cu/ci_portal_uho/index.php/recursos_pre/my_grocery_recursos_pred/upload_file/archivo",data=query,timeout=60*30) as resp:
					url = loads(await resp.text())["files"][0]["url"]
					logslinks.append(url)
					root[username]["actual_root"] = "downloads/"+username  
			except Exception as ex:
				await bot.send_message(f'!Error:{ex}')
				return
		if len(logslinks) == len(files):
			await msg.delete()
			txtname = "downloads/"+username+"/"+str(filename).split('.')[0]+'.txt'
			with open(txtname,"w") as t:
				message = ""
				lin = ""
				for li in logslinks:
					message+=li+"\n"
					lin+=li+"\n"
				t.write(message)
				t.close()
			await bot.send_document(usid,txtname)
			shutil.rmtree("downloads/"+username+"/")
			root[username]["actual_root"] = "downloads/"+username
		else:
			await msg.edit("Ha fallado la subida ")
			shutil.rmtree("downloads/"+username+"/")
			root[username]["actual_root"] = "downloads/"+username+"/"
	else:
		async with aiohttp.ClientSession(connector=proxy) as session:
			try:	
				if file.endswith(".zip"):
					filename_god = file
				else:
					file = filezip(file,volume=None)
					filename_god = file[0].split("zip")[0]+".zip"
					os.rename(file[0],filename_god)
				fi = Progress(filename_god,lambda current,total,timestart,filename: uploadfile_progres(current,total,timestart,filename,msg))
				query = {"s97304e7e":fi}
				async with session.post("https://educa.uho.edu.cu/ci_portal_uho/index.php/recursos_pre/my_grocery_recursos_pred/upload_file/archivo",data=query,timeout=60*30) as resp:
					url = loads(await resp.text())["files"][0]["url"]
					await bot.send_message(usid,f"[{Path(filename_god).name}]({url})",disable_web_page_preview=True)
					logslinks.append(url)
					root[username]["actual_root"] = "downloads/"+username
			except Exception as ex:
				await bot.send_message(f'!Error:\n{ex}')
				return
							
			if len(logslinks) == 1:
				await msg.edit("**Finalizado exitosamente**")
				with open(filename_god+".txt","w") as t:
					message = ""
					lin = ""
					for li in logslinks:
						message+=li+"\n"
						lin+=li+"\n"
					t.write(message)
				await bot.send_document(usid,filename+".txt")
			else:
				await msg.edit("Ha fallado la subida")


@async_decorator
def nextcom(user, passw, host, proxy,send,files,msg,username,user_id):
	client = NexCloudClient.NexCloudClient(user,passw,host,proxy=proxy)
	loged = client.login()
	if loged:
		filesdata = []
		remotepath = ""
		for file in files:
		   msg.edit(f"Subiendo {file}..")
		   filename = str(file).replace(f'downloads/{username}/','')
		   data = client.upload_file(file,filename,path=remotepath,progressfunc=None,args=(None,None,filename,None),tokenize=None)
		   filesdata.append(data)
		   send(data)
		name = filename+'.txt'
		files = []
		txt = open(name,'w')
		message = ""
		for data in filesdata:
			message+=data+"\n"
		txt.write(message)
		txt.close()
		asyncio.run(bot.send_document(user_id,name))
		return
	else:
		return "Error"


@async_decorator
def next(user, passw, host, proxy,send,file,msg,username):
	client = NexCloudClient.NexCloudClient(user,passw,host,proxy=proxy)
	loged = client.login()
	if loged:
		filesdata = []
		remotepath = ""
		msg.edit(f"Subiendo {file}..")
		filename = str(file).replace(f'downloads/{username}/','')
		data = client.upload_file(file,filename,path=remotepath,progressfunc=None,args=(None,None,filename,None),tokenize=None)
		send(data)
		filesdata.append(data)
		return filesdata
	else:
		return "Error"
		

async def proccess(filex,user_id,msg,username):
        try:
        	send = msg.reply
        	logslinks = []
        	proxy = Configs[username]["gp"]
        	user = Config[username]["username"]
        	passw = Config[username]["password"]
        	host = Config[username]["host"]
        	zips = Configs[username]["z"]
        	file = filex
        	filesize = Path(file).stat().st_size
        	print(20)
        	zipssize = 1024*1024*int(zips)
        	filename = str(file).replace(f'downloads/{username}/','')        
        	if filesize>zipssize:
        	    await msg.edit(f"COMPRIMIENDO")
        	    zipname = str(filename).split('.')[0]
        	    files = sevenzip(file,volume=zipssize)
        	    await msg.edit(f"Preparando Entorno..")
        	    remotepath = "Descargas"        	    
        	    loged = await nextcom(user, passw, host, proxy,send,files,msg,username,user_id)
        	    print(21)
        	    if "Error" not in loged:
        	    	ms = "Links:\n"
        	    	await msg.edit(ms)
        	    	return
        	    await msg.edit(f"Error al loguear...")
        	    return
        	    
#####sincompress####        	    
        	if filesize<=zipssize:
        	   	await msg.edit(f"Preparando Entorno...")
        	   	remotepath = ""
        	   	loged = await next(user, passw, host, proxy,send,file,msg,username)
        	   	if "Error" not in loged:
        	   		client = loged       
        	   		await msg.edit(f"Finalizado...") 	   		
        	   	return
        	   	await msg.edit(f"Error al loguear...")
        	   	return
        except Exception as ex:
            		print(ex)	         		
            #		await msg.edit(f'??{str(ex)}??')
            	
            	      	
         	
try:
	os.unlink("bot.session")
except:pass
try:
	os.unlink("bot.session-journal")
except:pass

print("started")
bot.start()
print(10)
bot.loop.run_forever()
