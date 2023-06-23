counter = {}
N = int(input("Enter N > "))

for elementNumb in range (1, N + 1):
    element = input(str(elementNumb) + ".Enter element > ")
    if element in counter:
        counter[element] += 1
    else:
        counter[element] = 1

key = input("\nEnter the desired item > ")
print("\nItem > " + key + ' - ' + str(counter[key]))