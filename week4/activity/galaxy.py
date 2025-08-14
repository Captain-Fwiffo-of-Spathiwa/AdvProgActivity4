from typing import Any

class Galaxy:
    def __init__(self, name: str, mass: float):
        self.name = name
        self.mass = mass

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Galaxy):
            return NotImplemented
        return self.mass == other.mass and self.name == other.name

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Galaxy):
            return NotImplemented
        if self.mass != other.mass:
            return self.mass < other.mass
        return self.name < other.name

    def __le__(self, other: Any) -> bool:
        return self == other or self < other

    def __gt__(self, other: Any) -> bool:
        return not self <= other

    def __ge__(self, other: Any) -> bool:
        return not self < other

    def __ne__(self, other: Any) -> bool:
        return not self == other

    def __hash__(self) -> int:
        data = (self.name + str(self.mass)).encode('utf-8')
        permutation_table = list(range(256))
        hash_value = 0
        for byte in data:
            hash_value = permutation_table[hash_value ^ byte]
        return hash_value



