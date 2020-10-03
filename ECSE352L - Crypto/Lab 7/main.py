#first generating the public, private key set
from public_private_keygen import KeyGen
from Decrypt import Decrypt
from Encrypt import Encrypt

if __name__=='__main__':

    #initialzing a 1024 bit key generator
    Generator = KeyGen(1024)

    #public and private key
    publicKey, privateKey = Generator.getKeys()
    print(f'''
    Public Key is: {publicKey}
    Private Key is: {privateKey}
    ''')

    #initializing the encryptor and decryptor with public and private keys
    encryptor = Encrypt(privateKey) #using private key to encrypt which is only availaible to the home agent
    decryptor = Decrypt(publicKey) #this public key is used to decrypt which is availaible to anyone

    #taking input of the message
    message = str(input('Enter the message to sign\n'))
    #hashing the message
    hashed_message = str(hash(message))

    #encrypting the hashed message
    encrypted_hashed_message = encryptor.getEncryptedText(hashed_message)

    print(f'''
    The message that is sending is this: {message}
    The digital signature is as follows: {encrypted_hashed_message}
    This signature can be decrypted with public key and the message can be hashed and compared with the decrypted result to verify the authencity
    ''')

    #the message along with encrypted hash message is sent
    #now to simulate this, since message is already availaible we're just calculating the decrypted and comparing hashes
    decrypted_hash_message = decryptor.getDecrypted(encrypted_hashed_message)

    print(f'''
    The decrypted message (hash value) is as follows: {decrypted_hash_message}
    The original hash value: {hashed_message}
    Is it verified: {decrypted_hash_message == hashed_message}
    ''')



