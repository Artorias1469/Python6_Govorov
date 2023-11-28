#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    sentence = input("Введите предложение: ")

    letter_to_find = "п"

    words = sentence.split()

    found_word = None
    for word in words:

        if word.lower().startswith(letter_to_find.lower()):
            found_word = word
            break

    if found_word:
        print(f"Слово, начинающееся на букву '{letter_to_find}': {found_word}")
    else:
        print(f"В предложении нет слова, начинающегося на букву '{letter_to_find}'.")
