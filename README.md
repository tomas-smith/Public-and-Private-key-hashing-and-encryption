# Public and Private key hashing and encryption
 A python script that with the combination of multiple parts(Combined Linear Congruntial Generator, Diffie-Hellman algorithm, R4C is able to make public private keys for two users, encript them, and also transform any provided text into a binary encryption and from it.


Description:

The code is comprised of multiple functions that in combination allows to generate the secret and private keys. 

The code's functions are:

rng:
that selectes randomly from a array a number and stores it, applying the Combined Linear Congruntial generator formula. https://en.wikipedia.org/wiki/Combined_linear_congruential_generator

clg:
the calculations for the combined Linear Congruntial, with the variables (y, m, a, mod) representing the values within the formula.

DiffieHellman:
Applying the values from the clg() function, it generates two G keys for two users, and with the application of the key exchange (https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange), 
it generates a public key shares between user A and user B, and private keys for both users for later on key exchanges, whiles keeping relation between the different keys.

Text_to_binary:
This function opens a text file, ecnripts it in generating 64 bit blocks, with the last one not ecnrypted, and sent to R4C with the secret key for Diffie-Hellman key exchange.

S,stream_generation,covert_key:
encrypts the plaintext, swapping bytes of the text accordingly to the array and applying XOR'ing rules of encryption.

R4C:
applies the encryption from the S functions, whiles using the last plaintext bit of text with the secret key to encrypt the data.

binary_to_text:
transforms the binary text, applying the last bit of text and applying the the last un-encrypted data to decypher it.


Main body:

initialized the functions and executes the functions in according manner. 



This code was written in Python 3.7, using only the binascii library for encryption. Future updates would involve a more randomly selected encryption variants, with possibilities to insert personal data values. 
