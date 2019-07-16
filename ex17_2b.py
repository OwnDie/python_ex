import draw_network_graph as dng
import yaml
from pprint import pprint

def transform_topology(yaml_file_name):
	result = {}
	with open(yaml_file_name, 'r') as f:
		topology_file = yaml.load(f)

	for key,value in topology_file.items():
		for key_2,value_2 in value.items():
			for key_3,value_3 in value_2.items():
				if not (result.get((key,key_2,)) or result.get((key_3,value_3))):
					result.update({(key,key_2,):(key_3,value_3)})
				
	return result



dng.draw_topology(transform_topology('topology.yaml'))