#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sqlite3
import yaml
import re
from tabulate import tabulate

def create_db(name, schema):
	db_exists = os.path.exists(name)
	conn = sqlite3.connect(name)
	with conn:
		if not db_exists:
			print('Создаю базу данных...')
			with open(schema, 'r') as f:
				schema = f.read()
			conn.executescript(schema)
			print('Успешно')
		else:
			print('База данных уже существует')

def add_data_switches(db_file, filename):
	query_switches = '''insert into switches (hostname, location) 
						values (?, ?)'''
	db_exists = os.path.exists(db_file)
	conn = sqlite3.connect(db_file)
	with conn:
		if db_exists:
			for row in switches_yaml_to_list(filename[0]):
				print(row)
				conn.execute(query_switches,row)
			print('Успешно')
		else:
			print('База данных не существует')

def add_data(db_file, filename):
	query_dhcp = '''replace into dhcp (mac, ip, vlan, interface, switch)
					   values (?, ?, ?, ?, ?)'''
	db_exists = os.path.exists(db_file)
	conn = sqlite3.connect(db_file)
	with conn:
		if db_exists:
			for row in parse_dhcp_snooping(filename):
				print(row)
				conn.execute(query_dhcp,row)
				conn.execute("UPDATE dhcp set active = 1 WHERE mac = ?", (row[0],))
				conn.execute("UPDATE dhcp set last_active = datetime('now') WHERE mac = ?", (row[0],))
			print('Успешно')
		else:
			print('База данных не существует')
	
def get_data(db_file, key, value):
	keys = ['mac', 'ip', 'vlan', 'interface', 'switch', 'active', 'last_active']
	headers = ['mac', 'ip', 'vlan', 'interface', 'switch', 'active', 'last_active']
	result = []

	conn = sqlite3.connect(db_file)
	conn.row_factory = sqlite3.Row

	if not key in keys:
		print("parse_dhcp_snooping.py get: error: argument -k: invalid choice: '{}' (choose from 'mac', 'ip', 'vlan', 'inerface', 'switch')".format(key))
	else:
		keys.remove(key)
		query = 'select * from dhcp where {} = ? and active = ?'.format(key)
		result_active = conn.execute(query, (value,1,))
		result_inactive = (conn.execute(query, (value,0,))).fetchall()

	print('\nАктивные записи:\n')
	print(tabulate(result_active, headers=headers))
	if result_inactive:
		print('\nНеактивные записи:\n')
		print(tabulate(result_inactive, headers=headers))

def get_all_data(db_file):
	print(db_file)
	keys = ['mac', 'ip', 'vlan', 'interface', 'switch', 'active', 'last_active']
	query = 'select * from dhcp where active = ?'

	db_exists = os.path.exists(db_file)
	conn = sqlite3.connect(db_file)
	with conn:
		if db_exists:
			result_active = conn.execute(query, (1,))
			result_inactive = (conn.execute(query, (0,))).fetchall()
			print('\nАктивные записи:\n')
			print(tabulate(result_active, headers=keys))
			if result_inactive:
				print('\nНеактивные записи:\n')
				print(tabulate(result_inactive, headers=keys))
		else:
			print('База данных не существует')

def switches_yaml_to_list(switches_filename_yaml):
	switches_list = []
	with open(switches_filename_yaml, 'r') as f:
		switches = yaml.load(f)
		for hostname,location in switches['switches'].items():
			switches_list.append((hostname, location,))

	return switches_list

def parse_dhcp_snooping(dhcp_snooping_filename_list):
	regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
	result = []
	for filename in dhcp_snooping_filename_list:
		hostname = re.search('(\w+?)_', filename)
		all_record_inactive_from_switch('db_filenma.db',hostname.group(1))
		with open(filename) as data:
			for line in data:
				match = regex.search(line)
				if match:
					match = list(match.groups())
					match.append(hostname.group(1))
					result.append(tuple(match))
	return result	

def all_record_inactive_from_switch(db_filename, switch):
    connection = sqlite3.connect('dhcp_snooping.db')
    with connection:
        for row in connection.execute('select * from dhcp'):
            connection.execute("UPDATE dhcp set active = 0 WHERE  switch = ? ", (switch,))