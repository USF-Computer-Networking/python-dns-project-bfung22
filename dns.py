'''
Program that takes in user input of a domain name and utilizes 'dig' similar to terminal command

source: http://www.dnspython.org/examples.html
https://stackoverflow.com/questions/5235569/using-the-dig-command-in-python
Author: Benny Fung
'''
import socket
import argparse
import dns.resolver, sys

def parse_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', help = "Enter domain name [ex: www.yahoo.com]")
    return parser.parse_args()

def dig(arg): #recursively prints out data from CNAME to A
	host = arg
	try:
		while True:
			for rdata in dns.resolver.query(arg, 'CNAME'):
				print(rdata.target)
				host = rdata.target
	except:#recursively prints out data from CNAME to A
		for rdata in dns.resolver.query(host):
			print(rdata)

if __name__ == '__main__':
    arg = parse_args()
    dig(arg)

