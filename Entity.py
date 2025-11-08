
from DBMock import DBMock

class Entity:

    def index(self):
        registries = []
        with open(self.filepath, 'r') as f:
            registries = [eval(line.strip()) for line in f]

        
        return registries

    def register(self, data):
        if(not self.validateRequiredData(data)):
            print('Você precisa incluir: ' + ', '.join(self.requiredFields))
            return False

        data = self.truncateDataWithoutField(data)
        data = self.fillDefaults(data)

        dbmock = DBMock()
        dbmock.writeData(data, self.filepath)
        return True

    def validateRequiredData(self, data):
        for field in self.requiredFields:
            if(field not in data):
                return False
        return True
    
    def fillDefaults(self, data: dict):
        newData = data.copy()
        for field in self.defaults:
            if(field not in data):
                newData[field] = self.defaults[field]
        
        return newData

    
    def truncateDataWithoutField(self, data : dict):
        newData = data.copy()
        for field in data:
            if(field not in self.fields):
                newData.pop(field)
        
        return newData

    