import shutil
import asyncio
import tgcrypto
import aiohttp
import aiohttp_socks
import yt_dlp
import os
import aiohttp
import re
import requests
import json
import psutil
import platform
import pymegatools
from pyrogram import Client , filters
from pyrogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
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
import threading

#BoT Configuration Variables
api_id = 10181262
api_hash = "f52b5a057b73b9974eaa7403e04907f0"
bot_token = "5827190779:AAG_e6U2HkzVLZ38yNuqm7RRPkgUp_PDMGw"
Channel_Id = -1001858527257
msg_id = 3
bot = Client("bot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)
boss = ['UHTRED_OF_BEBBANBURG','luisernesto95']#usuarios supremos
Configs = {"vcl":'035649148fac062426ee3c5d72a6ec1f',"gtm":"cc9c6b9c0523b17c7f00202993ceac1c","uvs":"4ce7bf57fb75c046a9fbdd30900ea7c9","ltu":"a816210ff41853b689c154bad264da8e",
			"ucuser": "", "ucpass":"","uclv_p":"", "gp":'socks5://181.225.255.48:9050', "s":"On", 
			'luisernesto95': {'z': 99,"m":"u","a":"c","t":"y"}, 
			'luisernesto95': {'z': 99,"m":"u","a":"upltu","t":"y"}
			}
start = time()
Urls = {} #urls subidos a educa
Urls_draft = {} #urls para borrar de draft
Config = {} #configuraciones privadas de moodle
id_de_ms = {} #id de mensage a borrar con la funcion de cancelar
root = {} #directorio actual
downlist = {} #lista de archivos descargados
procesos = 0 #numero de procesos activos en el bot

##Base De Datos

###############

###Buttons
@bot.on_message(filters.command('timer') & filters.private)
async def timer(bot, message):
    uptime = get_readable_time(time() - start)
    username = message.from_user.username
    msg =  await bot.send_message(username, uptime)
    global seg
    if seg != localtime().tm_sec:
        try: await message.edit(msg)
        except:pass
    seg = localtime().tm_sec

nubess = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('☁️ UVS.LTU ☁️', callback_data="uvs"),
        InlineKeyboardButton('☁️ GTM ☁️', callback_data="gtm"),
        InlineKeyboardButton('☁️CMW ☁️', callback_data="cmw")],
        [InlineKeyboardButton('☁️Eduvirtual☁️', callback_data="edu"),
        InlineKeyboardButton('☁️Nube Personal☁️', callback_data="personal"),
        InlineKeyboardButton('☁️Extra☁️', callback_data="extra")],
        [InlineKeyboardButton('☁️ Eduvirtual Preconfigurada ☁️', callback_data="edup")],
        [InlineKeyboardButton('ᐊᐊᐊᐊᐊ', callback_data="home")
        ]]
    )
hom = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('☁️ Seleccionar Nube ☁️', callback_data="nubes")],
        [InlineKeyboardButton('⚙️ Info De Usuario ⚙️', callback_data="infouser"),
        InlineKeyboardButton('📈 Info Del BoT 📈', callback_data="infobot")],
        [InlineKeyboardButton('⚠️🆘⛑️ Ayuda ⛑️ 🆘 ⚠️', callback_data="ayuda")
        ]]
    )
atras = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ᐊᐊᐊᐊᐊ', callback_data="home")
        ]]
    )
delete = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🗑️Borrar Todo📂🗑️', callback_data="delet")
        ]]
    )
