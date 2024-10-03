#Pasamos el valor de cadena a hexadecimal
textocifrado_bytes = bytes.fromhex("9c8d968f8b90a08f868b979091a0c5bb")
llave_bytes = bytes.fromhex("ffffffffffffffffffffffffffffffff")

#Declaramos un array de bytes donde almacenara el resultado.
descifrado = bytearray()

#Hacemos un for, donde empezara a comprara entre los bytes del texto cifrado y la llave almacenando el resultado en la variable del array de bytes declarado
for i in range(len(textocifrado_bytes)):
  descifrado.append(textocifrado_bytes[i] ^ llave_bytes[i])

#Decodificamos en asccii de acuerdo a solicitud de la tarea.
print(descifrado.decode('ascii'))
#Mensaje: cripto_python_:D

#Esta parte es para comprobar que el mensaje sea el correcto por lo cual hacemos la misma operacion pero para obtener el cifrado
for i in range(len(descifrado)):
  descifrado.append(descifrado[i] ^ llave_bytes[i])
  
print(descifrado.hex())

# cifrado obtenido: 63726970746f5f707974686f6e5f3a44        9c8d968f8b90a08f868b979091a0c5bb <-- Valor mostrado en el string
# Cifrado brindado en texto                                 9c8d968f8b90a08f868b979091a0c5bb