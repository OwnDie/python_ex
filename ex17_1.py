import glob
import re
import csv

sh_version_files = glob.glob('sh_vers*')
#print(sh_version_files)
headers = ['hostname', 'ios', 'image', 'uptime']

def parse_sh_version(sh_version_str):
	regex = r"Cisco IOS.+Version ([\w().]+)[\w\W]+^router uptime is (.+)[\w\W]+^System image.+\"(.+)\""
	match = re.search(regex, sh_version_str, re.M)
	if match:
		return match.group(1,3,2)


def write_inventory_to_csv(data_filenames, csv_filename):
	result = []
	with open(csv_filename,'w') as csv_file:
		writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
		writer.writerow(headers)
		for file_name in data_filenames:
			hostname = re.search(r"sh_version_(\w+).txt",file_name).group(1)
			with open(file_name) as f:
				result = list(parse_sh_version(f.read()))
				result.insert(0,hostname)
				writer.writerow(result)


write_inventory_to_csv(sh_version_files, 'routers_inventory.csv')