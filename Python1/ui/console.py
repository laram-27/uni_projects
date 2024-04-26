class Console:

    def __init__(self, service):
        self._service = service

    def _adaugare_student(self):
        id = input("ID: ")
        nume = input("NUME: ")
        numar_prezente = input("NUMAR PREZENTE: ")
        nota = input("NOTA:")

        try:
            self._service.adaugare_student(id, nume, numar_prezente, nota)
        except ValueError as error:
            print(error)

    def _afisare_fisier(self):
        for student in self._service.afisare_fisier():
            print(f"ID: {str(student.id)}\n"
                  f"NUME: {student.nume}\n"
                  f"Numar Prezente: {str(student.numar_prezente)}\n"
                  f"Nota: {str(student.nota)}\n")

    def _afisare(self):
        for student in self._service.afisare():
            print(f"ID: {str(student.id)}\n"
                  f"NUME: {student.nume}\n"
                  f"Numar Prezente: {str(student.numar_prezente)}\n"
                  f"Nota: {str(student.nota)}\n")

    def _acordare_bonus(self):
        p = input("PREZENTE: ")
        b = input("BONUS: ")
        self._service.acorda_bonus(p,b)

    def run_menu(self):
        while True:
            print("1 - Afisare fisier.\n"
                  "2 - Adaugare student.\n"
                  "3 - Afisare studenti din baza de date.\n"
                  "4 - Acordare bonus.\n")

            options = {"1": self._afisare_fisier,
                       "2": self._adaugare_student,
                       "3": self._afisare,
                       "4": self._acordare_bonus}

            opt = input("COMANDA: ")

            try:
                options[opt]()
            except KeyError as ke:
                print(ke)
