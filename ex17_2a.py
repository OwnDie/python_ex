import glob
import re
import ex17_2
import yaml
from pprint import pprint

sh_cdp_files = glob.glob('sh_cdp_n_*')

def generate_topology_from_cdp(list_of_files, save_to_filename=None):
	result = {}
	for file in list_of_files:
		with open(file, 'r') as f:
			result.update(ex17_2.parse_sh_cdp_neighbors(f.read()))

	if save_to_filename:
		with open(save_to_filename, 'w') as f_write:
			yaml.dump(result, f_write)

	return result

pprint(generate_topology_from_cdp(sh_cdp_files, 'topology.yaml'))

