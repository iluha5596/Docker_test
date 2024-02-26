import json


class ReadData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_data = self.request_data()

    def request_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
