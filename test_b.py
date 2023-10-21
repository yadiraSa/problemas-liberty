from descripciones_tests import *

def test_b():
    print('-----Bienvenidos a la prueba B------')
    print(desc_test_b)
    
    n = int(input('Ingrese el valor del entero y las lineas (letras):'))
    
    imagen = []
    for _ in range(n):
        fila = input()
        imagen.append(fila)
    
    zoom_imagen = []
    for fila in imagen:
        for _ in range(3):
            zoom_fila = ''
            for caracter in fila:
                zoom_fila += caracter * 3
            for _ in range(3):
                zoom_imagen.append(zoom_fila)
    
    for fila in zoom_imagen:
        print(fila)                
        
# En este problema tuve que consultar con varias fuentes para poder resolverlo