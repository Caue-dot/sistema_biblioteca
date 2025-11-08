
from datetime import datetime
from DBMock import DBMock
from Emprestimo import Emprestimo


class EmprestimoLog():
    
    
    def generateExpiredLoans():
        loans = DBMock.get('data/emprestimos.txt', status='ativo')
        expiredLoans = []

        for loan in loans:
            if(Emprestimo.verifyLoanDate(loan['data'])):
                expiredLoans.append(loan)
        with open('data/usuariosAtrasados.txt', 'a') as f:
            f.write('Log gerado em: ' + str(datetime.now()) + '\n \n')
            f.write('Usuarios Atrasados: \n \n')
            for loan in expiredLoans:
                user = DBMock.find('data/usuarios.txt', matricula=loan['matricula'])
                book = DBMock.find('data/livros.txt', ISBN=loan['ISBN'])

                f.write('Nome do usuário: ' + user['nome'] + '\n')
                f.write('Matricula: ' + user['matricula'] + '\n')
                f.write('Titulo do Livro: ' + book['titulo'] + '\n')
                f.write('ISBN: ' +  book['ISBN'] + '\n')
                f.write('Data de entrega: '+ loan['data'] + '\n')
                f.write('-'*20 + '\n')
            f.write('\n \n')

    def generatePendentLoans():
        loans = DBMock.get('data/emprestimos.txt', status='ativo')

        with open('data/usuariosEmprestimos.txt', 'a') as f:
            f.write('Log gerado em: ' + str(datetime.now()) + '\n \n')
            f.write('Emprestimos: \n \n')
            for loan in loans:
                user = DBMock.find('data/usuarios.txt', matricula=loan['matricula'])
                book = DBMock.find('data/livros.txt', ISBN=loan['ISBN'])

                f.write('Nome do usuário: ' + user['nome'] + '\n')
                f.write('Matricula: ' + user['matricula'] + '\n')
                f.write('Titulo do Livro: ' + book['titulo'] + '\n')
                f.write('ISBN: ' +  book['ISBN'] + '\n')
                f.write('Data de entrega: '+ loan['data'] + '\n')
                f.write('-'*20 + '\n')
            f.write('\n \n')

