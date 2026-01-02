from scipy.special import gamma, erf, beta # 필요한 함수 임포트
import numpy as np

from scipy import ndimage
import matplotlib.pyplot as plt


# 1. 감마 함수 (Gamma function) 예시 ~~
# gamma(x) = (x-1)! (정수 x > 0)
print(f"gamma(5) = {gamma(5)}") # 4! = 24
print(f"gamma(0.5) = {np.sqrt(np.pi)}") # sqrt(pi)

# 2. 오류 함수 (Error function) 예시
# erf(x) = (2/sqrt(pi)) * integral(exp(-t^2) dt) from 0 to x
print(f"erf(0) = {erf(0)}") # 0
print(f"erf(inf) = {erf(np.inf)}") # 1

# 3. 베타 함수 (Beta function) 예시
# beta(a, b) = (Gamma(a) * Gamma(b)) / Gamma(a+b)
print(f"beta(2, 3) = {beta(2, 3)}") # (1! * 2!) / 4! = 2/24 = 1/12

# 1. NumPy 배열(ndarray) 생성하기
# 파이썬 리스트를 NumPy 배열로 변환
my_list = [1, 2, 3, 4, 5]
arr = np.array(my_list)
print(f"1차원 배열: {arr}")

print("Hello, World!")
print("새로운 세상입니다!")

# 샘플 이미지 로드
image = plt.imread('your_image.png')

# 가우시안 필터 적용
filtered_image = ndimage.gaussian_filter(image, sigma=3)

# 원본 이미지와 필터링된 이미지 표시
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Filtered Image')
plt.imshow(filtered_image, cmap='gray')

plt.show()
