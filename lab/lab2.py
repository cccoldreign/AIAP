import math
from dataclasses import dataclass, field

@dataclass
class Point:
        latitude: float 
        longitude: float

@dataclass
class Sphere:
    radius: int
    points: list = field(default_factory=list)

        
    def addPoint(self, point):
        self.points.append(point)

    def calcDist(self, point1, point2):
        point1.latitude = math.radians(point1.latitude)
        point2.latitude = math.radians(point2.latitude)
        point1.longitude = math.radians(point1.longitude)
        point2.longitude = math.radians(point2.longitude)
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