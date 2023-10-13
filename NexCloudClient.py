import requests
import os
import uuid
import requests_toolbelt as rt
from requests_toolbelt import MultipartEncoderMonitor
from requests_toolbelt import MultipartEncoder
from functools import partial
import time
from bs4 import BeautifulSoup
from ProxyCloud import ProxyCloud
import json
import asyncio
from datetime import datetime
import base64
import socket
import socks

#import S5Crypto
def parse(text):   
        proxy_tokens = text.split('://')
        print(proxy_tokens)
        type = proxy_tokens[0]
        print(type)
        da = proxy_tokens[1]
        de = da.split(':')
        ip = str(de[0])
        print(ip)
        port = de[1]
        print(port)
        return {'http':f'{type}://'+ip+':'+str(port)+'',
                'https':f'{type}://'+ip+':'+str(port)+''}
        
class CloudUpload:
    def __init__(self, func,filename,args):
        self.func = func
        self.args = args
        self.filename = filename
        self.time_start = time.time()
        self.time_total = 0
        self.speed = 0
        self.last_read_byte = 0
    def __call__(self,monitor):
        self.speed += monitor.bytes_read - self.last_read_byte
        self.last_read_byte = monitor.bytes_read
        tcurrent = time.time() - self.time_start
        self.time_total += tcurrent
        self.time_start = time.time()
        if self.time_total>=1:
                if self.func:
                     self.func(self.filename,monitor.bytes_read,monitor.len,self.speed,self.args)
                self.time_total = 0
                self.speed = 0



class NexCloudClient(object):
    def __init__(self, user,password,path='https://nube.uclv.cu/',proxy:ProxyCloud=None):        
        b = base64.b64encode(bytes(user+" y "+password, 'utf-8')) # bytes
        base64_str = b.decode('utf-8') # conver
        print(base64_str)        
        self.user = user
        self.password = password
        self.session = requests.Session()
        self.path = path
        self.log = ''
        self.tokenize_host = 'https://rayserver.url/'
        self.proxy = None
        if proxy:
            print(proxy)
            self.proxy = parse(proxy)
            
    def login(self):
        print(1)
        loginurl = self.path + 'index.php/login'
        resp = self.session.get(loginurl,proxies=self.proxy,verify=False)
        print(2)
        soup = BeautifulSoup(resp.text,'html.parser')
        requesttoken = soup.find('head')['data-requesttoken']
        print('requesttoken: ',requesttoken)
        timezone = 'America/Mexico_City'
        timezone_offset = '-5'
        payload = {'user':self.user,'password':self.password,'timezone':timezone,'timezone_offset':timezone_offset,'requesttoken':requesttoken};
        resp = self.session.post(loginurl, data=payload,proxies=self.proxy)
        print('Login Exito!!')
        soup = BeautifulSoup(resp.text,'html.parser')
        title = soup.find('div',attrs={'id':'settings'})
        if title:
            return True
        return False

    def nameRamdom():
        populaton = 'abcdefgh1jklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        name = "".join(random.sample(populaton,5))
        return name

    def delete(self,urlname):

        try:
            files = self.path + 'index.php/apps/files/'
      #      self.proxy = parse(proxy)
            resp = self.session.get(files)

            soup = BeautifulSoup(resp.text,'html.parser')

            requesttoken = soup.find('head')['data-requesttoken']

            print('Mira el token mmwvo: ',requesttoken)

            geturl = self.path + 'apps/files/'

            resp1 = self.session.get(files)

            soup1 = BeautifulSoup(resp1.text,'html.parser')

            value_access = soup1.find('div',attrs={'id':'avatardiv-menu'})['data-user']

            print('Value_access: ',value_access)

            name = str(urlname).split('/')[-1]

            urldelete = 'https://nube.uo.edu.cu/remote.php/dav/files/' + value_access + '/Raul/' + name

            #urldelete = 'https://nube.uo.edu.cu/remote.php/dav/files/6A8DF518-C7A7-451B-973A-E8C710602E24/Raul/' + name

            resp = self.session.delete(urldelete,headers={'requesttoken':requesttoken},proxies=self.proxy)

            #print(resp)

            if resp.status_code==204:

                return True

            else:

                return False

        except Exception as ex:

            print(str(ex))

            return False

    def clear(self):

        try:
            files = self.path + 'index.php/apps/files/'
     #       self.proxy = parse(proxy)

            resp = self.session.get(files)

            soup = BeautifulSoup(resp.text,'html.parser')

            requesttoken = soup.find('head')['data-requesttoken']

            print('Mira el token mmwvo: ',requesttoken)

            geturl = self.path + 'apps/files/'

            resp1 = self.session.get(files)

            soup1 = BeautifulSoup(resp1.text,'html.parser')

            value_access = soup1.find('div',attrs={'id':'avatardiv-menu'})['data-user']

            print('Value_access: ',value_access)

            urldelete = self.path + 'remote.php/dav/files/' + value_access + '/Raul/'

            resp3 = self.session.delete(urldelete,headers={'requesttoken':requesttoken},proxies=self.proxy)

            print(resp)

            if resp3.status_code==204:

                url = self.path + 'remote.php/dav/files/' + value_access + '/Raul/'

                print('url: ',url)

                resp4 = self.session.request('MKCOL',url,headers={'requesttoken':requesttoken},proxies=self.proxy)

                print('MKCOL: ',resp4)

                if resp4.status_code==201:

                    return True

                else:

                    return False

            else:

                return False

        except Exception as ex:

            print(str(ex))

            return False



    def espace(self):
        try:
  #          self.proxy = parse(proxy)
            files = self.path + 'index.php/apps/files/'
            resp = self.session.get(files)
            soup = BeautifulSoup(resp.text,'html.parser')
            requesttoken = soup.find('head')['data-requesttoken']
            print('Mira el token mmwvo: ',requesttoken)
            url = self.path + 'apps/files/ajax/getstoragestats?dir=/'
            resp1 = self.session.get(url,headers={'requesttoken':requesttoken},proxies=self.proxy)
            print('==========resp1===========: ',resp1)
            resp1 = resp1.json()
            print('resp1json: ',resp1)
            libre = resp1['data']['freeSpace'] / 1073741
            usado = resp1['data']['used'] / 1073741
            total = resp1['data']['total'] / 1073741
            return {'libre':libre,'usado':usado,'total':total}
        except Exception as ex:
            print(str(ex))
            return False
        
    def upload_file(self,file,filename,path='',progressfunc=None,args=(),tokenize=False):
        try:
            files = self.path + 'index.php/apps/files/'
