import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Vetor
v1 = np.array([1, 2, 3])

# Origem do vetor
origin = [0, 0, 0]

# Configuração do gráfico
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotando o vetor
ax.quiver(*origin, *v1, length=1, normalize=False, color='blue')

# Ajustando os limites dos eixos
ax.set_xlim([0, 2])
ax.set_ylim([0, 3])
ax.set_zlim([0, 4])

# Rótulos e título
ax.set_title("Representação de um Vetor 3D")
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")
ax.set_zlabel("Eixo Z")

plt.show()
