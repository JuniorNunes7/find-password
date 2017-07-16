#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#### Find password
#
# @author Junior Nunes
##########################

checkedNumbers = []

def correctPlaced(code, checkCode, n):
    global checkedNumbers
    for i in range(len(code)):
        if(code[i] == checkCode[i]):
            checkedNumbers.append([code[i], i])
            n -= 1

    return n == 0

def correctNumber(code, checkCode, n):
    for i, number in enumerate(checkCode):
        if(number in code and number != code[i]):
            if([number, i] in checkedNumbers):
                return False
            n -= 1

    return n == 0

def check5(code):
    checkCode = [7,8,0]
    return correctNumber(code, checkCode, 1)

def check4(code):
    checkCode = [7,3,8]
    return check5(code) if correctNumber(code, checkCode, 0) else False

def check3(code):
    checkCode = [2,0,6]
    return check4(code) if correctNumber(code, checkCode, 2) else False

def check2(code):
    checkCode = [6,1,4]
    return check3(code) if correctNumber(code, checkCode, 1) else False

def check1(code):
    checkCode = [6,8,2]
    return check2(code) if correctPlaced(code, checkCode, 1) else False

def check(code):
    code = [int(i) for i in code]
    return check1(code)

def generateCode(length):
    global checkedNumbers
    maxRepeat = 10**length;
    pre = str(maxRepeat)[-length:]

    for x in range(0, maxRepeat):
        checkedNumbers = []
        code = (pre + str(x))[-length:]
        if(check(code)):
            print("A senha é: " + code);

generateCode(3)
