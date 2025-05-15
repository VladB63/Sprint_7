import pytest
import allure
from data import Order
from methods.orders_methods import OrderMethods


class TestOrderMethods:

    @allure.title('Создание заказа с проверкой параметров и получение трек номера')
    @pytest.mark.parametrize(
    "order_date", [Order.ORDER_DATA_1, Order.ORDER_DATA_2, Order.ORDER_DATA_3, Order.ORDER_DATA_4]
    )
    def test_create_order(self, order_date):
        order_methods = OrderMethods()
        status_code, response = order_methods.create_orders(order_date)
        assert status_code == 201 and response["track"]


    @allure.title('Проверка получение списка заказов')
    @pytest.mark.parametrize(
        "order_params", [
            {"courierId": "", "nearestStation": ["1", "2"], "limit": "", "page": ""},
            {"courierId": "1", "nearestStation": ["3"], "limit": "20", "page": "1"}
        ]
    )
    def test_giv_order_list(self, order_params):
        order_methods = OrderMethods()
        status_code, response = order_methods.order_list(order_params)
        assert status_code == 200 and response["orders"]