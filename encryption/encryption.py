#importing the libraries
import random as rnd
################################################################
#function to get the message from the user
response_type = input('Do you want to input a message or read from the text file? (msg\text) \n')

if response_type == 'msg':  
    message = input('Input your message and hit enter: \n')
elif response_type == 'txt':
    message = open("message.txt", "r").read()
else:
    raise ValueError('The response is invalid input (txt or msg)\n')
################################################################
#generate the encryption key
def keygen(message):
    key = []
    for word in message:
        key.append((rnd.randint(0, 128))) #range of asci characters
        
    #write the encrypted text file
    file1 = open('key.txt', 'w', encoding = "utf-8") 
    for i in key:
        file1.write(str(i))
        file1.write(', ')
    file1.close()
    
    return key
################################################################
#function to encrypt the message with xor cipher
def encyption(message, key):
    hash_pile = []
    enc_message = []   
    for word in message:
        binary = (ord(word))
        hash_pile.append(binary)
    for i in range(0, len(key)):
        enc_message.append(hash_pile[i] ^ key[i])
        
    #print the encrypted message
    encrypted = ''.join(chr(characters) for characters in enc_message)
    print('Your message is encrypted to : \n', encrypted)
    
    #write the encrypted text file
    file2 = open('encrypted.txt', 'w', encoding = "utf-8") 
    file2.write(encrypted)
    file2.close()
    return enc_message
################################################################
#function to decrypt the message
def decrypt(enc_message, key):
    dec_message = []
    for i in range(0, len(key)):    
        dec_message.append(enc_message[i] ^ key[i])
    
    #print the decrypted message 
    decrypted = ''.join(chr(characters) for characters in dec_message)
    print('Your message is decrypted to : \n', decrypted)
    
    #write the encrypted text file
    file3 = open('decrypted.txt', 'w', encoding = "utf-8") 
    file3.write(decrypted)
    file3.close()
    
    return decrypted
################################################################
#generate the key
key = keygen(message)
#encrypt the message with the key
enc_message = encyption(message, key)
################################################################
#ask user for password for the decription
premission = input('Do you want to decrypt the message?(y/n) \n')
   
if premission == 'n':
    exit
elif premission == 'y':
    password = input('Enter the user password: \n')
    
    try:
        val = int(password)
    except ValueError:
        print("That's not an int!")
   
    if val == 12345:
        dec_message = decrypt(enc_message, key)
    else:
        print('The password is incorrect please try again \n')
else:
    raise ValueError('The character enter is invalid please try again \n')

################################################################
    