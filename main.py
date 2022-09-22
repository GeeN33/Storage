from abc import ABC, abstractmethod, abstractproperty
"""
Имитация программы, обслуживающую логистику, перемещения товара из склада в магазин
"""
class Storage(ABC):
    """
    абстрактный класс Storage
    """
    items = {}  # название: количество
    capacity = 100 # целое число

    @abstractmethod
    def add(self): #< название >, < количество >  - увеличивает запас items
        pass

    @abstractmethod
    def remove(self):  #< название >, < количество > - уменьшает запас items
        pass

    @property
    @abstractmethod
    def get_free_space(self): # вернуть количество свободных мест
        pass

    @property
    @abstractmethod
    def get_items(self): # возвращает сожержание склада в словаре {товар: количество}
        pass

    @property
    @abstractmethod
    def get_unique_items_count(self): # возвращает количество уникальных товаров.
        pass

class Store(Storage):
    """
    класс Store.
    """
    def __init__(self, items:dict):
        self.__items = items  # название: количество
        self.__capacity = 100  # целое число
    def add(self, name:str, count:int):  # < название >, < количество >  - увеличивает запас items
        if(self.__capacity < self.__capacity + count):
            self.__items[name] = count
    def remove(self,name:str, count:int):  #< название >, < количество > - уменьшает запас items
        del self.__items[name]
    @property
    def get_free_space(self) -> int : # вернуть количество свободных мест
        return self.__capacity - len(self.__items.keys())
    @property
    def get_items(self) -> dict: # возвращает сожержание склада в словаре {товар: количество}
        return self.__items
    @property
    def get_unique_items_count(self) -> int: # возвращает количество уникальных товаров.
        return len(self.__items.keys())

class Shop(Storage):
    """
     класс Shop
    """
    def __init__(self, items:dict):
        self.__items = items  # название: количество
        self.__capacity = 20  # целое число
    def add(self, name:str, count:int):  # < название >, < количество >  - увеличивает запас items
        if(self.__capacity < self.__capacity + count):
            self.__items[name] = count
    def remove(self,name:str, count:int):  #< название >, < количество > - уменьшает запас items
        del self.__items[name]
    @property
    def get_free_space(self) -> int : # вернуть количество свободных мест
        return self.__capacity - len(self.__items.keys())
    @property
    def get_items(self) -> dict: # возвращает сожержание склада в словаре {товар: количество}
        return self.__items
    @property
    def get_unique_items_count(self) -> int: # возвращает количество уникальных товаров.
        return len(self.__items.keys())

class Request:
    """
    класс Request
    """
    def __init__(self,froms:str , to:str, amount:int, product:str):
        self.__from = froms # "склад"
        self.__to = to  # "магазин"
        self.__amount = amount # 3
        self.__product = product # "печеньки"
    def __repr__(self)-> str:
        return f"Доставить {self.__amount} {self.__product} из {self.__from} в {self.__to}"
    def get_product(self) -> str:
        return self.__product
    def get_amount(self) -> int:
        return self.__amount

def print_store_shop(store:Store, shop:Shop):
    """
     Выводит товар магазина и склада
    """
    print('В склад хранится:')
    for k, v in store.get_items.items():
        print(v, k)
    print('-' * 21)
    print('В магазин хранится:')
    for k, v in shop.get_items.items():
        print(v, k)
    print('-' * 21)

def main():
    print('Для выхода из программы введите стоп')
    store = Store({'печеньки': 6, 'собачки': 4, 'коробки': 5})
    shop = Shop({'собачки': 2, 'коробки': 3})
    while True:
        print_store_shop(store, shop)
        print('Для перемещения товара из склада в магазин')
        p = input('Введи имя товара\n')
        while not p:
            print('поле товар не может быть пустым')
            p = input('Введи имя товара\n')
        if(p == 'стоп'): break

        a = input('Введи количество товара\n')
        if (a == 'стоп'): break
        while not a.isdigit():
            print('поле количество товара быть пустым или строкой')
            a = input('Введи количество товара\n')
            if (a == 'стоп'): break

        request = Request('склад', 'магазин', int(a), p)
        print(request)

        if request.get_product() in store.get_items:
            print('Продукт есть на складе')
            product = request.get_product()
            amount = request.get_amount()
            if store.get_items[product] >= amount:
                print('Нужное количество есть на складе')
                print(f'Курьер забрал {amount} {product} со склад')
                print(f'Курьер везет {amount} {product} со склад в магазин')
                print(f'Курьер доставил {amount} {product} в магазин')
                store.get_items[product] -= amount
                if shop.get_unique_items_count <= 5:
                    if request.get_product() in shop.get_items:
                        shop.get_items[product] += amount
                    else:
                        shop.get_items[product] = amount
                else:
                    print('В магазин недостаточно места, попобуйте что то другое')
            else:
                print('Не хватает на складе, попробуйте заказать меньше')
        else:
            print('Нет такого продукта на складе')
    print('-' * 21)

main()