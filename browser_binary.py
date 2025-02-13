import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('https://www.mendoza.edu.ar/wp-content/uploads/2022/02/logodge2024enc-300x67.png')
man_a = open('logo-dge.png', 'wb')
tamano = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    tamano = tamano + len(info)
    man_a.write(info)

print(tamano, 'caracteres copiados.')
man_a.close()

# Código: https://es.py4e.com/code3/curl2.py