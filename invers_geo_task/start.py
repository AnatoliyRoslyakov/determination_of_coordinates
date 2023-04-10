import pathlib
import webbrowser
from pathlib import Path

from pygeoguz.objects import Point2D, PointBL
from pygeoguz.simplegeo import ogz
from pygeoguz.transform import bl2xy

from plot_and_map import plt

# Точка-1
dLat1 = float(input("Введите широту-1 (например: 55.749979):"))  # Широта (положительная для северного полушария)
dLon1 = float(input("Введите долготу-1 (например: 37.620953):"))
p1 = PointBL(b=dLat1, l=dLon1)
xy1 = bl2xy(point=p1)

# Точка-2
dLat2 = float(input("Введите широту-2 (например: 55.7501):"))
dLon2 = float(input("Введите долготу-2 (например: 37.621):"))
p2 = PointBL(b=dLat2, l=dLon2)
xy2 = bl2xy(point=p2)

# Обратная геодезическая задача
p1 = Point2D(x=xy1.x, y=xy1.y)
p2 = Point2D(x=xy2.x, y=xy2.y)
line = ogz(point_a=p1, point_b=p2)

length = line.length
direction = line.direction

with open('Выходные данные.txt', 'w') as f:
    print('-----------------------------------', file=f)
    print('Точка 1 в географических координатах', file=f)
    print('-----------------------------------', file=f)
    print('Широта1:', dLat1, file=f)
    print('Долгота1:', dLon1, file=f)
    print('-----------------------------------', file=f)
    print('Точка 1 в географических координатах', file=f)
    print('-----------------------------------', file=f)
    print('Широта1:', dLat2, file=f)
    print('Долгота1:', dLon2, file=f)
    print('-----------------------------------', file=f)
    print('Расстояние и направление между точками', file=f)
    print('-----------------------------------', file=f)
    print('Расстояние', length, file=f)
    print('Направление:', direction, file=f)



dir_path = pathlib.Path.cwd()
path = Path(dir_path, 'map.html')
webbrowser.open(str(path))

plt.show()

