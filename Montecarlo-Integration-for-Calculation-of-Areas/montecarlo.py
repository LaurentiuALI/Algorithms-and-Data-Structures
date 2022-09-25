import random


class MonteCarlo:
    def __init__(self, length, width, rectangles):
        self.length = length
        self.width = width
        self.rectangles = []
        if len(rectangles):
            for i in range(len(rectangles)):
                self.rectangles.append(rectangles[i])

    def area(self, num_of_shots):
        hit = 0
        miss = 0
        points = []
        enclose_rectangle_area = self.width * self.length

        for i in range(num_of_shots):
            random_number_x = random.random() * self.length
            random_number_y = random.random() * self.width
            auxiliar_list = [random_number_x, random_number_y]
            points.append(auxiliar_list)

        for i in range(len(points)):
            vb = 0
            for j in range(len(self.rectangles)):
                if self.inside(points[i][0], points[i][1], self.rectangles[j]):
                    vb = 1
                    break
            if vb == 0:
                miss += 1
            else:
                hit += 1
            if num_of_shots == None :
                raise ValueError("Parameter is none")
        return enclose_rectangle_area * (1 - (hit) / (hit + miss))

    def inside(self, x, y, rect):
        lower_rectangle_x = rect.get_x()
        lower_rectangle_y = rect.get_y()

        upper_rectangle_x = rect.get_x() + rect.get_length()
        upper_rectangle_y = rect.get_y() + rect.get_width()
        if(x == None or y == None or rect == None):
            raise ValueError("Parameter is none")
        if lower_rectangle_x <= x <= upper_rectangle_x and lower_rectangle_y <= y <= upper_rectangle_y:
            return True
        else:
            return False
