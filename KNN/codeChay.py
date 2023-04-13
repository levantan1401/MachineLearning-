################################

# Định nghĩa dữ liệu huấn luyện
train_data = [(2, 3), (3, 4), (4, 2), (4, 4), (1, 2), (2, 1)]
train_labels = ['A', 'A', 'A', 'B', 'B', 'B']

# Định nghĩa một điểm mới
test_point = (3, 3)

#  định nghĩa số lượng điểm láng giềng cần tìm kiếm (K) để dự đoán nhãn lớp cho điểm mới.
k = 3

# Tính khoảng cách giữa 1 cặp điểm
def euclidean_distance(point1, point2):
    distance = ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5  # tính toán khoản cách giữa 2 điểm <2,3>
    return distance
"""
Ở đoạn code này, chúng ta đang định nghĩa hàm tính khoảng cách Euclid giữa hai điểm point1 và point2. 
Khoảng cách Euclid được tính bằng căn bậc hai của tổng bình phương của hiệu tọa độ của hai điểm.
"""

# Tìm K điểm khoảng cách láng giềng với các điểm mới của test point 
distances = [] # lưu các khoảng cách mỗi điểm huấn luyện với điểm mới.
for i, point in enumerate(train_data):                  # enumerate cho phép lắp và điếm số lần lặp
    distance = euclidean_distance(point, test_point)    # tính khoảng cách giữa từng cặp huấn luyện với điểm cũ
    distances.append((distance, i))                     # Thêm khoảng cách vừa tính vào cuối danh sách distances
distances.sort()                                        # Sắp xếp danh sách distances theo thứ tự tăng dần
neighbors = [train_labels[i] for _, i in distances[:k]] 
# chọn ra K điểm láng giềng gần nhất bằng cách lấy k phần tử đầu tiên của danh sách distances và trích xuất nhãn lớp tương ứng của chúng từ danh sách train_labels.

# Dự đoán nhãn của điểm mới tìm
counts = {}                                 # Đếm số lần xuất hiện của mỗi nhãn lớp trong danh sách neighbors
for label in neighbors:
    if label in counts:
        counts[label] += 1                  # nếu các nhẵn lớp đã có trong count thì ta tăng giá trị trong count lên 1
    else:
        counts[label] = 1                   # nếu không thì khởi tạo giá trị đó là 0 
prediction = max(counts, key=counts.get)    # hàm max để tìm nhãn lớp có giá trị tương ứng lớn nhất trong từ điển count

# In ra màn hình nhãn dự đoán
print(f"Nhãn dự đoán cho điểm kiểm tra là: Điểm {test_point} là {prediction}.")
   