# Lists: ordered, mutable, allows duplicate elements
fruits = ["banana", "cherry", "apple"]

print(fruits)

fruits_copy1 = fruits  # this refers to the same list

# when the copied list is mutated, the original will also be changed.
fruits_copy1.append("durian")

fruits_copy2 = fruits.copy()

fruits_copy2.append("elderberry")

fruits_copy3 = list(fruits)

print(fruits)
print(fruits_copy1)
print(fruits_copy2)
print(fruits_copy3)

for fruit in fruits:
    print(fruit)

if "banana" in fruits:
    print("yes")
else:
    print("no")


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[1:5])  # start index and stop index // [2, 3, 4, 5]

print(nums[5::1])  # double colon means optional index

print(nums[0::1])  # this will start from the first item the last item

print(nums[::1])  # this will start from the first item the last item

print(nums[::2])  # this will take every second items [1,3,5,7,9]

print(nums[::-1])

num_list = [3, 6, 9, 12, 15, 18, 21]

squared_num_list = [x * x for x in num_list]

print(num_list)
print(squared_num_list)
