#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 08:13:02 2019

@author: Tyler Steele
"""

# Module used to record how long the program takes to run
import time
# Class for looking up the IP addresses
from ipwhois import IPWhois
# Error that is raised for IP addresses with unrecognized ASNs
from ipwhois import ASNRegistryError

# Capture time at beginning
timer = time.time()

# List of IP addresses
addresses = ['72.72.72.72', '132.14.234.2', '133.15.235.3', '2.18.254.1', '12.18.254.1', '134.28.53.15', '101.98.127.2', '175.45.176.5', '31.193.79.10', '37.190.127.15']

# Iterate over the IP addresses and print their asn_descriptions
for address in addresses:
  try:
    result = IPWhois(address).lookup_whois()
    result2 = IPWhois(address).lookup_rdap()
    print(result['asn_description'], '\n\n')
  except ASNRegistryError:
    print(address, 'ASN UNRECOGINED\n\n')
  
print('This program took ', time.time() - timer, ' seconds.')
