# Известно, что среди 8-ми внешне одина­ко­вых монет имеется ровно одна фальшивая, причем она чуть легче, чем настоящие. 
# Для взвешивания монет используются чашечные весы, с помощью которых можно определять, что один предмет легче, тяжелее или равен по весу другому. 
# Разработайте алгоритм и напишите программу, которая находит фальшивую монету, используя минимальное число взвешиваний. 

def countN():
    if 8 <= 3:
        print(1)
    elif 8 % 3 != 0:
        print(1 + countN(8/3+1))
    else:
        print(1 + countN(8/3))

countN()