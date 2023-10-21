desc_test_a = '''
¿Conoces el juego de PI?
En el área de desarrollo de Liberty Fianzas nos gusta organizar reuniones virtuales y este es un
juego muy común con el afán de castigar a alguien. Consiste principalmente en decir los números
naturales en el orden que conocemos, pero cualquier número múltiplo de 7 o que termine en 7 o
que la suma de sus dígitos sea múltiplo de 7, debe decirse “pi” en vez del número. De esta forma
la serie de un juego perfecto empezaría con
1, 2, 3, 4, 5, 6, pi, 8, 9, 10, 11, 12, 13, pi, 15, pi, pi, 18, 19, 20, pi, 22, 23, 24, pi, 26, pi, pi, 29 ...
Para realizar el juego se forma un círculo. Alguien empieza diciendo “1”, y siguiendo el giro de las
manecillas del reloj la persona de lado le toca decir el siguiente valor de la serie y así
consecutivamente hasta que alguien no diga el número de PI correcto. Aquella persona que falla
es castigada y empieza el siguiente juego con el “1”.
//Entrada// 
La entrada consiste en varios casos de prueba. Cada caso consiste en una línea que contiene un
número entero positivo n < 10^9.
//Salida//
Por cada caso, imprime una línea con el número de PI correcto es decir el mismo número o PI.
'''

desc_test_b = '''En el equipo de desarrollo tenemos un amigo conocido como “topo el ciego”, no puede ver muy
bien, a menudo usa lentes o lupa para distinguir las letras de los textos. Topo el ciego es una
persona voluntariosa, por lo que a pesar de su problema visual estudia computación. Él requiere
de un programa especial que haga un zoom sobre las imágenes para que las pueda distinguir
mejor; por ello, necesita de tu ayuda para que le diseñes un programa que reciba una imagen y la
procese para que esta aparezca más grande en el monitor especial que él utiliza.
//Entrada//
En la primera línea recibirás un entero n < 101. Luego le siguen una matriz de n líneas por n letras
minúsculas que representa el color del píxel del monitor.
//Salida//
Imprime la imagen con un zoom de tamaño 3.
'''

desc_test_c = '''Seguramente ya has resuelto el problema A y quizás como desarrollador curioso te preguntes
cuantas veces se puede decir PI durante el juego.
Este problema consiste en dado un número n entre 1 y 100, calcula la cantidad de números que
existen entre [1, n ^2] de tal forma que hay que decir 'pi' en vez del número, en un juego de PI
perfecto.
//Entrada//
La entrada consiste en varios casos de entrada. Cada caso consiste en una línea que contiene un
número entero positivo n <= 100.
//Salida//
Por cada caso imprime una línea con el número que representa a la cantidad de número que
existen entre [1, n ^2] de tal forma que hay que decir 'pi' en vez del número, en un juego de PI
perfecto.
'''

desc_test_d = '''Jimmy un inspector de agricultura del gobierno del Estado. Recorre diversas poblaciones agrícolas
donde el Estado ha dado apoyo. Su trabajo consiste en hacer un reporte de lo que actualmente se
está sembrando en cada una de estas poblaciones. Por propósitos de simplicidad Jimmy anota en
su cuaderno primero el nombre de la población y posteriormente por cada diferente terreno
visitado una letra indicando el tipo de cultivo de la siguiente forma: 'a' si es alfalfa, 'b' si es brócoli,
'c' si es calabaza, así hasta la 'z' si es zanahoria; en caso de haber un cultivo desconocido pone
un *.
Tu trabajo consiste en ayudar a Jimmy a hacer su reporte a partir de la información que anotó en
su cuaderno.
//Entrada//
Cada caso consiste en dos líneas, la primera contiene una cadena 'p' con el nombre de la población,
la segunda línea contiene una cadena 's' que representa la información obtenida de la población,
dicha información está formada únicamente de los caracteres 'a' a la 'z' y '*'.
//Salida//
La salida consistirá en un reporte en el siguiente formato:
POBLACION: p
TIPOS DE CULTIVOS: k
DESCONOCIDOS: d
CANTIDADES:
c1-n1
c2-n2
...
cm-nm

***Donde p es el nombre de la población, k es la cantidad de
tipos de cultivos conocidos distintos entre sí encontrados en
la población p, d es el número de terrenos con cultivos
desconocidos. Por último (c1, n1) .. (cm, nm) corresponde a
la lista de cultivos ordenada primero por la cantidad de
terrenos que tienen el mismo cultivo (de mayor a menor),
en caso de empate, por la letra que lo representa (de menor
a mayor léxico-gráficamente).***
'''

desc_test_e = '''Las oficinas de Liberty Fianzas tienen un inusual camino semicircular que puede acomodar 26
autos en una sola fila, con salidas en la parte delantera y trasera. Esto es bueno porque cuando
organiza una fiesta, todos pueden estacionarse en el camino de entrada. Sin embargo, causa
complicaciones cuando un empleado quiere irse, porque otros autos bloquean a esa persona y
deben moverlos temporalmente. Cuando alguien se va, los autos que deben moverse regresan al
camino de entrada en orden inverso. Dado que hay dos formas de salida del automóvil que sale (a
través de la salida delantera o trasera), los automóviles en el camino más corto hacia una salida
deben moverse (y regresar en orden inverso). Si el coche que quiere salir está exactamente en el
medio, los coches delanteros (a la izquierda) deben moverse.
Por ejemplo, suponga que la configuración inicial del camino de entrada se representa como
ABCDEFG. Suponga además que el propietario del automóvil E decide irse. Entonces, los
propietarios de los autos F y G deben moverse (ya que están en el camino más corto hacia una
salida) para dejar espacio para que E se vaya y luego regresar al camino de entrada en orden
inverso. La nueva configuración del camino de entrada será ABCDGF. Supongamos que ahora C
quiere irse. Aquí, A y B tienen que moverse (ya que están en el camino más corto hacia una salida),
con la configuración resultante BADGF. Digamos que ahora D quiere irse. En este caso, B y A deben
moverse (ya que ambos caminos de salida tienen la misma longitud, y A y B están en el camino
hacia la salida frontal). La configuración resultante es ABGF.
//Entrada//
Cada conjunto de datos comienza con una línea que contiene solo una cadena de letras
mayúsculas, que representa el orden inicial de los automóviles en la entrada, como se describió
anteriormente. La cadena contendrá al menos una letra y no se duplicará ninguna letra. La
siguiente línea contiene un número entero n ≥ 0. Las siguientes n líneas contienen sola una letra
mayúscula, lo que indica el próximo automóvil en salir de la fiesta.
//Salida//
Comienza la salida con el orden inicial de los automóviles en el camino de entrada. A medida que
cada automóvil se va, el nuevo orden de los autos.
'''