import os
import sqlite3
import re
import yaml

dhcp_snooping_filename_list = ['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']
db_filename = 'dhcp_snooping.db'
schema_filename = 'dhcp_snooping_schema.sql'
switches_filename_yaml = 'switches.yml'

'''
regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

result = []

for filename in data_filename:
    with open(filename) as data:
        for line in data:
            match = regex.search(line)
            if match:
                result.append(match.groups())
'''

def db_exist(db_filename):
    if not os.path.exists(db_filename):
        print('Database not exist. Before add data, create her.')
        return False
    else:
        return True

def wirite_rows_to_db(connection, query, data, verbose=False):
    for row in data:
        try:
            with connection:
                connection.execute(query,row)
        except sqlite3.IntegrityError as e:
            if verbose:
                print('When trying write {} Error occured: {}.'.format(row,e))
        else:
            if verbose:
                print('Success for write data {}.'.format(row))

def switches_yaml_to_list(switches_filename_yaml):
    switches_list = []

    with open(switches_filename_yaml) as f:
        switches = yaml.load(f)
        for hostname,location in switches['switches'].items():
            switches_list.append((hostname, location,))

    return switches_list

def parse_dhcp_snooping(dhcp_snooping_filename_list):
    regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
    result = []


    for filename in dhcp_snooping_filename_list:
        hostname = re.search('(\w+?)_', filename)
        with open(filename) as data:
            for line in data:
                match = regex.search(line)
                if match:
                    match = list(match.groups())
                    match.append(hostname.group(1))
                    result.append(tuple(match))
    return result

def add_data(db_filename):
    query_switches = '''insert into switches (hostname, location)
                        values (?, ?)'''
    query_dhcp = '''insert into dhcp (mac, ip, vlan, interface, switch)
                       values (?, ?, ?, ?, ?)'''
    connection = sqlite3.connect(db_filename)
    with connection:
        print('Addding data in table switches...')
        wirite_rows_to_db(connection, query_switches, switches_yaml_to_list(switches_filename_yaml), True)
        print('Adding data in table dhcp...')
        wirite_rows_to_db(connection, query_dhcp, parse_dhcp_snooping(dhcp_snooping_filename_list), True)


if __name__ == '__main__':
    if db_exist(db_filename):
        add_data(db_filename)