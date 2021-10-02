# Task 1

eng_rus_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(eng_word):
    return eng_rus_dict.get(eng_word)


print(num_translate('seven'))

# Task 2

eng_rus_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(eng_word):
    if eng_word[0].isupper():
        eng_word = eng_word.lower()
        return eng_rus_dict[eng_word].capitalize()
    else:
        return eng_rus_dict[eng_word]


print(num_translate_adv('seven'))
print(num_translate_adv('Seven'))


# Task 3

def thesaurus(*names):
    out_dict = dict()
    for name in names:
        out_dict.setdefault(name[0], [])
        out_dict[name[0]].append(name)
    return out_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))


# Task4

def thesaurus_adv(*names_surnames):
    out_dict = {}
    for name_surname in names_surnames:
        name, surname = name_surname.split()
        out_dict.setdefault(surname[0], {})
        out_dict[surname[0]].setdefault(name[0], [])
        out_dict[surname[0]][name[0]].append(name_surname)

    sorted_dict = {x: out_dict[x] for x in sorted(out_dict)}  # Dict Comprehensions
    return out_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов",
                    "Анна Савельева"))

# Task 5

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num):
    joke_list = []
    for i in range(num):
        cur_nouns = random.choice(nouns)
        cur_adverbs = random.choice(adverbs)
        cur_adjectives = random.choice(adjectives)
        joke_list.append(f'{cur_nouns} {cur_adverbs} {cur_adjectives}')
    return joke_list


print(get_jokes(1))
print(get_jokes(2))


def get_jokes_adv(num, repeats=True):
    joke_list = []

    if not repeats:
        if num > min(len(nouns), len(adverbs), len(adjectives)):
            return 'No way'
        else:
            random.shuffle(nouns)
            random.shuffle(adverbs)
            random.shuffle(adjectives)
            for i in range(num):
                joke_list.append(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')

    else:
        for i in range(num):
            cur_nouns = random.choice(nouns)
            cur_adverbs = random.choice(adverbs)
            cur_adjectives = random.choice(adjectives)
            joke_list.append(f'{cur_nouns} {cur_adverbs} {cur_adjectives}')
    return joke_list


print(get_jokes_adv(4, False))
print(get_jokes_adv(5, False))
print(get_jokes_adv(6, False))