import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5]
temperatures = [22, 24, 23, 25, 26]
plt.plot(days, temperatures, marker = "*")
plt.title("Daily Temperatures")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()

fruits = ["Apple", "Banana", "Cherry", "Date"]
counts = [10, 15, 7, 12]
plt.plot(fruits, counts)
plt.title("Fruit Counts")
plt.xlabel("Fruits")
plt.ylabel("Counts")
plt.show()

hours_studied = [1, 2, 3, 4, 5]
test_scores = [55, 60, 65, 70, 75]
plt.scatter(hours_studied, test_scores, color = "green")
plt.title("Hours Studied")
plt.xlabel("Test Scores")
plt.ylabel("Study Hours vs Test Scores")
plt.show()