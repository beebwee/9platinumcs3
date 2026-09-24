#Code
class ParentClass:
    def __init__(self, value):
        self.value = value

class Cell(ParentClass):
    def __init__(self, cellular_organization, dna_sequence, life_status):
        super().__init__(cellular_organization)
        self.dna_sequence = dna_sequence
        self.life_status = life_status
        self.atp_energy = 100  

    def metabolize(self):
        self.atp_energy -= 15
        print(f"Energy is now: {self.atp_energy}")

    def replicate(self):
        print("Cell split into two.")
        return Cell(self.value, self.dna_sequence, "Alive")

    def build_proteins(self, rna_sequence):
        print(f"Constructed protein from sequence: {rna_sequence}")

class Organelle:
    def __init__(self, name):
        self.name = name

class ChildClass(ParentClass):
    def __init__(self, value, extra):
        super().__init__(value)
        self.extra = extra

class EukaryoticCell(Cell):
    def __init__(self, cellular_organization, dna_sequence, life_status, 
                 true_nucleus, membranebound_organelles, cell_division):
        
        super().__init__(cellular_organization, dna_sequence, life_status)
        self.true_nucleus = true_nucleus               
        self.cell_division = cell_division                  
        self.organelles = [Organelle(name) for name in membranebound_organelles]

    def replicate(self):
        print(f"Dividing via: {self.cell_division}")
        names = [org.name for org in self.organelles]
        return EukaryoticCell(self.value, self.dna_sequence, "Alive", self.true_nucleus, names, self.cell_division)

#Test Run (w/ code)

if __name__ == "__main__":
    print("=== TEST 1: INHERITANCE ===")
    my_amoeba = EukaryoticCell("Single-celled", "AGCT_101", "Alive", True, ["Mitochondria"], "Mitosis")
    print(f"From Parent: {my_amoeba.value}")
    print(f"From Parent: {my_amoeba.dna_sequence}")
    my_amoeba.metabolize()

    print("\n=== TEST 2: COMPOSITION ===")
    print(f"Contains Organelle object: {my_amoeba.organelles[0].name}")
    my_amoeba.replicate()












