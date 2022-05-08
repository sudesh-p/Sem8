import socket
import math
import random
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.bind(('127.0.0.1',8584))
ss.listen(1)
c,addr=ss.accept()
a=int(input("enter the value of a: "))
b=int(input('enter the value of b: '))
n=int(input('enter the value of n: '))

if( ((4*(a**3))+(27*(b**2)))==0):
	print("Special Condition Encountered. Enter Other values of a,b,n: ")
	exit(1)
	
x=1
while True:
	y=math.sqrt(x**3+(a*x)+b)
	if y.is_integer():
		break
	x=x+1
y=int(y)
G=(x,y)
b_pri=random.randint(1,n)
B_pub=(b_pri*x,b_pri*y)
print('Bob\'s private key: ',b_pri)
print('Bob\'s public key: ', B_pub)


msg1=str(x)+' '+str(y)+' '+str(n)+' '+str(B_pub[0])+' ' +str(B_pub[1])
c.send(msg1.encode())

msg2=c.recv(2048)
A_pub0,A_pub1=msg2.decode().split()
A_pub0=int(A_pub0)
A_pub1=int(A_pub1)
A_pub=(A_pub0,A_pub1)
print('Alice\'s public key: ',A_pub)
print('Generator: ',G)
m=int(input("Enter the plaintext integer: "))
k=random.randint(1,n)

cipher1=k*(G[0]+G[1])
cipher2=m+k*(A_pub[0]+A_pub[1])
print('Ciphertext: ',cipher1,' ',cipher2)
msg3=str(cipher1)+' '+str(cipher2)
c.send(msg3.encode())






ss.close()


