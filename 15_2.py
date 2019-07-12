import re

def parse_sh_ip_int_br(filen_name):
	regex = '(\S+) + ([\d.]+) +\w+ +\w+ +(up|down|administatively down) +(up|down)'

	with open(filen_name, 'r') as f:
		file = f.read()
		#match = re.search(regex.line)
		result = [match.groups() for match in re.finditer(regex, read)]

	return result

print(parse_sh_ip_int_br(sh_ip_int_br.txt))