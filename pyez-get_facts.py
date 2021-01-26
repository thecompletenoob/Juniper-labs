#!/usr/bin/python3

from jnpr.junos import Device
from pprint import pprint

switch = {'host': '10.92.105.228', 'user': 'enoc', 'password': 'New@2019'}

with Device(
    host=switch['host'],
    user=switch['user'],
    password=switch['password']
) as node:

    print(node.facts['hostname'])
    pprint(node.facts)
