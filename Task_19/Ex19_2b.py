# -*- coding: utf-8 -*-
from netmiko import ConnectHandler
import yaml
from netmiko import ssh_exception
import re
from pprint import pprint

commands = ['interface',
			'interface ggggg',
			'i ro',
			'define interface-range TEST1 gigabitEthernet 1/0/18-20',
			'define interface-range TEST2 gigabitEthernet 1/0/17-20',
			'define interface-range TEST3 gigabitEthernet 1/0/16-20']


filename = 'devices.yaml'

def send_config_commands(device, commands, verbose=True):
	log = ({},{},)
	
	if verbose:
		print('Подключение к устройству {}'.format(device['ip']))

	try: 
		with ConnectHandler(**device) as ssh:
			ssh.enable()
			for command in commands:
				result = ssh.send_config_set(command)
				if re.search('Invalid input detected',result):
					print('''Комманда "{}" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве {}'''.format(command, device['ip']))
					log[0].update({command:result})
				elif re.search('Incomplete command',result):
					print('''Комманда "{}" выполнилась с ошибкой "Incomplete command." на устройстве {}'''.format(command, device['ip']))
					log[0].update({command:result})
				elif re.search('Ambiguous',result):
					print('''Комманда "{}" выполнилась с ошибкой "Ambiguous command: "{}"" на устройстве {}'''.format(command, command, device['ip']))
					log[0].update({command:result})				
				else:
					print(result)
					log[1].update({command:result})
	except ssh_exception.NetMikoAuthenticationException:
		print('Ошибка аутентификации')
	except ssh_exception.NetMikoTimeoutException:
		print('Заданное устройство недоступно')

	return log

if __name__ == '__main__':
	with open(filename) as f:
		devices = yaml.load(f)
		for device in devices:
			print()
			result = send_config_commands(device, commands)
			good, bad = result
			pprint(result, width=120)
			print(good.keys())
			print(bad.keys())

