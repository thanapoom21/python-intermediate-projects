# Dictionary: Key-value pairs, unordered, mutable.

person = {"name": "Payet", "age": 30, "city": "Marseille"}
# print(person)

# if "name" in person:
#     print(person["name"])

# try:
#     print(person["age"])
# except:
#     print("Error")

# for key in person:
#     print(key)

# for key, value in person.items():
#     print(key, value)

person_copy = person

person_copy2 = person.copy()

person_copy3 = dict(person)

person_copy["email"] = "payetdimitri@gmail.com"
print(person_copy)
print(person_copy2)
print(person_copy3)
print(person)
