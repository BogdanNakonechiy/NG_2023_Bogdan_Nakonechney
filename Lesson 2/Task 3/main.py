array = []

for counter in range(0,3):
    array[counter] = input("Enter element > ")

for symbol in array:
    seen = set()
    duplicates = set()

    for item in symbol:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    print("Duplicate > " + str(duplicates))