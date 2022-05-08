def gcd(a,b): 
    if b==0: 
        return a 
    else: 
        return gcd(b,a%b) 
        
p = int(input('Enter the value of p = ')) 
q = int(input('Enter the value of q = ')) 
pt = input('Enter the value of text = ')



n = p*q 
t = (p-1)*(q-1) 

for e in range(2,t): 
	if gcd(e,t)== 1: 
		break
        
print("e:",e)     


  
for d in range(1,t):
	if e*d%t==1:
		break       
print("d:",d)        

l=[]  
s1=""      
for i in pt:
	ctt =pow(ord(i),e) 
	ct = ctt % n 
	l.append(ct)
  
for j in range(len(l)):
	dtt = pow(l[j],d) 
	dt = dtt % n 
	s1+=chr(dt)



print("Plain Text",pt)
print("Cipher Text",l)
print("Original Text",s1)
