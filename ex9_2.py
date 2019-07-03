
trunk_dict = {'FastEthernet0/1':[10,20],
			  'FastEthernet0/2':[11,30],
			  'FastEthernet0/4':[17]}

def generate_trunk_config(trunk):
	'''
	trunk - словарь trunk-портов для которых необходимо сгенерировать конфигурацию.

	Возвращает список всез команд, которые были сгенерированы на основе шаблона
	'''
	trunk_template = ['switchport trunk encapsulation dot1q',
					  'switchport mode trunk',
					  'switchport trunk native vlan 999',
					  'switchport trunk allowed vlan']

	trunk_config = {}

	for interface,vlans in trunk.items():
		interface = 'interface {}'.format(interface)
		trunk_config[interface] = []
		for line in trunk_template:
			if line.endswith('allowed vlan'):
				temp = []
				for vlan in vlans: vlan = temp.append(str(vlan))
				trunk_config[interface].append('{} {}'.format(line, ','.join(temp)))
				continue
			trunk_config[interface].append(line)
	return trunk_config

config = generate_trunk_config(trunk_dict)
print(config)