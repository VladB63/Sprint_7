import pytest
from data import CreateCourier
from methods.courier_methods import CourierMethods

@pytest.fixture()
def courier():
    courier_methods = CourierMethods()
    courier_methods.create_courier(CreateCourier.LOGIN, CreateCourier.PASSWORD, CreateCourier.FIRSTNAME)
    yield courier_methods
    courier_methods.delete_courier()

