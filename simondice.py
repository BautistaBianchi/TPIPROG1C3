colores = ['rojo', 'verde', 'azul', 'amarillo']
import random

while True:
    secuencia = []
    puntaje = 0

    print("\n--- Simón Dice ---")
    respuesta = input("Presiona ENTER para comenzar (o 'salir' para terminar): ")
    
    if respuesta.lower() == 'salir':
        break

    while True:
        secuencia.append(random.choice(colores))
        
        print("\nSimón dice:")
        for color in secuencia:
            print(color, end=' ')
        print("\n")

        for color_correcto in secuencia:
            entrada = input("Tu color: ").lower()
            
            if entrada != color_correcto:
                print(f"¡Perdiste! Puntaje: {puntaje}")
                break
            
        else:
            puntaje += 1
            print(f"¡Nivel {puntaje} superado!")
            continue

        break