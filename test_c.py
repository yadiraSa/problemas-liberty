from descripciones_tests import *

def test_c():
    print('-----Bienvenidos a la prueba C ------')
    print(desc_test_c)
    
    num = int(input('Ingrese un número que este dentro del siguiente rango [1,100]:'))
    
    if num < 1 or num > 100:
        print('El número no está dentro del rango')
        return
    
    conteo_pi = 0
    for i in range(1, num ** 2 + 1):
        if '7' in str(i) or i % 7 == 0 or i % 10 == 7 or sum(int(digit) for digit in str(i)) % 7 == 0:
            conteo_pi += 1
    print(f'El número de veces de "pi" en ese rango es de: {conteo_pi}')        
            
    
    
