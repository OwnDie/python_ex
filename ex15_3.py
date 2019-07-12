import re

def convert_ios_nat_to_asa(nat_read_file, nat_write_file):
	regex = 'ip nat inside source static tcp ([\d.]+) (\d+) interface \S+ (\d+)'
	nat_template = 'object network LOCAL_{}\n host {}\n nat (inside,outside) static interface service tcp {} {}\n'
	with open(nat_read_file, 'r') as f_read, open(nat_write_file, 'w') as f_write:
		for line in f_read:
			match = re.search(regex, line)
			if match:
				print(match)
				f_write.write(nat_template.format(match.group(1),match.group(1),match.group(2),match.group(3)))


convert_ios_nat_to_asa('cisco_nat_config.txt','asa_nat_config.txt')