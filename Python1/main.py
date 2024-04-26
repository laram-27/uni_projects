from repository.repository import Repository
from service.service import Service
from ui.console import Console


if __name__ == '__main__':
    student_repository = Repository()
    serv = Service(student_repository)
    console = Console(serv)
    
    console.run_menu()
