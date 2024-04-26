
from domain.studenti import Student


class Repository:
    
    def __init__(self):
        self.all_studenti = {}
        self.citire()
        
    def add_studenti(self, student):
        if self.get_byID(student.id) is not None:
            raise ValueError("ID este deja existent!")
        self.all_studenti[student.id] = student
        self.scrie()
        
    def get_byID(self, id):
        if id in self.all_studenti:
            return self.all_studenti[id]
        return None
    
    def print_all(self):
        return list(self.all_studenti.values())
    
    def scrie(self):
        fisier = open("studenti.txt", 'w')
        for student in self.print_all():
            fisier.write(f"{student.id},{student.nume},{student.numar_prezente},{student.nota}\n")
        
        fisier.close()
        
    def citire(self):
        try:
            fisier = open("studenti.txt", 'r')
            file_list = fisier.readlines()
            for line, e in enumerate(file_list):
                file_list[line] = e.strip()
                linie = file_list[line].split(",")
                student = Student(linie[0], linie[1], linie[2], linie[3])
                self.all_studenti[student.id] = student
        except:
            raise ValueError("FISIER INEXISTENT/NU ARE DATE!")
 
    def afisare_fisier(self):
        try:
            studenti = {}
            
            fisier = open("studenti.txt", 'r')
            file_list = fisier.readlines()
            for line, e in enumerate(file_list):
                file_list[line] = e.strip()
                linia = file_list[line].split(",")
                student = Student(linia[0], linia[1], linia[2], linia[3])
                studenti[student.id] = student
                
            return list(studenti.values())
        except:
            raise ValueError("FISIER INEXISTENT/NU ARE DATE!")
        