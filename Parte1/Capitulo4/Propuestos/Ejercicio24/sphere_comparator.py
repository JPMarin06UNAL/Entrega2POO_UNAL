class SphereComparator:
    def __init__(self, sphere_a, sphere_b, sphere_c):
        self.sphere_a = sphere_a
        self.sphere_b = sphere_b
        self.sphere_c = sphere_c

    def find_heaviest_sphere(self):
        if self.sphere_a.weight > self.sphere_b.weight and self.sphere_a.weight > self.sphere_c.weight:
            return self.sphere_a.name
        elif self.sphere_b.weight > self.sphere_a.weight and self.sphere_b.weight > self.sphere_c.weight:
            return self.sphere_b.name
        else:
            return self.sphere_c.name
