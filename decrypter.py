import os
import pyaes

## abrur o arquivo criptografado

file_name = "teste.txt.ransomweretroll"
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## chave de descriptografia

key = b'testeransomweres'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## criar um novo arquivo descriptografado

new_file = 'teste.txt'
new_fila = open(f'{new_file}','wb')
new_file.write.decrypt_data)
new_file.close()
