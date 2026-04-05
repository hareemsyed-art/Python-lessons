import numpy as np
a = 15
dictionary = {
    "product_id" : list(range(1, a+1)),
    "ratings" : np.round(np.random.uniform(3.5, 5, a), 1),
    "price" : np.random.randint(200, 5000, a),
    "reviews" : np.random.randint(1, 100, a),
    "discount" : np.random.randint(10, 50, a),
    "seller_type" : np.random.choice(["small", "big"], a)
}
import pandas as pd
data = pd.DataFrame(dictionary)

data["formula1"] = data["ratings"] * np.log(data["reviews"])

data["formula2"] = (data["reviews"] * np.sqrt(data["ratings"])) / np.sqrt(data["price"])

rank1 = data.sort_values("formula1", ascending = False).head()

rank2= data.sort_values("formula2", ascending = False).head()

print("Top five for formula1")
print(rank1)

print("Top five for formula2")
print(rank2)

print("mean of price, reviews, and ratings from data")
print(data[["price", "reviews", "ratings"]].mean())

print("mean of price, reviews, and ratings from rank1")
print(rank1[["price", "reviews", "ratings"]].mean())

print("mean of price, reviews, and ratings from rank2")
print(rank2[["price", "reviews", "ratings"]].mean())

reviews_under_fifty = data[data["reviews"] < 50]
print(reviews_under_fifty.sort_values("formula1", ascending = False))
print(rank1)

users = 1000
asignments = np.random.choice(["A", "B"], users)
print(asignments[1:20])

def clicks(ranking):
    top = ranking.iloc[0]
    p = top["ratings"] / 5
    click = np.random.binomial(1, p)
    return click

print(clicks(rank1))

print(clicks(rank2))


def simulasion(asignments, rank_1, rank_2):
    clicks_a = []
    clicks_b = []
    for i in asignments:
        if i == "A":
            click = clicks(rank_1)
            clicks_a.append(click)
        if i == "B":
            click2 = clicks(rank_2)
            clicks_b.append(click2)
    return clicks_a, clicks_b
clicka, clickb = simulasion(asignments, rank1, rank2)
print(clicka)
print(clickb)
print(sum(clicka))
print(sum(clickb))
ctr_a = sum(clicka) / len(clicka)
print(ctr_a)
ctr_b = sum(clickb) / len(clickb)
print(ctr_b)

# for simulasion in range(10):
#     print(simulasion)

results = []

for i in range(1, 11):
    clicka, clickb = simulasion(asignments, rank1, rank2)
    ctr_a = sum(clicka) / len(clicka)
    ctr_b = sum(clickb) / len(clickb)
    results.append((ctr_a, ctr_b))
print(results)

avg_a = np.mean([r[0] for r in results])
avg_b = np.mean([r2[1] for r2 in results])
print(avg_a)
print(avg_b)