def contar_palabras(texto):
    # Eliminar los espacios en blanco al inicio y al final del texto
    texto = texto.strip()
    # Separar el texto en palabras usando los espacios en blanco como delimitador
    palabras = texto.split()
    # Contar el número de palabras
    numero_palabras = len(palabras)
    return numero_palabras

texto_ejemplo = "Este es un ejemplo de texto para contar palabras."
resultado = contar_palabras(texto_ejemplo)

# Imprimir el resultado
print("Número de palabras:", resultado)
