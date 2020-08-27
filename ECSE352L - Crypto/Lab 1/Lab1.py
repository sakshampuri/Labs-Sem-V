#QUESTION 1
# Implementation of Caesar cipher encryption and decryption using a key


a =int(input(("Select 1: To Encrypt \nSelect 2: To Decrypt\n\n=>")))
Message=input("Enter Message: ")
Key=int(input("Enter Key: "))
output = ""
if a == 1:
  for i in range(len(Message)):
    output = output + (str(chr(ord(Message[i])+Key)))
if a == 2:
  for i in range(len(Message)):
    output = output + (str(chr(ord(Message[i])-Key)))
print(output)








#QUESTION 2
# Write a code to generate cryptographic nonce

import random
print("10 cryptographic nonce in the range [1, 10000]\n\n\n")
for i in range(0,10,1):
  print("Nonce" ,i+1,": ",random.randint(1, 10000))