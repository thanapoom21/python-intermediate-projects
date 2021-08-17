# Tuple: ordered, immutable, allows duplicate elements

mytuple = tuple(["Thanapoom", 32, "Las Vegas"])
print(mytuple)

item = mytuple[1]

for x in mytuple:
    print(x)

if "Thanapoom" in mytuple:
  print("Yes")
else:
  print("No")