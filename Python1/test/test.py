from unittest import TestCase

from domain.studenti import Student
from repository.repository import Repository
from service.service import Service


class TestADAUGARE(TestCase):

    def test_domain(self):
        student = Student("1", "asd asd", "12", "10")

        assert student.id == 1
        assert student.nume == "asd asd"
        assert student.numar_prezente == 12
        assert student.nota == 10

        with self.assertRaises(ValueError):
            student = Student("abc", "asd asd", "12", "10")

            student = Student("1", "", "12", "10")
            student = Student("1", "asd", "12", "10")
            student = Student("1", "as asd", "12", "10")

            student = Student("1", "asd asd", "abc", "10")

            student = Student("1", "asd asd", "12", "abc")

    def test_repository(self):
        student_repository = Repository()

        all_studenti = student_repository.all_studenti
        assert len(all_studenti) == 0

        student_repository.add_studenti(Student("1", "asd asd", "12", "10"))

        assert len(all_studenti) == 3

        assert all_studenti[0].id == 1
        assert all_studenti[0].nume == "asd asd"
        assert all_studenti[0].numar_prezente == 12
        assert all_studenti[0].nota == 10

        with self.assertRaises(ValueError):
            student_repository.add_studenti(Student("1", "asd asd", "12", "10"))

    def test_service(self):
        student_repository = Repository()
        student_serv = Service(student_repository)

        student_serv.adaugare_student("1", "asd asd", "12", "10")
        all_studenti = student_serv.afisare()

        assert len(all_studenti) == 1
        assert all_studenti[0].id == 1
        assert all_studenti[0].nume == "asd asd"
        assert all_studenti[0].numar_prezente == 12
        assert all_studenti[0].nota == 10


