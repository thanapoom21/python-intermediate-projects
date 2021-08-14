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

print(nums[5::1]) # double colon means optional index

print(nums[0::1]) # this will start from the first item the last item

print(nums[::1])  # this will start from the first item the last item

print(nums[::2])  # this will take every second items [1,3,5,7,9]

print(nums[::-1])