# PYTHON AUTOEXPLICADO
# Crash course

# Tipos principales de variables en Python
# IMPORTANTE: Observa como _NO_ se establece el tipo de dato a la hora de declarar variables ! ("tipado dinámico")
# Más abajo en el código se ve cómo saber el TIPO de la variable en caso de duda

nombre = "Mike" # String
apellido = 'Solo' # Otro String, con comillas simples
edad = 45 # int
estatura1 = 1,85 # Más abajo se puede ver que Python ha reconocido esta variable como "tuple" en vez de "float", porque va con coma en vez de punto
estatura2 = 1.85 # float   Tiene que ir con PUNTO, no con coma !
esProgramador = True # booleano
tienePerro = False # observa como True y False empiezan con MAYÚSCULA

"""
En el siguiente código tenemos varios eejmplos:
    • Concatenación de cadenas. Se concatena tanto texto directamente como variabvles de tipo cadena de taexto en la misma expresión.
    • Conversión de tipos (casting). Si no convertimos "edad" en String da error.

El caracter "bullet point" es ALT + 0149    
"""
print("Mi nombre es " + nombre + " " + apellido + " y tengo " + str(edad) + " años.")

print(estatura1) # Imprime el VALOR de la variable
print(estatura2) # Imprime el VALOR de la variable

print(type(estatura1)) # Imprime el TIPO de la variable
print(type(estatura2)) # Imprime el TIPO de la variable
