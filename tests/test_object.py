from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.ubdate_object import UpdateObject
from endpoints.delete_object import DeleteObject
from data.read_data import ReadData
import allure


@allure.feature('Тестирование REST сайта restful-api')
class TestObject:

    @allure.story('Проверка POST запроса')
    def test_create_object(self):
        new_object_endpoint = CreateObject()
        request_data_payload = ReadData('data/payload_create.json')
        payload = request_data_payload.request_data()
        new_object_endpoint.new_object(payload)
        new_object_endpoint.check_response_is_200()
        new_object_endpoint.check_name(payload['name'])

    @allure.story('Проверка GET запроса')
    def test_get_object(self, obj_id):
        get_object_endpoint = GetObject()
        get_object_endpoint.get_by_id(obj_id)
        get_object_endpoint.check_response_is_200()
        get_object_endpoint.check_response_id(obj_id)

    @allure.story('Првоерка PUT запроса')
    def test_update_object(self, obj_id):
        update_object_endpoint = UpdateObject()
        update_data_payload = ReadData('data/payload_update.json')
        payload = update_data_payload.request_data()
        update_object_endpoint.update_by_id(obj_id, payload)
        update_object_endpoint.check_response_is_200()
        update_object_endpoint.check_response_name(payload['name'])

    @allure.story('Поверка DELETE запроса')
    def test_delete_object(self, obj_id):
        delete_object_endpoint = DeleteObject()
        delete_object_endpoint.delete_by_id(obj_id)
        delete_object_endpoint.check_response_is_200()

    @allure.story('Проваленный тест GET запрос')
    def test_failed(self, obj_id):
        get_object_endpoint = GetObject()
        get_object_endpoint.get_by_id(obj_id)
        get_object_endpoint.check_response_is_400()









