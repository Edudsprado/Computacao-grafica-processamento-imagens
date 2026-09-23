import numpy as np
import matplotlib.pyplot as plt

imagem = np.zeros((100, 100, 3), dtype=np.uint8)

# Canal R (vermelho)
imagem[:50, :, 0] = 255

# Canal B (azul)
imagem[50:, :, 2] = 255

plt.imshow(imagem)
plt.show()
