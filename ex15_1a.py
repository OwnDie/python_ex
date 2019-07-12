import re



def get_ip_from_cfg(file_name):
	regex = ' +ip address (?P<ip_address>\S+) (?P<mask>\S+)|^interface (?P<interface>\S+)'
	result = {}
	interface = ''
	with open(file_name, 'r') as f:
		for line in f:
			match = re.search(regex, line)
			if match:
				if not match.group(3):
					print(match)
					result[interface] = match.group(1,2)
					interface = None
					continue
				interface = match.group(3)

	return result

print(get_ip_from_cfg('config_r1.txt'))