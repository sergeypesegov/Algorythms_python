from collections import deque
fout = open('output.txt', mode='w')

stack = deque()
answer = []

with open('input.txt', mode='r') as fin:
	n = int(fin.readline())

	for i in range(n):
		line = fin.readline()
		sign = line[0]
		if sign == '+':
			stack.append(line[1:-1])
		else:
			answer.append(stack.pop())
answer = [str(i + '\n') for i in answer]
fout.write(''.join(answer))




	
#
#	for line in range(n):
#		line = fin.readline()
#		stack.append(line[:-1])

#print(stack)
#for i in range(n):
	#if stack[i] == '-' or stack[i] == '':
		#fout.write((stack[i - 1][1:]) + '\n')

#answer = [int(i) for i in answer]
#fout.write(str(answer))