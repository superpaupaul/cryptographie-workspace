import math

# prend un message en entrée sous forme de liste d'entiers 1 ou 0
# ainsi qu'une clé
# renvoie le message chiffré par vernam (XOR message - clé)
def vernam(message,key):
    res = []
    for i in range(len(message)):
        res.append(message[i] ^ key[i%len(key)])
    return res


def is_prime(n):
    res = True
    if n == 0:
        return False
    if n == 1:
        return True
    for i in range(2,int(n/2)+1):
        if n % i == 0:
            res = False
            break
    return res

def primes_list(n):
    res = []
    for i in range(1,n):
        if is_prime(i):
            res.append(i)
    return res

# Renvoie le tableau de tuples de nombres premiers composant N
def decomposition_primaire(N):
    res = []
    primes = primes_list(N)
    for prime in primes:
        if prime != 1 and N%prime == 0:
            puissance = 0
            while N % prime == 0:
                puissance += 1
                N = N / prime
            if puissance != 0:
                res.append((prime,puissance))
    return res

# calcule l'indicateur d'Euler phi
def calculate_phi(n):
    decomposition = decomposition_primaire(n)
    res = 1
    for c in decomposition:
        res *= (c[0]-1)* c[0]**(c[1]-1)
    return res

# retourne l'inverse de a modulo b
def euclide(a,b):
    r, u, v, rp, up, vp = a, 1, 0, b, 0, 1
    while rp != 0:
        q = r//rp   # // donne le reste de la division 
        r, u, v, rp, up, vp = rp, up, vp, r - q *rp, u - q*up, v - q*vp
    #print ("L'inverse de ", a, " modulo ", b, "est :", u%b)
    return (u%b)

# Décompose un nombre en une liste de ses puissances de 2
def decomposition_puissance_2(n):
    puissances2 = []
    res = []
    for i in range(n):
        puissance = 2**i
        if puissance > n:
            break
        else:
            puissances2.append(i)
    puissances2.reverse()
    courant = 0
    for puissance in puissances2:
        if 2**puissance + courant <= n:
            res.append(2**puissance)
            courant += 2**puissance
    return res

# calcule l'exponentiation modulaire de n puissance pow modulo mod => en gros calcule juste le reste de la division euclidienne
def exponentiation_modulaire(n,pow,mod):
    puissances = decomposition_puissance_2(pow)
    res = 1
    for puissance in puissances:
        res *= n**puissance
        res = res % mod
    return res

# Renvoie le message chiffré et le message chiffré 2x (initial)
def chiffrement_rsa(n,p,e,M):
    N = n*p
    phi = calculate_phi(N)
    d = euclide(e,phi)
    M_prime = exponentiation_modulaire(M,e,N)
    M_prime_prime = exponentiation_modulaire(M_prime,d,N)
    return (M_prime,M_prime_prime)


#print(vernam([1,0,0,1,0,0,1,1,1,0,0],[1,1,0]))
#print(decomposition_puissance_2(50))
n = 101
p = 103
e = 7
M = 10331
print(chiffrement_rsa(n,p,e,M))