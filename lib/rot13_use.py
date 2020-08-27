#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import string
from colorama import Fore,init,Style

init(autoreset=True)

r = Fore.RED + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
w = Fore.WHITE + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT



def rot13():
    s1 = input(r + "[" + c + "~"+ r + "] " + g + "Please enter ciphertext" + w + " ➜  " + y + "")
    rot13_1 = string.ascii_lowercase[:13]
    rot13_2 = string.ascii_lowercase[13:]
    result = []
    for i in s1:
        find_1 = rot13_1.find(i.lower())
        if find_1 != -1:
            if i.isupper():
                result.append(rot13_2[find_1].upper())
                continue
            result.append(rot13_2[find_1])
        find_2 = rot13_2.find(i.lower())
        if find_2 != -1:
            if i.isupper():
                result.append(rot13_1[find_2].upper())
                continue
            result.append(rot13_1[find_2])
        if find_1 == -1 and find_2 == -1:
            result.append(i)
    
    print(g + "[" + w + "+"+ g + "] " + y + "Clear text is " + w + "". join(result))