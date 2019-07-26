import subprocess
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import time

ipaddress_test_list = ['10.0.1.68', '10.0.2.2', '192.168.2.14', '10.0.1.40','10.0.1.30','10.0.1.63','10.0.1.69']


def ping_ip(ipaddress):
	reply = subprocess.run(['ping','-c','3','-n',ipaddress], stdout=subprocess.DEVNULL)
	if reply.returncode == 0:
		return {ipaddress: True}
	else:
		return {ipaddress: False}


def ping_ip_address(ipaddress_list, limit=2):
	alive_list = []
	unreachable_list = []
	with ThreadPoolExecutor(max_workers=limit) as executor:
		f_result = executor.map(ping_ip, ipaddress_list)
		
	return f_result

if __name__ == '__main__':
	start_time = datetime.now()
	for status in ping_ip_address(ipaddress_test_list,3):
		print(status)
	print(datetime.now()-start_time)
