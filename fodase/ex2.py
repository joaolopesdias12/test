moneyAccept = [0.01,0.02,0.05,0.1,0.2,0.5,1,2,5,10,20,50,100,200,500]

billet = 2.20
tcasual = 10.20
tmes = 54.0
ttrimestre = 145.30
tjove = 105.00

amountToPay = 0.0

def zones_ticket (zone: float):
    match zone:
        case zone if zone == 1:
            return 1
        case zone if zone == 2:
            return 1.35
        case zone if zone == 3:
            return 1.89

def buy_ticket (type: str, zone: int):
    match type:
        case type if type == "Billet senzill":
            print("Price to pay " + str(round((billet * zones_ticket(zone)),2)))
            return round((billet * zones_ticket(zone)),2)
        
        case type if type == "TCasual":
            print("Price to pay " + str(round((tcasual * zones_ticket(zone)),2)))
            return round((tcasual * zones_ticket(zone)),2)
        
        case type if type == "TMes":
            print("Price to pay " + str(round((tmes * zones_ticket(zone)),2)))
            return round((tmes * zones_ticket(zone)),2)

        case type if type == "TTrimestre":
            print("Price to pay " + str(round((ttrimestre * zones_ticket(zone)),2)))
            return round((ttrimestre * zones_ticket(zone)),2)

        case type if type == "TJove":
            print("Price to pay " + str(round((tjove * zones_ticket(zone)),2)))
            return round((tjove * zones_ticket(zone)),2)


choice = str(input("What ticket would you like to purchase? "))
zone = int(input("How many zones? (1,2,3)"))


amountToPay = buy_ticket(choice,zone)

while amountToPay > 0.0:
    print(str(amountToPay) + " left to pay!")
    money = float(input("Insert money:"))
    if money in moneyAccept:     
        amountToPay = round((amountToPay - money),2)
        if amountToPay < 0.0:
            print("You change is " + str(amountToPay * -1) + "€")
    else:
        print("This currency doesnt exist")
