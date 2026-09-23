import numpy as np
import matplotlib.pyplot as plt

imagem = np.zeros((9, 9))

imagem[4, :] = 1
imagem[:, 4] = 1

plt.imshow(imagem, cmap="gray")
plt.grid()
plt.show()
