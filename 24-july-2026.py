# Lists

# # Shopoing list
# 1.clothes
# 2.electornics
# 3.fruis
# 4.vegetables

# # fruits list
# 1. Apples
# 2. Bananas
# 3. Pears
# 4. Strawberries


# fruit_1 = "Apples"
# fruit_2 = "Bananas"
# fruit_3 = "Pears"
# fruit_4 = "Strawberries"
# fruit_5 = "Grapes"


i = 0
name = 'mouse'

fruits = ["Apples", "Bananas", "Pears", "Strawbs", "Grapes",]
# Index      0          1         2         3          4

print(fruits)


# Reading an item from a list
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])
# print(fruits[5])

# Additon
# 1 + 1, 1.1 + 2.3

# String concatentation
# 'hi' + 'there'

# List concatentation
# [] + []


# Adding a value to a list - List concatentation

fruits = fruits + ["Blackberries"]
#        ["Apples", "Bananas", "Pears", "Strawbs", "Grapes",] + ["Blackberries"]

print(fruits)
# ["Apples", "Bananas", "Pears", "Strawbs", "Grapes", "Blackberries"]

fruits = fruits + ["Cats"]

print(fruits)
# ["Apples", "Bananas", "Pears", "Strawbs", "Grapes", "Blackberries", "Cats"]

print("Length of fruits:", len(fruits))
print("Last value in fruits:", fruits[len(fruits) - 1])

print(fruits[5])


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64,
        65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]

# int()
# str()
# input()
# len()

print(nums[len(nums) - 1])

# huge_list = [f"user_session_{i}" for i in range(100)]

huge_list = ['user_session_0', 'user_session_1', 'user_session_2', 'user_session_3', 'user_session_4', 'user_session_5', 'user_session_6', 'user_session_7', 'user_session_8', 'user_session_9', 'user_session_10', 'user_session_11', 'user_session_12', 'user_session_13', 'user_session_14', 'user_session_15', 'user_session_16', 'user_session_17', 'user_session_18', 'user_session_19', 'user_session_20', 'user_session_21', 'user_session_22', 'user_session_23', 'user_session_24', 'user_session_25', 'user_session_26', 'user_session_27', 'user_session_52', 'user_session_53', 'user_session_54', 'user_session_55',
             'user_session_56', 'user_session_57', 'user_session_58', 'user_session_59', 'user_session_60', 'user_session_61', 'user_session_74', 'user_session_75', 'user_session_76', 'user_session_77', 'user_session_78', 'user_session_79', 'user_session_80', 'user_session_81', 'user_session_82', 'user_session_83', 'user_session_84', 'user_session_85', 'user_session_86', 'user_session_87', 'user_session_88', 'user_session_89', 'user_session_90', 'user_session_91', 'user_session_92', 'user_session_93', 'user_session_94', 'user_session_95', 'user_session_96', 'user_session_97', 'user_session_98', 'user_session_99', 'user_session_39', 'user_session_40', 'user_session_41', 'user_session_42', 'user_session_43', 'user_session_44', 'user_session_45', 'user_session_46', 'user_session_47', 'user_session_48', 'user_session_49', 'user_session_50', 'user_session_51', 'user_session_52', 'user_session_53', 'user_session_54', 'user_session_55', 'user_session_56', 'user_session_57', 'user_session_58', 'user_session_59', 'user_session_60', 'user_session_61', 'user_session_62', 'user_session_63', 'user_session_64', 'user_session_80', 'user_session_81', 'user_session_82', 'user_session_83', 'user_session_84', 'user_session_85', 'user_session_86', 'user_session_87', 'user_session_88', 'user_session_89', 'user_session_90', 'user_session_91']

total_number_of_items = len(huge_list)
print("Total_number_of_items", total_number_of_items)

last_index = len(huge_list) - 1
print("Last Index", last_index)

print("Lats value")
print(huge_list[last_index])


list = []
