import ex15_2
import re

headers_lsit = ['interface', 'address', 'status', 'protocol']


def convert_to_dict(headers_lsit, value_list):
	result = []
	for line in value_list:
		result.append(dict(zip(headers_lsit,line)))

	return result

print(convert_to_dict(headers_lsit, ex15_2.parse_sh_ip_int_br('sh_ip_int_br.txt')))
