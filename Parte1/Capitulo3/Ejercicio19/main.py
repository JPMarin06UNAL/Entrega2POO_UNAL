from Triángulo_equilátero import Trianguloequilatero

def main():
    # Solicitar el valor del lado al usuario
    lado = float(input("Ingrese el valor del lado del triángulo equilátero: "))

    # Crear una instancia de TrianguloEquilatero
    triangulo = Trianguloequilatero(lado)

    # Llamar a los métodos para calcular los valores
    perimetro = triangulo.obtener_perimetro()
    altura = triangulo.obtener_altura()
    area = triangulo.obtener_area()

    # Mostrar resultados
    print(f"Perímetro: {perimetro}")
    print(f"Altura: {altura}")
    print(f"Área: {area}")

if __name__ == "__main__":
    main()