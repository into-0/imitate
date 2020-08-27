#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
from lib.affine_use import affine
from lib.ailfence_use import ailfence
from lib.caesar_use import caesar
from lib.morse_use import morse
from lib.pigpen_use import pigpen
from lib.rot13_use import rot13
from core.banner_use import banner
from core.about_use import about
from colorama import Fore,init,Style

init(autoreset=True)

r = Fore.RED + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
w = Fore.WHITE + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT

def main():
    banner()
    print(r + "[" + c + "1" + r + "] " + y + "affine              " + r + "[" + c + "2" + r + "] " + y + "ailfence")
    print(r + "[" + c + "3" + r + "] " + y + "caesar              " + r + "[" + c + "4" + r + "] " + y + "morse")
    print(r + "[" + c + "5" + r + "] " + y + "pigpen              " + r + "[" + c + "6" + r + "] " + y + "rot13")
    print(r + "[" + c + "0" + r + "] " + y + "about               " + r + "[" + c + "x" + r + "] " + y + "exit")
    print()
    ask = input(r + "[" + c + "~"+ r + "] " + g + "Please enter serial number" + w + " ➜  " + y + "")
    if (ask == "1"):
        affine()
    elif (ask == "2"):
        ailfence()
    elif (ask == "3"):
        caesar()
    elif (ask == "4"):
        morse()
    elif (ask == "5"):
        pigpen()
    elif (ask == "6"):
        rot13()
    elif (ask == "0"):
        about()
    elif (ask == "x"):
        sys.exit(0)
    else:
        print(r + "[" + w + "Error" + r + "] " + g + "It will exit for you soon")
        sys.exit(3)
