#!/usr/bin/python3

from jnpr.junos import Device
from pprint import pprint

switch = {'host': 'hostname', 'user': 'username', 'password': 'password'}

with Device(
    host=switch['host'],
    user=switch['user'],
    password=switch['password']
) as node:

    print(node.facts['hostname'])
    pprint(node.facts)
