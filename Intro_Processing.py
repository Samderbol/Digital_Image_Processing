import matplotlib.pyplot as plt
from skimage import io, color

# 1. 读取图像
flower = io.imread('flower.tif')

# 2. 提取图像基本信息
print("flower.tif的基本信息：")
print(flower.shape)
print(flower.dtype)

# 3. 显示图像
plt.imshow(flower, cmap='gray')
plt.title('flower.tif')
plt.axis('off')
plt.show()

# 4. 获取图像文件的详细信息
info = io.imread('flower.tif', plugin='tifffile')
print("flower.tif的详细信息：")
print(info)

# 5. 压缩图像并保存为flower.jpg
quality = 50  # 设置压缩质量
io.imsave('flower.jpg', flower, quality=quality)

# 6. 将原图保存为bmp格式
io.imsave('flower.bmp', flower)

# 7. 读取Lenna.jpg 和cameraman.jpg
lenna = io.imread('Lenna.jpg')
cameraman = io.imread('cameraman.jpg')

# 8. 获取图像大小
print("Lenna.jpg 的大小：", lenna.shape)
print("cameraman.jpg 的大小：", cameraman.shape)

# 9. 显示图像
plt.figure()
plt.imshow(lenna)
plt.title('Lenna.jpg')
plt.axis('off')

plt.figure()
plt.imshow(cameraman)
plt.title('cameraman.jpg')
plt.axis('off')
plt.show()

# 10. 将灰度图像转化为二值图像并显示
gray_image = color.rgb2gray(lenna)  # 将彩色图像转为灰度图像
threshold = 0.5  # 设置阈值
binary_image = gray_image > threshold
plt.imshow(binary_image, cmap='binary')
plt.title('Binary Image')
plt.axis('off')
plt.show()
