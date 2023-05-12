## Ejercicio 1
def costo_plato(platos, ingredientes, precios, plato):
    """costo_plato(list platos, list ingredientes, list precios, string'Churrasco Italiano')"""
    if plato in platos:
        indicePlato=platos.index(plato)
        ingredientesSolicitados=ingredientes[indicePlato]
        costo=_obtener_costo_ingredientes(ingredientesSolicitados,precios)
        return costo
    return 0

def _obtener_costo_ingredientes(ingredientesSolicitados,precios):
    costoTotal=0
    for ingrediente in ingredientesSolicitados:
        for ingredient,valorIngrediente in precios:
            if ingredient == ingrediente:
                costoTotal+=valorIngrediente
    return costoTotal

## Ejercicio 2
def buscar_opciones(platos, ingredientes, disponibles, precios):
    listaDisponibles=[]
    for indice,opcionesPlatos in enumerate(ingredientes):
        if descartar_platos(disponibles,opcionesPlatos):
            listaDisponibles.append(indice)
    lista=lista_opciones_precio(listaDisponibles,platos,ingredientes,precios)
    return lista

def descartar_platos(ingredienteDisponible,opciones):
    for ingrediente in opciones:
        if not ingrediente in ingredienteDisponible:
            return False
    return True

def lista_opciones_precio(listaDisponible,platos,ingredientes,precios):
    listaPlato=[]
    for disponible in listaDisponible:
        costo=_obtener_costo_ingredientes(ingredientes[disponible],precios)
        listaPlato=orden_lista(listaPlato,costo,platos[disponible])
    return listaPlato

def orden_lista(listaPlato,costo,plato):
    for indice,itemLista in enumerate(listaPlato):
        if costo<=itemLista[0]:
            listaPlato.insert(indice,[costo,plato])
            return listaPlato
    listaPlato.append([costo,plato])
    return listaPlato


if __name__=="__main__":
    platos = [
        'Churrasco Aliado',
        'Churrasco Italiano',
        'Churrasco Al-i-talia',
        'Lomito Alemán',
        'Vegetariano', 
        'El muy chancho', 
        'El Pedro Pascal',
        'Estoy Pato',
        'Igual Pato'
    ]
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
    precios =  [
        ['churrasco', 3000],
        ['queso', 2000],
        ['jamón', 4000],
        ['palta', 4500],
        ['mayonesa', 1500],
        ['tomate', 1000],
        ['lomito', 2500],
        ['chucrut', 1000],
        ['salsa americana', 1000]
    ]

    disponibles = ['queso', 'mayonesa', 'tomate', 'salsa americana']
    print(costo_plato(platos, ingredientes, precios, 'Churrasco Italiano'))
    print(buscar_opciones(platos, ingredientes, disponibles,precios))
