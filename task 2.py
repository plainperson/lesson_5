with open ('test text', 'r') as f:
    lines = f.readlines()
    print('в тексте' + str(len(lines)) + 'строк')
    f.seek(0)
    text = f.readline()
    res = len(text.split())
    print('в строке' + str(res) + 'слов')