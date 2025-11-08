

from DBMock import DBMock
from Entity import Entity


FILEPATH = 'data/usuarios.txt'

class Usuario(Entity):

    def __init__(self):
        self.fields = ['nome', 'matricula', 'tipo', 'email']
        self.requiredFields = ['nome', 'matricula','email', 'tipo']
        self.defaults = {'tipo': 'Aluno'}
        self.filepath = FILEPATH 


    def register(self, data):
        
        if('matricula' in data and DBMock.checkData(data['matricula'], self.filepath)):
            print('Essa matricula já existe no sistema')
            
        super().register(data)
        return True

    def getUserLoans(self, matricula):
        if(not DBMock.checkData(matricula, FILEPATH)):
            print('Esse usuário não existe')
            
        user = DBMock.find('data/usuarios.txt', matricula=matricula)
        loans = DBMock.get('data/emprestimos.txt', matricula=matricula)
        print(f'\nEmprestimos realizados pelo {user['nome']}: \n')
        for loan in loans:
            book = DBMock.find('data/livros.txt', ISBN=loan['ISBN'])
            print(f'Titulo: {book['titulo']}')
            print(f'ISBN: {book['ISBN']}')
            print(f'Status: {loan['status']}')
            print(f'Data do emprestimo: {loan['createdAt']}')
            print(f'Data de vencimento: {loan['data']}')
            print('-'*20)




def main():
    usuario = Usuario()
    # dataTest = {'nome': 'marcos','matricula': '24242323223552322', 'tipo': 'Professor', 'asdasd': 'asdsad'}
    # usuario.register(dataTest)
    usuario.getUserLoans('24242323223552322')

if(__name__ == '__main__'):
    main()