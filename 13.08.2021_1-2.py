def determinant(x, translator):
    if x in translator.keys():
        return translator[x]
    elif x in translator.values():
        translator = {i: j for j, i in translator.items()}
        return translator[x]
    else:
        return None


def capitalizer(translator):
    for i in translator.keys():
        translator[i] = translator[i].capitalize()
    return translator


def num_translate(x):
    translator = {
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять",
        "zero": "нуль",
    }
    answer = determinant(x, translator)
    if answer is None:
        capitalizer(translator)
        translator = {a: b for b, a in translator.items()}
        capitalizer(translator)
    answer = determinant(x, translator)
    return answer


print(num_translate("Нуль"))

