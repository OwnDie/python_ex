
london_cp = {
	'r1' : {
	'location': '21 New Globe Walk',
	'vendor': 'Cisco',
	'model': '4451',
	'ios': '15.4',
	'ip': '10.255.0.1'
	},
	'r2' : {
	'location': '21 New Globe Walk',
	'vendor': 'Cisco',
	'model': '4451',
	'ios': '15.4',
	'ip': '10.255.0.2'
	},
	'sw1' : {
	'location': '21 New Globe Walk',
	'vendor': 'Cisco',
	'model': '3850',
	'ios': '3.6.XE',
	'ip': '10.255.0.101',
	'vlans': '10,20,30',
	'routing': True
	}
}


ch_device = input('Please enter device name: ')
parametr_list = london_cp.get(ch_device).keys()
parametr_list_string = ','.join(parametr_list)
ch_parametr = input('Please enter parametr name ({}): '.format(parametr_list_string))

print(london_cp.get(ch_device).get(ch_parametr.lower(), 'This parametr does not exist'))