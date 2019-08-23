#-*- coding: utf-8 -*-
import random

def get_names(file_path):
    with open(file_path) as f:
        names = f.read().split(',')
        return names


def last_names():
    return get_names('./last_name.txt')


def first_names():
    return get_names('./first_name.txt')


def generate_name(first_names, last_names):
    last_name = random.choice(last_names)
    first_name = random.choice(first_names)
    first_name += random.choice(first_names)
    full_name = last_name + first_name
    return (first_name, last_name, full_name)


def generate_mobile():
    provider_nums = [131, 130, 182, 187, 180, 159]
    tail_nums = random.randint(0, 100000000)
    return "{}{:08d}".format(random.choice(provider_nums), tail_nums)


def generate_vcard(first_name, last_name, full_name):
    template_str = \
'''\
BEGIN:VCARD
VERSION:4.0
N;CHARSET=UTF-8:{};{};;;
FN;CHARSET=UTF-8:{}
TEL;type=HOME:{}
END:VCARD\
'''
    return template_str.format(first_name, last_name, full_name, generate_mobile())


if __name__ == "__main__":
    last_names = last_names()
    first_names = first_names()
    with open('demo.vcf', 'w') as f:
        for i in range(0, 2000):
            vcard = generate_vcard(*generate_name(first_names, last_names)) 
            f.write(vcard)
