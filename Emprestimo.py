

import Config
from DBMock import DBMock
from Entity import Entity
from Livro import Livro
from datetime import datetime

from Reserva import Reserva


FILEPATH = 'data/emprestimos.txt'

class Emprestimo(Entity):

    def __init__(self):
        self.filepath = FILEPATH 
        self._initRegister()

    def _initRegister(self):
        self.fields = ['ISBN', 'matricula', 'data', 'status' ,'createdAt']
        self.requiredFields = ['ISBN', 'matricula', 'data']
        self.defaults = {'status': 'ativo'}
        
    def _initReturnBook(self):
        self.fields = ['ISBN', 'matricula']
        self.requiredFields = ['ISBN', 'matricula']
        self.defaults = {}


    def register(self, data):
        self._initRegister()
        book = DBMock.find('data/livros.txt', ISBN=data['ISBN'])

        if(not book):
            print('Esse livro não está cadastrado no sistema!')
            return False

        if(not DBMock.checkData(data['matricula'], 'data/usuarios.txt')):
            print('Esse usuario não está cadastrado no sistema!')
            return False

        if(int(book['quantidade']) < 1):
            print('Esse livro está esgotado, tente novamente mais tarde!')
            self.promptReservation(data)
            return False
            
        
        if(DBMock.find(FILEPATH, ISBN=data['ISBN'], matricula=data['matricula'])):
            print('Este usuário já fez o emprestimo desse livro')
            return False

        Livro.decrementQuantity(book, 1)

        data['createdAt'] = str(datetime.now().date())

        super().register(data)

        return True

    def returnBook(self, data):
        self._initReturnBook()

        if (not super().validateRequiredData(data)):
            print('Você precisa incluir: ' + ', '.join(self.requiredFields))
            return

        loan = DBMock.find(FILEPATH, ISBN=data['ISBN'], matricula=data['matricula'])

        if (not loan):
            print('Esse usuário não solicitou um emprestimo desse livro')
            return
        

        if(Emprestimo.verifyLoanDate(loan['data'])):
            Emprestimo.applyFine(loan['createdAt'], loan['data'])


        DBMock.update({'status': 'inativo'}, FILEPATH, ISBN=data['ISBN'], matricula=data['matricula'])        
        
        book = DBMock.find('data/livros.txt' ,ISBN=data['ISBN'])
        Livro.incrementQuantity(book, 1)

        return True
    
    def verifyLoanDate(loanDate):
        loanDate = datetime.strptime(loanDate, '%Y-%m-%d')
        todayDate = datetime.now()

        return loanDate < todayDate

    def calculateFine(startDate: datetime, endDate: datetime):
        difference: datetime = endDate-startDate
        return int(difference.days) * Config.FINEPRICE
    
    def applyFine(createdAt, deliverDate):
        createdAt = datetime.strptime(createdAt, '%Y-%m-%d')
        deliverDate = datetime.strptime(deliverDate, '%Y-%m-%d')
        fine = Emprestimo.calculateFine(createdAt, deliverDate)
        print(f'Usuario atrasou a devolução, será aplicado multa de R${fine} reais!')

    def promptReservation(self, data):
        option = input('Você gostaria de reservar esse livro?(s/n): ')
        if(option.lower() == 's'):
            reservaModel = Reserva()
            reservaModel.register(data)
            print('Reserva realizada com sucesso!')

def main():
    loanModel = Emprestimo()
    loanModel.returnBook({'ISBN': '4104101', 'matricula': '24242323223552322'})


if(__name__ == '__main__'):
    main()

