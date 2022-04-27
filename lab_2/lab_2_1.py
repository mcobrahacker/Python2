#Составить алгоритм и разработать программу, которая по длине, ширине и высоте комнаты, вводимым с клавиатуры,  
# находит и выводит на экран площадь и объем этой комнаты.

def get_floor_area(length, width):
    return length * width
 
 
def get_walls_area(length, width, height):
    return (width * height, length * height) * 2
 
 
def get_room_volume(length, width, height):
    return length * width * height
 
 
def main():
    length = float(input('Введите длину помещения: '))
    width = float(input('Введите ширину помещения: '))
    height = float(input('Введите высоту помещения: '))
 
    print('Площадь пола: {}'.format(get_floor_area(length, width)))
    print('Площадь стен: {}'.format(get_walls_area(length, width, height)))
    print('Объём помещения: {}'.format(get_room_volume(length, width, height)))

main()