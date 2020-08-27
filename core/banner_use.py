#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from colorama import Fore,init,Style

init(autoreset=True)

r = Fore.RED + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
w = Fore.WHITE + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT

def banner():
    print(y + " ____  __  __  ____  ____   __   ____  ____") 
    print(y + "(_  _)(  \/  )(_  _)(_  _) /__\ (_  _)( ___)")
    print(c + " _)(_  )    (  _)(_   )(  /(__)\  )(   )__) ")
    print(r + "(____)(_/\/\_)(____) (__)(__)(__)(__) (____)")
    print()
    print(g + "[" + w + "+"+ g + "] " + y + "Used to crack cryptography in ctf")
    print()
