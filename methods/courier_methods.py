import allure
import requests
from data import UrlKey, CreateCourier

class CourierMethods:

    @allure.step('Создание курьера')
    def create_courier(self):
        payload = {
            'login': CreateCourier.LOGIN,
            'password': CreateCourier.PASSWORD,
            'firstname': CreateCourier.FIRSTNAME
        }
        response = requests.post(f'{UrlKey.BASE_URL}{UrlKey.COURIERS_URL}', json=payload)
        return response.status_code, response.json()

    @allure.step('Создание курьера с не полными данными')
    def create_courier_fail(self, payload):
        response = requests.post(f'{UrlKey.BASE_URL}{UrlKey.COURIERS_URL}', json=payload)
        return response.status_code, response.json()


    @allure.step('Авторизация курьера')
    def log_courier(self):
        payload = {
            'login': CreateCourier.LOGIN,
            'password': CreateCourier.PASSWORD
        }
        response = requests.post(f'{UrlKey.BASE_URL}{UrlKey.COURIER_LOG}', json=payload)
        return response.status_code, response.json()


    @allure.step('Авторизация курьера с не полными данными')
    def log_courier_failed(self, payload):
        response = requests.post(f'{UrlKey.BASE_URL}{UrlKey.COURIER_LOG}', json=payload)
        return response.status_code, response.json()


    @allure.step('Получение заказов')
    def give_orders_count(self):
        self.log_courier()
        status_code, response = self.log_courier()
        courier_id = response.get('id')
        response = requests.get(f'{UrlKey.BASE_URL}{UrlKey.COURIERS_URL}{courier_id}{UrlKey.COURIER_ORDERS}')
        return response.status_code, response.json()


    @allure.step('Удаление курьера')
    def delete_courier(self):
        self.log_courier()
        status_code, response = self.log_courier()
        courier_id = response.get('id')
        response = requests.delete(f'{UrlKey.BASE_URL}{UrlKey.COURIERS_URL}{courier_id}')
        return response.status_code, response.json()
