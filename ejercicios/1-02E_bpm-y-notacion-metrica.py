"""
INTRODUCCIÓN A LA PROGRAMACIÓN EN PYTHON A TRAVÉS DE LA MÚSICA
Ángel Faraldo, del 19 al 23 de julio de 2021
Campus Junior, Universitat Pompeu Fabra

EJERCICIO
=========
"1-06E-bpm-y-notacion-metrica"

El tiempo musical suele medirse de forma más flexible que el tiempo de los relojes,
a pesar de hacer referencia a ellos. El cómputo del tiempo musical utiliza normalmente
una unidad básica o tiempo, que se espacia en intervalos de tiempo constantes (como los segundos).
Sin embargo, una forma más flexible de medir el tiempo musical es en pulsaciones por minuto
(beats-per-minute o bpm en inglés), es decir, contando cuántas unidades de tiempo suceden
a lo largo de un minuto o 60 segundos.

Las unidades de tiempo musical suelen oscilar entre 40 y 250 pulsaciones por minuto.
El valor en pulsaciones por minuto de una pieza musical se conoce normalmente como "tempo".
En cambio, la música electrónica y por ordenador, los instrumentos midi, etc...
suelen utilizar medidas más precisas, como el milisegundo.

Una vez establecido el tempo, se consiguen figuras de diferentes duraciones simplemente
multiplicando o dividiendo por dobles o mitades. Así, si el pulso básico se corresponde con
una negra, las proporciones de las duraciones son las siguientes:

1 negra = unidad de tempo básica
1 blanca = 2 negras
1 redonda = 4 negras
1 corchea = 1/2 negra
1 semicorchea = 1/4 negra

En este EJERCICIO, quiero que conviertas las unidades de tiempo musical en bpm a su valor
equivalente en milisegundos, cosa que será muy muy útil en programas posteriores.

Una vez hecho esto, quiero que imprimas en la consola las duraciones de cada una de las figuras musicales.

Requisitos
1) utiliza la función de entrada input() para hacer la conversión interactiva.
2) recuerda hacer "typecasting" para pasar de int a str.
3) utiliza operadores aritméticos para convertir la unidad en pulsaciones por minuto en milisegundos.
4) imprime en la consola la duración de la unidad de tempo en milisegundos.
5) imprime en la consola las duraciones en milisegundos de todas las figuras musicales.
5) cuida que el programa sea autoexplicativo, formula bien las preguntas y los pasos al usuario potencial.

AYUDA:
1 segundo = 1000 ms.
1 minuto = 60 segundos
"""