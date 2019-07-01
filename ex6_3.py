access_template = ['switchport mode access',
				   'switchport access vlan',
				   'spanning-tree portfast',
				   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
				  'switchport mode trunk',
				  'switchport trunk allowed vlan']

fast_int = {'access':{'0/12':'10','0/14':'11','0/16':'17','0/17':'150'},
			'trunk':{'0/1':['add','10','20'],
					 '0/2':['only','11','30'],
					 '0/4':['del','17']} }
'''
for intf, vlan in fast_int['access'].items():
	print('interfcea FastEthernet' + intf)
	for command in access_template:
		if command.endswith('access vlan'):
			print(' {} {}'.format(command, vlan))
		else:
			print(' {}'.format(command))
'''


for intf,vlan in fast_int['trunk'].items():
	print('interface FastEthernet' + intf)
	for command in trunk_template:
		if command.endswith('allowed vlan'):
			if vlan[0] == 'add':
				temp = ','.join(vlan)
				temp = temp.replace('add,','add ')
				print(' {} {}'.format(command, temp))
			elif vlan[0] == 'only':
				temp = ','.join(vlan)
				temp = temp.replace('only,','')
				print(' {} {}'.format(command, temp))
			elif vlan[0] == 'del':
				temp = ','.join(vlan)
				temp = temp.replace('del,','remove ')
				print(' {} {}'.format(command, temp))
		else:
			print(' {}'.format(command))