@bot.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    username = msg.from_user.username
    if msg.data == "nubes":
        await msg.message.edit(
            text="Seleccione La Nube☁️ a Subir:",
            reply_markup=nubess
        )
    elif msg.data == "uvs":
        Configs[username]["m"] = "pedroamh01"
        Configs[username]["a"] = "01062862726Aa*"
        Configs[username]["z"] = 19
        await send_config()
        await msg.message.edit(
            text="Ha Seleccionado la Nube☁️: uvs.ltu\nTamaño de Zips de la Nube☁️: 19 Mb",
            reply_markup=nubess
        )
    elif msg.data == "gtm":
        Configs[username]["m"] = "juju"
        Configs[username]["a"] = "Lianet123*#"
        Configs[username]["z"] = 7
        await send_config()
        await msg.message.edit(
            text="Ha Seleccionado la Nube☁️: GTM\nTamaño de Zips de la Nube☁️: 7 Mb",
            reply_markup=nubess
        )
    elif msg.data == "cmw":
        Configs[username]["m"] = "pepe"
        Configs[username]["a"] = "Lianet123*#"
        Configs[username]["z"] = 10
        await send_config()
        await msg.message.edit(
            text="Ha Seleccionado la Nube☁️: CMW\nTamaño de Zips de la Nube☁️: 499 Mb",
            reply_markup=nubess
        )
    elif msg.data == "edu":
        Configs[username]["m"] = "eduvirtual"
        Configs[username]["a"] = "eduvirtual"
        Configs[username]["z"] = 500
        Config[username]["username"] = "---"
        Config[username]["password"] = "---"
        await send_config()
        await msg.message.edit(
            text="Ha Seleccionado la Nube☁️: Edvirtual\nTamaño de Zips de la Nube☁️: 500 Mb\n\nTenga en cuenta q está configuración es solo si posee una cuenta en la misma o de lo contrario no podrá Utilizarla, use /auth para añadir los datos",
            reply_markup=nubess
        )
    elif msg.data == "edup":
        Configs[username]["m"] = "edup"
        Configs[username]["a"] = "edup"
        Configs[username]["z"] = 500
        Config[username]["username"] = "miltongg"
        Config[username]["password"] = "1234567i"
        Config[username]["host"] = "https://eduvirtual.uho.edu.cu/"
        Config[username]["repoid"] = 3
        await send_config()
        await msg.message.edit(
            text="Ha Seleccionado la nube ☁️ Eduvirtual Preconfigurada",
            reply_markup=nubess
        )
    elif msg.data == "personal":
        Configs[username]["m"] = "personal"
        Configs[username]["a"] = "personal"
        Configs[username]["z"] = 100
        await send_config()
        await msg.message.edit(
            text="Ha Seleccionado la Nube☁️: Subida a Nube Personal\nTamaño de Zips de la Nube☁️: 100 Mb\n\nUse /auth para añadir los datos de su cuenta personal",
            reply_markup=nubess
        )
    elif msg.data == "extra":
        Configs[username]["m"] = "u"
        Configs[username]["a"] = "vcl"
        Configs[username]["z"] = 299
        await msg.message.edit(
            text="Ha Seleccionado la Nube☁️: Extra\nTamaño de Zips de la Nube☁️: 299 Mb",
            reply_markup=nubess
        )
    elif msg.data == "home":
        await msg.message.edit(
            text="Hola 👋🏻 a Stvz20_Upload, Bienvenido a este sistema de Descargas, estamos simpre para tí, y ayudarte a descagar cualquier archivo multimedia que desees☺️",
            reply_markup=hom
        )
    elif msg.data == "infouser":
        usuario = Config[username]["username"]
        passw = Config[username]["password"]
        host_moodle = Config[username]["host"]
        rid = Config[username]["repoid"]
        rar = Configs[username]["z"]
        mens = f"**Configuración ⚙️ @{username}**\n"
        mens += f"**User: {usuario}\nPasword: {passw}\nhost: {host_moodle}\nRepoID: {rid}\nZips: {rar}\n\n**"
        if Configs[username]["a"] == 'upgtm':
            subida = 'GTM ☁️'
        elif Configs[username]["a"] == 'upltu':
            subida = 'uvs.ltu ☁️'
        elif Configs[username]["a"] == 'upcmw':  
            subida = 'CMW ☁️' 
        elif Configs[username]["a"] == 'eduvirtual':
            subida = 'Eduvirtual ☁️'
        elif Configs[username]["a"] == 'vcl':
            subida = 'Nube Extra ☁️'
        else:   
            subida = 'Nube Personal ☁️'
        mens += f"**Nube En Uso: {subida}**"
        if Configs[username]["a"] == 'edup':
            await msg.message.edit(
                text='Estas usando una nube ☁️ a la que no puedes ver sus credenciales',
                reply_markup=atras
            )
        else:
            await msg.message.edit(
                text=mens,
                reply_markup=atras
            )
    elif msg.data == "delet":
        shutil.rmtree("downloads/"+username+"/")
        root[username]["actual_root"] = "downloads/"+username
        await msg.message.edit(
            text="⚠️🗑️ Archivos Borrados 🗑️⚠️",
        )

def get_readable_time(seconds: int) -> str:
    count = 0
    readable_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", " days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        readable_time += time_list.pop() + ", "
    time_list.reverse()
    readable_time += ": ".join(time_list)
    return readable_time

#Funcion
seg = 0
def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
           return "%3.2f%s%s" % (num, unit, suffix)
        num /= 1024.0 
    return "%.2f%s%s" % (num, 'Yi', suffix)

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
            msg+=f"**╭➣❮ /seven_{i} ❯─❮ /rmdir_{i} ❯─❮ /cd_{i} ❯\n╰➣**📂Carpeta:** `{n}`\n\n" 
            i += 1
        else:
        #    i += 1
            msg+=f"**╭➣❮ /up_{i} ❯─❮ /rm_{i} ❯─❮ /dl_{i} ❯\n╰➣ {sizeof_fmt(size)} - ** `📃 {n}`\n"
            i += 1
    #msg+= f"\n**Eliminar Todo**\n    **/deleteall**"
    return msg , final

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
            await bot.send_message(username,msg, reply_markup=delete)	
            msg = ''
        if msg == '':	
            msg+= l
        else:		
            msg+= "\n" +l	
        c += 1
        if len(text) == c and msg_ult != msg:
            await bot.send_message(username,msg, reply_markup=delete)

