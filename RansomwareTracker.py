import requests
from bs4 import BeautifulSoup

class IpInput_Reputation(object):
    
    def Ransomwaretracker_Reputation(self,Input):
            
            url = requests.post('https://ransomwaretracker.abuse.ch/tracker/?search='+Input)
            soup = BeautifulSoup(url.text, 'html.parser')
            
            for table in soup.find_all('table'):
                keys = [th.get_text(strip=True)for th in table.find_all('th')]
                values = [td.get_text(strip=True) for td in table.find_all('td')]
                Ransomwaretracker_OutPut = dict(zip(keys,values))
                
                return Ransomwaretracker_OutPut

        
print (IpInput_Reputation().Ransomwaretracker_Reputation('www.resumebuddy.net'))
