import math

def from_degree_to_radian(degree):
    return math.radians(degree)

def area_of_regular_polygon(number_of_sides,length):
    perimetr=length*number_of_sides
    radians = from_degree_to_radian(180/number_of_sides)
    apothem=length/(2*math.tan(radians))
    return int(perimetr*0.5*apothem)

print(area_of_regular_polygon(4,25))