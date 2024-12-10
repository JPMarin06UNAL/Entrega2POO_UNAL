class CompararEsferas:
    def __init__(self, esferaA, esferaB, esferaC, esferaD):
        self.esferaA = esferaA
        self.esferaB = esferaB
        self.esferaC = esferaC
        self.esferaD = esferaD

    def comparar(self):
        if self.esferaA.peso == self.esferaB.peso == self.esferaC.peso:
            if self.esferaD.peso != self.esferaA.peso:
                print("La esfera D es la diferente")
                if self.esferaD.peso > self.esferaA.peso:
                    print("Y es de mayor peso")
                else:
                    print("Y es de menor peso")
        elif self.esferaA.peso == self.esferaB.peso == self.esferaD.peso:
            print("La esfera C es la diferente")
            if self.esferaC.peso > self.esferaA.peso:
                print("Y es de mayor peso")
            else:
                print("Y es de menor peso")
        elif self.esferaA.peso == self.esferaC.peso == self.esferaD.peso:
            print("La esfera B es la diferente")
            if self.esferaB.peso > self.esferaA.peso:
                print("Y es de mayor peso")
            else:
                print("Y es de menor peso")
        else:
            print("La esfera A es la diferente")
            if self.esferaA.peso > self.esferaB.peso:
                print("Y es de mayor peso")
            else:
                print("Y es de menor peso")
