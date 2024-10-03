# Utilizamos la clase Hash de la cual importaremos de la libreria Cryptography
from cryptography.hazmat.primitives import hashes

#Declaramos una variable donde inicializamos el metodo hash e indicamos que tipo de algoritmo se utilizara para realizar el hash, en este caso MD5
hashmd5 = hashes.Hash(hashes.MD5())

# Ruta para abrir el archivo que queremos leer y obtener su hash (Importante, cambiar la ruta del destino para leer su propio archivo)
rutawinmd5 = "C://Users//Tecmadi//Desktop//Clases Ciberseguridad//Tarea N01//WinMD5.exe"
rutawinmd5_2 = "C://Users//Tecmadi//Desktop//Clases Ciberseguridad//Tarea N01//WinMD5_2.exe"

#Abrimos la ruta del archivo
ruta = open(rutawinmd5, "rb")
#Leemos el archivo, esto nos devuelte bytes, el cual lo pasamos al metodo update para indicarle lo que se quiere encriptar
hashmd5.update(ruta.read())
# damos por finalizado el encriptamiento y devolvemos un valor
md5s = hashmd5.finalize()
#Pasamos el valor obtenido a hexadecimales para que pueda ser legible.
hash_hexadecimal = md5s.hex()
print(hash_hexadecimal)