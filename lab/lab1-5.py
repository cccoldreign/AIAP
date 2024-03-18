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

moscow = Point(55.7558, 37.6176)
new_york = Point(40.7128, -74.0060)

earth.addPoint(moscow)
earth.addPoint(new_york)

print(earth.calcDist(moscow, new_york))