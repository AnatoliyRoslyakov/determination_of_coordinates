import webbrowser
from pygeoguz.objects import Point2D, PointBL
from pygeoguz.simplegeo import ogz
from pygeoguz.transform import bl2xy
from inverse_geodetic_task.plot_and_map import plt



# Точка-1
dLat1 = 55.749979  # Широта (положительная для северного полушария)
dLon1 = 37.620953  # Долгота (положительная для восточного полушария)
p1 = PointBL(b=dLat1, l=dLon1)
xy1 = bl2xy(point=p1)

# Точка-2
dLat2 = 55.750
dLon2 = 37.621
p2 = PointBL(b=dLat2, l=dLon2)
xy2 = bl2xy(point=p2)

# Обратная геодезическая задача
p1 = Point2D(x=xy1.x, y=xy1.y)
p2 = Point2D(x=xy2.x, y=xy2.y)
line = ogz(point_a=p1, point_b=p2)

length = line.length
direction = line.direction




print('-----------------------------------')
print('Точка 1 в географических координатах')
print('-----------------------------------')
print('Широта1:', dLat1)
print('Долгота1:', dLon1)
print('-----------------------------------')
print('Точка 1 в географических координатах')
print('-----------------------------------')
print('Широта1:', dLat2)
print('Долгота1:', dLon2)
print('-----------------------------------')
print('Расстояние и направление между точками')
print('-----------------------------------')
print('Расстояние', length)
print('Направление:', direction)

plt.show()
webbrowser.open('../map.html')