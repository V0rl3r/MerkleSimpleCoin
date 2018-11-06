import signEncrypt as se
import hashlib

class Transaction:
    #***
    #WHERE DO I CHECK VALIDITY OF AMOUNT
    #What is used to sign - private key of sender?
    #***
    def __init__(self, amt, origID, destID, origPrKey, tStamp):
        self.tStamp = tStamp
        self.signed = False
        self.destID = destID
        self.amtToAdd = amt
        self.origID = origID
        self.hash = None
        if not origID is None:
            signed = True
            self.genHash(self)
            self.hash = se.enanddecrypt(0, self.hash, origPrKey)

    def __repr__(self):
        return str(self.destID) + str(self.origID) + str(self.amtToAdd)

    def unsign(self, origPuKey):
        if self.signed:
            '''
            print("---------------------------")
            print(self.destID)
            print("---------------------------")
            print(origPuKey)
            print("---------------------------")
            '''
            #self.destID = se.enanddecrypt(1, self.destID, origPuKey)
            self.amtToAdd = se.enanddecrypt(1, self.amtToAdd, origPuKey)

    def verify(self):
        if amt >= 0:
            return True
        return False

    def genHash(self):
        sha = hashlib.sha256()
        sha.update(str(self.tStamp).encode())
        sha.update(str(self.destID).encode())
        sha.update(str(self.amtToAdd).encode())
        sha.update(str(self.origID).encode())
        self.hash = base64.b16encode(sha.digest()).decode()

#Should verify the Transaction
#Amount is greater than 0, sender has enough money
#Only signed when its not in a Block (recvID, amt)
