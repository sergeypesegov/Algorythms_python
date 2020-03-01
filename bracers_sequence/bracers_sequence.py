from collections import deque

fout = open('output.txt', mode='w')
with open('input.txt', mode='r') as fin:
    n = int(fin.readline())

    for i in range(n):
        line = fin.readline().strip()
        #line = line[:-1]
        #print(line)
        buf = deque()
        kek = 0

        for char in line:
            k = len(buf)
            if char in '([':
                buf.append(char)
                #print('добавлен элемент: ', char)

            elif ((char == ']') and (k != 0) and ('[' == buf[-1])) or ((char == ')') and (k != 0) and ('(' == buf[-1])):
                #print('удален элемент: ', char)
                buf.pop()

            elif k == 0:
                kek = 1
                #print('NO' + 'Здесь длина тсроки 0')
                #fout.write('NO')
            else:
                kek = 1
            #print(buf)
        k = len(buf)
        if k != 0:
            #print(str(len(buf))+ ' - длина строкu ' + 'NO' + '\n')
            fout.write('NO' + '\n')

        elif kek == 1:
            fout.write('NO' + '\n')
            #print(str(len(buf))+ ' - длина строкu ' + 'NO' + '\n')
        else:
            fout.write('YES' + '\n')
            #print(str(len(buf))+ ' - длина строкu ' + 'YES' + '\n')