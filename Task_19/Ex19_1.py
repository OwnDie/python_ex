# -*- coding: utf-8 -*-
from netmiko import ConnectHandler
import yaml

command = 'sh ip int br'
filename = 'devices.yaml'

def send_show_command(device, command):
	print('Подключение к устройству {}'.format(device['ip']))

	with ConnectHandler(**device) as ssh:
		ssh.enable()

		result = ssh.send_command(command)
		print(result)


if __name__ == '__main__':
	with open(filename) as f:
		devices = yaml.load(f)
		for device in devices:
			send_show_command(device, command)