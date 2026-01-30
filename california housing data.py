from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt
a = fetch_california_housing()
b = pd.DataFrame(a.data, columns = a.feature_names)
b["Price"] = a.target
# print(b.head())
# print(b.isnull().sum())
# print(b.info())
# print(b.describe())
from sklearn.model_selection import train_test_split
X = b.drop("Price", axis = 1)
Y = b["Price"]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
print(b.head())
print(Y_pred[:10])
from sklearn.metrics import mean_squared_error, r2_score
print("MSE: ", mean_squared_error(Y_test, Y_pred))
print("R2: ", r2_score(Y_test, Y_pred))

plt.scatter(Y_test, Y_pred)
plt.xlabel("The price that the AI has not seen")
plt.ylabel("The AI's predictions")
plt.title("House price predictions")
plt.show()