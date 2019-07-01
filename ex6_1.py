
ip_address = input('Please enter ip address (example 10.0.1.1): ')

ip_address_list = ip_address.split('.')

if int(ip_address_list[0]) >= 1 and int(ip_address_list[0]) <=223:
	print('unicast')
elif int(ip_address_list[0]) >= 224 and int(ip_address_list[0]) <=239:
	print('multicast')
elif int(ip_address_list[0]) == 255 and int(ip_address_list[1]) == 255 and int(ip_address_list[2]) == 255 and int(ip_address_list[3]) == 255:
	print('local broadcast')
elif int(ip_address_list[0]) == 0 and int(ip_address_list[1]) == 0 and int(ip_address_list[2]) == 0 and int(ip_address_list[3]) == 0:
	print('unassigned')
else:
	print('unused')