from utils import arrs


def test_get():
    """положительный индекс и он существует"""
    assert arrs.get([1, 2, 3], 1, "test") == 2
    """пустой массив"""
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    """Проверка с пустым массивом"""
    assert arrs.my_slice([], 0, 2) == []
    """Проверка с отрицательным start и end None"""
    assert arrs.my_slice([1, 2, 3, 4], -3) == [2, 3, 4]
    """Проверка со start=0 и end None"""
    assert arrs.my_slice([1, 2, 3, 4], 0) == [1, 2, 3, 4]
    """проверка если старт меньше -длинны строки"""
    assert arrs.my_slice([1, 2, 3, 4, 5], -10, 2) == [1, 2]