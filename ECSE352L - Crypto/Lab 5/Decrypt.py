#rsa decryption
class Decrypt:
    def __init__(self, key):
        self.d = key[0]
        self.n = key[1]

    def getDecrypted(self, text):
        print(text)
        text = text.split(' ')
        dec = ''
        for i in text:
            if i != '':
                dec+=chr(pow(int(i), self.d, self.n))
        return dec