def update_progress_bar(inte,max):
    percentage = inte / max
    percentage *= 100
    percentage = round(percentage)
    hashes = int(percentage / 5)
    spaces = 20 - hashes
    progress_bar = "[ " + "•" * hashes + "•" * spaces + " ]"
    percentage_pos = int(hashes / 1)
    percentage_string = str(percentage) + "%"
    progress_bar = progress_bar[:percentage_pos] + percentage_string + progress_bar[percentage_pos + len(percentage_string):]
    return(progress_bar)

def iprox(proxy):
    tr = str.maketrans(
        "@./=#$%&:,;_-|0123456789abcd3fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "ZYXWVUTSRQPONMLKJIHGFEDCBAzyIwvutsrqponmlkjihgf3dcba9876543210|-_;,:&%$#=/.@",
    )
    return str.translate(proxy[::2], tr)

#Acceso de Uso al BoT
def acceso(username):
    if username in Configs or username in boss:
        if exists('downloads/'+str(username)+'/'):pass
        else:os.makedirs('downloads/'+str(username)+'/')
       # else:os.makedirs(str(username)+'/')	
        try:Urls[username]
        except:Urls[username] = []
        try:Config[username]
        except:Config[username] = {"username":"","password":"","repoid":"","host":""}
        try:id_de_ms[username]
        except:id_de_ms[username] = {"JAGB2021":"","JAGB2021":""}
        try:root[username]
        except:root[username] = {"actual_root":f"downloads/{str(username)}"}
        try:downlist[username]
        except:downlist[username] = []
    else:return False
     
#Conf User
async def send_config():
    try:await bot.edit_message_text(Channel_Id,message_id=msg_id,text=dumps(Configs,indent=4))
    except:pass

#Comprobacion de Procesos
def comprobar_solo_un_proceso(username):
    if id_de_ms[username]["proc"] == "Up" :
        rup = "`Por Favor Espere, Ya posee una Tarea Activa\nUse: ` **/cancel** ` para Cancelar ❌ la Actual`"
        return rup
    else:
        return False

#Maximos Procesos
def total_de_procesos():
    global procesos
    hgy = "`⚠️BoT Ocupado, Prueba más Tarde ⚠️`"
    if procesos >= 100:
        return hgy
    else:
        return False


