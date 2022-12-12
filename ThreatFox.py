#!/usr/bin/Python3
#Author Shilpesh Trivedi

'''
Output of the script 

Python3 ThreatFox.py 1

  +++++++++++++++++++++++++++++++++++++++++++ 
 + ThreatFox IOC Collector                   +
 +                                           +
 +          By: Shilpesh Trivedi             +
 +          URL: https://threatfox.abuse.ch/ +
  +++++++++++++++++++++++++++++++++++++++++++

 [*] Malware family statistics for last 1 days :

{   'Agent Tesla': 1,
    'Alien': 3,
    'Anatsa': 2,
    'Aurora Stealer': 1,
    'Bashlite': 1,
    'Cobalt Strike': 61,
    'FAKEUPDATES': 1,
    'Hydra': 1,
    'IcedID': 2,
    'JSSLoader': 3,
    'LockBit': 1,
    'Loki Password Stealer (PWS)': 1,
    'Mirai': 2,
    'Nanocore RAT': 1,
    'PhotoLoader': 2,
    'QakBot': 4,
    'Raccoon': 14,
    'RedLine Stealer': 14,
    'Unknown malware': 7,
    'Vidar': 9}

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

    pprint (j_data,depth=1, indent=4)

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

            print (' [*] Malware family statistics for last',days,'days :\n')

            ThreatFox(days)

        else:

            print (" [-] ThreatFox says 'day's should be less then or equal to 7 days'\n")

    except:

        print (" [-] please add day's which should be in number or integer\n")

