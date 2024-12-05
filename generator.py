import secrets
import string

# Diccionario con los caracteres disponibles
diccionario = {
    'letras': string.ascii_letters,   # Letras mayúsculas y minúsculas
    'numeros': string.digits,        # Dígitos del 0 al 9
    'caracteres': string.punctuation # Caracteres especiales
}

def generar_contrasena(longitud=12, usar_letras=True, usar_numeros=True, usar_caracteres=True):
    """
    Genera una contraseña segura basada en los parámetros dados.

    :param longitud: Longitud de la contraseña (entero, por defecto 12).
    :param usar_letras: Incluir letras en la contraseña (booleano).
    :param usar_numeros: Incluir números en la contraseña (booleano).
    :param usar_caracteres: Incluir caracteres especiales en la contraseña (booleano).
    :return: Contraseña generada (cadena).
    """
    # Construir el conjunto de caracteres permitidos
    caracteres_permitidos = ""
    if usar_letras:
        caracteres_permitidos += diccionario['letras']
    if usar_numeros:
        caracteres_permitidos += diccionario['numeros']
    if usar_caracteres:
        caracteres_permitidos += diccionario['caracteres']

    if not caracteres_permitidos:
        raise ValueError("Debes seleccionar al menos un tipo de caracteres para generar la contraseña.")

    # Generar la contraseña
    return ''.join(secrets.choice(caracteres_permitidos) for _ in range(longitud))

# Ejemplo de uso
if __name__ == "__main__":
    print("Contraseña generada:", generar_contrasena(16, usar_letras=True, usar_numeros=True, usar_caracteres=True))
