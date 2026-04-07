a = ["apple", "strawberry", "milk", "sugar"]
for i in a:
    print(i)

for i, j in enumerate(a, 1):
    print(i, j)

def square(a): 
    number = a * a
    return number
# print(square(5))


print((lambda x:x*x)(5))

print((lambda x:x+x)(5))

print((lambda a,b:a+b)(10, 20))
