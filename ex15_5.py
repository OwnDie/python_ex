import re


def genertate_desctiption_from_cdp(file_name):
	regex = '(\S+)\s+(Eth [\d/]+).+(Eth [\d/]+)'
	result = {}
	with open(file_name, 'r') as f:
		file = f.read()
		match = re.finditer(regex, file)
		#print(match)
		for value in match:
			result[value.group(2)]=['description Connected to {} port {}'.format(value.group(1),value.group(3))]

	return result

print(genertate_desctiption_from_cdp('sh_cdp_n_sw1.txt'))