####### Inicio Todos los Comandos ########
@bot.on_message(filters.text & filters.private)
async def text_filter(client, message):
    global procesos
    user_id = message.from_user.id
    username = message.from_user.username
    send = message.reply
    mss = message.text
    try:await get_messages()
    except:await send_config()
    if acceso(username) == False:
        await send("**⚠️🔺No Tienes Contrato Activo en Este BoT🔺⚠️\nContacta al Administrador: @Stvz20**")
        return
    else:pass
    if "youtu.be/" in message.text or "twitch.tv/" in message.text or "youtube.com/" in message.text or "xvideos.com" in message.text or "xnxx.com" in message.text:
        list = message.text.split(" ")
        url = list[0]
        try:format = str(list[1])
        except:format = "720"
        msg = await send("**Por Favor Espere 🔍**")
        await client.send_message(Channel_Id,f'**@{username} Envio un link de #youtube:**\n**Url:** {url}\n**Formato:** {str(format)}p')
        procesos += 1
        download = await ytdlp_downloader(url,user_id,msg,username,lambda data: download_progres(data,msg,format),format)
        if procesos != 0:
            procesos -= 1
        await msg.edit("**Enlace De Youtube Descargado**")
        msg = files_formatter(str(root[username]["actual_root"]),username)
        await limite_msg(msg[0],username)
        return

    elif "mediafire.com/" in message.text:
        url = message.text
        if "?dkey=" in str(url):
            url = str(url).split("?dkey=")[0]
        msg = await send("**Por Favor Espere 🔍**")
        await client.send_message(Channel_Id,f'**@{username} Envio un link de #mediafire:**\n**Url:** {url}\n')
        procesos += 1
        download = await download_mediafire(url, str(root[username]["actual_root"])+"/", msg, callback=mediafiredownload)
        if procesos != 0:
            procesos -= 1
        await msg.edit("**Enlace De MediaFire Descargado**")
        msg = files_formatter(str(root[username]["actual_root"]),username)
        await limite_msg(msg[0],username)
        return

    elif "https://mega.nz/file/" in message.text:
        url = message.text
        mega = pymegatools.Megatools()
        try:
            filename = mega.filename(url)
            g = await send(f"Descargando {filename} ...")
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
            if "[400 MESSAGE_ID_INVALID]" in str(ex): pass
            else:
                await send(ex)	
                return
    elif "https://mega" in message.text:
        url = message.text
        mega = pymegatools.Megatools()
        try:
            filename = mega.filename(url)
            g = await send(f"Descargando {filename} ...")
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
            if "[400 MESSAGE_ID_INVALID]" in str(ex): pass
            else:
                await send(ex)	
                return
    elif '/wget' in mss:
        j = str(root[username]["actual_root"])+"/"
        url = message.text.split(" ")[1]
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                try:
                    filename = unquote_plus(url.split("/")[-1])
                except:
                    filename = r.content_disposition.filename	
                fsize = int(r.headers.get("Content-Length"))
                msg = await send("7**Por Favor Espere 🔍**")
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
                await msg.edit("**Enlace Descargado**")
                if procesos != 0:
                    procesos -= 1
                else:pass
                msg = files_formatter(str(root[username]["actual_root"]),username)
                await limite_msg(msg[0],username)
                return

    elif "/up_" in mss:
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
          list = int(message.text.split("_")[1])		
          msgh = files_formatter(str(root[username]["actual_root"]),username)
          try:
              path = str(root[username]["actual_root"]+"/")+msgh[1][list]
              msg = await send(f"Archivo 📂: {path}**")
              if Configs[username]["m"] == "u": 
                  fd = await uploadfile(path,user_id,msg,username)
              elif Configs[username]["m"] == "e":
                  if len(Urls[username]) >= 10  and username not in boss:
                      msg.edit('⛔️ 𝑬𝒍 𝒍𝒊𝒎𝒊𝒕𝒆 𝒅𝒆 𝒍𝒊𝒏𝒌𝒔 𝒇𝒖𝒆 𝒑𝒂𝒔𝒂𝒅𝒐 , 𝒖𝒕𝒊𝒍𝒊𝒛𝒆 **/deletelinks**')
                      return
                  else:
                      await uploadfileapi(path,user_id,msg,username)
              elif Configs[username]["m"] == "nexcloud":
                  await proccess(path,msg,username)
              elif Configs[username]["m"] == "revista":
                  await upload_revista(path,user_id,msg,username)
              elif Configs[username]["m"] == "eco":
                  await upload_eco(path,user_id,msg,username)
              else:
                  await uploaddraft(path,user_id,msg,username)
          except Exception as ex:
              await send(ex)

    elif '/start' in mss:
        await bot.send_photo(username,"logo.jpg",caption="`Hola 👋🏻 a Stvz20_Upload, Bienvenido a este sistema de Descargas, estamos simpre para tí, y ayudarte a descagar cualquier archivo multimedia que desees☺️`",
            reply_markup=hom)

