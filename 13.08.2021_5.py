from random import choice


def get_jokes(x, flag):
    """
    :param x:
    :param flag: True or False
    :return: massive_of_jokes
    """
    flag_check = set()
    massive_of_jokes = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for i in range(x):
        a = choice(nouns)
        b = choice(adverbs)
        c = choice(adjectives)
        if flag is True:
            while a in flag_check:
                a = choice(nouns)
            while b in flag_check:
                b = choice(adverbs)
            while c in flag_check:
                c = choice(adjectives)
        flag_check.add(a)
        flag_check.add(b)
        flag_check.add(c)
        joke = f'{a} {b} {c}'
        massive_of_jokes.append(joke)
    return massive_of_jokes


print(get_jokes(3, True))

