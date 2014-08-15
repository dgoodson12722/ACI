import sys
from cobra.model.bgp import AsP

from utility import *


def reset_autonomous_system_number(modir):

    bgp_asp = modir.lookupByDn('uni/fabric/bgpInstP-default/as')
    # Set Autonomous System Number
    if isinstance(bgp_asp, AsP):
        bgp_asp.delete()
    else:
        print 'Autonomous System Number has not been set.'

    print_query_xml(bgp_asp)
    commit_change(modir, bgp_asp)

if __name__ == '__main__':

    # Obtain the key parameters.
    try:
        host_name, user_name, password = sys.argv[1:5]
    except ValueError:
        host_name, user_name, password = input_login_info()

    # Login to APIC
    modir = apic_login(host_name, user_name, password)

    # Execute the main function
    reset_autonomous_system_number(modir)

    modir.logout()

