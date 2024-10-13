# PYTHON AUTOEXPLICADO
# Python Essentials || Crash Course

# Operadores LÓGICOS (AND, OR, NOT)
# Devuelven True or False
# 
# NOTA IMPORTANTE: observa como "True" y "False" empiezan con MAYÚSCULA
# cuando "and", "or" y "not" se escriben en _minúsculas_


print("Pruebas 'AND':") # Aquí aprovechamos para probar comillas anidadas

bool1 = True
bool2 = True
print (bool1 and bool2) 

bool1 = True
bool2 = False
print (bool1 and bool2)

bool1 = False
bool2 = False
print (bool1 and bool2)


print('\nPruebas "OR":') # Aquí aprovechamos para probar otra forma de comillas anidadas + añadir salto de línea al principio

bool1 = True
bool2 = True
print (bool1 or bool2)

bool1 = True
bool2 = False
print (bool1 or bool2)

bool1 = False
bool2 = False
print (bool1 or bool2)


print('\nPruebas "NOT" (negación):')

bool1 = True
bool2 = False
print (not bool1)
print (not bool2)
