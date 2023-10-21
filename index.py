from test_a import test_a
from test_b import test_b
from test_c import test_c
from test_d import test_d
from test_e import test_e

def show_menu():
  print('-------Menú------')
  print('A Prueba a')
  print('B Prueba b')
  print('C Prueba c') 
  print('D Prueba d') 
  print('E Prueba e')
  print('S Salir')
      
  
while True:
  show_menu()
  option = input('Porfavor, seleccione una opción (A,B,C,D,E, S):')
  
  if option == 'A':
    test_a()
  elif option == 'B':
    test_b()
  elif option == 'C':
    test_c() 
  elif option == 'D':
    test_d()
  elif option == 'E':
    test_e()
  elif option == 'S':
    print('Cerrando el menú')
    break
  else:
      print('No se encontró la opción. Favor de teclear una opción válida')                      