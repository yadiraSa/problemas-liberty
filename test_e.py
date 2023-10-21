from descripciones_tests import *

def test_e():
    print('-----Bienvenidos a la prueba E------')
    print(desc_test_e)

    configur = input('Ingrese la "configuración" inicial del estacionamiento (teniendo en cuenta que debe ser una cadena de letras mayúsculas sin repetirse):')
    entry = list(configur)

    num = int(input('Ingrese el número de autos que quieren salir:'))
    car_order = [configur]
    print('Orden inicial:', car_order)    


    for _ in range(num):
        exit_auto = input('Ingrese el próximo carro que quiera salir (letra mayúscula):')
    
        if exit_auto in entry:
            exit_auto_index = entry.index(exit_auto)
            entry.pop(exit_auto_index)
            
            entry.insert(0, exit_auto)
            
        car_order.append(''.join(entry))    
    

    for i in range(1, len(car_order)):
        print(f'Después de irse {car_order[i-1][-1]}: {car_order[i]}')    
    