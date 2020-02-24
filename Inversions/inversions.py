import re

with open('input.txt', mode='r') as fin:
	n = int(fin.readline())
	array = fin.readline()

array = re.split(r' ', array)
array = [int(i) for i in array]

def count_inversion(lst):
    return merge_count_inversion(lst)[1]

def merge_count_inversion(lst):
    if len(lst) <= 1:
        return lst, 0
    middle = int( len(lst) / 2 )
    left, a = merge_count_inversion(lst[:middle])
    right, b = merge_count_inversion(lst[middle:])
    result, c = merge_count_split_inversion(left, right)
    return result, (a + b + c)

def merge_count_split_inversion(left, right):
    result = []
    count = 0
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count 
result = count_inversion(array)


#for i in range(n - 1):
#	for j in range(n):
#		if i < j and array[i] > array[j]:
#			counter += 1
#print(counter)



fout = open('output.txt', mode='w')
fout.write(str(result))