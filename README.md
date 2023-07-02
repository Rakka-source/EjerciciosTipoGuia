# EjerciciosTipoGuia

## OVA 7

En esta tarea deberá escribir funciones para ayudar a gestionar la preparación de comidas a
partir de sus ingredientes. Los ejemplos se restringen a sandwiches pero el contexto debe
considerarse de manera general.
La lista platos contiene los nombres de las preparaciones acerca de las cuales se tiene
información. Por ejemplo:
platos = [
'Churrasco Aliado', 'Churrasco Italiano', 'Churrasco Al-i-talia',
'Lomito Alemán', 'Vegetariano', 'El muy chancho', 'El Pedro Pascal',
'Estoy Pato', 'Igual Pato'
]

Por otra parte, la lista ingredientes es una lista de listas que contiene los ingredientes
necesarios para preparar cada plato. Existe una correspondencia de índices entre la lista
platos y la lista ingredientes, es decir, los ingredientes del plato que está en la posición i
de la lista platos se encuentran en la lista que está en la posición i de la lista
ingredientes. Por ejemplo:

ingredientes = [
['churrasco', 'queso', 'jamón'],
['churrasco', 'palta', 'mayonesa', 'tomate'],
['churrasco', 'queso', 'jamón', 'palta'],
['lomito', 'chucrut', 'salsa americana'],
['queso', 'mayonesa', 'tomate'],
['queso', 'palta', 'tomate', 'lomito', 'chucrut', 'salsa americana'],
['queso', 'jamón', 'palta'],
['mayonesa', 'tomate'],
['mayonesa', 'tomate', 'salsa americana']
]

precios = [
['churrasco', 3000], ['queso', 2000], ['jamón', 4000], ['palta', 4500],
['mayonesa', 1500], ['tomate', 1000], ['lomito', 2500], ['chucrut', 1000],
['salsa americana', 1000]
]

Tarea 1. Escriba la función costo_plato(platos, ingredientes, precios, plato),
que recibe como parámetro tres listas con los formatos descritos anteriormente,
correspondientes a los platos, los ingredientes de esos platos y los precios de cada ingrediente.
El último parámetro de la función es un string con el nombre de un plato. La función debe
retornar el costo total involucrado en la preparación del plato indicado, es decir, la suma del
precio de todos los ingredientes que requiere.

>>> print(costo_plato(platos, ingredientes, precios, 'Churrasco Italiano'))
10000

Tarea 2. Escriba la función buscar_opciones(platos, ingredientes,
disponibles), que recibe como parámetro las listas de platos e ingredientes, y una tercera
lista que contiene los ingredientes que están disponibles actualmente en la cocina. La función
debe retornar una lista de listas, donde cada sublista corresponde a una preparación que es
posible hacer utilizando los ingredientes disponibles, junto con su costo. La lista debe estar
ordenada de acuerdo al costo de forma ascendente, es decir, los platos más baratos primero.

>>> disponibles = ['queso', 'mayonesa', 'tomate', 'salsa americana']
>>> print(buscar_opciones(platos, ingredientes, disponibles))
[[2500, 'Estoy Pato'], [3500, 'Igual Pato'], [4500, 'Vegetariano']]