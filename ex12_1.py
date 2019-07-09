
import subprocess


ipaddress_test_list = ['10.0.1.68', '10.0.2.2', '192.168.2.14']

def ping_ip_address(ipaddress_list):
	alive_list = []
	unreachable_list = []
	for ipaddress in ipaddress_list:
		reply = subprocess.run(['ping','-c','3','-n',ipaddress], stdout=subprocess.DEVNULL)
		if reply.returncode == 0:
			unreachable_list.append(ipaddress)
		else:
			alive_list.append(ipaddress)

	return alive_list, unreachable_list


print(ping_ip_address(ipaddress_test_list))