###Root Manejos de Archivos 
    elif '/ls' in mss:
        msg = files_formatter(str(root[username]["actual_root"]),username)
        await limite_msg(msg[0],username)
        return  
   
    elif '/mkdir' in mss:
        name = message.text.split("_")[1]
        if "." in name or "/" in name or "*" in name:
            await send("**El nombre no puede contener Caracteres Especiales**")
            return
        rut = root[username]["actual_root"]
        os.mkdir(f"{rut}/{name}")
        await send(f"**Carpeta Creada**\n\n`/{name}`")
        msg = files_formatter(str(root[username]["actual_root"]),username)
        await limite_msg(msg[0],username)

    elif '/rmdir' in mss:
        list = message.text.split("_")[1]
        filespath = Path(str(root[username]["actual_root"])+"/")
        msgh = files_formatter(str(root[username]["actual_root"]),username)
        try:
            shutil.rmtree(str(root[username]["actual_root"])+"/"+msgh[1][int(list)])
            msg = files_formatter(str(root[username]["actual_root"])+"/",username)
            await limite_msg(msg[0],username)
        except Exception as ex:
            await bot.send_message(username,ex)

    elif 'rm' in mss:
        list = message.text.split("_")[1]	
        msgh = files_formatter(str(root[username]["actual_root"]),username)
        try:
            unlink(str(root[username]["actual_root"])+"/"+msgh[1][int(list)])
            msg = files_formatter(str(root[username]["actual_root"])+"/",username)
            await limite_msg(msg[0],username)
        except Exception as ex:
            await bot.send_message(username,ex)

    elif '/info' in mss:
        usuario = Config[username]["username"]
        passw = Config[username]["password"]
        host_moodle = Config[username]["host"]
        rid = Config[username]["repoid"]
        rar = Configs[username]["z"]
        mens = f"**Configuración ⚙️ @{username}**\n"
        mens += f"**User: {usuario}\nPasword: {passw}\nhost: {host_moodle}\nRepoID: {rid}\nZips: {rar}\n\n**"
        if Configs[username]["a"] == 'upgtm':
            subida = 'GTM ☁️'
        elif Configs[username]["a"] == 'upltu':
              subida = 'uvs.ltu ☁️'
        elif Configs[username]["a"] == 'upcmw':  
              subida = 'CMW ☁️' 
        elif Configs[username]["a"] == 'eduvirtual':
              subida = 'Eduvirtual ☁️'
        else:   
            subida = 'Nube Personal ☁️'
        mens += f"**Nube En Uso: {subida}**"
        if Configs[username]["a"] == 'edup':
            await send('Estas usando una nube ☁️ a la que no puedes ver sus credenciales')
        else:
            await send(mens)

    elif '/zips' in mss:
        sip = int(message.text.split(" ")[1])
        Configs[username]["z"] = sip
        await send_config()
        await send(f"**Tamaño de Zips Configurados a: {sip} Mb**")    

    elif '/del_all'in mss:
        shutil.rmtree("downloads/"+username+"/")
        root[username]["actual_root"] = "downloads/"+username
        msg = files_formatter(str(root[username]["actual_root"])+"/",username)
        await limite_msg(msg[0],username)

    elif '/add' in mss:
        usr = message.text.split(" ")[1]
        if username in boss:
            Configs[usr] = {'z': 99,"m":"u","a":"upltu","t":"y"}
            await send_config()
            await send(f"@{usr} **Tiene Acceso**", quote=True)
            await bot.send_message(usr, "**Tienes Acceso Mamawebo!!**")
        else: 
            await send("⚠️Comando Para Administrador ⚠️", quote=True)
    elif '/users' in mss:
        if username in boss:
            username = message.from_user.username	
            total = len(Configs) - 10
            message = "**Usuarios: **"+ str(total)+'\n\n'
            i = 0
            for user in Configs:
                if user == "uclv":continue
                if user == "gtm":continue
                if user == "uvs":continue
                if user == "ltu":continue
                if user == "ucuser":continue
                if user == "ucpass":continue
                if user == "gp":continue
                if user == "s":continue
                if user == "UHTRED_OF_BEBBANBURG":continue
                if user == "JAGB2021":continue
                if user == "uclv_p":continue
                if user == "vcl":continue
                message+=f"@{user}\n"
                i += 1
            msg = f"@{message}\n"
            await client.send_message(username,msg)   
        else: 
            await send("⚠️Comando Para Administrador ⚠️", quote=True)
    elif '/get_db' in mss:
     #   db = Configs
        if username in boss:
            username = message.from_user.username
            await bot.send_message(username, "DB🔻")
            await bot.send_message(username, Configs)
        else: 
            await send("⚠️Comando Para Administrador ⚠️", quote=True)
    elif '/ban' in mss:
        usr = message.text.split(" ")[1]
        if username in boss:
            del Configs[usr]
            await send_config()
         #   await bot.edit_message_text(Channel_Id,message_id=msg_id,text=dumps(Configs,indent=4))
            await send(f"@{usr} **Ya no tiene acceso**", quote=True)
            await bot.send_message(usr, "**Ya no tienes Acceso**")
        else: 
            await send("⚠️Comando Para Administrador ⚠️", quote=True)
    elif '/proxy' in mss:
        if username in boss:
            Configs["gp"] = str(message.text.split(" ")[1])
            await send_config()
        #    await bot.edit_message_text(Channel_Id,message_id=msg_id,text=dumps(Configs,indent=4))
            await send(f"**Proxy Establecido**", quote=True)
        else: 
            await send("⚠️Comando Para Administrador ⚠️", quote=True)
    elif '/cancel' in mss:
        if id_de_ms[username]["proc"] == "Up":
            p = await bot.send_message(username, "`Por Favor Espere...`")
            try:
                await id_de_ms[username]["msg"].delete()
                id_de_ms[username] = {"msg":"", "proc":""}
                await p.edit("`Tarea Cancelada...`")
                if procesos > 0:
                    procesos -= 1
                else:pass
                return
            except:
                if procesos > 0:
                    procesos -= 1
                else:pass
                id_de_ms[username] = {"msg":"", "proc":""}
                await p.edit("`Tarea Cancelada...`")
                return
        else:
            await bot.send_message(username,"`No hay Tareas para Cancelar...`")
            return

