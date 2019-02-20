import csv, os
from passwords.models import PassValueModel
class PassValueService:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_passValue(self, passValue):
        with open(self.table_name, mode = 'a') as f:
            writer = csv.DictWriter(f, fieldnames=PassValueModel.schema())
            writer.writerow(passValue.to_dict())
    
    def list_passValues(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=PassValueModel.schema())
            return list(reader)
    
    def update_passvalue(self, updated_passValue):
        passValues = self.list_passValues()
        updated_passValues = []
        for passvalue in passValues:
            if passvalue['pid'] == updated_passValue.pid:
                updated_passValues.append(updated_passValue.to_dict())
            else:
                updated_passValues.append(passvalue)
        self._save_to_disk(updated_passValues)
    
    def _save_to_disk(self, passvalues):
        tmp_table_name = self.table_name + '.tmp'
        with open(tmp_table_name) as f:
            writer = csv.DictWriter(f, fieldnames=PassValueModel.schema())
            writer.writerows(passvalues)
        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)

            