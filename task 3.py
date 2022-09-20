salary_total = 0
workers = 0
with open('text task 3', 'r', encoding='utf-8') as f:
    for line in f:
        salary_total += float(line.split()[1])
        workers += 1
        if float(line.split()[1]) < 20000:
            print(line.split()[0])
print('Средний заработок составил: ', round (salary_total / workers, 2))





















