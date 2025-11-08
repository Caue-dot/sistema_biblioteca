
from Emprestimo import Emprestimo
from EmprestimoLog import EmprestimoLog
from Livro import Livro
from Reserva import Reserva
from Usuario import Usuario

userModel = Usuario()
bookModel = Livro()
loanModel = Emprestimo()
reservationModel = Reserva()

def main():
    menu()

def closeProgam():
    print('Fechando o progama...')
    exit()

def menu():
    print('Bem vindo ao Sistema! \nEscolha uma opção abaixo:')
    print('(1) Fazer emprestimo')
    print('(2) Pesquisar livro')
    print('(3) Cadastrar livro')
    print('(4) Devolver livro')
    print('(5) Cadastrar usuário')
    print('(6) Gerar um relatorio')
    print('(7) Cadastrar uma reserva')
    print('(8) Consultar emprestimos de um usuário')

    option = input('\nDigite a opção que deseja escolher: ')
    #TODO: Adicionar a interface da reserva
    match option:
        case '1':
            interfaceRegisterLoan()
        case '2':
            menuBookSearch()
        case '3':
            interfaceRegisterBook()
        case '4':
            interfaceGiveBackBook()
        case '5':
            interfaceRegisterUser()
        case '6':
            menuRelatorio()
        case '7':
            interfaceRegisterReservation()
        case '8':
            interfaceGetUserLoans()
        case _:
            print('Opção Inválida')
            option = input('\nQuer tentar novamente?(s/n) ')
            if(option.lower() == 's'):
                menu()
            else:
                closeProgam()
    
    restart = input('Deseja realizar outra ação?(s/n): ')

    if(restart.lower() == 's'):
        menu()
    else:
        closeProgam()
        

def menuRelatorio():
    print('(1) Gerar relatório de emprestimos atrasados')
    print('(2) Gerar relatório de emprestimos pendentes')
    print('(3) Voltar')

    option = input('Digite a opção que deseja escolher: ')

    match option:
        case '1':
            EmprestimoLog.generateExpiredLoans()
            print('Log gerado com sucesso em data/usuariosAtrasados.txt!')
        case '2':
            EmprestimoLog.generatePendentLoans()
            print('Log gerado com sucesso em data/usuarios.txt!')
        case '3':
            main()

def menuBookSearch():
    print('Qual campo abaixo você gostaria de pesquisar?\n')
    print('(1) Título')
    print('(2) Categoria')
    print('(3) Ano')
    print('(4) Quantidade')
    print('(5) ISBN')

    option = input('Digite a opção que deseja escolher: ')
    match option:
        case '1':
            fieldSearch = 'titulo'
        case '2':
            fieldSearch = 'categoria'
        case '3':
            fieldSearch = 'ano'
        case '4':
            fieldSearch = 'quantidade'
        case '5':
            fieldSearch = 'ISBN'
        case _:
            print('Opção Inválida')
            exit()

    interfaceBookSearch(fieldSearch)

def interfaceBookSearch(fieldSearch):

    search = input('Digite o que deseja pesquisar: ')
    bookModel.search(**{fieldSearch: search})



def interfaceRegisterUser():
    data = {}
    data['nome'] = input('Digite o nome do usuário: ')
    data['matricula'] = input('Digite a matrícula: ')
    data['email'] = input('Digite o email: ')
    data['tipo'] = input('Digite o tipo de usuário (Professor/Aluno): ')
    
    success = userModel.register(data)
    if(success):
        print('Usuário cadastrado com sucesso!')


def interfaceRegisterBook():
    data = {}
    data['titulo'] = input('Digite o titulo: ')
    data['autor'] = input('Digite o autor do livro: ')
    data['ano'] = input('Digite o ano de publicação do livro: ')
    data['categoria'] = input('Digite a categoria(opcional): ')
    data['quantidade'] = input('Digite a quantidade em estoque(Padrão: 0): ')
    data['ISBN'] = input('Digite o ISBN: ')

    
    success = bookModel.register(data)
    if(success):
        print('\nLivro cadastrado com successo!')


def interfaceRegisterLoan():
    data = {}
    data['matricula'] = input('Digite a matricula do usuário: ')
    data['ISBN'] = input('Digite o ISBN do lívro: ')
    data['data'] = input('Insira a data máxima de entrega(YYYY-MM-DD): ')

    success = loanModel.register(data)

    if(success):
        print('\nEmprestimo realizado com sucesso!')

def interfaceGiveBackBook():
    data = {}
    data['matricula'] = input('Digite a matricula do usuário: ')
    data['ISBN'] = input('Digite o ISBN do lívro: ')

    success = loanModel.returnBook(data)

    if(success):
        print('\nLivro devolvido com sucesso!')

def interfaceRegisterReservation():
    data = {}
    data['matricula'] = input('Digite a matricula do usuário: ')
    data['ISBN'] = input('Digite o ISBN do lívro: ')

    success = reservationModel.register(data)
    print(success)
    if(success):
        print('Reserva realizada com sucesso!')

def interfaceGetUserLoans():
    matricula = input ('Digite a matricula do usuário: ')

    userModel.getUserLoans(matricula)

if (__name__ == '__main__'):
    main()
