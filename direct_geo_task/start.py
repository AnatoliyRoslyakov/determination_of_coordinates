import pathlib
import webbrowser
from pathlib import Path

from pygeoguz.objects import Point2D, Line2D, PointBL
from pygeoguz.simplegeo import pgz
from pygeoguz.transform import xy2bl, bl2xy

from plot_and_map import plt

# Входные данные
dLat = float(input("Введите широту (например: 55.749979):"))   # Широта (положительная для северного полушария)
dLon = float(input("Введите долготу (например: 37.620953):"))  # Долгота (положительная для восточного полушария)
length = float(input("Введите дальность в метрах (например: 71):"))  # [м]
direction = float(input("Введите направление в градусах (например: 85):"))  # [deg]

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
with open("Выходные данные.txt", "w") as f:
    print('-----------------------------------', file=f)
    print('Точка 1 в прямоугольных координатах', file=f)
    print('-----------------------------------', file=f)
    print('X1:', xy1.x, file=f)
    print('Y1:', xy1.y, file=f)
    print('-----------------------------------', file=f)
    print('Точка 2 в прямоугольных координатах', file=f)
    print('-----------------------------------', file=f)
    print('X2:', xy2.x, file=f)
    print('Y2:', xy2.y, file=f)
    print('-----------------------------------', file=f)
    print('Точка 1 в географических координатах', file=f)
    print('-----------------------------------', file=f)
    print('Широта1:', latLon1.b, file=f)
    print('Долгота1:', latLon1.l, file=f)
    print('-----------------------------------', file=f)
    print('Точка 2 в географических координатах', file=f)
    print('-----------------------------------', file=f)
    print('Широта2:', latLon2.b, file=f)
    print('Долгота2:', latLon2.l, file=f)

dir_path = pathlib.Path.cwd()
path = Path(dir_path, 'map.html')
webbrowser.open(str(path))

plt.show()
