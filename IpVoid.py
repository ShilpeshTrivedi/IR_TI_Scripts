#Python 3.6

import unicodedata
import requests
import re
import os

print ('\n')
print (' +++++++++++++++++++++++++++++++++')
print (' + Title :- IP Reputation LookUp +')
print (' + Auther: Shilpesh Trivedi      +')
print (' +++++++++++++++++++++++++++++++++')
print ('\n')

class IpVoid(object):
    
    def IpInput(self,IpInput):

        cookies = {
            'cookiebanner-accepted': '1',
            'optinmodal': 'shown',
            '__utmt': '1',
            '__utma': '67803593.580391096.1496747284.1497281718.1497345596.7',
            '__utmb': '67803593.1.10.1497345596',
            '__utmc': '67803593',
            '__utmz': '67803593.1496747284.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        }

        headers = {
            'Origin': 'http://www.ipvoid.com',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Cache-Control': 'max-age=0',
            'Referer': 'http://www.ipvoid.com/',
            'Connection': 'keep-alive',
        }

        url = requests.post('http://www.ipvoid.com/ip-blacklist-check/',headers=headers, cookies=cookies,data={'ip' : IpInput})
        data = unicodedata.normalize('NFKD', url.text).encode('ascii', 'ignore').decode('ascii')
        response = data.translate(str.maketrans("\n\t\r", "   "))
  
        Black_List_Result=IpInput+str(re.findall(r'BLACKLISTED \d+\/\d+',str(response)))

        return Black_List_Result

print (IpVoid().IpInput('185.82.217.102'))
