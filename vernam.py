import math


def vernam(message,key):
    res = []
    for i in range(len(message)):
        res.append(message[i] ^ key[i%len(key)])
    return res

# print(vernam([1,1,0,1,1,0,1,0],[0,1,1]))

# def are_prime(n,v):
#     res = True
#     if n == 0 or v == 0:
#         return False
#     min = min(n,v)
#     max = max(n,v)
#     for i in range(min,1,-1):
#         if min % i == 0 and max % i == 0:
#             res = False
#             break
#     return res

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


# Fonction qui donne la somme des facteur avec leur puissance
def sum_puissance(n):
    res = 1
    for i in n:
        res *= i[0]**i[1]
    return res

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

# calculates indicateur d'euler de n 91 => 72; 20 =>  8
def calculate_phi(n):
    decomposition = decomposition_primaire(n)
    res = 1
    for c in decomposition:
        res *= (c[0]-1)* c[0]**(c[1]-1)
    return res

def calculate_euclide_etendu(a,b):
    r0 = a
    u0 = 1
    v0 = 0

    r1 = b
    u1 = 0
    v1 = 1

    while r1 != 0:
        q = (r0 / r1)
        (r0,u0,v0,r1,u1,v1) = (r1, u1, v1, r0 - q*r1, u0 - q*u1, v0 - q*v1)
    return r0,u0,v0

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

# calcule l'exponentiation modulaire de n^pow
def exponentiation_modulaire(n,pow,mod):
    puissances = decomposition_puissance_2(pow)
    res = 1
    for puissance in puissances:
        res *= n**puissance
        res = res % mod
    return res

def chiffrement_rsa(n,p,e,M):
    N = n*p
    phi = calculate_phi(N)
    d = calculate_euclide_etendu(e,phi)[0]
    M_prime = exponentiation_modulaire(M,e,N)
    M_prime_prime = exponentiation_modulaire(M_prime,d,N)
    return (M_prime,M_prime_prime)



print(chiffrement_rsa(101,103,7,10331))

print(calculate_euclide_etendu(7,10200))