#Descarga de Archivos y Enlaces
@bot.on_message(filters.media & filters.private)
async def delete_draft_y_down_media(client: Client, message: Message):
    global procesos
    username = message.from_user.username
    send = message.reply
    try:await get_messages()
    except:await send_config()
    if acceso(username) == False:
        await send("**⛔ No Tienes Acceso**")
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
    count = 0
    if str(message).split('"file_name": ')[1].split(",")[0].replace('"',"").endswith(".txt") and Configs[username]["m"] == "d" :
        if message.from_user.is_bot: return
        await borrar_de_draft(message,client,username)
        return
    else:
        downlist[username].append(message)
        msg = await send("**Verificando Archivo **", quote=True)
        for i in downlist[username]:
            filesize = int(str(i).split('"file_size":')[1].split(",")[0])
            try:filename = str(i).split('"file_name": ')[1].split(",")[0].replace('"',"")	
            except:filename = str(randint(11111,999999))+".mp4"
            await bot.send_message(Channel_Id,f'**@{username} Envio un #archivo:**\n**Filename:** {filename}\n**Size:** {sizeof_fmt(filesize)}')	
            start = time()		
            await msg.edit(f"**Iniciando Descarga...**\n\n`{filename}`")
            try:
                a = await i.download(file_name=str(root[username]["actual_root"])+"/"+filename,progress=downloadmessage_progres,progress_args=(filename,start,msg))
                if Path(str(root[username]["actual_root"])+"/"+ filename).stat().st_size == filesize:
                    await msg.edit("**Descarga Finalizada**")
                count +=1
            except Exception as ex:
                    if procesos > 0:
                        procesos -= 1
                    else:pass
                    if "[400 MESSAGE_ID_INVALID]" in str(ex): pass		
                    else:
                        await bot.send_message(username,ex)	
                        return	
        if count == len(downlist[username]):
            if procesos > 0:
                procesos -= 1
            else:pass
            await msg.edit("**Descaga Finalizada**")
            downlist[username] = []
            count = 0
            msg = files_formatter(str(root[username]["actual_root"]),username)
            await limite_msg(msg[0],username)
            return
        else:
            await msg.edit("**Error**")
            msg = files_formatter(str(root[username]["actual_root"]),username)
            await limite_msg(msg[0],username)
            downlist[username] = []
            return      

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

def update(username):
    Configs[username] = {"z": 900,"m":"e","a":"a"}

async def get_messages():
    msg = await bot.get_messages(Channel_Id,message_ids=msg_id)
    Configs.update(loads(msg.text))

async def send_config():
    try:
        await bot.edit_message_text(Channel_Id,message_id=3,text=dumps(Configs,indent=4))
    except:
        pass

async def extractDownloadLink(contents):
    for line in contents.splitlines():
        m = re.search(r'href="((http|https)://download[^"]+)', line)
        if m:
            return m.groups()[0]

async def mediafiredownload(chunk,total,filename,start,message):
    now = time()
    diff = now - start
    mbs = chunk / diff
    msg = f"`Nombre: {filename}`\n\n"
    try:
        msg+= update_progress_bar(chunk,total)+ "  " + sizeof_fmt(mbs)+"/s\n\n"
    except: pass
    msg+= f"`Progreso: {sizeof_fmt(chunk)} - {sizeof_fmt(total)}`\n\n"
    global seg
    if seg != localtime().tm_sec:
        try: await message.edit(msg)
        except:pass
    seg = localtime().tm_sec

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

@bot.on_message(filters.media & filters.private)
async def delete_draft_y_down_media(client: Client, message: Message):
    global procesos
    username = message.from_user.username
    send = message.reply
    try:await get_messages()
    except:await send_config()
    if acceso(username) == False:
        await send("⚠️Sin Acceso ⚠️")
        return
    else:pass
    if str(message).split('"file_name": ')[1].split(",")[0].replace('"',"").endswith(".txt") and Configs[username]["m"] == "d":
        if message.from_user.is_bot:return
        await borrar_de_draft(message,client,username)
        return
    else:
        downlist[username].append(message)
        await send("**/down Para Comenzar Descaga**", quote=True)
        return


#Mensajes De Progreso de Subida y Descaga
def download_progres(data,message,format):
    if data["status"] == "downloading":
        filename = data["filename"].split("/")[-1]
        _downloaded_bytes_str = data["_downloaded_bytes_str"]
        _total_bytes_str = data["_total_bytes_str"]
        if _total_bytes_str == "N/A":
            _total_bytes_str = data["_total_bytes_estimate_str"]
        _speed_str = data["_speed_str"].replace(" ","")
        _format_str = format
        msg = f"**Nombre: {filename}**\n\n"
        msg+= f"**Progreso: {_downloaded_bytes_str} | {_total_bytes_str}**\n\n"
        msg+= f"**Calidad: {_format_str}p**\n\n"
        global seg
        if seg != localtime().tm_sec:
            try:message.edit(msg,reply_markup=message.reply_markup)
            except:pass
        seg = localtime().tm_sec

