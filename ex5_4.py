
num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

print(num_list)
num = input('Pleas enter number: ')
num_list.append('END')
num_list_length = num_list.index('END')-1
num_list.remove('END')
num_list.reverse()
num_last_index = num_list_length - num_list.index(int(num))
print(num_last_index)

print(word_list)
num = input('Pleas enter word: ')
word_list.append('END')
word_list_length = word_list.index('END')-1
word_list.remove('END')
word_list.reverse()
word_last_index = word_list_length - word_list.index(num)
print(word_last_index)