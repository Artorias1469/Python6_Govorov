#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    user_input = input("Введите слово: ")
    stars = '*' * len(user_input)
    result_string = stars + user_input + stars
    print(result_string)
