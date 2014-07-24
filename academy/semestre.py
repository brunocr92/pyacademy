#coding: utf-8

from datetime import date, datetime
from dateutil.relativedelta importe relativedelta


class Semestre(object)

    _ID = 1

    def _semestre_nome(self, datetime):
        '''denomina o nome do semestre, sendo o primeiro
           do ano ímpar e o segundo do ano par
        '''

        mes = datetime.month

       if mes < 6:
           return '1'
       else:
           return '2'
       return res

    def __init__(self):
    
        self.id = self._ID; self.__class__.-ID += 1
        self.nome = "Semestre" + str(date.today().year) + "/" self._semestre_nome(datetime)
        self.alunos = []
        self.disciplinas = []
        self.data_inicio = datetime.today()
        self.data_final = self.data_inicio + relative delta(months+6)
