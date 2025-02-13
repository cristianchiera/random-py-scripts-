import socket
from translate import Translator

def dividir_texto(texto, max_len=500):
    palabras = texto.split()
    fragmento_actual = ""
    fragmentos = []

    for palabra in palabras:
        if len(fragmento_actual) + len(palabra) + 1 > max_len:
            fragmentos.append(fragmento_actual)
            fragmento_actual = palabra
        else:
            fragmento_actual += " " + palabra

    if fragmento_actual:
        fragmentos.append(fragmento_actual)

    return fragmentos

# Configurar el socket y hacer la solicitud HTTP
misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misock.connect(('data.pr4e.org', 80))
cmd = 'GET /clown.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'.encode()
misock.send(cmd)

contenido_bytes = b""

while True:
    datos = misock.recv(512)
    if len(datos) < 1:
        break
    contenido_bytes += datos

misock.close()

# Decodificar la respuesta HTTP
contenido = contenido_bytes.decode()

# Separar los encabezados del cuerpo
partes = contenido.split("\r\n\r\n", 1)
if len(partes) > 1:
    contenido_texto = partes[1]  # Solo el contenido del archivo
else:
    contenido_texto = contenido  # Si no hay separación, usar todo

# Imprimir el contenido original
print("=== Contenido original ===")
print(contenido_texto)

# Dividir el contenido en fragmentos pequeños para traducir
fragmentos = dividir_texto(contenido_texto, max_len=500)

# Configurar el traductor
translator = Translator(to_lang="es")

# Traducir cada fragmento
contenido_traducido = ""
for fragmento in fragmentos:
    try:
        contenido_traducido += translator.translate(fragmento) + " "
    except Exception:
        contenido_traducido += "\n[Error en la traducción de un fragmento]\n"

# Imprimir la traducción completa
print("\n=== Contenido traducido ===")
print(contenido_traducido)
