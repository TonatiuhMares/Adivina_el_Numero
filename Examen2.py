
#  2. Escribe un programa que te permita jugar un juego de mente. El juego consistirá en adivinar una  cadena de números distintos. 
#     Al principio, el programa debe pedir la longitud de la cadena (de 2 a 5 cifras). Después el programa debe ir pidiendo que intentes
#     adivinar la cadena de números. En cada intento, el programa informará de cuántos  números han sido acertados
#     (el programa considerará que se ha acertado un número si coincide el valor y la posición).

import random
print('******************************************\n')
print('         Bienvenido al juego \n')
print('******************************************\n')
digitos =('0','1','2','3','4','5','6','7','8','9')
codigo = ''
dificultad = int(input('Dificultad:  Muy Fácil(1) , Facil (2) , Medio(3) , Dificil(4) \n '))

if dificultad ==1:
    cantdig = 2
elif dificultad ==2:
    cantdig =3
elif dificultad ==3:
    cantdig = 4
elif dificultad >=4:
    cantdig = 5
else:
    print('Por favor ingresa un numero válido. ')

for i in range(cantdig):
    elegido = random.choice(digitos)
    codigo = codigo + elegido
# print(codigo)
print(f'El digito generado automáticamente tiene una longitud de: {len(codigo)} caracteres. \n')

propuesta = input('Ingresa tu primer intento: ')
intentos = 1
while propuesta != codigo:
    intentos += 1
    aciertos = 0
    coincidencias = 0
    for i in range(cantdig):
        if propuesta[i] == codigo[i]:
            aciertos = aciertos + 1
        elif propuesta[i] in codigo:
            coincidencias = coincidencias +1
    print(f'Con {propuesta} has adivinado {aciertos} valores.' )
    propuesta = input('Intenta adivinar la cadena: \n')

print(f'Acertaste después de {intentos} intento(s). \n')


