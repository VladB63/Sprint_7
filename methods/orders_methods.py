import allure
import requests
from data import UrlKey
from methods.courier_methods import CourierMethods


class OrderMethods:

    @allure.step('Создание заказа')
    def create_orders(self, parametrs):
        response = requests.post(f'{UrlKey.BASE_URL}{UrlKey.ORDERS_URL}', json=parametrs)
        return response.status_code, response.json()


    @allure.step('Принятие заказа')
    def accept_order(self):
        CourierMethods.log_courier()
        status_code, response = CourierMethods.log_courier()
        courier_id = response.get('id')
        self.create_orders()
        status_code, response = self.create_orders()
        orders_id = response.get('id')
        response = requests.put(f'{UrlKey.BASE_URL}{UrlKey.ORDER_ACCEPT}{orders_id}?courierId={courier_id}')
        return response.status_code, response.json()


    @allure.step('Получение заказа по номеру')
    def receiving_order(self):
        self.create_orders()
        status_code, response = self.create_orders()
        track_id = response.get('track')
        response = requests.put(f'{UrlKey.BASE_URL}{UrlKey.ORDER_ACCEPT}track?t={track_id}')
        return response.status_code, response.json()


    @allure.step('Отмена заказа по номеру')
    def order_cancel(self):
        self.create_orders()
        status_code, response = self.create_orders()
        track_id = response.get('track')
        response = requests.put(f'{UrlKey.BASE_URL}{UrlKey.ORDER_CANCEL}?track={track_id}')
        return response.status_code, response.json()


    @allure.step('Получение списка заказов')
    def order_list(self, parametrs):
        response = requests.get(f'{UrlKey.BASE_URL}{UrlKey.ORDERS_URL}', json=parametrs)
        return response.status_code, response.json()
