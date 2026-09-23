import numpy as np
import matplotlib.pyplot as plt

imagem = np.zeros((100, 120))

y, x = np.ogrid[:100, :120]

centro_x = imagem.shape[1] // 2
centro_y = imagem.shape[0] // 2
raio = 30

circulo = (x - centro_x)**2 + (y - centro_y)**2 <= raio**2

imagem[circulo] = 1

print("Dimensões:", imagem.shape)

plt.imshow(imagem, cmap="gray")
plt.show()
