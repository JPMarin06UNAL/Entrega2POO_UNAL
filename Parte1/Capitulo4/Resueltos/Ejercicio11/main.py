def find_largest_number(a, b, c):
    if a > b and a > c:
        largest = a
    elif b > a and b > c:
        largest = b
    else:
        largest = c
    
    return largest

# Ejemplo de uso
a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))
c = int(input("Ingresa el valor de c: "))

largest = find_largest_number(a, b, c)
print(f"El numero mas grande es: {largest}")
