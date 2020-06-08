import time
import json 
import urllib
import urllib2
import requests
import base64

class LookUP(object):
        
	def __init__(self):

                self.VT_api = "fa58ffe6784cdde787f739578c83f6a6269f339882095666e7d195125c373f1f" # Enter here your VT API key
                self.VT_base = "https://www.virustotal.com/vtapi/v2/"

                self.IBM_base = "https://api.xforce.ibmcloud.com:443"   # Enter here your IBM Base key
                self.IBM_api = "7ebd8514-af39-4e43-b348-8d8f2bcdc3a1"   # Enter here your IBM API key
                self.IBM_pass = "6bdf0743-8c8d-47ee-9d5b-3fabcd2ea462"  # Enter here your IBM Password

	def VirusTotal (self,data):

                param = {'resource':data,'apikey':self.VT_api,'allinfo': '1'}
                url = requests.get(self.VT_base + "url/report",params=param)
                json_response = url.json()
                response = int(json_response.get('response_code'))

                if response == 0:
                        return 'URL Not Found'
                        
                elif response == 1:
                        positives = int(json_response.get('positives'))
                
                        if positives == 0:
                            print ('URL Is Not Malicious In VirusTotal')
                        else:
                            positives= int(json_response.get('positives'))
                            total= int(json_response.get('total'))
                            scans=str(json_response.get('scans'))

                            return str(positives) +'/'+str(total)

        def IBM (self,data):

                token = base64.b64encode(self.IBM_api + ":" + self.IBM_pass)
                header = {'Authorization' : "Basic " + token, 'Accept': 'application/json'}

                url = requests.get(self.IBM_base+'/url/'+data,params='',headers=header,timeout=20)
                json_response = url.json()

                try:
                        for key in json_response['result']:

                                if 'score' in key:
                                        score = str(json_response['result']['score'])
                                        
                                        return score
                           
                except Exception, er:
                        return 'URL Not Malicious In IBM X-Force'



if __name__ == '__main__':


    VM_Obj = LookUP()

    print '+++++++++++++++++++++++++++++++++++++++++'
    print '+ Multiple IP/Domain Reputation Check   +'
    print '+                  By: Shilpesh Trivedi +'
    print '+++++++++++++++++++++++++++++++++++++++++'

    file_cvs=open('URL_Reputation.csv','a')
    file_cvs.write('IP/Domain,VirusTotal Score,IBM X-Force Score,\n')

    try: 

        fp = open ('input.txt') # Here entered input file

    except IOError:

        print (" \n\nOops!!! 'input.txt' IS NOT FOUND")
        exit()

    for i,data in enumerate(fp):

        VT_OP = VM_Obj.VirusTotal(data)
        IBM_OP = VM_Obj.IBM(data)

        if i%4==0 and i!=0:

            print '\t'+data.rstrip('\n'),'->','VirusTotal Score =',VT_OP,', IBM X-Force Score =',IBM_OP
            file_cvs.write(data.rstrip('\n')+','+str(VT_OP)+','+str(IBM_OP)+'\n')
            time.sleep(10)

        else:
            print '\t'+data.rstrip('\n'),'->','VirusTotal Score =',VT_OP,', IBM X-Force Score =',IBM_OP
            file_cvs.write(data.rstrip('\n')+','+str(VT_OP)+','+str(IBM_OP)+'\n')
        