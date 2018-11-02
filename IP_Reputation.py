import requests
from ipwhois import IPWhois
import dns.resolver
import dns.reversename

class Ip_Reputation(object):

    def Who_IS(self,IpInput):

        try:

            IpInputWhoIS = IPWhois(IpInput)
            return IpInputWhoIS.lookup_whois()
        
        except:

            message = 'Not Found'
            return message

    def Reverse_DNS(self,IpInput):

        try:
            
            query = dns.reversename.from_address(IpInput)
            DNS_Resonse = dns.resolver.query(query, 'PTR')

            for DNS in DNS_Resonse:
                return DNS
            
        except:
            
            message = 'Not Found'
            return message
            
print (Ip_Reputation().Who_IS('195.157.15.100'))
print (Ip_Reputation().Reverse_DNS('8.8.8.8'))
