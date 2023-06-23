import math

numbA = float(input("Enter A > "))
numbB = float(input("Enter B > "))
numbC = float(input("Enter C > "))

discr = numbB**2 - 4 * numbA * numbC

if discr > 0:
        print("\nRoot 1 > " + str((-numbB + math.sqrt(discr))/ 2 * numbA))
        print("Root 2 > " + str((-numbB - math.sqrt(discr)) / (2 * numbA)))

if discr == 0:
    print("\nRoot 1 > " + str(-numbB / (2 * numbA)))

if discr < 0:
    print("\nRoot no found")