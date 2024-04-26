
from dataclasses import dataclass


@dataclass
class AcordareNota:
    id: int
    nota: int


class DTO:
    
    @staticmethod
    def id_nota(id, nota):
        return AcordareNota(id, nota)
