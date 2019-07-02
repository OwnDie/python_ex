
protocol_template = ['Protocol: ',
					 'Prefix: ',
					 'AD/Metric: ',
					 'Nex-Hop: ',
					 'Last update: ',
					 'Outbound Interface: ']


with open('ospf.txt', 'r') as f:
	for line in f:
		temp = line.replace('O', 'OSPF')
		temp = temp.rstrip().split()
		temp[2] = temp[2].strip('[]')
		temp[4] = temp[4].rstrip(',')
		temp[5] = temp[5].rstrip(',')
		for i in range(6):
			print('{:<20}{:<20}'.format(protocol_template[i], temp[i]))
		print('\n')	
