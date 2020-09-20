#implementing encryption using the RSA public key
class Encrypt:
    '''
        This class should receive a public key as input following which
        the encryption function will encrypt text using that.

        The public key provided SHOULD NOT be base64 encoded as public_private_keygen.py
        does not encode in base64 limited to the scope of Computer Networks course Assignemnt.

        Format of the key SHOULD be 

        Encryption Process (Sender): 
            •	Use public key (e, n) 
            •	Represents the plaintext message as a positive integer m with 1<m<n 
            •	Computes the ciphertext C=Me mod n 
            •	Sends the ciphertext C to the destination B.

    '''

    def __init__(self, key):
        #since public key is vastly greater than n
        assert len(str(key[0])) <= len(str(key[1])) , 'Incorrect Format of the key. Make sure it is in the format of (e,n)' 
        self.e = key[0]
        self.n = key[1]
    
    def getEncryptedText(self, text):
        '''
            Formula used to encrypt is as follows:
                C = M^e mod n
        '''

        #first we'll encode the plain text
        text = [ord(c) for c in text]

        #now we'll encrypt
        enc = ''
        for m in text:
            enc+=str(pow(m,self.e,self.n))+' '
        return enc
        
