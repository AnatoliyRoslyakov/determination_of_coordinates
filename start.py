from pygeoguz.simplegeo import pgz
from pygeoguz.objects import Point2D, Line2D, PointBL
from pygeoguz.transform import xy2bl, bl2xy

# Входные данные
dLat = 55.752  # Широта (положительная для северного полушария)
dLon = 37.618  # Долгота (положительная для восточного полушария)
length = 10000  # [м]
direction = 140  # [deg]

# Геодезическая СК --> Плоская прямоугольная СК
p1 = PointBL(b=dLat, l=dLon)
xy = bl2xy(point=p1)
print('X1:', xy.x)
print('Y1:', xy.y)


# Прямая геодезическая задача
p2 = Point2D(x=xy.x, y=xy.y)
line = Line2D(length=length, direction=direction)
xy2 = pgz(point=p2, line=line)
print('X2:', xy2.x)
print('Y2:', xy2.y)


latLon = xy2bl(point=p2)
print('Долгота1:', latLon.b)
print('Широта1:', latLon.l)

# Плоская прямоугольная СК --> Геодезическая СК
latLon = xy2bl(point=xy2)
print('Долгота2:', latLon.b)
print('Широта2:', latLon.l)






# https://pypi.org/project/pygeoguz/ <-- прямая/обратная геодезическая задача
# https://www.latlong.ru/sk.php <-- проверка