from domain.dto import DTO
from domain.studenti import Student


class Service:
    
    def __init__(self, repository):
        self.repository = repository
        
    def adaugare_student(self, id, nume, numar_prezente, nota):
        """
        Functia transmite parametrii in zona de domain.Student si transmite entitatea nou formata catre repository
        :param id:
        :param nume:
        :param numar_prezente:
        :param nota:
        :return:
        """
        student = Student(id, nume, numar_prezente, nota)
        self.repository.add_studenti(student)
        
    def afisare(self):
        """

        :return:
        """
        return self.repository.print_all()
    
    def afisare_fisier(self):
        return self.repository.afisare_fisier()
    
    def acorda_bonus(self, p, b):
        try:
            p = int(p)
            b = int(b)
        except:
            raise ValueError("Punctajul/Bonusul trebuie sa fie int!")
            
        fisier = open("bonus.txt", 'w')
        
        all_studenti = self.repository.print_all()
        for student in all_studenti:
            if student.numar_prezente >= p and student.nota != 10:
                student.nota = min(student.nota + b, 10)
                studentus = DTO.id_nota(student.id, student.nota)
                fisier.write(f"{studentus.id},{studentus.nota}\n")
                
        self.repository.scrie()
                
        
                