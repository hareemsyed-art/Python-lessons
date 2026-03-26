import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = 15
dictionary = {
    "product_id" : list(range(1, a+1)),
    "rating" : np.round(np.random.uniform(3.5, 5, a), 1),
    "price" : np.random.randint(50, 500, a),
    "reviews" : np.random.randint(10, 500, a)
}

print(dictionary)

data = pd.DataFrame(dictionary)
print(data)

# data["search_rating"] = data["rating"]
# b = data.sort_values("search_rating", ascending = False)
# print(b)

# data["search_reviews"] = data["reviews"]
# c = data.sort_values("search_reviews", ascending = False)
# print(c)

data["rule_2"] = data["rating"] * data["reviews"]
d = data.sort_values("rule_2", ascending = False)
print(d)

# data["rule3"] = data["price"]
# e = data.sort_values("rule3", ascending = True)
# print(e)

# data["rule_4"] = data["rating"] / data["price"]
# f = data.sort_values("rule_4", ascending = False)
# print(f)

plt.bar(data["product_id"], data["reviews"])
plt.title("ratings * reviews")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

print(d)