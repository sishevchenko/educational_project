"""Реализуйте функцию fill_up_missing_dates(), которая принимает на вход один аргумент:

dates — список строковых дат в формате DD.MM.YYYY Функция должна возвращать список, в котором содержатся все даты из
списка dates, расположенные в порядке возрастания, а также все недостающие промежуточные даты.

Примечание 1. Рассмотрим первый тест. Список dates содержит период с 01.11.2021 по 07.11.2021:

dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
в котором отсутствуют даты 02.11.2021, 05.11.2021, 06.11.2021. Тогда вызов функции:

fill_up_missing_dates(dates)
должен вернуть список:

['01.11.2021', '02.11.2021', '03.11.2021', '04.11.2021', '05.11.2021', '06.11.2021', '07.11.2021']
Примечание 2. Функция должна создавать и возвращать новый список, а не изменять переданный.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию fill_up_missing_dates(),
но не код, вызывающий ее. """

from datetime import date, datetime


def fill_up_missing_dates(dates: list) -> list:
    dates = [datetime.strptime(d, '%d.%m.%Y') for d in dates]
    dates = (min(dates), max(dates))
    res = []
    for j in range(date.toordinal(dates[0]), date.toordinal(dates[1]) + 1):
        res.append((date.fromordinal(j)).strftime('%d.%m.%Y'))
    return res