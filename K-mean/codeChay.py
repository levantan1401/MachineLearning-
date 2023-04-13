import random
import math

def kmeans(k, data_points):
    # khởi tạo các cluster
    clusters = {}
    for i in range(k):
        clusters[i] = []
    
    # chọn ngẫu nhiên k điểm ban đầu làm centroid
    centroids = random.sample(data_points, k)
    
    # lặp cho đến khi các điểm không thay đổi nữa
    while True:
        # gán các điểm vào cluster gần nhất
        for point in data_points:
            distances = [math.dist(point, centroid) for centroid in centroids]
            closest_cluster = distances.index(min(distances))
            clusters[closest_cluster].append(point)
        
        # tính lại vị trí centroid cho từng cluster
        new_centroids = []
        for cluster in clusters.values():
            new_centroid = [sum(dim)/len(cluster) for dim in zip(*cluster)]
            new_centroids.append(new_centroid)
        
        # kiểm tra xem các centroid có thay đổi không
        if new_centroids == centroids:
            break
        
        # cập nhật centroid mới và reset các cluster
        centroids = new_centroids
        clusters = {i:[] for i in range(k)}
    
    return clusters

# ví dụ
data_points = [(1, 2), (1, 4), (1, 0), (4, 2), (4, 4), (4, 0), (7, 2), (7, 4)]
k = 4
clusters = kmeans(k, data_points)
print(clusters)