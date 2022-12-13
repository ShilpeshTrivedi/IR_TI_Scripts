#!/usr/bin/Python3
#Author Shilpesh Trivedi

'''
Output of the script 

  +++++++++++++++++++++++++++++++++++++++++++ 
 + ThreatFox IOC Collector                   +
 +                                           +
 +          By: Shilpesh Trivedi             +
 +          URL: https://threatfox.abuse.ch/ +
  +++++++++++++++++++++++++++++++++++++++++++ 

 [*] Malware family statistics for last 1 days :
  |
  |_[+] QakBot = 503
  |_[+] Cobalt Strike = 64
  |_[+] Unknown malware = 7
  |_[+] Vidar = 7
  |_[+] IcedID = 3
  |_[+] Alien = 3
  |_[+] JSSLoader = 3
  |_[+] Loki Password Stealer (PWS) = 2
  |_[+] Anatsa = 2
  |_[+] PhotoLoader = 2
  |_[+] Hydra = 1
  |_[+] FAKEUPDATES = 1
  |_[+] LockBit = 1
  |_[+] Agent Tesla = 1
  |_[+] Nanocore RAT = 1
  |_[+] Mirai = 1

 [+] Indicator has been written in => ThreatFox_IOC.csv <= file

'''

import sys
import json
import requests
from pprint import pprint
from collections import Counter,OrderedDict

def ThreatFox(days):

    malware = []

    headers = {

        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = '{ "query": "get_iocs", "days": '+days+' }'

    response = requests.post('https://threatfox-api.abuse.ch/api/v1/', headers=headers, data=data)

    json_data = response.json()

    json_temp = json_data['data']

    file_csv = open('ThreatFox_IOC.csv','a')

    file_csv.write('Indicator,Malware Family\n')

    for jsn in json_temp:

        malware.append(jsn['malware_printable'])

        file_csv.write(str(jsn['ioc'])+','+str(jsn['malware_printable'])+'\n')

    j_data = json.loads(json.dumps(OrderedDict(Counter(malware).most_common())))

    new_data = dict(sorted(Counter(malware).items(), key=lambda kv:kv[1], reverse=True))

    for key,value in new_data.items():

        print ("  |_[+]",key,'=',value,)

    print ('\n [+] Indicator has been written in => ThreatFox_IOC.csv <= file\n')

    file_csv.close()

if __name__ == '__main__':

    try:

        days = sys.argv[1]

        print ('\n')
        print ("  +++++++++++++++++++++++++++++++++++++++++++ ")
        print (" + ThreatFox IOC Collector                   +")
        print (" +                                           +")
        print (" +          By: Shilpesh Trivedi             +")
        print (" +          URL: https://threatfox.abuse.ch/ +")
        print ("  +++++++++++++++++++++++++++++++++++++++++++",'\n')

        if int(days) <= 7 :

            print (' [*] Malware family statistics for last',days,'days :\n  |')

            ThreatFox(days)

        else:

            print (" [-] ThreatFox says 'day's should be less then or equal to 7 days'\n")

    except:

        print (" [-] please add day's which should be in number or integer\n")
