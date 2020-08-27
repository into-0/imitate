#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from colorama import Fore,init,Style

init(autoreset=True)

r = Fore.RED + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
w = Fore.WHITE + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT
 
dict1 = {'a':'.-'  ,'b':'-...','c':'-.-.','d':'-.'  ,'e':'.'   ,
         'f':'..-.','g':'--.' ,'h':'....','i':'..'  ,'j':'.---',
         'k':'-.-' ,'l':'.-..','m':'--'  ,'n':'-.'  ,'o':'---' ,
         'p':'.--.','q':'--.-','r':'.-.' ,'s':'...' ,'t':'-'   ,
         'u':'..-' ,'v':'...-','w':'.--' ,'x':'-..-','y':'-.--','z':'--..',
         '0':'-----' ,'1':'.----' ,'2':'..---' ,'3': '...--','4': '....-' ,
         '5': '.....','6': '-....','7': '--...','8': '---..','9': '----.' }

# dict of morse2words
dict2 = dict(zip(dict1.values(),dict1.keys()))

def morse():
    codes = input(r + "[" + c + "~"+ r + "] " + g + "Please enter ciphertext" + w + " ➜  " + y + "").strip().split(" ")
    print(g + "[" + w + "+"+ g + "] " + y + "Clear text: " + w + "")
    for sign in codes:
        if sign == '/':
            print(' ',end='')
        else:
            print(dict2[sign], end = "")


