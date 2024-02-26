import allure
import requests
from endpoints.base_endpoint import Endpoint


class CreateObject(Endpoint):

    def new_object(self, payload):
        with allure.step('Отправка запроса'):
            self.response = requests.post('https://api.restful-api.dev/objects', json=payload)
        self.response_json = self.response.json()

    def check_name(self, name):
        with allure.step('Проверка того, что был верно записан отправленный запрос'):
            assert self.response_json['name'] == name


