import numpy as np
from egcd import egcd
def matrix_mod_inv(matrix, modulus):
	det = int(np.round(np.linalg.det(matrix)))  # Step 1)
	det_inv = egcd(det, modulus)[1] % modulus  # Step 2)
	matrix_modulus_inv = (
			det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
	)  # Step 3)

	return matrix_modulus_inv

keyMatrix = [[0] * 3 for i in range(3)]
messageVector = [[0] for i in range(3)]
cipherMatrix = [[0] for i in range(3)]
messMatrix = [[0] for i in range(3)]
message = input("Enter plain text of 3 characters : ")
key = input("Enter key of 9 characters : ")
k = 0
for i in range(3):
	for j in range(3):
		keyMatrix[i][j] = ord(key[k]) % 65
		k += 1


for i in range(3):
	messageVector[i][0] = ord(message[i]) % 65
cip = ''
for i in range(3):
		for j in range(3):
			cipherMatrix[i][0] += (keyMatrix[i][j] *
								   messageVector[j][0])
		cipherMatrix[i][0] = cipherMatrix[i][0] % 26
		cip = cip + chr(cipherMatrix[i][0] + 65)
print(cip)

inv_mat = matrix_mod_inv(keyMatrix,26)
for i in range(3):
	messageVector[i][0] = ord(cip[i]) % 65
mess = ''
for i in range(3):
	for j in range(3):
			messMatrix[i][0] += (inv_mat[i][j] *
								   messageVector[j][0])
		messMatrix[i][0] = messMatrix[i][0] % 26
		mess = mess + chr(messMatrix[i][0] + 65)
print(mess)















