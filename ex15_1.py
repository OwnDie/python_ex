import re



def get_ip_from_cfg(file_name):
	regex = re.compile(' +ip address (\S+) (\S+)')
	result = []
	with open(file_name, 'r') as f:
		for line in f:
			match = regex.search(line)
			if match:
				result.append(match.groups())

	return result

print(get_ip_from_cfg('config_r1.txt'))