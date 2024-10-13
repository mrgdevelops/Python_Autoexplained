# PYTHON AUTOEXPLICADO
# Crash course

# Tipos de datos en Python (continuación)

# Las LISTAS son como ARRAYS en otros lenguajes.
# Observa, que la misma lista en Python puede contener DIFERENTES tipos de datos
miLista = [13, "Agosto", 2024, True] #  lista           Se delimitan con CORCHETES '[]'
print("lista:")
print(miLista)

# Las tuplas son como listas, pero son INMUTABLES
miTupla = (13, "Agosto", 2024, True)    # tupla         Se delimitan con PARÉNTESIS '()'
print("\ntupla:")
print(miTupla)

# Los diccionarios son colecciones de elementos compuestos por parejas CLAVE-VALOR
meses_traducidos = {                     #diccionario    Se delimita por CORCHETES '{}'
    "enero": "January",
    "febrero": "February",
    "marzo": "March",
    "abril": "April",
    "mayo": "May",
    "junio": "June",
    "julio": "July",
    "agosto": "August",
    "septiembre": "September",
    "octubre": "October",
    "noviembre": "November",
    "diciembre": "December"
}


print("\nDiccionario:")
print(meses_traducidos)

# Ejemplo de uso:
print("\nElemento del diccionario:")
print(meses_traducidos["enero"])  # Salida: January

"""
En este ejercicio también hemos visto como se utiliza '\n' para el salto de línea en instrucción "print"
y como se nombran variables en "camelCase" y "snake_case" (Esto solo es un ejemplo, ¡_NO_ mezclar estilos en el mismo programa real!)
"""