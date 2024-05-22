def word_counter(texto):
    texto = texto.strip()
    palabras = texto.split()
    numero_palabras = len(palabras)
    return numero_palabras

texto_ejemplo = "COMO TA MUCHACHO, YO A UTEDES LES VEO MUY BIEN. JIJIJIJI JIJIJI JA"
resultado = word_counter(texto_ejemplo)

print("Número de palabras:", resultado)
