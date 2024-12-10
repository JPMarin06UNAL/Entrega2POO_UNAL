from esfera import Esfera
from comparar_esferas import CompararEsferas

def main():
    # Solicitar los valores de las esferas por teclado
    print("Ingrese el peso de la esfera A: ")
    pesoA = float(input())  

    print("Ingrese el peso de la esfera B: ")
    pesoB = float(input())  

    print("Ingrese el peso de la esfera C: ")
    pesoC = float(input())  

    print("Ingrese el peso de la esfera D: ")
    pesoD = float(input())  

    # Crear instancias de la clase Esfera con los pesos proporcionados por el usuario
    esferaA = Esfera(pesoA)
    esferaB = Esfera(pesoB)
    esferaC = Esfera(pesoC)
    esferaD = Esfera(pesoD)

    # Crear una instancia de la clase CompararEsferas
    diferenciar_esferas = CompararEsferas(esferaA, esferaB, esferaC, esferaD)

    # Llamar la función o método para comparar los pesos
    diferenciar_esferas.comparar()

# Ejecutar la función principal
if __name__ == "__main__":
    main()
