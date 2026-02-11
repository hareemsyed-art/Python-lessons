import pandas as pd
a = pd.read_csv("vgsales.csv")
#       Part 1: Basic Inspection
# ========================================
# # 1. Show the first 5 rows of the dataset.
# print(a.head())

# # 2. Show the last 5 rows of the dataset.
# print(a.tail())

# 3. Find the total number of rows and columns in the dataset.
# print(a.shape)

# # 4. List all column names.
# print(a.columns)

# # 5. Show the dataset information (data types and non-null values).
# print(a.info())

# # 6. Show the statistical summary of the dataset.
# print(a.describe())


#       Part 2: Column Selection
# =======================================================
# # 7. Show only the "Name" column.
# print(a["Name"])

# # 8. Show the "Name" and "Genre" columns together.
# print(a[["Name", "Genre"]])

# # 9. Show the "Name", "Platform", and "Year" columns.
# print(a[["Name", "Platform", "Year"]])


# #       Part 3: Filtering Data
# # ========================================
# # 10. Show all games released after the year 2010.
# print(a[a["Year"] == 2010])
# # 11. Show all games released before the year 2005.
# print(a[a["Year"] == 2005])

# # 12. Show all games with Genre "Action".
# print(a[a["Genre"] == "Action"])

# # 13. Show all games with Genre "Sports".
# print(a[a["Genre"] == "Sports"])

# # 14. Show all games released on the "PS4" platform.
# print(a[a["Platform"] == "PS4"])

# # 15. Show all games released on the "PC" platform
# print(a[a["Platform"] == "PC"])


# #       Part 4: Multiple Conditions
# # ==========================================
# # 16. Show all Action games released after 2010.
# print(a[(a["Genre"] == "Action") & (a["Year"] >= 2010)])

# # 17. Show all Sports games released before 2008.
# print(a[(a["Genre"] == "Sports") & (a["Year"] <= 2008)])

# # 18. Show all games released on PS4 after 2015.
# print(a[(a["Platform"] == "PS4") & (a["Year"] >= 2015)])

# # 19. Show all games released on PC before 2000.
# print(a[(a["Platform"] == "PC") & (a["Year"] >= 2000)])