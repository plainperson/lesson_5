dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('text task 4_transl', 'w', encoding='utf-8') as f_write:
    with open('text task 4', 'r', encoding='utf-8') as f_read:
        for line in f_read:
            f_write.writelines([line.replace(line.split()[0], dic[line.split()[0]])])

