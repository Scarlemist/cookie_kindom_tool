import pytest
import csv

from bin.model import Connection


@pytest.fixture(scope='function', autouse=True)
def start(request):
    """"""
    print('=' * 10 + request.function.__name__ + '=' * 10)
    yield
    print()
    print('=' * 50)


@pytest.fixture(scope='module')
def connect(request):
    """"""
    con = Connection()
    yield con


def test_get_all_topping(connect: Connection):
    connect.get_all_toppings()


def test_import_topping(connect: Connection):
    with open('./topping.csv', 'r', encoding='utf-8') as f:
        cr = csv.reader(f, delimiter=',')
        data = [row for row in cr]
        connect.import_toppings(data)


def test_search_topping(connect: Connection):
    cond_dict = {
        'type': 0,
        'ATK': 3,
        'CRIT': 2,
        'COOL': 1.3
    }
    rows = connect.search_toppings(cond_dict)
    for row in rows:
        print(row)


def test_fuzzy_search_topping(connect: Connection):
    cond_dict = [
        {
            'key': 'type',
            'value': 0,
            'operator': '='
        },
        {
            'key': 'ATK',
            'value': 2.5,
            'operator': '>='
        },
        {
            'key': 'COOL',
            'value': 1.5,
            'operator': '>='
        }
    ]
    rows = connect.fuzzy_search_toppings(cond_dict)
    for row in rows:
        print(row)


@pytest.mark.parametrize('name', ['野莓餅乾'])
def test_add_cookie(connect: Connection, name):
    connect.add_cookie(name, 10)
    connect.get_all_cookies()


def test_add_record(connect: Connection):
    connect.add_record(1, 1, 8)
    connect.get_records()


def test_get_top_record(connect: Connection):
    rows = connect.get_topping_records(1)
    for row in rows:
        print(row)


def test_delete_record(connect: Connection):
    rows = connect.get_topping_records(1)
    connect.delete_record(rows[-1][0], rows[-1][-1])
    for row in connect.get_topping_records(1):
        print(row)


def test_init_color(connect: Connection):
    connect.init_color()
    connect.get_color_setting()


def test_set_color(connect: Connection):
    connect.set_color(0, 'ffffff')
    connect.get_color_setting()
