#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from colorama import Fore,init,Style

init(autoreset=True)

r = Fore.RED + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
w = Fore.WHITE + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT

def about():
    print(g + "[" + w + "+"+ g + "] " + y + "Version" + r + " => " + y + "1.0")
    print(g + "[" + w + "+"+ g + "] " + y + "URL" + r + " => " + y + "https://github.com/into-0/imitate")
