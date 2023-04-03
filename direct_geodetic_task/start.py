
import webbrowser
from pygeoguz.objects import Point2D, Line2D, PointBL
from pygeoguz.simplegeo import pgz
from pygeoguz.transform import xy2bl, bl2xy

from direct_geodetic_task.plot_and_map import plt

# Входные данные
dLat = 55.749979  # Широта (положительная для северного полушария)
dLon = 37.620953  # Долгота (положительная для восточного полушария)
length = 71  # [м]
direction = 85  # [deg]

# Геодезическая СК --> Плоская прямоугольная СК
p1 = PointBL(b=dLat, l=dLon)
xy1 = bl2xy(point=p1)

# Прямая геодезическая задача
p2 = Point2D(x=xy1.x, y=xy1.y)
line = Line2D(length=length, direction=direction)
xy2 = pgz(point=p2, line=line)

# Плоская прямоугольная СК --> Геодезическая СК
latLon1 = xy2bl(point=p2)

# Плоская прямоугольная СК --> Геодезическая СК
latLon2 = xy2bl(point=xy2)


print('-----------------------------------')
print('Точка 1 в прямоугольных координатах')
print('-----------------------------------')
print('X1:', xy1.x)
print('Y1:', xy1.y)
print('-----------------------------------')
print('Точка 2 в прямоугольных координатах')
print('-----------------------------------')
print('X2:', xy2.x)
print('Y2:', xy2.y)
print('-----------------------------------')
print('Точка 1 в географических координатах')
print('-----------------------------------')
print('Широта1:', latLon1.b)
print('Долгота1:', latLon1.l)
print('-----------------------------------')
print('Точка 2 в географических координатах')
print('-----------------------------------')
print('Широта2:', latLon2.b)
print('Долгота2:', latLon2.l)

plt.show()
webbrowser.open('../map.html')


# https://pypi.org/project/pygeoguz/ <-- прямая/обратная геодезическая задача
# https://www.latlong.ru/sk.php <-- проверка