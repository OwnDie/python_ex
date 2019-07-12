import re



def get_ip_from_cfg(file_name):
	regex = ' +ip address (?P<ip_address>\S+) (?P<mask>\S+)|^interface (?P<interface>\S+)'
	result = {}
	#nterface = ''
	with open(file_name, 'r') as f:
		for line in f:
			match = re.search(regex, line)
			if match:
				print(match)
				if not match.group(3):
					if result.get(interface):
						result[interface].append(match.group(1,2))
					else:
						result[interface] = [match.group(1,2)]
					continue
				else:
					interface = match.group(3)

	return result

print(get_ip_from_cfg('config_r2.txt'))