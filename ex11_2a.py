import ex11_1
import draw_network_graph

cdp_neigbors_list = ['sh_cdp_n_sw1.txt',
					 'sh_cdp_n_r1.txt',
					 'sh_cdp_n_r2.txt',
					 'sh_cdp_n_r3.txt']


def create_network_map(file_name_list):
	netwrok_amp_list = {}
	for f in file_name_list:
		with open(f,'r') as device:
			temp = ex11_1.parse_cdp_neigbors(device.read())
			for item in temp.items():
				if not any((sorted(list(item)) == sorted(list(i))) for i in netwrok_amp_list.items()):
					netwrok_amp_list.update({list(item)[0]:list(item)[1]})

	return netwrok_amp_list

draw_network_graph.draw_topology(create_network_map(cdp_neigbors_list))