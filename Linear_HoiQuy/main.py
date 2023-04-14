import numpy as np
import matplotlib.pyplot as plt

# Tập dữ liệu 
X = np.array([147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]) # chiều cao
Y = np.array([49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68])  # cân nặng

# Tính toán hệ số hồi quy tuyến tính
n = np.size(X)                          # số lượng dự liệu đầu vào 
mean_x = np.mean(X)                     # giá trị trung bình của X
mean_y = np.mean(Y)                     # giá trị trung bình của Y 
SS_xy = np.sum(Y*X) - n*mean_y*mean_x   # tổng bình phương của sự sai số khác giữa giá trị trung bình X và Y
SS_xx = np.sum(X*X) - n*mean_x*mean_x   # tổng bình phương sự sai khác giữa X và giá trị trung bình của X 

b_1 = SS_xy / SS_xx                     # hệ số hồi quy b_1 ( độ dốc ) là gì là đại lượng biểu thị mức độ tăng giảm của biến phụ thuộc (được dự đoán) y khi biến độc lập x tăng lên 1 đơn vị.
b_0 = mean_y - b_1*mean_x               # hệ số hồi quy b_0 (điểm cắt) là  là giá trị của y khi x = 0


# Predict the values
Y_pred = b_0 + b_1*X                   

"""
Y_pred là một vector (một mảng 1 chiều) lưu trữ các giá trị được dự đoán bởi mô hình hồi quy tuyến tính trên tập dữ liệu huấn luyện. 
Tức là, với mỗi giá trị của biến độc lập x trong tập dữ liệu huấn luyện, mô hình sẽ dự đoán một giá trị tương ứng cho biến phụ thuộc y, 
và Y_pred sẽ lưu trữ các giá trị dự đoán này.
"""

y1 = b_0 + b_1*155
y2 = b_0 + b_1*160 

print( u'Predict weight of person with height 155 cm: %.2f (kg), real number: 52 (kg)'  %(y1) )
print( u'Predict weight of person with height 160 cm: %.2f (kg), real number: 56 (kg)'  %(y2) )

# Plot the regression line
plt.scatter(X, Y)
plt.plot(X, Y_pred, color='green')
plt.show()

"# BAI 2"
# import numpy as np
# import matplotlib.pyplot as plt

# # Tạo dữ liệu giả lập
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([3, 4, 2, 4, 5])

# # Khởi tạo learning rate và số lần lặp lại để tối ưu hàm chi phí
# learning_rate = 0.01
# epochs = 1000

# # Khởi tạo các tham số của mô hình
# b = 0 # intercept
# m = 0 # slope

# # Sử dụng gradient descent để tối ưu tham số của mô hình
# n = float(len(x))
# for i in range(epochs):
#     y_pred = m*x + b
#     cost = np.sum((y_pred-y)**2) / n
#     dm = (-2/n) * np.sum(x * (y - y_pred))
#     db = (-2/n) * np.sum(y - y_pred)
#     m = m - learning_rate * dm
#     b = b - learning_rate * db
#     if i % 100 == 0:
#         print(f"Epoch {i}: cost = {cost:.4f}, m = {m:.4f}, b = {b:.4f}")

# # Vẽ đường thẳng dự đoán trên đồ thị
# plt.scatter(x, y)
# plt.plot(x, m*x + b, color='red')
# plt.show()

# # Dự đoán giá trị đầu ra với giá trị đầu vào mới
# x_new = 6
# y_new = m*x_new + b
# print(f"Giá trị đầu ra dự đoán với giá trị đầu vào {x_new}: {y_new:.4f}")

# from __future__ import division, print_function, unicode_literals

"""CODE CỦA web"""
# import numpy as np 
# import matplotlib.pyplot as plt

# # height (cm)
# X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# # weight (kg)
# y = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T

# # Building Xbar 
# one = np.ones((X.shape[0], 1))
# Xbar = np.concatenate((one, X), axis = 1)

# # Calculating weights of the fitting line 
# A = np.dot(Xbar.T, Xbar)
# b = np.dot(Xbar.T, y)
# w = np.dot(np.linalg.pinv(A), b)
# print('w = ', w)
# # Preparing the fitting line 
# w_0 = w[0][0]
# w_1 = w[1][0]
# x0 = np.linspace(145, 185, 2)
# y0 = w_0 + w_1*x0

# # Drawing the fitting line 
# plt.plot(X.T, y.T, 'ro')     # data 
# plt.plot(x0, y0)               # the fitting line
# plt.axis([140, 190, 45, 75])
# plt.xlabel('Height (cm)')
# plt.ylabel('Weight (kg)')
# plt.show()


