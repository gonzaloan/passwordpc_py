import uuid

class PassValueModel:
    def __init__(self, application, value, password, description, pid=None):
        self.application = application
        self.value = value
        self.password = password
        self.description = description
        self.pid = pid or uuid.uuid4()

    def to_dict(self):
        return vars(self)
    
    @staticmethod
    def schema():
        return ['application','value','password','description','pid']