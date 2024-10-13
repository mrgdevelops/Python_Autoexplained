# PYTHON AUTOEXPLICADO
# Python Essentials || Crash Course

# Los identificadores de constantes en Pyuthon se escriben en MAYÚSCULAS, para que se diferencien visualmente de las variables
EDAD = 18
print(EDAD)

# Aunque en realidad _NO_ son constantes y pueden cambiar su valor:
EDAD = 21
print(EDAD)


# Para evitar modificar valores de constantes accidentalmente en el código, se recomienda tener constantes definidas en un archivo aparte:

import misConstantes        # Importación de constantes, están en un archivo "misConstantes.py" en la misma carpeta que este código
print("Mi nombre es " + misConstantes.NAME + " " + misConstantes.SURMANE + " y tengo " + str(misConstantes.AGE) + " años.") # acceder a constantes utilizando la sintaxis "archivo_constantes.NOMBRE_CONSTANTE"
