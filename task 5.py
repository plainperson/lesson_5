from random import randint

with open('task 5', 'w', encoding='utf-8') as f:
    li = [randint(1, 10) for _ in range(30)]
    f.write(' '.join(map(str, li)))