def is_heap(array, n):
	for i in range(1, n // 2):
		if not((2 * i <= n and array[i] <= array[2 * i]) and (2 * i + 1 <= n and array[i] <= array[2 * i + 1])):
			return False
	return True

with open('input.txt', 'r') as fin, open('output.txt', 'w') as fout:
    n = int(fin.readline())
    array = [0]
    [array.append(int(i)) for i in fin.readline().split()]
    fout.write('YES' if is_heap(array, n) else 'NO')

#with open('input.txt', mode='r') as fin:
#	n = int(fin.readline())
#	array = fin.readline()
#
#array = re.split(r' ', array)
#array = [int(i) for i in array]
#
#fout = open('output.txt', mode = 'w')
#
#fout.write('YES' if is_heap(array, n) else 'NO')	

#def is_heap(heap, size):
#    for i in range(1, size // 2):
#        if not((2 * i <= size and heap[i] <= heap[2 * i]) and (2 * i + 1 <= size and heap[i] <= heap[2 * i + 1])):
#            return False
 #   return True
#
#
#with open('input.txt', mode='r') as fin, open('output.txt', mode='w') as fout:
    #n = read_object.readline()
    #h = [0]
    #[h.append(int(i)) for i in read_object.readline().split()]
    #write_object.write('YES' if is_heap(h, int(n)) else 'NO')