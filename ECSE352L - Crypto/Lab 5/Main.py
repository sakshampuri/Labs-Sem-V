from public_private_keygen import KeyGen
from Decrypt import Decrypt
from Encrypt import Encrypt

if __name__ == '__main__':
    Generator = KeyGen(1024)
    publicKey, privateKey = Generator.getKeys()
    print(f'''
    Public Key: {publicKey}
    Length of Public Key: {len(str(publicKey[0]))}
    Private Key: {privateKey}
    Length of Private Key: {len(str(privateKey[0]))}
    ''')
    t = str(input('Enter text to encrypt\n'))
    encryptor = Encrypt(publicKey)
    decryptor = Decrypt(privateKey)
    enText = encryptor.getEncryptedText(t)
    print('Encrypted text: ', enText)
    deText = decryptor.getDecrypted(enText)
    print('Decrypted Text: ', deText)
