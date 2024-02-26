import allure
import requests
from endpoints.base_endpoint import Endpoint


class UpdateObject(Endpoint):

    def update_by_id(self, object_id, payload):
        with allure.step('Отправка запроса'):
            self.response = requests.put(f'https://api.restful-api.dev/objects/{object_id}', json=payload)
        self.response_json = self.response.json()

    def check_response_name(self, name):
        with allure.step('Проверка того, что был верно записан отправленный запрос'):
            assert self.response_json['name'] == name
