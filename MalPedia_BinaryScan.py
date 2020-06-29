import sys
import json
import pprint
import requests

class MalPedia(object):

        def __init__(self):
                
                self.key = "e3675f6ab71d61793f1c690f709ab883e03eb3d4" 
                self.base = "https://malpedia.caad.fkie.fraunhofer.de/api"


        def ScanBinary(self,FileName):

                url = '/scan/binary'

                file = {'upload_file': open (FileName,'rb')}

                header = {'Authorization' : "apitoken "+self.key,'Accept': 'application/json'}

                data = requests.post(self.base+url,params='',headers=header,timeout=120,files=file)

                Scan_Output = json.loads(data.text)

                Json_OutPut = json.dumps(Scan_Output, indent=4, separators=(',', ': '), sort_keys=True)

                print Json_OutPut



if __name__ == '__main__':

        print '+++++++++++++++++++++++++++++++++'
        print '+ Binary Scan on MalPedia       +'
        print '+          By: Shilpesh Trivedi +'
        print '+++++++++++++++++++++++++++++++++\n'

        try:
                FileName = sys.argv[1]
                MalPedia().ScanBinary(FileName)
        except:
                print ('\tFile Name Must Required as a Argument\n')