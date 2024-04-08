import matplotlib.pyplot as plt
import numpy as np
from skimage import io

# 1. 读取图像
flower = io.imread('flower.tif')
rice = io.imread('rice.tif')

# 2. 图像的加法运算
added_image = flower + rice

# 3. 图像的减法运算
subtracted_image = flower - rice

# 4. 图像的乘法运算
multiplied_image = np.multiply(flower, 1.2)

# 5. 图像的除法运算
divided_image = np.divide(flower, (rice + 1))

# 显示结果图像
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# 原始图像
axes[0, 0].imshow(flower, cmap='gray')
axes[0, 0].set_title('Flower')
axes[0, 0].axis('off')

axes[0, 1].imshow(rice, cmap='gray')
axes[0, 1].set_title('Rice')
axes[0, 1].axis('off')

# 加法运算
axes[0, 2].imshow(added_image, cmap='gray')
axes[0, 2].set_title('Added Image')
axes[0, 2].axis('off')

# 减法运算
axes[1, 0].imshow(subtracted_image, cmap='gray')
axes[1, 0].set_title('Subtracted Image')
axes[1, 0].axis('off')

# 乘法运算
axes[1, 1].imshow(multiplied_image, cmap='gray')
axes[1, 1].set_title('Multiplied Image')
axes[1, 1].axis('off')

# 除法运算
axes[1, 2].imshow(divided_image, cmap='gray')
axes[1, 2].set_title('Divided Image')
axes[1, 2].axis('off')

plt.show()
