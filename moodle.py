from requests import Session
#from requests.packages.urllib3.util import Retry
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup as s
import urllib
import re

session = Session()
#session.mount('https://', HTTPAdapter(max_retries=Retry(total=30,allowed_methods=['GET'])))

usernamemoodleid = []
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'}

#created by anonedev
def delete(user,passw,host,urls,proxy):
	url = f'{host}/login/index.php'
	resp = session.get(url, headers=header, proxies=proxy)
	soup = s(resp.text,'html.parser')
	ltoken = soup.find("input", attrs={"name": "logintoken"})
	
	if ltoken:
		ltoken = ltoken['value']
	else:
		ltoken = ''
	
	payload = {
                "anchor": "",
                "logintoken": ltoken,
                "username": user,
                "password": passw,
                "rememberusername": 1,
            }
		
	resp2 = session.post(url, data=payload, headers=header, proxies=proxy)
	if 'loginerrors' in resp2.text:
		print("loging1")
		return
	else:
		soup2 = s(resp2.text,'html.parser')
		try:
			userid = soup2.find('div',{'id':'nav-notification-popover-container'})['data-userid']
			usernamemoodleid.append(userid)
			print(usernamemoodleid)
		except:
			print(usernamemoodleid)
			userid = usernamemoodleid[-1]
	
	try:
		delurl = f'{host}/user/edit.php?id='+str(userid)+'&returnto=profile'
		resp3 = session.get(delurl, headers=header, proxies=proxy)
		soup3 = s(resp3.text,'html.parser')
		sesskey = soup3.find('input',attrs={'name':'sesskey'})['value']
		client_id = str(soup3.find('div',{'class':'filemanager'})['id']).replace('filemanager-','')
		spliturl = urls.split('/')
		filename = urllib.parse.unquote(spliturl[-1])
		itemid = spliturl[-2]
		
		datadel = {'sesskey':sesskey,
					'client_id':client_id,
					'filepath':'/',
					'itemid':itemid,
					'filename':filename
			}
		dellurl = f'{host}/repository/draftfiles_ajax.php?action=delete'
		response = session.post(dellurl, data=datadel,headers=header, proxies=proxy)
	except:
		return False
