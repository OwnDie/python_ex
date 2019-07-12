import re

def parse_sh_ip_int_br(filen_name):
	regex = '(\S+) +([\d.]+|unassigned) +\w+ +\w+ +(up|down|administratively down) +(up|down)'

	with open(filen_name, 'r') as f:
		file = f.read()
		result = [match.groups() for match in re.finditer(regex, file)]

	return result
if __name__ == '__main__':
	print(parse_sh_ip_int_br('sh_ip_int_br.txt'))