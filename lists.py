# Lists: ordered, mutable, allows duplicate elements
fruits = ["banana", "cherry", "apple"]
print(fruits)

for fruit in fruits:
    print(fruit)

if "banana" in fruits:
    print("yes")
else:
    print("no")


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[1:5])  # start index and stop index // [2, 3, 4, 5]
