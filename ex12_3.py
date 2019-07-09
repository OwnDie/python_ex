import ex12_2
from tabulate import tabulate

ipaddress_test_list = ['10.0.4.1','10.0.1.68-10.0.1.72', '10.0.2.2', '192.168.2.14-20']

def ip_table(reachable_list, unreachable_list):
	dict_ipaddress = {'Reachable':[], 'Unreachable':[]}
	for ipaddress in reachable_list:
		dict_ipaddress['Reachable'].append(ipaddress)
	for ipaddress in unreachable_list:
		dict_ipaddress['Unreachable'].append(ipaddress)
	print(tabulate(dict_ipaddress, headers='keys'))

ip_table(*ex12_2.ping_ip_address(ipaddress_test_list))