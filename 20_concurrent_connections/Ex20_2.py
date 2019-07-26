# -*- coding: utf-8 -*-
from netmiko import ConnectHandler,ssh_exception
import yaml
import re
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import time

commands = ['interface',
			'interface ggggg',
			'i ro',
			'define interface-range TEST1 gigabitEthernet 1/0/18-20',
			'define interface-range TEST2 gigabitEthernet 1/0/17-20',
			'define interface-range TEST3 gigabitEthernet 1/0/16-20']
command_sh = 'sh ip int br'
filename = 'devices.yaml'

def continue_execute():
	answer = input('Продолжать выполнять команды? [y]/n: ');
	if answer == 'n' or answer == 'no':
		return False

	return True

def send_show_command(device, command):
	print('Подключение к устройству {}'.format(device['ip']))

	try: 
		with ConnectHandler(**device) as ssh:
			ssh.enable()

			result = ssh.send_command(command)
			print(result)
	except ssh_exception.NetMikoAuthenticationException:
		print('Ошибка аутентификации')
	except ssh_exception.NetMikoTimeoutException:
		print('Заданное устройство недоступно')

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
					if not continue_execute():
						break
				elif re.search('Incomplete command',result):
					print('''Комманда "{}" выполнилась с ошибкой "Incomplete command." на устройстве {}'''.format(command, device['ip']))
					log[0].update({command:result})
					if not continue_execute():
						break
				elif re.search('Ambiguous',result):
					print('''Комманда "{}" выполнилась с ошибкой "Ambiguous command: "{}"" на устройстве {}'''.format(command, command, device['ip']))
					log[0].update({command:result})
					if not continue_execute():
						break				
				else:
					print(result)
					log[1].update({command:result})
	except ssh_exception.NetMikoAuthenticationException:
		print('Ошибка аутентификации')
	except ssh_exception.NetMikoTimeoutException:
		print('Заданное устройство недоступно')

	return log

def send_commands(device, show=None, config=None):
	if show:
		send_show_command(device,show)
	if config:
		send_config_commands(device, config)

def send_commands_threads(devices, show=None, config=None):
	with ThreadPoolExecutor(max_workers=limit) as executor:
		f_result = ececutor.map(send_commands, devices, repeat(show), repeat(config))
if __name__ == '__main__':
	with open(filename) as f:
		devices = yaml.load(f)
		for device in devices:
			send_commands(device, show=command_sh)
			send_commands(device, config=commands)

