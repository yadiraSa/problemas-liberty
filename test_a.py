from descripciones_tests import *

def test_a():
    print('-----Bienvenidos a la prueba A------')
    print(desc_test_a)
    num = int(input('Ingresa un número:'))
    sum_digit = sum(int(digit) for digit in str(num)) % 7 == 0
    
    if num == 7 or num % 7 == 0 or num % 10 == 7 or sum_digit:
      print('Resultado: pi')
    else:
        print(f'Resultado: {num}')