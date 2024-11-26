import random

palabras = ["PYTHON", "PROGRAMACION", "AHORCADO", "DESARROLLADOR", "TECNOLOGIA"]

palabra = random.choice(palabras)
palabra_oculta = ["_"] * len(palabra)
letras_adivinadas = []
letras_erroneas = []
intentos_restantes = 6

print("¡Bienvenido al juego del ahorcado!")
print("Adivina la palabra:")
print(" ".join(palabra_oculta))

while intentos_restantes > 0:
    print("\nPalabra:", " ".join(palabra_oculta))
    print("Letras incorrectas:", " ".join(letras_erroneas))
    print("Intentos restantes:", intentos_restantes)

    letra = input("Ingresa una letra: ")

    if len(letra) != 1:
        print("Por favor, ingresa solo una letra.")
        continue

    if letra in letras_adivinadas or letra in letras_erroneas:
        print("Ya ingresaste esa letra. Intenta con otra.")
        continue

    if letra in palabra:
        print("¡Bien hecho! La letra está en la palabra.")
        letras_adivinadas = letras_adivinadas + [letra]
        for i in range(len(palabra)):
            if palabra[i] == letra:
                palabra_oculta[i] = letra
    else:
        print("Lo siento, esa letra no está en la palabra.")
        letras_erroneas = letras_erroneas + [letra]
        intentos_restantes -= 1

    if "_" not in palabra_oculta:
        print("\n¡Felicidades! Has adivinado la palabra:")
        print("Palabra:", "".join(palabra_oculta))
        break
else:
    print("\n¡Has perdido! La palabra era:", palabra)