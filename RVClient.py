from random import randint
import aiohttp
import urllib.parse
import json
from bs4 import BeautifulSoup
import re


async def Rlogin(host: str, user: str, passw: str) -> list:
    connector = aiohttp.TCPConnector()
    async with aiohttp.ClientSession(connector=connector) as session:
        # login
        try:
            # Login
            async with session.get(host + "login") as response:
                html = await response.text()
            soup = BeautifulSoup(html, "html.parser")
            csrfToken = soup.find("input",attrs={"name":"csrfToken"})['value']
            print(csrfToken)
            url_post = host + 'login/signIn'
            payload = {}
            payload['csrfToken'] = csrfToken
            payload['source'] = ''
            payload['username'] = user
            payload['password'] = passw
            payload['remember'] = '1'
            print(payload)
            async with session.post(url_post, data=payload) as e:
                print(e.url)

            url = host + 'user/profile'
            async with session.get(url) as resp:
                try:
                    u = resp.url
                except:
                    u = resp.url()
                print(u)
                print(url)
                if u==url:
                    return csrfToken,session
        except Exception as ex:
            print(str(ex))
            return None,None
