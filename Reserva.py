from DBMock import DBMock
from Entity import Entity

FILEPATH = 'data/reservas.txt'

class Reserva(Entity):

    def __init__(self):
        self.fields = ['matricula', 'ISBN']
        self.requiredFields = ['ISBN', 'matricula']
        self.defaults = {}
        self.filepath = FILEPATH 

    def register(self, data):
        
        book = DBMock.find('data/livros.txt', ISBN=data['ISBN'])

        if(int(book['quantidade']) > 0):
            print('Esse livro está disponivel, não é possível reserva-lo')
            return False
        
        if(DBMock.find(FILEPATH, ISBN=data['ISBN'], matricula=data['matricula'])):
            print('Esse usuário já reservou esse livro')
            return False

        super().register(data)
        return True

    def alertReservations(book):
        reservations = DBMock.get('data/reservas.txt', ISBN=book['ISBN'])

        for reservation in reservations:
            user = DBMock.find('data/usuarios.txt', matricula=reservation['matricula'])
            print('Um usuário reservou esse livro, mandado email para ' + user['email'])

            DBMock.delete('data/reservas.txt', ISBN=book['ISBN'])