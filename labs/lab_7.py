dic = {'cat': ['кошка','кот'], 'dog': ['собака'], 'cow': ['корова'],
       'tiger': ['тигр'], 'elephant': ['слон'], 'rhino': ['носорог'],
       'eagle': ['орел'], 'crocodile': ['крокодил'], 'spider': ['паук'],
       'bug': ['жук']}


def addpair(dic):
    """Добавление пары"""
    slovo = input('Введите новое слово на английском:')
    value = input('Введите перевод слова:')
    x=value.split(',')
    print(x)
    if slovo in dic:
        for i in range(len(x)):
            dic[slovo].append(x[i])
    else:
        dic[slovo]=x


    print(dic)


def delpair(dic):
    """Удаление пары"""
    word = input('Введите слово на английском,которое хотите удалить:')
    if word in dic:
        del dic[word]
    print(dic)


def find(dic):
    """Проверка"""
    x = input('Введите слово для проверки:')
    if x in dic.keys():
        print("Да входит")
    else:
        print('Нет,не входит')


def output_5_len(dic):
    """Вывод слов меньше 5"""
    for i in dic:
        if len(i) < 5:
            print(i, end=' ')
            print()


def clear():
    """Очистка словаря"""
    global dic
    dic.clear()
    print()
    print(dic)


def sortir(dic):
    """Сортировка"""
    dic = dict(sorted(dic.items(), key=lambda x: x[0]))
    print()
    print(dic)


def alldict(dic):
    """Вывод всего"""
    for i in dic:
        for j in range(len(dic[i])):
            print(i, '-->', dic[i][j])


def changepair(dic):
    '''Изменение пары'''
    keyw = input('Введите ключ который хотите поменять:')
    if keyw in dic:
        key= input('Введите новое значение для слова:')
        dic[keyw].clear()
        dic[keyw].append(key)
    else:
        print("Данного слова нет в словаре")
    print((dic))


def key_to_value():
    """Меняет ключ с значением"""
    global dic
    dic2={}
    for slovo in dic.values():
        for j in range(len(slovo)):
            dic2[slovo[j]] = []
    for value in dic2.keys():
        for key in dic.keys():
            if value in dic[key]:
                dic2[value].append(key)

    dic=dic2
choise = int(input('Выберите действие со словарем:\n'
                   '1)добавать пару\n'
                   '2)удалить\n'
                   '3)проверить есть ли уже в базе\n'
                   '4)вывести слова на англ короче 5 симвлов\n'
                   '5)очистить словарь\n'
                   '6)отсортировать словарь\n'
                   '7)вывести весь словарь\n'
                   '8)изменить пару \n'
                   '9)поменять ключ и значение\n'
                   'Ваш выбор:'))
try:
    while 1<=choise<=9:
        if choise == 1:
            addpair(dic)
        elif choise == 2:
            delpair(dic)
        elif choise == 3:
            find(dic)
        elif choise == 4:
            output_5_len(dic)
        elif choise == 5:
            clear()
        elif choise == 6:
            sortir(dic)
        elif choise == 7:
            alldict(dic)
        elif choise == 8:
            changepair(dic)
        else:
            key_to_value()
        choise = int(input('Выберите действие со словарем:\n'
                           '1)добавать пару\n'
                           '2)удалить\n'
                           '3)проверить есть ли уже в базе\n'
                           '4)вывести слова на англ короче 5 симвлов\n'
                           '5)очистить словарь\n'
                           '6)отсортировать словарь\n'
                           '7)вывести весь словарь\n'
                           '8)изменить пару \n'
                           '9)поменять ключ и значение\n'
                           'Ваш выбор:'))
    else:
        print("Нет такой функции")
except ValueError:
    print('Try again')