#            self.proxy = parse(proxy)
            filepath = str(file).split('/')[-1]
            uploadUrl = self.path + 'remote.php/webdav/'+ 'Raul/' + filepath
            resp = self.session.get(files)
            soup = BeautifulSoup(resp.text,'html.parser')
            requesttoken = soup.find('head')['data-requesttoken']
            f  = open(file,'rb')
            upload_file = {'file':(file,f,'application/octet-stream')}
            resp = self.session.put(uploadUrl,data=f,headers={'requesttoken':requesttoken},proxies=self.proxy)
            f.close()
            retData = {'upload':False,'name':filepath}
            if resp.status_code == 201:
                linked = resp.url
                print('Linked: ',linked)
                name = str(linked).split('/')[-1]
                print('Pasando a Compartir')
                if self.proxy == None:
                    proxyto = "" 
                else:
                    proxyto = str(self.proxy['http'])
                
                actual = datetime.now()
                year = actual.year
                mes = actual.month
                dia = actual.day + 6
                if dia>30:
                    mes = mes + 1
                    dia = dia - 30
                    if dia<10:
                        dia = '0' + str(dia)
                        print(dia)
                    else:
                        pass
                else:
                    pass
                expire = str(year) + '-' + str(mes) + '-' + str(dia)
                print('expire 201: ',expire)
                #exipire = 2022-12-1
                
                direct_payload = {
                    "attributes": "[]",
                    "expireDate": expire,
                    "path": "/Raul/"+filename,
                    "shareType": 3
                }
                print('Payload: ',direct_payload)
                urlpostq = self.path + "ocs/v2.php/apps/files_sharing/api/v1/shares"
                resp5 = self.session.post(urlpostq, data=direct_payload, headers={'requesttoken':requesttoken},proxies=self.proxy)
                print('Hecho el post en 201')
                soup5 = BeautifulSoup(resp5.text,'html.parser')
                print(soup5)
                f = soup5.find('url').contents[0]
                token = str(f).split('/s/')[1]
                print('token: ',token)
                url = self.path + 's/' + token + '/download/' + name
                print('Mira quien esta aqui en 201: ',url)
                if tokenize:
                    url = self.tokenize_host + S5Crypto.encrypt(url) + '/' + S5Crypto.tokenize([self.user,self.password])
                retData = {'name':filepath,'url':str(url)}
                return retData
            if resp.status_code == 204:
                linked = resp.url
                print('Linked: ',linked)
                name = str(linked).split('/')[-1]
                print('Pasando a Compartir')
                if self.proxy == None:
                    proxyto = "" 
                else:
                    proxyto = str(self.proxy['http'])
                    
                actual = datetime.now()
                year = actual.year
                mes = actual.month
                dia = actual.day + 6
                if dia>30:
                    mes = mes + 1
                    dia = dia - 30
                    if dia<10:
                        dia = '0' + str(dia)
                        print(dia)
                    else:
                        pass
                else:
                    pass
                expire = str(year) + '-' + str(mes) + '-' + str(dia)
                print('Expire 204: ',expire)
                #expire = 2022-12-1
                    
                direct_payload = {
                    "attributes": "[]",
                    "expireDate": expire,
                    "path": "/Raul/" + filename,
                    "shareType": 3
                }
                print('Payload: ',direct_payload)
                urlpostq = self.path + "ocs/v2.php/apps/files_sharing/api/v1/shares"
                resp5 = self.session.post(urlpostq, data=direct_payload, headers={'requesttoken':requesttoken},proxies=self.proxy)
                print('Hecho el post en 204')
                soup5 = BeautifulSoup(resp5.text,'html.parser')
                print('aqaaa:',soup5)
                f = soup5.find('url').contents[0]
                token = str(f).split('/s/')[1]
                print('token: ',token)
                url = self.path + 's/' + token + '/download/' + name
                return str(url)
                print('Mira quien esta aqui en 204: ',url)
                
                retData = {'name':filepath,'url':str(url)}
                return retData
            if resp.status_code == 409:
                retData = {'name':filepath,'url':'https://no.se.subio/correctamente'}
                return retData
        except Exception as ex:
            print(str(ex))
            
#proxy = None
#user = "yonnier.pacheco"
#passw = "yonnier.09"
#_code == 409:

#                retData = {'upload':False,'msg':'Not ' + user + ' Folder Existent!','name':filepath}

#            return retData

#        except Exception as ex:

#           