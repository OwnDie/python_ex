ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command(command, ignore):
	return any(word in command for word in ignore)


def config_generator(file_name):
	config = {}
	fist_level_command = ''
	second_level_command = ''
	list_to_dict_flag = True
	with open(file_name) as f:
		for line in f:
			if not '!' in line and line.strip() and not ignore_command(line, ignore):
				if line.startswith('  '):
					if list_to_dict_flag:
						config[fist_level_command] = {key: [] for key in config[fist_level_command]}
					config[fist_level_command][second_level_command].append(line.strip())
					list_to_dict_flag = False
				elif line.startswith(' '):
					config[fist_level_command].append(line.strip())
					second_level_command = line.strip()
					list_to_dict_flag = True
				else:
					config[line.strip()] = []
					fist_level_command = line.strip()

	return config

config = config_generator('config_r1.txt')
print(config)