async def downloadmessage_progres(chunk,filesize,filename,start,message):
    now = time()
    diff = now - start
    mbs = chunk / diff
    msg = f"`**Nombre: **{filename}`\n\n"
    try:
       msg+= update_progress_bar(chunk,filesize)+ "  " + sizeof_fmt(mbs)+"/s\n\n"
    except:pass
    msg+= f"**Progreso: {sizeof_fmt(chunk)} | {sizeof_fmt(filesize)}**\n\n"	
    global seg
    if seg != localtime().tm_sec:
        try: await message.edit(msg)
        except:pass
    seg = localtime().tm_sec

def uploadfile_progres(chunk,filesize,start,filename,message):
    now = time()
    diff = now - start
    mbs = chunk / diff
    msg = f"**Name: **{filename}\n\n"
    try:
       msg+=update_progress_bar(chunk,filesize)+ "  " + sizeof_fmt(mbs)+"/s\n\n"
    except:pass
    msg+= f"**Progreso: {sizeof_fmt(chunk)} | {sizeof_fmt(filesize)}**\n\n"
    global seg
    if seg != localtime().tm_sec: 
        message.edit(msg)
    seg = localtime().tm_sec

async def downloadmessage_tg(chunk,filesize,filename,start,message):
    now = time()
    diff = now - start
    mbs = chunk / diff
    msg = f"**Nombre: {filename}**\n\n"
    try:
       msg+=update_progress_bar(chunk,filesize)+ "  " + sizeof_fmt(mbs)+"/s\n\n"
    except:pass
    msg+= f"**Nombre: {sizeof_fmt(chunk)} | {sizeof_fmt(filesize)}**\n\n"	
    global seg
    if seg != localtime().tm_sec:
        try: await message.edit(msg)
        except:pass
    seg = localtime().tm_sec                   

async def upload_revista(path,usid,msg,username):
    #send = message.reply
    namefile = os.path.basename(path)
    zips = Configs[username]["z"]
    filesize = Path(path).stat().st_size
    zipssize = 1024*1024*int(zips)
    #msg = await send(f"Archivo 📂: {namefile}**")
    links = []
    filename = Path(path).name
   # id_de_ms[username] = {"msg":msg, "pat":filename, "proc":"Up"}
   
 #Login
 '/rv' in mss:
     await msg.edit("Iniciando Sesión...❗")
    log = "https://revistas.udg.co.cu/index.php/olimpia/login/signIn"
    session = requests.Session()
    user = "luisernestorb95"
    passw = "Luisito1995*"
    resp = session.get(log)
    soup = BeautifulSoup(resp.text, 'html.parser') 
    csrfToken = soup.find("input", attrs={"name": "csrfToken"})["value"]
    print(csrfToken)
    data = {
        "username": user,
        "password": passw
    }
    a = session.post(log, data=data)
    if "El nombre" in a.text:
        await msg.edit("error de login")
    else:
        if filesize-1048>zipssize:
            parts = round(filesize / zipssize)
            await msg.edit("Comprimiendo ❗")
            files = sevenzip(path,volume=zipssize)
            thread = threading.Thread(target=upresv, args=(session,csrfToken,files,msg,username))
            thread.start() 
        else: 
            thread = threading.Thread(target=upresvs, args=(session,csrfToken,path,msg,username))
            thread.start()
            

def upresv(session,csrfToken,files,msg,username):
    for filed in files:
        namefiles = os.path.basename(filed)
        upload_url = "https://revistas.udg.co.cu/index.php/olimpia/$$$call$$$/wizard/file-upload/file-upload-wizard/upload-file?submissionId=3880&stageId=1&fileStage=2&reviewRoundId=&assocType=&assocId="
        payload = {"name": namefiles, 'genreId': "1", "filename": "jdjfd"}
        filess = {"uploadedFile": (namefiles, open(filed, 'rb'), 'application/octet-stream')}
        headers = {"X-Csrf-token": csrfToken}
        msg.edit(f"⬆️Subiendo🔽⏬:\n`{namefiles}")
        response = session.post(upload_url, data=payload, files=filess, headers=headers)
        response_json = response.json()
        urls = response_json["uploadedFile"]["fileId"]
        bot.send_message(username, f"{namefiles} Subido🔽\n{urls}")

def upresvs(session,csrfToken,path,msg,username):
    namefile = os.path.basename(path)
    msg.edit(f"**⬆️Subiendo:** `{namefile}`")
    upload_url = "https://santiago.uo.edu.cu/index.php/stgo/api/v1/submissions/16520/files"
    payload = {'fileStage': '2', 'name[es_ES]': namefile}
    files = {'file': (namefile, open(path, 'rb'), 'application/octet-stream')}
    headers = {"X-Csrf-token": csrfToken}
    response = session.post(upload_url, data=payload, files=files, headers=headers)
    response_json = response.json()
    urls = response_json["url"]
    msg.edit(f"**{namefile} Subido🔽\n{urls}**")

