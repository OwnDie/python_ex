
temp = []

#Take line with MAC
with open('CAM_table.txt', 'r') as f:
	temp_list = f.read().split('\n')
	for line in temp_list:
		if line.find('DYNAMIC') != -1:
			temp.append(line.split())

#Sort VLAN 
for mac_line in temp:
	mac_line[0] = int(mac_line[0])
temp.sort()

#Print line with format
for mac_line in temp:
	print('{:<8}{:<16}{:<10}'.format(mac_line[0], mac_line[1], mac_line[3]))
