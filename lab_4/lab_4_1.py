# Разработать программу, которая по номеру месяца и номеру дня 2001 года ищет день недели, который припадает на эту дату.

R = 1

def getGT(d,m,y):
    A = round(14 - m) / 12
    C = round(y / 100)
    y = y - A
    m = m + 12 * A - 2
    print(C)
    if C > 15:
        R = round((7000 + (d+y+y / 4-y / 100 + y / 400 + (31 * m) / 12)) % 7)
    else:
        R = round((d + (13*m-1) / 5+5 * (y % 100) / 4+5-C % 7))
    
    print(R)
    switcher = {
        0: "Воскресенье",
        1: "Понедельник",
        2: "Вторник",
        3: "Среда",
        4: "Четверг",
        5: "Пятница",
        6: "Суббота",
    }
    
    return switcher.get(R, "NOTHING")

D = int(input(""))
M = int(input(""))
Y = int(input(""))

print(getGT(D,M,Y))
