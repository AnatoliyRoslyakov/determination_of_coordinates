import math

import folium
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from start import length, xy1, xy2, dLat1, dLon1, dLat2, dLon2

# Построение графика
fig, ax = plt.subplots()
ax.set_aspect('equal')
# Окружность с градусами
R = length
circle = Circle((xy1.x, xy1.y), R, fill=False, linestyle='dashed', linewidth=1, color='green')

circle2 = Circle((xy1.x, xy1.y), 5, fill=True, linestyle='dashed', linewidth=1, color='red')

colorR = (1, 0, 0, 0.5)
colorG = (0, 1, 0, 0.5)

if R >= 5:
    circle2.set_facecolor(colorR)
    plt.title('Вне заданной области')
else:
    circle2.set_facecolor(colorG)
    plt.title('В заданной области')


ax.add_patch(circle2,)
ax.add_patch(circle,)
for degree in range(0, 361, 10):
    x = xy1.x + (R * math.cos(math.radians(degree)))
    y = xy1.y + (R * math.sin(math.radians(degree)))
    ax.text(x, y, degree, ha='center', va='center', fontsize=8, color='green')

# Линия между точками
ax.plot([xy1.x, xy2.x], [xy1.y, xy2.y], color='red', linewidth=1, marker='o', markersize=5, linestyle='dashed')

# Аннотации для точек
ax.annotate("Точка 1", xy=(xy1.x, xy1.y), xytext=(xy1.x+0.01, xy1.y+0.01), color='blue')
ax.annotate("Точка 2", xy=(xy2.x, xy2.y), xytext=(xy2.x+0.01, xy2.y+0.01), color='red')

dx = xy2.x - xy1.x
dy = xy2.y - xy1.y
distance = math.sqrt(dx**2 + dy**2)
ax.text((xy1.x+xy2.x)/2, (xy1.y+xy2.y)/2, f"{distance:.2f} м", fontsize=8, ha='center', va='bottom', color='red')

ax.grid(True)
ax.set_xlabel('X, m')
ax.set_ylabel('Y, m')



# Создание карты
m = folium.Map(location=[dLat1, dLon1], zoom_start=50)

# Добавление маркеров для точек
folium.Marker(location=[dLat1, dLon1], tooltip='Точка 1', icon=folium.Icon(color='blue')).add_to(m)
folium.Marker(location=[dLat2, dLon2], tooltip='Точка 2', icon=folium.Icon(color='red')).add_to(m)

# Добавление линии между точками
folium.PolyLine(locations=[[dLat1, dLon1], [dLat2, dLon2]], color='red').add_to(m)

# Отображение карты
m
m.save('map.html')

