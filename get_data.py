import sys
import sqlite3
from tabulate import tabulate

db_filename = 'dhcp_snooping.db'
key, value = None, None
#keys.remove(key)

def get_data(db_filename, key=None, value=None):
	keys = ['mac', 'ip', 'vlan', 'interface', 'switch', 'active']
	result = []
	conn = sqlite3.connect(db_filename)
	conn.row_factory = sqlite3.Row
	if key and value:
		if not key in keys:
			print('This parametr is not supported. Allow values: mac, ip, vlan, interface, switch')
		else:
			print('Iformation about device with this parametrs: {} {}'.format(key, value))
			keys.remove(key)
			query = 'select * from dhcp where {} = ?'.format(key)
			result = conn.execute(query, (value,))
	else:
		query = 'select * from dhcp'
		result = conn.execute(query)
	if result:
		print(tabulate(result))
		


if __name__ == '__main__':

	number_argv = len(sys.argv)
	if number-argv == 1:
		print('Records in dhcp table:')
		get_data(db_filename)
	elif number_argvl == 3:
		key, value = sys.argv[1:]
		get_data(db_filename, key, value)
	else:
		print('Please, enter two or zero parametrs')

