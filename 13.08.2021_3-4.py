# number 2
"""
def thesaurus(*names):
    names_dict = {}
    for name in names:
        names_dict.setdefault(name[0], [])
    for key in names_dict.keys():
        for name in names:
            if name[0] == key:
                names_dict[key].append(name)
    names_dict = dict(sorted(names_dict.items(), key=lambda x: x[0]))
    return names_dict


print(thesaurus('Настя', 'Миша', "Вася", "Маша"))
"""


# number 3
def thesaurus_adv(*names):
    names = sorted(list(names), key=lambda x: x[x.index(' ') + 1])
    print(names)
    names_dict = {}
    for name in names:
        names_dict.setdefault(name.split()[1][0], {})
    for name in names:
        first_name, second_name = map(str, name.split())
        for key in names_dict.keys():
            if second_name[0] == key:
                names_dict[key].setdefault(first_name[0], [])
    for name in names:
        first_name, second_name = map(str, name.split())
        for key in names_dict.keys():
            if second_name[0] == key:
                for name_key in names_dict[key].keys():
                    if first_name[0] == name_key:
                        names_dict[key][name_key].append(name)
                        names_dict[key] = dict(sorted(names_dict[key].items(), key=lambda x: x[0]))


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

