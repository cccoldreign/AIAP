import math

class Point:
    def __init__(self, latitude, longitude) -> None:
        self.latitude = math.radians(latitude)
        self.longitude = math.radians(longitude)

class Sphere:
    def __init__(self, radius) -> None:
        self.radius = radius
        self.points = []

    def addPoint(self, point) -> None:
        self.points.append(point)

    def calcDist(self, point1, point2) -> float:
        dLatitude = point2.latitude - point1.latitude
        dLongitude = point2.longitude - point1.longitude
        a = math.sin(dLatitude / 2)**2 +  math.cos(point1.latitude) * math.cos(point2.latitude) * math.sin(dLongitude / 2)**2
        c = 2 * math.asin(math.sqrt(a))
        return self.radius * c

earth = Sphere(6371)

perm = Point(58.064211, 56.363566)
spb = Point(59.93861, 30.31411)
zero = Point(0.0, 0.0)
negative = Point(-20.0, -20.0)

earth.addPoint(perm)
earth.addPoint(spb)
earth.addPoint(zero)
earth.addPoint(negative)

print(earth.calcDist(perm, spb))
print(earth.calcDist(perm, zero))
print(earth.calcDist(spb, negative))