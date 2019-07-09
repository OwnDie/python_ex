

import subprocess
from pprint import pprint

ipaddress_test_list = ['10.0.4.1','10.0.1.68-10.0.1.72', '10.0.2.2-8', '192.168.2.14-20']


def ping_ip_address(ipaddress_list):
	alive_list = []
	unreachable_list = []
	ipaddress_list = convert_ranges_to_ip_list(ipaddress_list)
	for ipaddress in ipaddress_list:
		reply = subprocess.run(['ping','-c','3','-n',ipaddress], stdout=subprocess.DEVNULL)
		if reply.returncode == 0:
			unreachable_list.append(ipaddress)
		else:
			alive_list.append(ipaddress)

	return alive_list, unreachable_list

def convert_ranges_to_ip_list(ipaddress_list):
	converted_list = []
	fist_part_ipaddress = ''
	for ipaddress in ipaddress_list:
		if ipaddress.find('-') != -1:
			if ipaddress.split('-')[-1].isdigit():
				fist_part_ipaddress = ipaddress.split('.')
				fist_part_ipaddress.remove(ipaddress.split('.')[-1])
				fist_part_ipaddress = '.'.join(fist_part_ipaddress)
				for i in range(int(ipaddress.split('.')[-1].split('-')[0]),int(ipaddress.split('.')[-1].split('-')[1])+1):
					converted_list.append(fist_part_ipaddress + '.' + str(i))
			else:
				fist_part_ipaddress = ipaddress.split('.')
				fist_part_ipaddress = fist_part_ipaddress[0] + '.' + fist_part_ipaddress[1] + '.' + fist_part_ipaddress[2]
				for i in range(int(ipaddress.split('-')[0].split('.')[-1]),int(ipaddress.split('-')[-1].split('.')[-1])+1):
					converted_list.append(fist_part_ipaddress + '.' + str(i))
		else:
			converted_list.append(ipaddress)

	return converted_list


if __name__ == '__main__':
	pprint(ping_ip_address(convert_ranges_to_ip_list(ipaddress_test_list)))
