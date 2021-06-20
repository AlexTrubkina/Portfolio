import numpy as np
import matplotlib.pyplot as plt
import pandas

data = pandas.read_csv('sample_data/data.csv')
x = data['square_house']
y = data['cost']

x = x[~np.isnan(y)]
y = y[~np.isnan(y)]

# Линейная модель, которая учитывает размер жилья
f1p, residuals, rank, sv, rcond = np.polyfit(x, y, 1, full=True)
f1 = np.poly1d(f1p)
fx = np.linspace(0, max(x)) 

# Визуализация данных зависимость цены от площади дома (линейная модель)
plt.scatter(x, y, s=10)
plt.plot(fx,f1(fx),linewidth=1.0,color='g')
plt.title('Зависимость цены от площади')
plt.xlabel("Площадь дома")
plt.ylabel("Цена")

plt.autoscale(tight=True)
plt.show()

#Полимиальная модель
f1p, residuals, rank, sv, rcond = np.polyfit(x, y, 3, full=True)
f1 = np.poly1d(f1p)
fx = np.linspace(0, max(x)) 

