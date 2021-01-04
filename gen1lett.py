import random

abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","$"] #le dernier smbole signifie début ou fin de mot

with open("/home/titus/Programmation/Python/word-gen/mots.txt", "r", encoding="latin-1") as f:
    mots = f.readlines()

def lire(): #crée le tableau l
    l = [[0]*27 for i in range(27)]
    #l[i][j] correspond aux nombre de fois que dans le dico on trouve la lettre i suivie de la lettre j.
    #Si la lettre i est $, alors c'est la proba qu'un mot commence par la lettre j
    #Si la lettre j est $, alors c'est la proba que le mot se termine par la lettre i
    for mot in mots:
        prec = mot[0]
        
        if prec in abc: #on traite la première lettre
            i = abc.index(prec)
            l[26][i] += 1
            
        for lettre in mot[1:-2]: #on enlève le "\n" à lafin du mot et la première lettre qui a été traîtée
            lettre = lettre.lower()
            if lettre in abc and prec in abc: #on ne sauvegarde pas l'enchaînement s'il fait intervenir des lettres non reconnues
                j = abc.index(lettre)
                l[i][j] += 1
            i = j
            prec = lettre

        if prec in abc: #on traite la dernière lettre, dont la valeur est déjà enregistrée dans i
            l[i][26] += 1
    return l

#autre manière de faire, plus rapide mais un peu moins compréhensible:
def lirebis():
    l = [[0]*27 for i in range(27)]
    for mot in mots:
        motbis = "$" + mot[:-2] + "$" #on ajoute au mot (auquel on prend le soin d'enlever le \n à la fin) un $ de chaque côté pour signifier le début et la fin
        #les cas particuliers de début et de fin de mot se feront alors automatiquement!
        prec = "$"
        i = 26
        for lettre in motbis[1:]: #on commence à la deuième lettre du mot car la première est le $
            if lettre in abc and prec in abc: #on ne sauvegarde pas l'enchaînement s'il fait intervenir des lettres non reconnues
                j = abc.index(lettre)
                l[i][j] += 1
            i = j
            prec = lettre
    return l

def proba(l): #transforme le tableau l de lire() en un tableau des probabilités
    p = [[0]*27 for i in range(27)]
    #p[i][j] est la probabilité que la lettre i soit suivie de la lettre j
    for i in range(len(l)):
        total = sum(l[i]) #c'est le nombre de fois que la lettre i apparaît dans l'alphabet
        for j in range(len(l[0])):
            p[i][j] = l[i][j]/total
    return p

#bonus: création d'un mot aléatoire compte tenu de la probabilité de succession des lettres
import random
def suivant(p, prec):
    r = random.random()
    som = 0
    for j,i in enumerate(p[abc.index(prec)]): #cette boucle est une technique qui permet de tirer aléatoirement la lettre suivante avec la probabilité donnée dans p
        som += i
        if som >=r:
            break
    return abc[j]

def gen(p):
    mot = ""
    lettre = suivant(p, "$")
    while lettre != "$":
        mot += lettre
        lettre = suivant(p, lettre)
    return mot

def suivantplusprobable(p, prec):
    l = p[abc.index(prec)]
    return abc[l.index(max(l))]

def plusprobable(p):
    mot = ""
    lettre = suivantplusprobable(p, "$")
    while lettre != "$":
        mot += lettre
        lettre = suivantplusprobable(p, lettre)
        print(lettre, end = "")
    return mot


p = lirebis()
gen(p)
