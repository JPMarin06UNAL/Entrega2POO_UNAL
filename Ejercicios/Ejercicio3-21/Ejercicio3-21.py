import math

def triangle_properties(a, b, c):

    # Verificar que los lados formen un triángulo válido
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Los lados proporcionados no forman un triángulo válido.")

    # Cálculo del perímetro
    perimetro = a + b + c

    # Cálculo del semiperímetro
    semiperimetro = perimetro / 2

    # Cálculo del área utilizando la fórmula de Herón
    area = math.sqrt(semiperimetro * (semiperimetro - a) * (semiperimetro - b) * (semiperimetro - c))

    return {
        "perimetro": perimetro,
        "semiperimetro": semiperimetro,
        "area": area
    }

a = float(input("Ingrese un lado a del triángulo: "))
b = float(input("Ingrese un lado b del triángulo: "))
c = float(input("Ingrese un lado c del triángulo: "))
try:
    propiedades = triangle_properties(a, b, c)
    print(f"Perímetro: {propiedades['perimetro']}")
    print(f"Semiperímetro: {propiedades['semiperimetro']}")
    print(f"Área: {propiedades['area']}")
except ValueError as e:
    print(e)

