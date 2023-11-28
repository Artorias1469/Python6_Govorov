#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def matching_initial_letters(word1, word2):
    min_length = min(len(word1), len(word2))
    count = 0

    for i in range(min_length):
        if word1[i] == word2[i]:
            count += 1
        else:
            break

    return count

if __name__ == "__main__":
    word1 = input("Первое слово: ")
    word2 = input("Второе слово: ")

    result = matching_initial_letters(word1, word2)

    if result == 0:
        print("The words are different, initial letters do not match.")
    else:
        print(f"Number of matching initial letters: {result}")
