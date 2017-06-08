# coding: utf-8


def remove_kigo(tokens):
    s = [".", ",", "!", "?", ";", ":", "(", ")", "[", "]", "'", '"']

    words = []
    for token in tokens:
        if token == "":
            continue
        if len(token) > 0:
            if token[0] in s:
                token = token[1:]
            if len(token) > 0:
                if token[-1] in s:
                    token = token[:-1]
        words.append(token)
    return words


import sys

with open("enwiki-20150112-400-r100-10576.txt") as f:
    for line in f.readlines():
        tokens = line[:-1].split(" ")
        tokens = remove_kigo(tokens)
        if len(tokens) > 0:
            for token in tokens:
                sys.stdout.write("{} ".format(token))
            sys.stdout.write("\n")
