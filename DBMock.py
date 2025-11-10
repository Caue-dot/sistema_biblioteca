

import os


tables = [
    'emprestimos.txt',
    'livros.txt',
    'reservas.txt',
    'usuarios.txt',
    'usuariosAtrasados.txt',
    'usuariosEmprestimos.txt'
]

class DBMock:

    def writeData(self, data, filepath):
        stringData = str(data)
        with open(filepath, 'a') as f:
            f.write(stringData + '\n')

    def checkData(text, filepath):
        if(text in open(filepath).read()):
            return True
        return False
    

    def findLines(filepath, signal , **criteria):
        lines = []
        with open(filepath, 'r') as f:
            if (not criteria):
                return [line.strip() for line in f]

            for line in f:

                registry = eval(line.strip())
                match = all(registry[c] == v for c,v in criteria.items())

                if(match and signal=='eq'):
                    lines.append(line.strip())
                elif(not match and signal=='ne'):
                    lines.append(line.strip())
        return lines

    def find(filepath, **criteria):
        with open(filepath, 'r') as f:
            for line in f:
                registry = eval(line.strip())
                match = all(registry[k] == v for k,v in criteria.items())

                if(match):
                    return eval(line)
        
        return None
    
    def get(filepath, signal=None ,**criteria):
        lines = DBMock.findLines(filepath, 'eq', **criteria)

        registries = []        
        for line in lines:
            registries.append(eval(line))
            
        return registries

    
    def update(data, filepath, **criteria):
        modified = False
        
        registries = DBMock.get(filepath)
        for registry in registries:
            if(all(registry[key] == value for key, value in criteria.items())):
                for editedElement in data:
                    registry[editedElement] = data[editedElement]
                modified = True
                break
        if(modified):
            with open(filepath, 'w') as f:
                for registry in registries:
                    f.write(str(registry) + '\n')

    def delete(filepath, **criteria):
        new_lines = DBMock.findLines(filepath, 'ne', **criteria)

        new_lines = list(map(lambda line: line + '\n', new_lines))
        with open(filepath, 'w') as f:
            f.writelines(new_lines)

    def initializeDB():
        os.mkdir('data')
        for table in tables:
            with open('data/' + table, 'w') as f:
                pass
        
        
        
        