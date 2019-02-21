import csv, os
from passwords.models import PassValueModel
class PassValueService:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_pass_value(self, pass_value):
        with open(self.table_name, mode = 'a') as f:
            writer = csv.DictWriter(f, fieldnames=PassValueModel.schema())
            writer.writerow(pass_value.to_dict())
    
    def list_pass_values(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=PassValueModel.schema())
            return list(reader)
    
    def update_pass_value(self, updated_pass_value):
        pass_values = self.list_pass_values()
        updated_pass_values = []
        for pass_value in pass_values:
            if pass_value['pid'] == updated_pass_value.pid:
                updated_pass_values.append(updated_pass_value.to_dict())
            else:
                updated_pass_values.append(pass_value)
        self._save_to_disk(updated_pass_values)
    
    def _save_to_disk(self, pass_values):
        tmp_table_name = self.table_name + '.tmp'
        with open(tmp_table_name, mode='w') as f:
            writer = csv.DictWriter(f, fieldnames=PassValueModel.schema())
            writer.writerows(pass_values)
        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)

    def delete_pass_value(self, pass_value_to_delete):
        pass_values_list = self.list_pass_values()
        pass_values_list.remove(pass_value_to_delete[0])
        self._save_to_disk(pass_values_list)


