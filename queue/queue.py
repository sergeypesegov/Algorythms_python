from collections import deque
fout = open('output.txt', mode='w')

queue = deque()
answer = []

with open('input.txt', mode='r') as fin:
	n = int(fin.readline())

	for i in range(n):
		line = fin.readline()
		sign = line[0]
		if sign == '+':
			queue.append(line[1:-1])
		else:
			answer.append(queue.popleft())
answer = [str(i + '\n') for i in answer]
fout.write(''.join(answer))