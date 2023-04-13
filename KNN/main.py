from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
# Load iris dataset
iris = load_iris()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

# Create KNN classifier // K=3 (tức là tìm 3 điểm gần nhất).
knn = KNeighborsClassifier(n_neighbors=3)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Predict the class labels for the test set
y_pred = knn.predict(X_test)

# Print the accuracy score of the classifier
print('Accuracy:', knn.score(X_test, y_test))
