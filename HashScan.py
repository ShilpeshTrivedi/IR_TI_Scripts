#Written in Python 2.7

import requests
import time

try :
        fp = open ('input.txt') # Here entered input file
except IOError:
        print (" \n\nOops!!! 'input.txt' IS NOT FOUND IN SAME FOLDER ")
        exit()

key = '6d16c3de361a1c18585463803344bea6f66296e14b02718785ccb659b81eb8cd' # Enter Your Virus Total API key

print ('\n')
print (' +++++++++++++++++++++++++++++++++++')
print (' + Author:- Shilpesh Trivedi       +')
print (' + Title :- Multiple Hash Scanning +')
print (' +++++++++++++++++++++++++++++++++++')
print ('\n')


try:
        file = open('OutPut.csv','a')
        file.write('Hash,Malicious (YES/NO),Hit Ratio,MD5')
        file.close()
        
        for i, fyl in enumerate(fp):
                hashs=str(fyl.strip())
                if i%4==0:
# Virus Total Analysis
                        if len(key) == 64: # Cheking For API Key
                                try:
                                        params = {'apikey': key, 'resource': fyl}
                                        url = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params)
                                        json_response = url.json()
                    
                                        response = int(json_response.get('response_code'))

                                        if response == 0:
                                                print ('\n')
                                                print (' [-] '  + fyl + ' is not in Virus Total')
                                                file = open('OutPut.csv','a')
                                                file.write('\n')
                                                file.write(hashs+',N.A,N.A,Hash is not in Virus Total')
                                                file.close()
                                
                                        elif response == 1:
                                                positives = int(json_response.get('positives'))

                                                if positives == 0:
                                                        print ('\n')
                                                        file = open('OutPut.csv','a')
                                                        file.write('\n')
                                                        file.write(hashs+',NO,N.A,N.A')
                                                        file.close()
                                                        print (' [-] ' + fyl + ' is not malicious')
                                                else:
                                                        md5 = json_response.get('md5')
                                                        positives= int(json_response.get('positives'))
                                                        total= int(json_response.get('total'))
                                                        scans=str(json_response.get('scans'))
                        
                                                        print ('\n [*] Malware Hit Count ' + str(positives) +'/'+str(total))
                                                        print ('\n [*] ' + fyl + ' IS MALICIOUS')
                                                        print ('\n [*] MD5 Value is = ' + md5)
                                                        file = open('OutPut.csv','a')
                                                        file.write('\n')
                                                        file.write(hashs+',YES,'+(str(positives)+' Out Of '+str(total))+','+md5)
                                                        file.close()
                                        else:
                                                print (fyl + ' [-] could not be searched. Please try again later.')
            
                                except:
                                        print ('\n [-] Oops!!, Somthing Wrong Check Your Internet Connection Or Entered Hash')
                        else:
                                print (" [-] There is something Wrong With Your API Key.")
                                exit()
                        time.sleep(60) # Here Used Time Sleep mathod here i used 40 sec mex
            
                else:
# Virus Total Analysis
                        if len(key) == 64: # Cheking For API Key
                                try:
                                        params = {'apikey': key, 'resource': fyl}
                                        url = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params)
                                        json_response = url.json()
                    
                                        response = int(json_response.get('response_code'))

                                        if response == 0:
                                                print ('\n')
                                                print (' [-] '  + fyl + ' is not in Virus Total')
                                                file = open('OutPut.csv','a')
                                                file.write('\n')
                                                file.write(hashs+',N.A,N.A,Hash is not in Virus Total')
                                                file.close()
                                
                                        elif response == 1:
                                                positives = int(json_response.get('positives'))

                                                if positives == 0:
                                                        print ('\n')
                                                        file = open('OutPut.csv','a')
                                                        file.write('\n')
                                                        file.write(hashs+',NO,N.A,N.A')
                                                        file.close()
                                                        print (' [-] ' + fyl + ' is not malicious')
                                                        
                                                else:
                                                        md5 = json_response.get('md5')
                                                        positives= int(json_response.get('positives'))
                                                        total= int(json_response.get('total'))
                                                        scans=str(json_response.get('scans'))
                        
                                                        print ('\n [*] Malware Hit Count ' + str(positives) +'/'+str(total))
                                                        print ('\n [*] ' + fyl + ' IS MALICIOUS')
                                                        print ('\n [*] MD5 Value is = ' + md5)
                                                        file = open('OutPut.csv','a')
                                                        file.write('\n')
                                                        file.write(hashs+',YES,'+str(positives)+' Out Of '+str(total)+','+md5)
                                                        file.close()
                                        else:
                                                print (fyl + ' [-] could not be searched. Please try again later.')
            
                                except:
                                        print ('\n [-] Oops!!, Somthing Wrong Check Your Internet Connection Or Entered Hash')
                        else:
                                print (" [-] There is something Wrong With Your API Key.")
                                exit()
								
except KeyboardInterrupt:
        print ("\n\n Oops!!! PEROGRAM HALTED B'COZ YOU PRESS CTRL+C. ")
