import pandas as pd
dictionary = {
    "student_name" : ["Hina", "Usman", "Ali", "Sara", "Hina", "Ahmed", "Ayesha"],
    "age" : [19, 21, 20, None, 19, 22, 21], 
    "course" : ["Python", "data Science", "           Python", "Web dev", "Python", "dAta Science", "Web Dev"],
    "city" : ["Lahore", "Karachi                ", "Lahore", "Islamabad", "lahore", "karachi", "                   Islamabad"],
    "fee_paid" : [45000, 60000, 45000, 50000, 45000, None, 50000]
}
a = pd.DataFrame(dictionary)

a['age'] = a['age'].fillna(a['age'].mean())
# print(a)
a['fee_paid'] = a['fee_paid'].fillna(a['fee_paid'].mean())
# print(a)
a['course'] = a['course'].str.strip().str.title()
# print(a)
a['city'] = a['city'].str.strip().str.title()
# print(a)
a.to_csv("Student.csv",index = False)
# print(a)
c = pd.read_csv('Student.csv')
# print(c)

# new_student = int(input("How many students do you want to enter: "))
# for i in range(new_student):

#     name = input("Enter a new student: ").strip().title()
#     age = int(input("Enter the age: "))
#     course = input("Enter the course: ").strip().title()
#     city = input("Enter the city: ").strip().title()
#     feepaid = input("Enter the amout of fee: ")

    # student = pd.DataFrame({
    #     'student_name': [name],
    #     'age': [age],
    #     'course': [course],
    #     'city': [city],
    #     'fee_paid': [feepaid]
    # })

    # a = pd.concat([a, student], ignore_index = True)
# print(a)
# searchname = input("What name do you want to search for: ")
# name = a[a['student_name'].str.contains(searchname)]
# print(name)

# searchcity = input("What city do you want to search for: ")
# citys = a[a['city'].str.contains(searchcity)]
# print(citys)

total = len(a)
# print(total)

avg = a['age'].mean()
# print(avg)

maxi = a['fee_paid'].max()
# print(maxi)

mini = a['fee_paid'].min()
# print(mini)

totalnumber = a['fee_paid']
number = 0
for i in totalnumber:
    number += i
print(number)

totalnum = a['fee_paid'].sum()
print(totalnum)

count1 = a['course'].value_counts()
# print(count1)

count2 = a['city'].value_counts()
# print(count2)

row_number = int(input("Enter the row number of student to update: "))
if row_number in a.index:
    new_name = input(f"Name {a.loc[row_number, 'student_name']} : ").strip().title()
    if new_name:
        a.loc[row_number, 'student_name'] = new_name
    new_age = input(f"Age {a.loc[row_number, 'age']}: ")
    if new_age:
        a.loc[row_number, 'age'] = float(new_age)
    new_course = input(f"Course {a.loc[row_number, 'course']}").strip().title()
    if new_course:
        a.loc[row_number, 'course'] = new_course
    new_city = input(f"City {a.loc[row_number, 'city']}").strip().title()
print(a)