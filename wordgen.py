import time
import random


LEN_PRE = 3


with open("french.txt", "r") as f:
    mots = f.readlines()


def co():
    k=1
    long = len(mots)
    l = {}
    for mot in mots:
        pre = "%"*LEN_PRE
        for letter in mot:
            letter = letter.lower()
            if letter == '%': continue
            if not pre in l:
                l[pre] = {}
            if not letter in l[pre]:
                l[pre][letter] = 1
            else:
                l[pre][letter] += 1
            pre = pre[1:]+letter
        k += 1
        if k%10000 == 0:
            print(format(round(k/long*100,2)), "%")
    for key in l:
        som = sum(l[key].values())
        for subkey in l[key]:
            l[key][subkey] /= som
    return l


def next(pre):
    k = l[pre]
    r = random.random()
    som = 0
    for key,val in k.items():
        som += val
        if som > r:
            break
    return key


def gen():
    pre = "%"*LEN_PRE
    letter = next(pre)
    mot  = ""
    while letter!= "\n":
        mot += letter
        pre = pre[1:]+letter
        letter = next(pre)
    return mot


def prob(pro, word):
    pre = "%"*LEN_PRE
    p = 1
    for i in word+"\n":
        if i in pro[pre]:
            p*=pro[pre][i]
        else:
            return 0
        pre = pre[1:]+i
    return p**(1/len(word+"\n"))


if __name__ == '__main__':
    l = co()
