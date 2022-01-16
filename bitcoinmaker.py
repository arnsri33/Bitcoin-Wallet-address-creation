#import bitcoin 

from bitcoin import *

#creation of the private key in bitcoin

PrivateKey = random_key()
print(PrivateKey)

#creation of the private key 

PublicKey = privtopub(PrivateKey)
print (PublicKey)

#creation of the bitcoin address

Address = pubtoaddr(PublicKey)
print (" The address created is" + Address)