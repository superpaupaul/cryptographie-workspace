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
    for i in range(len(primes)-1,0,-1):
        prime = primes[i]
        if prime != 1 and N%prime == 0:
            puissance = 1
            current = []
            while(sum_puissance(res) * (prime**puissance) <= N):
                current.append((prime,puissance))
                puissance += 1
            if len(current) > 0:
                res.append(current[-1])
        if(sum_puissance(res) == N):
            break
    return res

print(decomposition_primaire(20))

