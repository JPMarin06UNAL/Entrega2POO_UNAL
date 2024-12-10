from sphere import Sphere
from sphere_comparator import SphereComparator

# Ejemplo de uso
name_a = input("Ingrese el nombre de la esfera A: ")
weight_a = float(input("Ingrese el peso de la esfera A: "))

name_b = input("Ingrese el nombre de la esfera B: ")
weight_b = float(input("Ingrese el peso de la esfera B: "))

name_c = input("Ingrese el nombre de la esfera C: ")
weight_c = float(input("Ingrese el peso de la esfera C: "))

sphere_a = Sphere(name_a, weight_a)
sphere_b = Sphere(name_b, weight_b)
sphere_c = Sphere(name_c, weight_c)

comparator = SphereComparator(sphere_a, sphere_b, sphere_c)
heaviest_sphere = comparator.find_heaviest_sphere()
print(f"La esfera más pesada es la esfera {heaviest_sphere}.")
