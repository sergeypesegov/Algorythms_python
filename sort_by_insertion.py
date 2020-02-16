import re

with open('input.txt', mode='r') as fin:
	n = fin.readline()
	array = fin.readline()

array = re.split(r' ', array)
array = [int(i) for i in array]

def sort_by_insertion(array):
	indexes = []
	for i in range(len(array)):
		j = i - 1 
		key = array[i]
		while array[j] > key and j >= 0:
			array[j + 1] = array[j]
			j -= 1
		array[j + 1] = key
		indexes.append(j + 2)
	return indexes, array

result = sort_by_insertion(array)
indexes = result[0]
answer = result[1]
indexes =[str(i) for i in indexes]
answer = [str(i) for i in answer]

fout = open('output.txt', mode='w')
fout.write(' '.join(indexes) + '\n' + ' '.join(answer))