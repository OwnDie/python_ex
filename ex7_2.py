from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

file_name_read, file_name_write = argv[1:]

#print(file_name_write[0], file_name_read[0])

with open(file_name_read, 'r') as f_read, open(file_name_write, 'w') as f_write:
	for line in f_read:
		ignore_find = False
		for ignore_word in ignore:
			if line.find(ignore_word) != -1:
				ignore_find = True
				break
		if not ignore_find:
			f_write.write(line)
