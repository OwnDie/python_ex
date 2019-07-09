
from pprint import pprint

def parse_cdp_neigbors(command_output):
	command_output_list = command_output.split('\n')
	interface_flag = False
	cdp_dict_value_list_flag = False
	cdp_dict = {}
	for line in command_output_list:
		if line == '':
			continue
		elif interface_flag :
			device_id, local_int_type, local_int_num, *other, des_int_type, des_int_num = line.split()
			cdp_dict[(locale_device, local_int_type + local_int_num,)] = (device_id, des_int_type + des_int_num,)
		elif '>' in line:
			locale_device = line[0:line.find('>')]
		elif 'Device ID' in line:
			interface_flag = True

	return  cdp_dict


if __name__ == '__main__':
	with open('sh_cdp_n_sw1.txt', 'r') as f:
		cdp_dict = parse_cdp_neigbors(f.read())
	pprint(cdp_dict)