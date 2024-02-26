import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from data.read_data import ReadData


@pytest.fixture()
def obj_id():
    create_object = CreateObject()
    request_data_payload = ReadData('data/payload_create.json')
    payload = request_data_payload.request_data()
    create_object.new_object(payload)
    yield create_object.response_json['id']
    delete_object = DeleteObject()
    delete_object.delete_by_id(create_object.response_json['id'])
