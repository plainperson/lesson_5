f = open(r'test text', 'r', encoding='utf-8')
for line in f:
    print(line, end='')

f.close()
