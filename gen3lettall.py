import time
import random
f = open("/home/titus/Programmation/Python/word-gen/german.txt", "r", encoding='latin-1')
mots = f.readlines()

def co():
    k=1
    long = len(mots)
    l = {}
    for mot in mots:
        prec1 = "nil"
        prec2 = "nil"
        prec3 = "nil"
        for letter in mot:
            letter = letter.lower()
            try:
                try:
                    try:
                        try:
                            l[prec3][prec2][prec1][letter] += 1
                        except KeyError:
                            l[prec3][prec2][prec1][letter] = 1
                    except KeyError:
                        l[prec3][prec2][prec1] = {letter:1}
                except KeyError:
                    l[prec3][prec2] = {prec1:{letter:1}}
            except KeyError:
                l[prec3] = {prec2:{prec1:{letter:1}}}
            prec3 = prec2
            prec2 = prec1
            prec1 = letter
        k += 1
        if k%10000 == 0:
            print("{0} %".format(round(k/long*100,2)))
    return l
    
def pro(l):
    for prec3 in l:
        for prec2 in l[prec3]:
            for prec1 in l[prec3][prec2]:
                som = 0
                for nb in l[prec3][prec2][prec1]:
                    som += l[prec3][prec2][prec1][nb]
                for nb in l[prec3][prec2][prec1]:
                    l[prec3][prec2][prec1][nb] /= som
    return l
    
try:
    a = l
except:
    l = pro(co())
    
def next(prec3,prec2,prec1):
    k = l[prec3][prec2][prec1]
    r = random.random()
    lis = list(k.keys())
    long = len(lis)
    sum = 0
    n = 0
    while sum<r:
        sum += k[lis[n]]
        n += 1
    n -= 1
    return lis[n]

def gen():
    prec1 = "nil"
    prec2 = "nil"
    prec3 = "nil"
    letter = next(prec3,prec2,prec1)
    mot  = ""
    while letter!= "\n":
        mot += letter
        prec3 = prec2
        prec2 = prec1
        prec1 = letter
        letter = next(prec3,prec2,prec1)
    return mot

def t():
    for i in range(2000):
        print(gen(),end=" ")
        
while True:
    print(gen())
    time.sleep(0.5)
