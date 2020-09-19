
import sympy
import random


class KeyGen:

    '''
        This class has methods to generate both the public and private key for asymmetric
        encryption. The standard used for the calculation is as follows:

        	Generate two large random primes, p and q
        	Compute n=pxq
        	Compute ϕ=(p−1)(q−1)
        	Choose an integer e, 1<e<ϕ, such that gcd(e,ϕ)=1
        	Compute the secret exponent d, 1<d<ϕ, such that ed≡1modϕ
        	The public key= (e, n)
        	The private key (d, n)

    '''

    e = None

    def __init__(self, bits):
        self.bits = bits
        self.p, self.q = sympy.randprime(
            2**(bits-1), 2**bits), sympy.randprime(2**(bits-1), 2**bits)
        self.n = self.p*self.q
        self.fi = (self.p-1)*(self.q-1)
        self.puK = self.getPublicKey()
        self.prK = self.getPrivateKey()

    def getKeys(self):
        return self.puK, self.prK

    def getPublicKey(self):
        # public key is (e, n)

        # computing all e's s.t gcd(e,fi)=1
        # taking out a random e
        while True:
            randNum = random.randrange(2**(self.bits-1), 2**self.bits)
            if self.gcd(randNum, self.fi) == 1:
                self.e = randNum
                break

        # returning the public key
        return (self.e, self.n)

    def getPrivateKey(self):
        # private key is (d, n)
        assert self.e != None, 'Generate Public Key First'

        # calculating 'd'
        d = self.findModInverse(self.e, self.fi)
        # returning private key
        return (d, self.n)

    def gcd(self, a, b):
        while a != 0:
            a, b = b % a, a
        return b

    def findModInverse(self, a, m):
        if self.gcd(a, m) != 1:
            return None
        u1, u2, u3 = 1, 0, a
        v1, v2, v3 = 0, 1, m

        while v3 != 0:
            q = u3 // v3
            v1, v2, v3, u1, u2, u3 = (
                u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

        return u1 % m


if __name__ == '__main__':
    Generator = KeyGen(1024)
    publicKey, privateKey = Generator.getKeys()
    print(f'''
    Public Key: {publicKey}
    Length of Public Key: {len(str(publicKey[0]))}
    Private Key: {privateKey}
    Length of Private Key: {len(str(privateKey[0]))}
    ''')
