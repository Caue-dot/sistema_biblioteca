
from DBMock import DBMock
from Entity import Entity
from Reserva import Reserva

FILEPATH = 'data/livros.txt'

class Livro(Entity):
    def __init__(self):
        self.fields = ['titulo', 'autor', 'ano', 'ISBN', 'categoria', 'quantidade']
        self.requiredFields =  ['titulo', 'autor', 'ano', 'ISBN']
        self.defaults = {
            'quantidade': 0,
            'categoria': '',
        }
        self.filepath = FILEPATH 


    def register(self, data):

        if('ISBN' in data and DBMock.checkData(data['ISBN'], FILEPATH)):
            print('Essa ISBN já existe no sistema')
            return False

        super().register(data)
        return True
    
    def search(self, **query):
        books = DBMock.get(FILEPATH, **query)
        print('\nResultados: \n')
        for book in books:
            print('Nome: ' + book['titulo'])
            print('Ano: ' + str(book['ano']))
            print('Autor: '+ book['autor'])
            print('Quantidade: ' + str(book['quantidade']))
            print('ISBN:' + book['ISBN'])
            print('Categoria: '+ book['categoria'])
            print('-'*20)


        print(str(len(books)) + ' Resultados Encontrados \n')

    def changeQuantity(book, value):
        DBMock.update({'quantidade': int(book['quantidade'])+value}, FILEPATH, ISBN=book['ISBN'])
  
    def incrementQuantity(book, value):
            
        if(DBMock.checkData(book['ISBN'], 'data/reservas.txt') and int(book['quantidade']) <= 0):
            Reserva.alertReservations(book)
        Livro.changeQuantity(book, value)

    def decrementQuantity(book, value):
        Livro.changeQuantity(book, -value)

def main():
    livro = DBMock.find('data/livros.txt', ISBN='9788576573005')
    Livro.incrementQuantity(livro, 1)




if(__name__ == '__main__'):
    main()