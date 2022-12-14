"""Число 1313 считалось дьявольским издавна. Это имеет свое объяснение, и не одно: тут есть трактовки, связанные с
Тайной вечерей — где были Христос и 1212 апостолов, один из которых стал предателем. Есть поверье, что для шабаша
нужны 1212 ведьм и сатана. В истории число 1313 в связке с пятницей стало «несчастливым» в 13071307 году,
когда король Франции Филипп Красивый отдал приказ схватить всех тамплиеров — членов рыцарского ордена крестоносцев.
Все они были сожжены на кострах инквизиции, и произошло это в пятницу, 1313 апреля.

Докажите, что 1313-е число месяца чаще всего приходится на пятницу. Напишите программу, которая вычисляет,
сколько тринадцатых чисел приходится на каждый день недели в период с 01.01.0001 по 31.12.9999.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных Программа должна вывести 77 чисел — количество тринадцатых чисел, которые приходятся на
понедельник, вторник, среду, четверг, пятницу, субботу и воскресенье в период с 01.01.0001 по 31.12.9999. Числа
должны быть расположены каждое на отдельной строке. """

from datetime import date


def friday_13():
    start_day = date(year=1, month=1, day=1).toordinal()
    end_day = date(year=9999, month=12, day=31).toordinal()
    days = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }

    for d in range(start_day, end_day):
        dt = date.fromordinal(d)
        if dt.day == 13:
            days[dt.weekday()] += 1

    print(*days.values(), sep='\n')


friday_13()
