#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    input_sentence = input("Введите предложение: ")
    output_sentence = ''.join(char for char in input_sentence if char.lower() != 'с' and char.lower() != 'c')

    print("Исходное предложение:", input_sentence)
    print("Предложение без буквы 'с' и 'c':", output_sentence)

