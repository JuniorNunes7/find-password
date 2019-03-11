#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#### Find password
#
# @author Junior Nunes
##########################

IGNORED_NUMBERS = []

def correct_placed(code, check_code, n):
    for i, value in enumerate(code):
        if value == check_code[i]:
            n -= 1

    return n == 0

def correct_number(code, check_code, num):
    for i, number in enumerate(check_code):
        if number in code and number != code[i]:
            num -= 1

    return num == 0

def check(code, tests):
    code = [int(i) for i in code]
    for test in tests:
        if not test['method'](code, test['code'], test['corrects']):
            return False
    
    return True

def get_password(tests):
    length = len(tests[0]['code'])
    max_repeat = 10 ** length
    pre = str(max_repeat)[-length:]

    for test in tests:
        if test['method'] == correct_number and test['corrects'] == 0:
            IGNORED_NUMBERS.extend(test['code'])

    for x in range(0, max_repeat):
        code = (pre + str(x))[-length:]

        if any(str(a) in code for a in IGNORED_NUMBERS):
            continue

        if check(code, tests):
            print "Possible password: " + code

# 042
get_password([
    {'code': [6, 8, 2], 'method': correct_placed, 'corrects': 1},
    {'code': [6, 1, 4], 'method': correct_number, 'corrects': 1},
    {'code': [2, 0, 6], 'method': correct_number, 'corrects': 2},
    {'code': [7, 3, 8], 'method': correct_number, 'corrects': 0},
    {'code': [7, 8, 0], 'method': correct_number, 'corrects': 1}
])

# 718
# get_password([
#     {'code': [5, 4, 8], 'method': correct_placed, 'corrects': 1},
#     {'code': [5, 3, 0], 'method': correct_number, 'corrects': 0},
#     {'code': [1, 5, 7], 'method': correct_number, 'corrects': 2},
#     {'code': [8, 0, 6], 'method': correct_number, 'corrects': 1},
#     {'code': [6, 4, 7], 'method': correct_number, 'corrects': 1}
# ])

# 281
# get_password([
#     {'code': [6, 3, 1], 'method': correct_placed, 'corrects': 1},
#     {'code': [7, 3, 0], 'method': correct_number, 'corrects': 0},
#     {'code': [1, 0, 2], 'method': correct_number, 'corrects': 2},
#     {'code': [6, 7, 8], 'method': correct_number, 'corrects': 1},
#     {'code': [0, 8, 7], 'method': correct_placed, 'corrects': 1}
# ])

# 682
# get_password([
#     {'code': [3, 4, 2], 'method': correct_placed, 'corrects': 1},
#     {'code': [4, 7, 3], 'method': correct_number, 'corrects': 0},
#     {'code': [1, 4, 6], 'method': correct_number, 'corrects': 1},
#     {'code': [0, 6, 9], 'method': correct_number, 'corrects': 1},
#     {'code': [8, 7, 6], 'method': correct_number, 'corrects': 2}
# ])
