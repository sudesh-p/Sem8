import socket
import random
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8584))
msg1=s.recv(2048)
x,y,n,B_pubx,B_puby=msg1.decode().split()
x=int(x)
y=int(y)
G=(x,y)
n=int(n)
B_pubx=int(B_pubx)
B_puby=int(B_puby)
B_pub=(B_pubx,B_puby)
a_pri=random.randint(1,n)
A_pub=(a_pri*x,a_pri*y)
msg2=str(A_pub[0])+' '+str(A_pub[1])
s.send(msg2.encode())

print('Alice\'s private key: ',a_pri)
print('Alice\'s public key: ',A_pub)
print('Bob\'s public key: ',B_pub) 
print('Generator: ',G)
msg3=s.recv(2048)
msg3=msg3.decode()
cipher1,cipher2=msg3.split()
cipher1=int(cipher1)
cipher2=int(cipher2)

print('ciphertext: ',cipher1,' ',cipher2)
temp=a_pri*(cipher1)
text=cipher2-temp

print("Message Received: " +str(text))

s.close()
