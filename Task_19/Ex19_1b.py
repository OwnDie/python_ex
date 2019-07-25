# -*- coding: utf-8 -*-
from netmiko import ConnectHandler
import yaml
from netmiko import ssh_exception

command = 'sh ip int br'
filename = 'devices.yaml'

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

if __name__ == '__main__':
	with open(filename) as f:
		devices = yaml.load(f)
		for device in devices:
			print()
			send_show_command(device, command)