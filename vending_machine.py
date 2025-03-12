drinks = {
    "cola":3.35,
    "pepsi":2.10,
    "orange": 2.85
}


accepted_coins = [5, 10, 15, 20]

def get_coin():
    while True:
        try:
            coin = int(input(f"Please insert a coin: {accepted_coins}: "))

            if coin in accepted_coins:
                return coin

            print("Invalid coin")     
        except ValueError:
            print("Invalid input")
    


def vending_machine():
    print("Welcome to the vending machine")
    total_coins = 0;
    

    total_coins += get_coin()
    while True:

        print(f"Please select a drink: {drinks}")
        drink = input().strip().lower()

        if drink not in drinks:
            print("Invalid drink")
            continue

        while total_coins < drinks[drink]:
            print("Not enough coins")
            total_coins += get_coin()
            continue

        total_coins -= drinks[drink]
        print(f"Here is your {drink}, your remaining balance is {total_coins:.2f}")


        print("Want to buy another drink? (y/n)")
        another_drink = input()
        if another_drink == "n":
            break






vending_machine()
