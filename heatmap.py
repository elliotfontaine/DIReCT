import os
import numpy as np
from PIL import Image

os.chdir("/Users/elliotfontaine/Documents/github/DIReCT")

# Créer un tableau de données numériques aléatoires
np.random.seed(42)  # Pour reproduire les mêmes résultats à chaque exécution
data = np.random.rand(10, 10)  # Un tableau 5x5 de nombres aléatoires entre 0 et 1

# Dessiner la heatmap en niveaux de gris
pic = Image.fromarray(np.uint8(data * 255) , 'L')
pic.save("pillow_heatmap.png")

import matplotlib.pyplot as plt
plt.imshow(data, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.savefig('heatmap.png', bbox_inches='tight', pad_inches=0)