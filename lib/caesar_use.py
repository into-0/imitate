#!/usr/bin/env python3
# -*- encoding: utf-8 -*-i

import string
from colorama import Fore,init,Style

init(autoreset=True)

r = Fore.RED + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
w = Fore.WHITE + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT

def caesar():
    inputStr = input(r + "[" + c + "~"+ r + "] " + g + "Please enter ciphertext" + w + " ➜  " + y + "").lower()
    caseS1 = string.ascii_lowercase * 2
    # caseS1 = string.ascii_uppercase * 2

    for j in range(26):
        result_list = []
        for i, num in zip(inputStr, range(len(inputStr))):
            status = caseS1.find(i)
            if status != -1:
                result_list.append(caseS1[status + j])
            else:
                result_list.append(inputStr[num])
        print(g + "[" + w + "+"+ g + "] " + y + "Key #{}: ".format(j),w + "".join(result_list))