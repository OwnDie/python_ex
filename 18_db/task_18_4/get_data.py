import sys
import sqlite3
from tabulate import tabulate

db_filename = 'dhcp_snooping.db'
key, value = None, None

def get_data(db_filename, key=None, value=None):
	keys = ['mac', 'ip', 'vlan', 'interface', 'switch']
	result = []
	conn = sqlite3.connect(db_filename)
	conn.row_factory = sqlite3.Row
	if key and value:
		if not key in keys:
			print('This parametr is not supported. Allow values: mac, ip, vlan, interface, switch')
		else:
			print('Iformation about device with this parametrs: {} {}'.format(key, value))
			keys.remove(key)
			query = 'select * from dhcp where {} = ? and active = ?'.format(key)
			result_active = conn.execute(query, (value,1,))
			result_inactive = (conn.execute(query, (value,0,))).fetchall()
	else:
		query = 'select * from dhcp where active = ?'
		result_active = conn.execute(query, (1,))
		result_inactive = (conn.execute(query, (0,))).fetchall()
	print('\nActive records:\n')
	print(tabulate(result_active))
	if result_inactive:
		print('\nInactive records:\n')
		print(tabulate(result_inactive))
		


if __name__ == '__main__':


	if len(sys.argv) == 1:
		print('Records in dhcp table:')
		get_data(db_filename)
	elif len(sys.argv) == 3:
		key, value = sys.argv[1:]
		get_data(db_filename, key, value)
	else:
		print('Please, enter two or zero parametrs')

