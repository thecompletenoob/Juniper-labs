#!/usr/bin/python3

from jnpr.junos import Device
from jnpr.junos.utils.config import Config

switch = {'host': '', 'user': '', 'password': ''}

# We use \\ because we need the \ on the node. Without it python
# will interpret it as another line which will mess the code up

loginMessage = '\\n************ WARRNING***WARNING***WARNING***WARNING****************************\\n*  YOU HAVE ACCESSED A RESTRICTED DEVICE.USE OF THIS DEVICE FOR PURPOSES      *\\n*    FOR WHICH AUTHORISATION HAS NOT BEEN GIVEN IS PROHIBITED                 *\\n*                  LOG OFF IMMEDIATELY IF YOU ARE NOT AUTHORIZED!!!           *\\n*                                                                 *\\n*******************************************************************************\\n'

loginMessageCommand = f'set system login message "{loginMessage}"'


with Device(
    host=switch['host'],
    user=switch['user'],
    password=switch['password']
) as node:
    print(f"\nWorking on {node.facts['hostname']}\n")

    with Config(node, mode='exclusive') as nodeConfig:
        nodeConfig.load(loginMessageCommand, format='set')

        # Print the changes about to happen
        print(nodeConfig.diff())
        if nodeConfig.commit_check() is True:
            print('Commit check passed!')
            nodeConfig.commit(timeout=360)
        # Committing keeps longer than the default 30s so we set
        # the timeout for the rpc
        else:
            nodeConfig.rollback()

print("\nSystem Login Message configured.\n")
