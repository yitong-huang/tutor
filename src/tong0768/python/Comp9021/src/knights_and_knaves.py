import re
from collections import defaultdict


Knave = 0
Knight = 1

AtLeast = 0
AtMost = 1
OneOf = 2
AllOf = 3
IS = 4
OR = 5
AND = 6


def read_from_file():
    filename = input("Which text file do you want to use for the puzzle? ")
    f = open(filename, 'r')
    content = f.read()
    f.close()
    return content


def cut2sentence(content):
    content = content.replace("\r", " ")
    content = content.replace("\n", " ")
    sentences = re.findall('\"*[A-Za-z,\": ]*[.?!]\"{0,1}', content)
    return sentences


def add_name_to_set(names, sirs):
    for name in names:
        sirs.add(name)


def get_sirs(sentences):
    sirs = set()
    for sentence in sentences:
        if 'Sir ' in sentence:
            name = re.findall('Sir\\s([A-Z][a-z]+)', sentence)
            add_name_to_set(name, sirs)
        if 'Sirs ' in sentence:
            names = re.split('Sirs ', sentence)[1]
            names_list = re.findall('[A-Z][a-z]+', names)
            add_name_to_set(names_list, sirs)
    sirs.discard('Knight')
    sirs.discard('Knights')
    sirs.discard('Knave')
    sirs.discard('Knaves')
    return sirs


def print_sirs(sirs):
    print('The Sirs are: ', end='')
    print(" ".join(sorted(sirs)))


def add_val_to_list_val(_list_person, _val, person_binary):
    return_list = list()
    return_list.append(_list_person)
    return_list.append(_val)
    return_list.append(person_binary)
    return return_list


class SirQuote:
    name = ''
    type = ''
    persons = []
    knave_or_knight = Knave

    def __init__(self, name, type, quote):
        self.name = name
        self.type = type


def sir_quote(sentences, sirs):
    sir_quote_dict = defaultdict(list)
    for sentence in sentences:
        if '"' in sentence:
            quote = re.findall('"([^"]*)"', sentence)
            new_sentence = sentence.replace(quote[0], '')
            name = re.findall('Sir\\s([A-Z][a-z]+)', new_sentence)
            sir_quote_dict[name[0]] += quote
            print(name, " === ", quote)

    for name, quotes in sir_quote_dict.items():
        for quote in quotes:
            persons = []

    return sir_quote_dict


def main():
    content = read_from_file()
    sentences = cut2sentence(content)
    sirs = get_sirs(sentences)
    print_sirs(sirs)
    sir_quote_dict = sir_quote(sentences, sirs)


if __name__ == '__main__':
    main()
