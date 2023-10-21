from descripciones_tests import *

def test_d():
    print('-----Bienvenidos a la prueba D------')
    print(desc_test_d)
    
    poblation = input('Ingrese el nombre de la población:')
    info = input('Ingrese la información de los cultivos obtenida: ')
    city = input('Ingrese la locación:')
    
    known = {}
    unknown = 0
    
    for cultive in info:
        if cultive.isalpha() and cultive.islower():
            if cultive in known:
                known[cultive] += 1
            else:
                known[cultive] = 1
        elif cultive == '*':
            unknown += 1
    
    known_types = len(known)
    ordered_cultives = sorted(known.items(), key=lambda x: (-x[1], x[0]))
    
    print(f'Población: {poblation}')
    print(f'Tipos de cultivos: {known_types}')
    print(f'Desconocidos: {unknown}')
    print(f'Localidad: {city}')
    print('Cantidades:')
    for cultive, cantidad in ordered_cultives:
        print(f'{cultive} - {cantidad}')       
 
    
 
 # En este problema tuve que consultar con varias fuentes para poder resolverlo       
        
                        
               
