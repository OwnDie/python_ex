import re


def parse_sh_cdp_neighbors(sh_cdp_neighbors_str):
	regex = r"^(\S+) +(Eth [\w/]+).+(Eth [\w/]+)"	
	match = re.finditer(regex, sh_cdp_neighbors_str,re.M)
#	print(match)

	hostname = re.search(r"(\w+)>", sh_cdp_neighbors_str)
	result = {hostname.group(1) : {}}
	for line in match:
		result[hostname.group(1)].update({line.group(2) : {line.group(1) : line.group(3)}})

	return result

if __name__ == '__main__':
	with open('sh_cdp_n_sw1.txt','r') as f:
		print(parse_sh_cdp_neighbors(f.read()))

