#!/usr/bin/python3

from jnpr.junos import Device
from jnpr.junos.utils.config import Config

switch = {'host': '', 'user': 'root', 'password': ''}
interfaces = {
    'ge-0/0/0': {'description': ''},
}

with Device(
    host=switch['host'],
    user=switch['user'],
    password=switch['password']
) as node:
    print(f"\nWorking on {node.facts['hostname']}")

    with Config(node, mode='exclusive') as nodeConfig:
        for interface in interfaces:
            nodeCommand = f"set interfaces {interface} description \
                {interfaces[interface]['description']}"

            nodeConfig.load(nodeCommand, format='set')

        # Print the difference
        print(nodeConfig.diff())

        # TODO: Add confirmation in future

        if nodeConfig.commit_check() is True:
            print('Commit check passed!')
            nodeConfig.commit(timeout=360)
        # Committing keeps longer than the default 30s so we set
        # the timeout for the rpc
        else:
            nodeConfig.rollback()

print("\nInterfaces have been configured.\n")
