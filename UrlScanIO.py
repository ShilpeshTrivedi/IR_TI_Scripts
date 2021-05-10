#!/usr/bin/Python2
#Author Shilpesh Trivedi

import sys
import time
import json
import urllib
import requests

class UrlScanIO(object):

	def __init__(self):

		self.key = "" #Enter Yor API Key Here
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

			
			time.sleep(30)
			
			urllib.urlretrieve(self.urlss+uuid+'.png',uuid+'.png')

			print '\n\t [*] GUI Websit Snaphost sava as ',uuid+'.png'
			
			print '\n\t [*] For More Click ','https://urlscan.io/result/'+uuid,'\n'

			dom = requests.get("https://urlscan.io/api/v1/result/%s/" % uuid,headers=header)

			ou = dom.content.decode("utf-8")

			J_Data = json.loads(ou)

			Malicious = J_Data['verdicts']['urlscan']['malicious']

			Score = J_Data['verdicts']['urlscan']['score']

			Categories_temp = str(J_Data['verdicts']['urlscan']['categories'])

			Categories = Categories_temp.replace("u'",'').replace('[','').replace(']','').replace("'",'')

			print '\t [*] Url Scan Result -> Malicious = ',Malicious, ', Score = ',Score, ', Categories = ',Categories,'\n'

		except:

			print '\t[*] ',Json_Data['description'],'\n'


if __name__ == '__main__':

        print ' +++++++++++++++++++++++++++++++++'
        print ' + Url Scan on UrlScanIO         +'
        print ' +          By: Shilpesh Trivedi +'
        print ' +++++++++++++++++++++++++++++++++\n'

        try:
	        Url = sys.argv[1]
	        print '\t [*] This Sript Will takes only 30 Second to run'
	        print '\n\t [*] Subited Url:',Url
	        UrlScanIO().SubmitURL(Url)

        except:
                print '\t [*] Url/Domain Must Required as a Argument\n'
