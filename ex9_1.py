
access_dict = {'FastEthernet0/12':10,
			   'FastEthernet0/14':11,
			   'FastEthernet0/16':17,
			   'FastEthernet0/17':150}


def generate_access_config(access, psecurity=False):
	access_config = {}
	access_template = ['switchport mode access',
					   'switchport access vlan',
					   'switchport nonegotiate',
					   'spanning-tree portfast',
					   'spanning-tree bpduguard enable']
	port_security = ['switchoprt port-security maximum 2',
					 'switchoprt port-security violation restrict',
					 'switchoprt port-security']
	#Создагте списка конфигурации
	for interface,vlan in access.items():
		interface = 'interface {}'.format(interface)
		access_config[interface] = [] #.append('interface {}'.format(interface))
		for line in access_template:
			if line.endswith('access vlan'):
				access_config[interface].append('{} {}'.format(line,vlan))
				continue
			access_config[interface].append(line)
	#Если psecurity=True добавить конфигурации psecurity
		if psecurity:
			for security in port_security:
				access_config[interface].append(security)
	#Возвращение списка конфигурации	
	return access_config


config = generate_access_config(access_dict, True)
print(config)