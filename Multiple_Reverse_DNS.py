#Python 2.7

import dns.resolver
import dns.reversename


print ('\n')
print (' ++++++++++++++++++++++++++++++++++++++++')
print (' + Title :- Multiple Reverse DNS Lookup +')
print (' + Auther: Shilpesh Trivedi             +')
print (' ++++++++++++++++++++++++++++++++++++++++')
print ('\n')

g = open('ips.txt','r')

filename = 'DNSLookUp.csv'
f = open(filename, 'a')
f.write('IP,Domain Name')

#read lines into array
a = g.readlines()
a = [x.strip('\n') for x in a]

for x in a:
	print(x)

	try:
		query = dns.reversename.from_address(x)
		DNS_Resonse = dns.resolver.query(query, 'PTR')

		for DNS in DNS_Resonse:

			f.write('\n')
			f.write(str(x)+','+str(DNS))

			print '\t Suceefully Found..'

	except dns.resolver.NXDOMAIN:
		f.write('\n')
		f.write(str(x)+',Domain Name Not Found')
		print '\t Domain Name Not Found...'
		
	except dns.resolver.NoNameservers:
		f.write('\n')
		f.write(str(x)+',No Name Servers')
		print '\t No Name Servers...'
	
	except dns.resolver.Timeout:
		f.write('\n')
		f.write(str(x)+',Timeout')

		print '\t Timeout...'

	except KeyboardInterrupt:
		print 'Script hasbeen halt... [Ctrl+c]'

		
		
