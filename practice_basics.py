#set up an empty list
list = []

#append names to the list
list.append("tonny")
list.append("jack")
list.append("mike")
list.append("smith")
list.append("james")
list.append("robert")

#display the list after appending names
print(list)

#3 ways to remove names from the list
list.remove("jack")
del list[2]  #removing "smith" by index
first_friend = list.pop(0)  #removing and storing the first name
print(list)
print(f"{first_friend} is my best friend.")

print(f"{list[0]} and {list[1]} are good friends.")

#insert a new name at a specific position
list.insert(2, "alice")  #adding a new name at the 3rd position
print(list)

#display names in different formats
print(list[0].upper())
print(list[1].title())
print(list[2].lower())