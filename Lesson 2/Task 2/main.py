elements = input("Enter > ")
sortedElements = []

for element in elements:
    if element not in sortedElements:
        sortedElements.append(element)

print("Elements without duplicates > " + str(sortedElements))