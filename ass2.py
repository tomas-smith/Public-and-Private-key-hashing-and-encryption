import random as rnd
import binascii
#global values for modulus
m1 = [2,147,483,642]
m2 = [2,147,483,423]
#global values for the diffel-hellman algorithm
q = 353
a = 3

#selects randomly a number from the given list
def rng(m):
    seed = rnd.choice(m)

    return seed

#calculates the combined Linear Cong
def clg():

    #initializing y values
    y1 = 0
    y2 = 0

    m_range1 = [1,2,147,483,642]
    m_range2 = [1,2,147,483,423]
    #multiplier values are the static and not changing.
    a1 = 450
    a2 = 234

    #randomly selects from the list of mods
    mod1 = rng(m1)
    mod2 = rng(m1)
    
    n = 2 
    
    



    #initializing initial Y values(from [1,2,147,483,642/423])
    y1 = rnd.choice(m_range1)

    y2 = rnd.choice(m_range2)
    

    for i in range(1, n):
        #counting y values
        y1 = (a1 * y1) % mod1
        y2 = (a2 * y2) % mod2
        #getting values for x
        x = (y1 - y2) % (mod1- 1)
        
    return x
    


def DiffieHellman():
    #getting results from part A) 
    AprivateKey = clg()
    BprivateKey = clg()


    print("the clg for A is ",AprivateKey)
    print("the clg for B is ",BprivateKey)


    #getting public key values
    ApublicKey = a**AprivateKey % q
    BpublicKey = a**BprivateKey % q

    #calculating shared secret (both will be the same)
    AsharedSecret = BpublicKey**AprivateKey % q
    BsharedSecret = ApublicKey**BprivateKey % q
    print("The secret key for A is: ", AsharedSecret)
    print("The secret key for A is: ", AsharedSecret)

    #converting values into string to use in part B)
    UniversalSecret=str(AsharedSecret)

        
    return UniversalSecret

  


#Converts text into binary 
def Text_to_binary ():
    #opens file
    file = open("test.txt", "r")
    stream = file.read()
    file.close()
    #this value is used to generate a 64 bit block, since every character in acsii is 8 bites. 8*4 = 64
    n = 4

    #couple every 4 characters in the text (spaces included)
    chunk = [stream[i:i+n]for i in range (0, len(stream),n)]
    
    #reserve the lat bit for RC4
    last_bit =chunk[-1]
    #delete it, since it will be added later on
    del chunk[-1]
    
    fixed = " ".join(chunk)

    
    #convert the whole text into binary in a set of 4 characters
    y = ' '.join(format(ord(z), 'b')for z in fixed)

    #return the text and the last bit
    return last_bit,y 



 
def S(key):
    #initialization
    keylength = len(key)
    S = list(range(256))
    #initial permutation of S
    j=0
    for i in range(256):
        j = (j+ S[i] + key[i%keylength]) %256
        #swapping values
        S[i], S[j] = S[j], S[i]
    return S

def stream_generation(S):
    i = 0
    j = 0
    
    while True:
        i = (i+1) % 256
        j = (j+S[i]) % 256
        #xoring values
        S[i], S[j] = S[j], S[i]
        t=S[(S[i]+S[j])%256]

        yield t

#converting key to binary
def covert_key(z):
    return [ord(c) for c in z]

#initialization of RC4
def RC4(self):
    s=S(key)
    return stream_generation(s)


def binary_to_text():
    last_bit,text = Text_to_binary()
    text.decode()
    data_b2a = binascii.b2a_uu(text)
    return data_b2a


#MAIN BODY



key= DiffieHellman()
last_bit,y = Text_to_binary()
print("the binary version of the txt file is: \n",y)


key=covert_key(key)

keystream = RC4(key)
#using sys print due to a need to ord the text, which would involve making
#a new def function for printing.
print("the 4RC encryption for part B is:")
import sys
for c in last_bit:
    sys.stdout.write("%02x" % (ord(c) ^ keystream.__next__()))
print



