from datetime import date
from materia import Materia
class Sessao:
    def __init__(self, materia: Materia, minutos: int, data: date | None = None):
        self.materia = materia
        self.minutos = minutos
        self.data = data or date.today()






       
    

        
