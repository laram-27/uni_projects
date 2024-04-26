
class Student:

    def __init__(self, id, nume, numar_prezente, nota):
        self.id = self._validare_id(id)
        self.nume = self._validare_nume(nume)
        self.numar_prezente = self._validare_prezente(numar_prezente)
        self.nota = self._validare_nota(nota)
        
    def _validare_id(self, id):
        """

        :param id:
        :return:
        """
        try:
            return int(id)
        except:
            raise ValueError("ID ul trebuie sa fie de tip int!")
        
    def _validare_nume(self, nume):
        """

        :param nume:
        :return:
        """
        if nume == "":
            raise ValueError("Numele trebuie sa contina cel putin un caracter")
        
        if len(nume.split(" ")) < 2:
            raise ValueError("Numele trebuie sa contina cel putin 2 cuvinte!")
        
        for cuvant in nume.split(" "):
            if len(cuvant) < 3:
                raise ValueError("Unu din nume are mai putin de 3 caractere!")

        return nume
            
    def _validare_prezente(self,numar_prezente):
        """

        :param numar_prezente:
        :return:
        """
        try:
            numar_prezente = int(numar_prezente)
        except:
            raise ValueError("Numar prezente trebuie sa fie un int!")
        
        if numar_prezente < 0:
            raise ValueError("Numar prezente trebuie sa fie pozitiv!")
        
        return numar_prezente
    
    def _validare_nota(self, nota):
        """

        :param nota:
        :return:
        """
        try:
            nota = int(nota)
        except:
            raise ValueError("Nota trebuie sa fie de tip int!")
        
        if nota < 0 and nota > 10:
            raise ValueError("Nota trebuie sa fie in intervalul [0,10]")
        
        return nota
    
    def __str__(self):
        return f"{self.id} {self.nume} {self.numar_prezente} {self.nota}"
            