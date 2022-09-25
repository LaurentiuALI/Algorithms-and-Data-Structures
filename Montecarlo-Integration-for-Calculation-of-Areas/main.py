from montecarlo import MonteCarlo
from rectangle import Rectangle


def main():
    rect1 = Rectangle(0.0, 0.0, 50.0, 30.0)
    rects = [rect1]
    mc = MonteCarlo(100.0, 30.0, rects)
    area = mc.area(10)
    print("1st test: " + str(area))
    area = mc.area(100)
    print("2nd test: " + str(area))
    area = mc.area(1000)
    print("3rd test: " + str(area))
    area = mc.area(100000)
    print("4th test: " + str(area))


if __name__ == "__main__":
    main()
