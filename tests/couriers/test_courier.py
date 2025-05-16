from methods.courier_methods import CourierMethods
from data import CreateCourier
import allure
import pytest

class TestCourierMethods:

    @allure.title('Проверка успешного создания курьера')
    def test_create_courier_passed(self):
        courier_methods = CourierMethods()
        status_code, response = courier_methods.create_courier()
        assert status_code == 201 and response == {'ok': True}
        courier_methods.delete_courier()


    @allure.title('Проверка создания дубля курьера')
    def test_create_courier_passed(self):
        courier_methods = CourierMethods()
        courier_methods.create_courier()
        courier_methods.create_courier()
        status_code, response = courier_methods.create_courier()
        assert status_code == 409 and response == {
            'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}



    @allure.title('Проверка неуспешного создания курьера')
    @pytest.mark.parametrize(
        "payload", [
            {'login': CreateCourier.LOGIN, 'firstname': CreateCourier.FIRSTNAME},
            {'password': CreateCourier.PASSWORD, 'firstname': CreateCourier.FIRSTNAME}
        ]
    )
    def test_create_courier_failed(self, payload):
        courier_methods = CourierMethods()
        status_code, response = courier_methods.create_courier_fail(payload)
        assert status_code == 400 and response == {
            "code": 400, "message": "Недостаточно данных для создания учетной записи"}


    @allure.title('Проверка удаления курьера')
    def test_delete_courier(self):
        courier_methods = CourierMethods()
        courier_methods.create_courier()
        status_code, response = courier_methods.delete_courier()
        assert status_code == 200 and response == {'ok': True}


    @allure.title('Проверка авторизации курьера')
    def test_auth_courier_passed(self):
        courier_methods = CourierMethods()
        courier_methods.create_courier()
        courier_methods.log_courier()
        status_code, response = courier_methods.log_courier()
        assert status_code == 200 and response['id']
        courier_methods.delete_courier()


    @allure.title('Проверка авторизации курьера c не полными данными')
    @pytest.mark.parametrize(
        "payload", [
            {"login": CreateCourier.LOGIN, "password": ""},
            {"login": "", "password": CreateCourier.PASSWORD}
        ]
    )
    def test_auth_courier_failed(self, payload):
        courier_methods = CourierMethods()
        status_code, response = courier_methods.log_courier_failed(payload)
        assert status_code == 400 and response == {'code': 400, 'message': 'Недостаточно данных для входа'}


    @allure.title('Проверка авторизации курьера с несуществующими данными')
    @pytest.mark.parametrize(
        "payload", [
            {"login": "ук34куцк43к43", "password": "34пуа3е"}
        ]
    )
    def test_auth_courier_not_found(self, payload):
        courier_methods = CourierMethods()
        status_code, response = courier_methods.log_courier_failed(payload)
        assert status_code == 404 and response == {'code': 404, 'message': 'Учетная запись не найдена'}
