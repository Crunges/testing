import Random
from collections import Counter


n_customers = random.randint(0, 100)
n_first_id = random.randint(0, 100)


def func1(n: int):
    """
    Функция, которая подсчитывает число покупателей, попадающих в каждую группу,
     если нумерация ID сквозная и начинается с 0.
    :param n:  n_customers (количество клиентов)
    :return:  Группа: Число покупателей
    """
    ID = []
    group = []
    for i in range(0, n):
        ID.append(i)
    print(ID)  # список id
    for i in ID:
        group.append(sum(map(int, str(i)[::-1])))
    print(group)  # список групп
    return Counter(group)


def func2(n: int, m: int):
    """
    Функция, которая подсчитывает число покупателей, попадающих в каждую группу,
     если ID начинается с произвольного числа.
    :param n: n_customers (количество клиентов)
    :param m: n_first_id (первый ID в последовательности).
    :return: Группа: Число покупателей
    """
    ID = []
    group = []
    for i in range(m, m + n):
        ID.append(i)
    print(ID)  # список id
    for i in ID:
        group.append(sum(map(int, str(i)[::-1])))
    print(group)  # список групп
    return Counter(group)


print(n_customers)
print(n_first_id)
print(func1(n_customers))
print(func2(n_customers, n_first_id))