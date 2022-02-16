def vernam(message,key):
    res = []
    for i in range(len(message)):
        res.append(message[i] ^ key[i%len(key)])
    return res

# print(vernam([1,1,0,1,1,0,1,0],[0,1,1]))

def decomposition_primaire(N):
    return