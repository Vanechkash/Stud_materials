import re

lines = []
rectangles = []
buckets = []

# открываем и получаем файл условия
file_in = open('input.txt', 'r')
datas = (file_in.read()).split('\n')

# создаём класс для холста, в дальнейшем без него не будет работать программа, + показываем что знакомы с ООП :)
class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height

# решулярными выражениями получаем параметры линий, прямоугольников и т.д.
for i in datas:
    if i[0] == 'C':
        Canvas1 = Canvas(int(re.findall(r'C\D+(\d+)', i)[0]), int(re.findall(r'C\D+\d+\D+(\d+)', i)[0]))
    elif i[0] == 'L':
        lines.append((int(re.findall(r'L\D+(\d+)', i)[0]), int(re.findall(r'L\D+\d+\D+(\d+)', i)[0]),
            int(re.findall(r'L\D+\d+\D+\d+\D+(\d+)', i)[0]),int(re.findall(r'L\D+\d+\D+\d+\D+\d+\D+(\d+)', i)[0])))
    elif i[0] == 'R':
        rectangles.append((int(re.findall(r'R\D+(\d+)', i)[0]), int(re.findall(r'R\D+\d+\D+(\d+)', i)[0]),
            int(re.findall(r'R\D+\d+\D+\d+\D+(\d+)', i)[0]),int(re.findall(r'R\D+\d+\D+\d+\D+\d+\D+(\d+)', i)[0])))
    elif i[0] == 'B':
        buckets.append((int(re.findall(r'B\D+(\d+)', i)[0]), int(re.findall(r'B\D+\d+\D+(\d+)', i)[0]),
            (re.findall(r'B\D+\d+\D+\d+\D+(\S)', i)[0])))

# делаем функцию которая будет за один раз создавать массив с картинкой
def draw():
    # отрисовка холста
    w = Canvas1.width
    h = Canvas1.height
    drawing = []
    drawing.extend('—' * (w + 2) + '\n')
    drawing.extend(('|' + ' ' * (w) + '|\n') * h)
    drawing.extend('—' * (w + 2))

    # отрисовка линий
    for l in lines:
        x1 = l[0]
        y1 = l[1]
        x2 = l[2]
        y2 = l[3]

        point1 = ((w + 3) * y1 + (x1))
        point2 = ((w + 3) * y2 + (x2))

        # горизонтальная
        if y1 == y2:
            for i in range(point1, point2 + 1):
                drawing[i] = 'x'
            for i in range(point2, point1 + 1):
                drawing[i] = 'x'

        # вертикальная
        elif x1 == x2:
            for i in range(point1, ((w + 3) * (y2 + 1) + (x2)), w + 3):
                drawing[i] = 'x'
            for i in range(point2, ((w + 3) * (y1 + 1) + (x1)), w + 3):
                drawing[i] = 'x'

    # отрисовка прямоугольника
    for r in rectangles:
        x1 = r[0]
        y1 = r[1]
        x2 = r[2]
        y2 = r[3]

        point1 = ((w + 3) * y1 + (x1))
        point2 = ((w + 3) * y2 + (x2))

        # если первая точка выше и левее второй
        if y1 <= y2 and x1 <= x2:
            for i in range(point1, point2 - ((w + 3) * (y2 - y1)) + 1):
                drawing[i] = 'x'
            for i in range(point1 + ((w + 3) * (y2 - y1)), point2 + 1):
                drawing[i] = 'x'
            for i in range(point1 + (x2 - x1), point2, (w + 3)):
                drawing[i] = 'x'
            for i in range(point2 - (x2 - x1), point1, -(w + 3)):
                drawing[i] = 'x'

        # если первая точка выше и правее второй
        if y1 <= y2 and x1 >= x2:
            for i in range(point2, point1 + ((w + 3) * (y2 - y1)) + 1):
                drawing[i] = 'x'
            for i in range(point2 - ((w + 3) * (y2 - y1)), point1 + 1):
                drawing[i] = 'x'
            for i in range(point2, point1 - (x1 - x2), -(w + 3)):
                drawing[i] = 'x'
            for i in range(point1, point2 + (x1 - x2), (w + 3)):
                drawing[i] = 'x'

        # если первая точка ниже и левее второй
        if y1 >= y2 and x1 <= x2:
            for i in range(point1, point2 + ((w + 3) * (y1 - y2)) + 1):
                drawing[i] = 'x'
            for i in range(point1 - ((w + 3) * (y1 - y2)), point2 + 1):
                drawing[i] = 'x'
            for i in range(point1 + (x2 - x1), point2, -(w + 3)):
                drawing[i] = 'x'
            for i in range(point2 - (x2 - x1), point1, (w + 3)):
                drawing[i] = 'x'

        # если первая точка ниже и правее второй
        if y1 >= y2 and x1 >= x2:
            for i in range(point2, point1 - ((w + 3) * (y1 - y2)) + 1):
                drawing[i] = 'x'
            for i in range(point2 + ((w + 3) * (y1 - y2)), point1 + 1):
                drawing[i] = 'x'
            for i in range(point2, point1 - (x1 - x2), (w + 3)):
                drawing[i] = 'x'
            for i in range(point2 + (x1 - x2), point1 + 1, (w + 3)):
                drawing[i] = 'x'

    # составляем функцию которая должна проверять точки рядом с начальной точки заливки на их ненаполненность
    def buck(p):
        if drawing[p] == ' ':
            drawing[p] = color
        if drawing[p - (w + 3)] == ' ':
            buck(p - (w + 3))
        if drawing[p - 1] == ' ':
            buck(p - 1)
        if drawing[p + 1] == ' ':
            buck(p + 1)
        if drawing[p + (w + 3)] == ' ':
            buck(p + (w + 3))

    # отрисовка заливки
    for b in buckets:
        x = b[0]
        y = b[1]
        color = b[2]
        bp = ((w + 3) * y + (x))

        buck(bp)

    # записываем результат в файл output в виде строки вместо листа drawing
    with open('output.txt', 'w') as file_out:
        result = ''.join(drawing)
        file_out.write(str(result))

draw()



