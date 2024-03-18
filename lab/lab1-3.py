class Cat:
    def __init__(self, breed: str, color: str, legs=4, ears=2) -> None:
        self.breed = breed
        self.color = color
        self.legs = legs
        self.ears = ears

    def __str__(self):
        return f"{self.color} {self.breed} cat with {self.legs} legs and {self.ears} ears."

    def __repr__(self):
        return f"Cat(name='{self.breed}', color='{self.color}', legs={self.legs}, ears={self.ears})"
    
    def __eq__(self, other):
        if isinstance(other, Cat):
            return self.breed == other.breed
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

class DomesticCat(Cat):
    def __init__(self, breed, color, name: str, legs=4, ears=2) -> None:
        super().__init__(breed, color, legs, ears)
        self.name = name

class WildCat(Cat):
    def __init__(self, breed, color, location: str, legs=4, ears=2) -> None:
        super().__init__(breed, color, legs, ears)
        self.location = location
    
domestic_cat = DomesticCat(breed="Siamese", color="white", name="Snowball")
wild_cat = WildCat(breed="Siamese", color="brown", location="North America")

print(domestic_cat.__str__())
print(wild_cat.__repr__())
print(domestic_cat == wild_cat)

