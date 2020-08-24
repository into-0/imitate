import click
import string

def NI(x,b): #定义求x关于b的逆元的函数NI,其中(NI(x,b)*x) mod b = 1 当x和b互质时求出的逆元唯一
  i = 1
  while (x*i)%b != 1:
    i = i + 1
  return i

@click.command()
@click.option("-r","--rot13",required=True,help = "Cracking rot13 cipher.")

def rot13pd(rot13):
    '''Used to crack rot13 cipher in ctf'''
    s1 = f"{rot13}"
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
    
    print("". join(result))
if __name__ == "__main__":
    rot13pd()
