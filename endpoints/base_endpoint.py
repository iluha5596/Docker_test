import allure


class Endpoint:
    response = None
    response_json = None

    def check_response_is_200(self):
        with allure.step('Проверка, что код ответа == 200'):
            assert self.response.status_code == 200

    def check_response_is_400(self):
        with allure.step('Проверка, что код ответа == 400'):
            assert self.response.status_code == 400, f'Статус код не равен 400, статус код == {self.response.status_code}'

