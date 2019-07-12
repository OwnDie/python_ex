import re


def get_ints_without_description(file_name):
	regex = '\ninterface (\S+)\n (description)?'
	result = []
	with open(file_name, 'r') as f:
		file = f.read()
		match = re.finditer(regex,file)
		for value in match:
			print(value)
			if not value.group(2):
				result.append(value.group(1))

	return result

print(get_ints_without_description('config_r1.txt'))