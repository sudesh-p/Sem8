alpha = 'abcdefghijklmnopqrstuvwxyz' #String with all chars

final = ''
myinput = input("Enter a String: ")
key = int(input("Enter Value of Key: "))
myinput = myinput.lower()
for x in myinput:
    if(x in alpha):
        pos = alpha.find(x)
        pos = (pos+key)%26
        final+=(alpha[pos])
    else:
        final+=x
print(final)

print("DECRYPTION PHASE")

encinput = input("Enter Encrypted String: ")
enckey = int(input("Enter Value of Key: "))
encinput = encinput.lower()
final2=''
for y in encinput:
    if(y in alpha):
        posn = alpha.find(y)
        posn = (posn-enckey)%26
        final2+=(alpha[posn])
    else:
        final2+=y

print(final2)