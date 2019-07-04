import ex11_1
import draw_network_graph




with open('sh_cdp_n_sw1.txt','r') as f:
	draw_network_graph.draw_topology(ex11_1.parse_cdp_neigbors(f.read()))
