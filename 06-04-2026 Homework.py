#                 Homework – Simulation and A/B Testing Practice
# ===============================================================================

# ● Create a dataset of 20 products using numpy and pandas with the same columns (price,
# rating, reviews, discount, delivery_days)
import numpy as np
a = 20
dictionary = {
    "product_id" : list(range(1, a+1)),
    "price" : np.random.randint(200, 5000, a),
    "ratings" : np.round(np.random.uniform(3.5, 5, a), 1),
    "reviews" : np.random.randint(1, 100, a),
    "discount" : np.random.randint(10, 50, a),
    "delivery_days" : np.random.randint(7, 14, a)
}
import pandas as pd
data = pd.DataFrame(dictionary)
print(data)


# ● Create Rule A and Rule B exactly like class and print top 5 products for both
data["formula1"] = data["ratings"] * np.log(data["reviews"])
data["formula2"] = (data["reviews"] * np.sqrt(data["ratings"])) / np.sqrt(data["price"])

rank1 = data.sort_values("formula1", ascending = False).head()
rank2= data.sort_values("formula2", ascending = False).head()

# print("Top five for formula1")
# print(rank1)

# print("Top five for formula2")
# print(rank2)



# ● Explain in 2–3 lines why the top 5 of A and B are different
# Becuase A is printed based on ratings and reviews.
# Meanwhile B is printed pased on reviews, ratings, and price.



# ● Create assignments for 1500 users and print first 20 values
users = 1500
asignments = np.random.choice(["A", "B"], users)
print(asignments[1:20])

def clicks(ranking):
    top = ranking.iloc[0]
    p = top["ratings"] / 5
    click = np.random.binomial(1, p)
    return click
print(clicks(rank1))
print(clicks(rank2))



# ● Run the simulation using run_simulation function and print total clicks for A and B
def simulasion(asignments, rank_1, rank_2):
    list_A = []
    list_B = []
    for i in asignments:
        if i == "A":
            click = clicks(rank_1)
            list_A.append(click)
        if i == "B":
            click2 = clicks(rank_2)
            list_B.append(click2)
    return list_A, list_B
clicka, clickb = simulasion(asignments, rank1, rank2)

print(clicka)
print(clickb)

# ● Calculate CTR for both rules and print them
ctr_a = sum(clicka) / len(clicka)
print(ctr_a)
ctr_b = sum(clickb) / len(clickb)
print(ctr_b)



# ● Write in 1–2 lines which rule performed better and why you think so
# I think rule 'B' performed better becuase there were 13 'B's printed and only 6 'A's.



# ● Run the experiment 15 times and store CTR values in results list
results = []
for i in range(1, 16):
    clicka, clickb = simulasion(asignments, rank1, rank2)
    ctr_a = sum(clicka) / len(clicka)
    ctr_b = sum(clickb) / len(clickb)
    results.append((ctr_a, ctr_b))



# ● Print the full results list
print(results)



# ● Calculate average CTR for A and B
avg_a = np.mean([r[0] for r in results])
avg_b = np.mean([r2[1] for r2 in results])
print(avg_a)
print(avg_b)



# ● Create two separate lists list_A and list_B and store CTR values in them
list_A = [r[0] for r in results]
list_B = [r[1] for r in results]
print(list_A)
print(list_B)

# ● Print max and min CTR for both A and B
min_a = np.min([min_a[0] for min_a in results])
max_a = np.max([max_a[0] for max_a in results])
min_b = np.min([min_b[1] for min_b in results])
max_b = np.max([max_b[0] for max_b in results])
print(min_a)
print(max_a)
print(min_b)
print(max_b)



# ● Plot CTR values for A and B using matplotlib (Practice)
import matplotlib.pyplot as plt
# plt.bar(data["list_A"], data["list"])
# plt.title("ctr values for A and B")
# plt.xlabel("A")
# plt.ylabel("B")
# plt.show()

plt.plot(list_A, label = "rule_a")
plt.plot(list_B, label = "rule_b")
plt.xlabel("simulation")
plt.ylabel("customer choice")
plt.title("A and B values")
plt.show()


desc_discount = data.sort_values("discount", ascending = False)
print(desc_discount)


print(data[data["ratings"] > 4])
print(data[data["discount"] > 20])

print(data[(data["ratings"] > 4) & (data["discount"] > 20)])

print(data[(data["delivery_days"] > 10) & (data["ratings"] > 3.5)])

for number1, number2 in enumerate(results, 1):
    print(number1, number2)

