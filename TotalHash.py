import requests
import json
from bs4 import BeautifulSoup

class TotalHash(object):

    def TotalHash_Hash(self,SHA1_Hash):

        url = requests.post("https://totalhash.cymru.com/analysis/?"+SHA1_Hash)
        soup = BeautifulSoup(url.text, 'html.parser')

        TotalHash_OutPut = []


        for table in soup.find_all('tr'):

                        data = table.findAll('td')
                        values = table.findAll('th')

                        VirusName=''
                        

                        datas=str(data[0].string)
                        value=str(values[0].string)

                        #print (value)
                        
                        for entry in table.find_all('td'):
                                            value=entry.findAll('td')
                                            if data[0].string != entry.string:
                                                VirusName=str(' : '+entry.string)
                                            else:
                                                pass
                         
                        TotalHash_OutPut.append(str(values[0].string)+' : '+str(datas)+VirusName)

        return TotalHash_OutPut

print(TotalHash().TotalHash_Hash('1ce201cf28c6dd738fd4e65da55242822111bd9f'))

