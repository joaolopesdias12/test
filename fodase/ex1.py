def ex1(water: int):
    match water:
        case water if water <= 50.0:
         return print("Your cost is 6€")
    
        case water if water >  50 and water < 200:
         water2 = (water - 50) * 0.1 + 6
         return print("Your cost is " + str(water2))

        case water if water > 200:
         water3 = (water - 50) * 0.3 + 6
         return print("Your cost is " + str(water3))

print("How many liters of water did you consume this month?")
water = int(input())

ex1(water)