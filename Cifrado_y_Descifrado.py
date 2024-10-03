#importamos una libreria estandar
import os

#Importo la libreria cryptography pero con la opcion de traer solo algunas clases como algorithms,base,modes
from cryptography.hazmat.primitives.ciphers import algorithms,base,modes

#Preparo el metodo encriptar
def encriptar(modo,llave,texto):     
    
    llave_bytes = llave.encode('utf-8')
    texto_bytes = texto.encode('utf-8')    
    
    # Se degenera un random de vector de inicializador de 16 bytes
    iv = os.urandom(16)
    # Se realiza if para reutilizar el metodo con otros modos de crifrado
    if modo == "CBC":
        mode = modes.CBC(iv)
    elif modo == "OFB":
        mode = modes.OFB(iv)
    elif modo == "CFB":
        mode = modes.CFB(iv)
    elif modo == "ECB":
        mode = modes.ECB()
    
    #Utilizo la clase base con el metodo Cipher para pasar indicar que algoritmo de cifrado se usara asi como su llave, adicional a ello se brindara el modo de cifrado
    cifrado = base.Cipher(algorithms.AES(llave_bytes),mode)
    #llamar a la funcion encryptar
    encriptado = cifrado.encryptor()    
    #Finalizo componiendo los bytes para el texto encriptado. Colocando primero el vector de inicializacion, junto con el texto encriptado y su finalizacion de encriptacion.
    textoencriptado = iv + encriptado.update(texto_bytes) + encriptado.finalize()
    #retorno el array de bytes y muestro su valor hexadecimal para una mejor visualizacion en texto.
    return textoencriptado.hex()

def desencriptar(modo,llave,texto):  
    
    iv =bytes.fromhex(texto)[:16]    
    llave_bytes = llave.encode('utf-8')    
    texto_bytes = bytes.fromhex(texto)[16:]
    
    
    
    #Transformo el valor hexadecimal a bytes y saco el vector de inicializacion de los primero 16 bytes
    iv =bytes.fromhex(texto)[:16]
    #Transformo a bytes la clave que se encuentre en formato utf8
    llave_bytes = llave.encode('utf-8')
    #Obtengo el texto de los bytes restantes
    texto_bytes = bytes.fromhex(texto)[16:]
    
    # Se realiza if para reutilizar el metodo con otros modos de crifrado
    if modo == "CBC":
        mode = modes.CBC(iv)
    elif modo == "OFB":
        mode = modes.OFB(iv)
    elif modo == "CFB":        
        mode = modes.CFB(iv)
    elif modo == "ECB":
        mode = modes.ECB()
    
    
    cifrado = base.Cipher(algorithms.AES(llave_bytes),mode)
    desencriptado = cifrado.decryptor()

    textodesencriptado = desencriptado.update(texto_bytes) + desencriptado.finalize()    
    return textodesencriptado.decode()

#----------------------- CBC ------------------------------
encrypted_data = encriptar("CBC", '12345678901234567890123456789012', 'a secret message')
print("Encriptado AES CBC: ",encrypted_data)
des = desencriptar("CBC", '12345678901234567890123456789012', encrypted_data)
print("Desencriptado AES CBC: ",des)
#----------------------- OFB ------------------------------
encrypted_data = encriptar("OFB", '12345678901234567890123456789012', 'a secret message')
print("Encriptado AES OFB: ",encrypted_data)
des = desencriptar("OFB", '12345678901234567890123456789012', encrypted_data)
print("Desencriptado AES OFB: ",des)
#----------------------- CFB ------------------------------
encrypted_data = encriptar("CFB", '12345678901234567890123456789012', 'a secret message')
print("Encriptado AES CFB: ",encrypted_data)
des = desencriptar("CFB", '12345678901234567890123456789012', encrypted_data)
print("Desencriptado AES CFB: ",des)
#----------------------- ECB ------------------------------
encrypted_data = encriptar("ECB", '12345678901234567890123456789012', 'a secret message')
print("Encriptado AES ECB: ",encrypted_data)
des = desencriptar("ECB", '12345678901234567890123456789012', encrypted_data)
print("Desencriptado AES ECB: ",des)

