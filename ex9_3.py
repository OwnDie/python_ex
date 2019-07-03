
def str_list_to_int_list(str_list):
	int_list = []
	for i in str_list:
		int_list.append(int(i))
	return int_list

def get_int_vlan_map(file_name):
	interface,vlan,vlans,mode = '',1,[],''
	trunk_config = {}
	access_config = {}
	with open(file_name, 'r') as f:
		for line in f:
			line = line.strip()	
			if line.startswith('interface ') and not line.startswith('interface Vlan'):
				if interface:
					if mode.strip() == 'access':
						access_config[interface] = int(vlan)
						vlan = 1
					else:
						trunk_config[interface] = str_list_to_int_list(vlans)	
				interface = line.split()[-1]
			elif line.startswith('switchport mode'):
				mode = line.split()[-1]
				#print(mode)
			elif line.startswith('switchport access vlan'):
				vlan = line.split()[-1]
				#print(vlan)
			elif line.startswith('switchport trunk allowed'):
				vlans = line.split()[-1].split(',')
				#print(vlans)

	return trunk_config,access_config

t_config,a_config = get_int_vlan_map('config_sw2.txt')
print(t_config,a_config)