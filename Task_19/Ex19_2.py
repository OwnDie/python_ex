# -*- coding: utf-8 -*-
from netmiko import ConnectHandler
import yaml
from netmiko import ssh_exception

commands = ['define interface-range TEST1 gigabitEthernet 1/0/18-20',
			'define interface-range TEST2 gigabitEthernet 1/0/17-20',
			'define interface-range TEST3 gigabitEthernet 1/0/16-20']


filename = 'devices.yaml'

def send_config_commands(device, commands):
	print('Подключение к устройству {}'.format(device['ip']))

	try: 
		with ConnectHandler(**device) as ssh:
			ssh.enable()
			for command in commands:
				result = ssh.send_config_set('no ' + command)
				print(result)
	except ssh_exception.NetMikoAuthenticationException:
		print('Ошибка аутентификации')
	except ssh_exception.NetMikoTimeoutException:
		print('Заданное устройство недоступно')

if __name__ == '__main__':
	with open(filename) as f:
		devices = yaml.load(f)
		for device in devices:
			print()
			send_config_commands(device, commands)