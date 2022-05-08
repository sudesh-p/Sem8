p = int(input("Enter modulo(p): "))
g = int(input("Enter primitive root of "+str(p)+": "))
a = int(input("Choose 1st secret no(Alice): "))
b = int(input("Choose 2nd secret no(Bob): "))

A = (g**a)%p
B = (g**b)%p

S_A = (B**a)%p
S_B = (A**b)%p

if(S_A == S_B):
    print("Alice and Bob can communicate with each other!!!")
    print("They share a secret no = ", S_A)
else:
    print("Alice and Bob cannot communicate with each other!!!")