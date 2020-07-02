#!/usr/bin/Python2
#Author Shilpesh Trivedi


import sys
import time
import json
import urllib
import requests


class UrlScanIO(object):

	def __init__(self):

		self.key = "" #Enter Your API Key Here
		self.base = "https://urlscan.io/api/v1"
		self.header = {'Content-Type ': 'application/json','API-Key': self.key,}
		self.urlss = 'https://urlscan.io/screenshots/'

	def SubmitURL(self,submiturl):

		url = '/scan/'

		header = {'Content-Type ': 'application/json','API-Key': self.key,}

		data = {'url':submiturl}

		response = requests.post(self.base+url,headers=self.header,data=data)

		OutPut = response.content.decode("utf-8")

		try:
			Json_Data = json.loads(OutPut)

			uuid = Json_Data['uuid']

			print '\n\t [*] This Sript Will takes only 30 Seconds to Execute, OutPut Will Store as Screenshots\n'

			time.sleep(30)
			
			urllib.urlretrieve(self.urlss+uuid+'.png',uuid+'.png')

			print '\t [*] Please see',uuid+'.png\n'
			
			print '\t [*] For More Click ','https://urlscan.io/result/'+uuid,'\n'

		except:
			print '\n\t [*]',Json_Data['description'],'\n'


if __name__ == '__main__':

        print ' +++++++++++++++++++++++++++++++++'
        print ' + Url Scan on UrlScanIO         +'
        print ' +          By: Shilpesh Trivedi +'
        print ' +++++++++++++++++++++++++++++++++\n'

        try:
                Url = sys.argv[1]
                print '\t [*] Subited Url:',Url
                UrlScanIO().SubmitURL(Url)
		
        except:
                print '\tUrl\\Domain Must Required as a Argument\n'

		
