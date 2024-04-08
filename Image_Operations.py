import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, transform

# 1. 读取图像
flower = io.imread('fl.jpg')
rice_origin = io.imread('fl1.jpg')
rice = transform.resize(rice_origin, flower.shape[:2], mode='reflect')

# 将rice转换为与flower相同的数据类型
rice = (rice * 255).astype(np.uint8)

# 图像混合
alpha = 0.5  # 调整权重
blended_image = cv2.addWeighted(flower, alpha, rice, 1 - alpha, 0)

# 显示原始的两幅图像和混合后的图像
# plt.figure(figsize=(10, 6))
#
# plt.subplot(1, 3, 1)
# plt.imshow(flower)
# plt.title('Flower')
# plt.axis('off')
#
# plt.subplot(1, 3, 2)
# plt.imshow(rice)
# plt.title('Rice')
# plt.axis('off')
#
# plt.subplot(1, 3, 3)
# plt.imshow(cv2.cvtColor(blended_image, cv2.COLOR_BGR2RGB))
# plt.title('Blended Image')
# plt.axis('off')
#
# plt.show()

#  2. 图像的加法运算
# added_image = np.clip(flower + rice, 0, 255).astype(np.uint8)
#
# # 显示结果图像
# fig, axes = plt.subplots(1, 3, figsize=(15, 5))
#
# # 原始图像
# axes[0].imshow(flower)
# axes[0].set_title('Flower')
# axes[0].axis('off')
#
# # 第二个图像
# axes[1].imshow(rice)
# axes[1].set_title('Rice')
# axes[1].axis('off')
#
# # 加法运算结果图像
# axes[2].imshow(added_image)
# axes[2].set_title('Added Image')
# axes[2].axis('off')
#
# plt.show()

#
# import cv2
# import matplotlib.pyplot as plt
#
# # 读取图像
# RGB = cv2.imread('fl2.jpg')
#
# # 将图像的每一个像素值增加50，增加亮度
# RGB2 = cv2.add(RGB, (50, 50, 50))
#
# # 显示原始图像和增加亮度后的图像
# plt.subplot(1, 2, 1)
# plt.imshow(cv2.cvtColor(RGB, cv2.COLOR_BGR2RGB))
# plt.title('Original Image')
# plt.axis('off')
#
# plt.subplot(1, 2, 2)
# plt.imshow(cv2.cvtColor(RGB2, cv2.COLOR_BGR2RGB))
# plt.title('Increased Brightness Image')
# plt.axis('off')
#
# plt.show()

# import cv2
# import matplotlib.pyplot as plt
#
# # 读取图像
# I = cv2.imread('cameraman.jpg')
#
# # 生成背景亮度图像
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
# background = cv2.morphologyEx(I, cv2.MORPH_OPEN, kernel)
#
# # 图像减法
# I2 = cv2.subtract(I, background)
#
# # 显示原始图像和减去背景后的图像
# plt.subplot(1, 2, 1)
# plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
# plt.title('Original Image')
# plt.axis('off')
#
# plt.subplot(1, 2, 2)
# plt.imshow(cv2.cvtColor(I2, cv2.COLOR_BGR2RGB))
# plt.title('Subtracted Image')
# plt.axis('off')
#
# # 保存减去背景后的图像
# cv2.imwrite('subtracted_image.jpg', I2)
#
# plt.show()

# import cv2
# import matplotlib.pyplot as plt
#
# # 读取图像
# I = cv2.imread('fl4.jpg')
#
# # 图像乘法运算
# J = cv2.multiply(I, 1.2)
#
# # 显示原始图像和乘以因子后的图像
# plt.subplot(1, 2, 1)
# plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
# plt.title('Original Image')
# plt.axis('off')
#
# plt.subplot(1, 2, 2)
# plt.imshow(cv2.cvtColor(J, cv2.COLOR_BGR2RGB))
# plt.title('Multiplied Image')
# plt.axis('off')
#
# plt.show()
#
# import cv2
# import matplotlib.pyplot as plt

#
# # 读取原始图像和背景图像
# cameraman = cv2.imread('cameraman.jpg', cv2.IMREAD_GRAYSCALE)
# background = cv2.imread('subtracted_image.jpg', cv2.IMREAD_GRAYSCALE)
#
# # 背景减法
# background_subtracted = cv2.subtract(cameraman, background)
#
# # 图像除法
# divided_image = cv2.divide(cameraman, background_subtracted)
#
# # 显示结果图像
# plt.imshow(divided_image, cmap='gray')
# plt.title('Divided Image')
# plt.axis('off')
# plt.show()

