#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from colorama import Fore,init,Style

init(autoreset=True)

r = Fore.RED + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
w = Fore.WHITE + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT


def NI(x,b): #定义求x关于b的逆元的函数NI,其中(NI(x,b)*x) mod b = 1 当x和b互质时求出的逆元唯一
  i = 1
  while (x*i)%b != 1:
    i = i + 1
  return i

def affine():
  d = input(r + "[" + c + "~"+ r + "] " + g + "Please enter ciphertext" + w + " ➜  " + y + "")
  C = []

  #对密文进行预处理并储存在列表中,储存形式是对应字母在26个英文字母中的位序
  for i in d:
    if i == ' ':
      C.append(i)
    else:
      C.append(ord(i)-65)

  #将加密算法中a可能的取值储存在列表中
  a = [3,5,7,9,11,15,17,19,21,23,25]
  P = []

  for keyb in range(0,26):
    for keya in a:
      ni_a = NI(keya,26)
      for s in C:
        if s == ' ':
          P.append(' ')
        else:
          P.append(((s-keyb)*ni_a)%26) #将明文字母对应的位次码依次加入到明文列表中
      strP = ''
      for t in P:
        if t==' ':
          strP = strP + ' '
        else:
          strP = strP + chr(t+97) #将明文转化为字符串并输出
      print(g + "[" + w + "+"+ g + "] " + y + "Clear text is ",strP)
      P = []