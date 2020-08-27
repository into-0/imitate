#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from colorama import Fore,init,Style

init(autoreset=True)

r = Fore.RED + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
w = Fore.WHITE + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT

def pigpen():
    table = {
    'a':'j','b':'k','c':'l','d':'m','e':'n','f':'o','g':'p','h':'q','i':'r','j':'a','k':'b',
    'l':'c','m':'d','n':'e','o':'f','p':'g','q':'h','r':'i','s':'w','t':'x','u':'y','v':'z',
    'w':'s','x':'t','y':'u','z':'v','A':'J','B':'K','C':'L','D':'M','E':'N','F':'O','G':'P',
    'H':'Q','I':'R','J':'A','K':'B','L':'C','M':'D','N':'E','O':'F','P':'G','Q':'H','R':'I',
    'S':'W','T':'X','U':'Y','V':'Z','W':'S','X':'T','Y':'U','Z':'V'
    }

    data = input(r + "[" + c + "~"+ r + "] " + g + "Please enter ciphertext" + w + " ➜  " + y + "")

    new = ""
    for ch in data:
	    if ch.isalpha():
		    new += table[ch]
	    else:
		    new += ch  
    print(g + "[" + w + "+"+ g + "] " + y + "Clear text is " + w + new)