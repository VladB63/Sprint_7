import random


class UrlKey:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
    ORDERS_URL = 'orders'
    COURIERS_URL = 'courier/'
    COURIER_LOG = 'courier/login/'
    COURIER_ORDERS = 'ordersCount/'
    ORDER_ACCEPT = 'orders/accept/'
    ORDER_CANCEL = 'orders/cancel/'

# осознанно не стал и пользовать код со страницы задания
# слишком громоздкий и мне кажется избыточный
class CreateCourier:
    LOGIN = f"YandexVezunTrue{random.randint(10, 1000)}"
    PASSWORD = random.randint(10, 100)
    FIRSTNAME = "Иван"



class Order:
    ORDER_DATA_1 = {
        "firstName": "Федор",
        "lastName": "Шабашин",
        "address": "Мира, 142",
        "metroStation": 4,
        "phone": "+7 800 111 35 35",
        "rentTime": 5,
        "deliveryDate": "2025-05-20",
        "comment": "Жду",
        "color": [
            "BLACK"
        ]
    }
    ORDER_DATA_2 = {
        "firstName": "Иван",
        "lastName": "Строгий",
        "address": "Мира, 162",
        "metroStation": 4,
        "phone": "+7 800 111 22 35",
        "rentTime": 2,
        "deliveryDate": "2025-05-26",
        "comment": "Жду",
        "color": [
            "GREY",
            "BLACK"

        ]
    }
    ORDER_DATA_3 = {
        "firstName": "Федор",
        "lastName": "Мирный",
        "address": "Мира, 172",
        "metroStation": 4,
        "phone": "+7 800 111 33 35",
        "rentTime": 5,
        "deliveryDate": "2025-05-21",
        "comment": "Жду",
        "color": [
            "BLACK"
        ]
    }
    ORDER_DATA_4 = {
        "firstName": "Иван",
        "lastName": "Строгий",
        "address": "Мира, 182",
        "metroStation": 4,
        "phone": "+7 800 111 77 35",
        "rentTime": 2,
        "deliveryDate": "2025-05-27",
        "comment": "Жду",
        "color": []
    }