#subida a eco
async def upload_eco(path,usid,msg,username):
    proxy = {'https': 'socks5://51.222.13.193:10084'}
    #send = message.reply
    namefile = os.path.basename(path)
    zips = Configs[username]["z"]
    filesize = Path(path).stat().st_size
    zipssize = 1024*1024*int(zips)
    #msg = await send(f"Archivo 📂: {namefile}**")
    links = []
    filename = Path(path).name
   # id_de_ms[username] = {"msg":msg, "pat":filename, "proc":"Up"}
   
 #Login
    
    await msg.edit("Iniciando Sesión...❗")
   # log = "https://anuarioeco.uo.edu.cu/index.php/aeco/login/signIn"
    log = "https://tecedu.uho.edu.cu/index.php/tecedu/login/signIn"
    session = requests.Session()
    user = "luisernesto95"
    passw = "Luisito1995*"
    #header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"}
    resp = session.get(log)
    soup = BeautifulSoup(resp.text, 'html.parser') 
    csrfToken = soup.find("input", attrs={"name": "csrfToken"})["value"]
    print("kd")
    print(csrfToken)
    data = {
        "username": user,
        "password": passw
    }
    a = session.post(log, data=data)
    if "El nombre" in a.text:
        await msg.edit("error de login")
    else:
        if filesize-1048>zipssize:
            parts = round(filesize / zipssize)
            await msg.edit("Comprimiendo ❗")
            files = sevenzip(path,volume=zipssize)
            thread = threading.Thread(target=upeco, args=(session,csrfToken,files,msg,username,proxy, path))
            thread.start() 
        else: 
            thread = threading.Thread(target=upecos, args=(session,csrfToken,path,msg,username,proxy))
            thread.start()
            

def upeco(session,csrfToken,files,msg,username, proxy, path):
    links = []
    msgs = "**Archivos Subidos🔽\n**"
    a = 1
    file_id = []
    for filed in files:
        ff = len(files) - len(links)
        hh = str(ff)
        namefiles = os.path.basename(filed)
        upload_url = "https://tecedu.uho.edu.cu/index.php/tecedu/api/v1/submissions/422/files"
        payload = {'fileStage': '2', 'name[es_ES]': namefiles}
        filess = {'file': (namefiles, open(filed, 'rb'), 'application/octet-stream')} 
        headers = {"X-Csrf-token": csrfToken}
        msg.edit(f"⬆️Subiendo🔽⏬:\n`{namefiles}\n{hh}")
        response = session.post(upload_url, data=payload, files=filess, headers=headers)
        response_json = response.json()
        urls = response_json["url"]
        links.append(urls)
        size = os.path.getsize(filed)/(1024 * 1024)
        id = response_json["id"]
        des = {"id": id, "name":namefiles}
        file_id.append(des)
    if len(links) == len(files):
       # gg = "```\n"+json.dumps(file_id)+"\n```"
     #   bot.send_message(username, gg)
        gg = json.dumps(file_id)
        for i in files:
            size = os.path.getsize(i)/(1024 * 1024)
            namefiles = os.path.basename(i)
            msgs += f"📂{a}🔸{size} Mb🔸{namefiles}\n"
            a += 1
        msg.edit(msgs)
        nombre = path.replace(" ","_")
        with open(nombre+".txt","w") as f:
            f.write(gg)
        bot.send_document(username, nombre+".txt")
        xxx = nombre.replace("downloads/Stvz20/","/")
        bot.send_message(username, f"`/storage/emulated/0/Download{xxx}.txt`")
      #  bot.send_message(username, xxx)
    else:
        msg.edit(f"No sé Pudieron subir todos los Archivos")

def upecos(session,csrfToken,path,msg,username, proxy):
    size = os.path.getsize(path)/(1024 * 1024)
    namefile = os.path.basename(path)
    msg.edit(f"**⬆️Subiendo:** `{namefile}`")
    upload_url = "https://tecedu.uho.edu.cu/index.php/tecedu/api/v1/submissions/422/files"
    payload = {'fileStage': '2', 'name[es_ES]': namefile}
    files = {'file': (namefile, open(path, 'rb'), 'application/octet-stream')}
    headers = {"X-Csrf-token": csrfToken}
    response = session.post(upload_url, data=payload, files=files, headers=headers)
    response_json = response.json()
    print(response_json)
    urls = response_json["url"]
    id = response_json["id"]
    des = [{"id": id, "name":namefile}]
    gg = "```\n"+json.dumps(des)+"\n```"
    bot.send_message(username, gg)
    msg.edit(f"**Subido🔽\nNombre: {namefile}\nTamaño:{size} Mb**")

bot.start()
bot.send_message(5416296262,'**BoT Iniciado**')
print("Iniciado")
bot.loop.run_forever()
