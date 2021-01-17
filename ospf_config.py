from netmiko import Netmiko
from getpass import getpass

###Device details for SSH connection###
###host value can be hostname of device or IP address###
###device_type is the OS on which you will be sending config###
###if you want to find what OS's are supported leave device_type value empty ###

ospf_device = {'host':'192.168.0.1',
               'username': 'admin',
               'password': getpass(),
               'device_type': 'cisco_ios'
}


###telling python to connect to device using ospf_device dict###
###this is also known as connecthandler###

device_conn = Netmiko(**ospf_device)

###list containing OSPF configuration for backbone area###
ospf_commands = ['router ospf 100',
                 'network 192.168.0.0 0.0.0.255 area 0',
                 'network 192.168.1.0 0.0.0.255 area 0',
                 'network 192.168.100.0 0.0.0.255 area 0',
                 'network 10.100.12.0 255.255.0.0 area 0',
                 'network 12.232.65.0 0.0.0.255 area 0',
]

###list containing OSPF configuration for backbone area###
###send_config_set will automatically even conf t mode###
###if you have an enable secret on the device, add 'secret' key to ospf_device dict ###
send_config = device_conn.send_config_set(ospf_commands)

###show protocols for confirmation and debugging###
show_ip_protocol = device_conn.send_command('show ip protocols')
show_ip_route =  device_conn.send_command('show ip route')
show_ospf_database =  device_conn.send_command('show ip ospf database database-summary')

###printing show commands to term###
print(send_config)

print(show_ip_protocol, show_ip_route, show_ospf_database)
