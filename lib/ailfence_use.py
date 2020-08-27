#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from colorama import Fore,init,Style

init(autoreset=True)

r = Fore.RED + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
w = Fore.WHITE + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT


def ailfence():
    string = input(r + "[" + c + "~"+ r + "] " + g + "Please enter ciphertext" + w + " ➜  " + y + "")
    frequency = [] # 获得栅栏的栏数
    result_len = len(string)        # 栅栏密码的总长度  25
    for i in range(2, result_len):   # 最小栅栏长度为2   逐个测试2,3,4....
        if(result_len % i == 0):        # 当栅栏密码的总长度 模 i 余数为0  则这个i就是栅栏密码的长度
            frequency.append(i)

    for numberOfColumn in frequency:   # 循环可能分的栏数
        RESULT = []                 #  保存各栏数的结果
        for i in range(numberOfColumn):     #   i : 开始取值的位置
            for j in range(i, result_len, numberOfColumn):  # 开始取值， 隔栏数取一个值， 起始位置是i
                RESULT.append(string[j])
        print(g + "[" + w + "+"+ g + "] " + y + "Clear text is " + w + "".join(RESULT))
