from figure import Rectangle, Square, Circle

rec_1 = Rectangle(3, 4)
rec_2 = Rectangle(12, 5)

print(rec_1.get_area())
print(rec_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(),
      square_2.get_area_square())

circle_1 = Circle(3)
circle_2 = Circle(10)

print(circle_1.get_area_circle())
print(circle_2.get_area_circle())


figures = [rec_1, rec_2, square_1, square_2, circle_1, circle_2]
for i in figures:
    if isinstance(i, Square):
        print(i.get_area_square())
    elif isinstance(i, Rectangle):
        print(i.get_area())
    else:
        print(i.get_area_circle())
