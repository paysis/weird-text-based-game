import random

multiplayer = False

player_1_money = 500
player_2_money = 500

player_1_level = 1
player_2_level = 1

STARTING_BUSINESS = "starting_business"
INVEST_IN_STOCKS = "invest_in_stocks"
INVEST_IN_REAL_ESTATE = "invest_in_real_estate"

# BEGIN BUSINESS
LEMONADE_STAND = "Lemonade stand"
CAR_WASH = "Car wash"
BAKERY = "Bakery"
RESTAURANT = "Restaurant"
TECH_COMPANY = "Tech company"
BANK = "Bank"
LAW_FIRM = "Law firm"

EBEBEK = "e-bebek"
KFC = "KFC"
MCDONALDS = "McDonald's"
BURGER_KING = "Burger King"

BEACH_HOUSE = "Beach House"
APARTMENT_COMPLEX = "Apartment Complex"
SHOPPING_MALL = "Shopping Mall"

player_1_businesses = []
player_1_stocks = []
player_1_real_estate = []

player_2_businesses = []
player_2_stocks = []
player_2_real_estate = []
# END BUSINESS


def get_businesses(player):
    global player_1_businesses, player_2_businesses
    if player == 1:
        return player_1_businesses
    else:
        return player_2_businesses


def add_business(player, business):
    global player_1_businesses, player_2_businesses
    if player == 1:
        player_1_businesses.append(business)
    else:
        player_2_businesses.append(business)


def get_stock(player):
    global player_1_stocks, player_2_stocks
    if player == 1:
        return player_1_stocks
    else:
        return player_2_stocks


def add_stock(player, stock):
    global player_1_stocks, player_2_stocks
    if player == 1:
        player_1_stocks.append(stock)
    else:
        player_2_stocks.append(stock)


def get_real_estate(player):
    global player_1_real_estate, player_2_real_estate
    if player == 1:
        return player_1_real_estate
    else:
        return player_2_real_estate


def add_real_estate(player, real_estate):
    global player_1_real_estate, player_2_real_estate
    if player == 1:
        player_1_real_estate.append(real_estate)
    else:
        player_2_real_estate.append(real_estate)


def get_money(player):
    global player_1_money, player_2_money
    if player == 1:
        return player_1_money
    else:
        return player_2_money


def print_money(player):
    global player_1_money, player_2_money
    if player == 1:
        print("You have $" + str(player_1_money))
    else:
        print("You have $" + str(player_2_money))


def get_level(player):
    global player_1_level, player_2_level
    if player == 1:
        return player_1_level
    else:
        return player_2_level


def print_level(player):
    global player_1_level, player_2_level
    if player == 1:
        print("You are level " + str(player_1_level))
    else:
        print("You are level " + str(player_2_level))


def increase_money(player, amount):
    global player_1_money, player_2_money
    if player == 1:
        player_1_money += amount
    elif player == 2:
        player_2_money += amount
    else:
        print("Error: Invalid player number.")


def decrease_money(player, amount):
    global player_1_money, player_2_money
    if player == 1:
        player_1_money -= amount
        if player_1_money < 0:
            player_1_money = 0
    elif player == 2:
        player_2_money -= amount
        if player_2_money < 0:
            player_2_money = 0
    else:
        print("Error: Invalid player number.")


def increase_level(player):
    global player_1_level, player_2_level
    if player == 1:
        player_1_level += 1
    elif player == 2:
        player_2_level += 1
    else:
        print("Error: Invalid player number.")


def decrease_level(player):
    global player_1_level, player_2_level
    if player == 1:
        player_1_level -= 1
        if player_1_level < 0:
            player_1_level = 0
    elif player == 2:
        player_2_level -= 1
        if player_2_level < 0:
            player_2_level = 0
    else:
        print("Error: Invalid player number.")


def random_business_gacha():
    business_gacha = random.randint(1, 7)

    if business_gacha == 1:
        return LEMONADE_STAND
    elif business_gacha == 2:
        return CAR_WASH
    elif business_gacha == 3:
        return BAKERY
    elif business_gacha == 4:
        return RESTAURANT
    elif business_gacha == 5:
        return TECH_COMPANY
    elif business_gacha == 6:
        return BANK
    elif business_gacha == 7:
        return LAW_FIRM


def random_stocks_gacha():
    stocks_gacha = random.randint(1, 4)

    if stocks_gacha == 1:
        return EBEBEK
    elif stocks_gacha == 2:
        return KFC
    elif stocks_gacha == 3:
        return MCDONALDS
    elif stocks_gacha == 4:
        return BURGER_KING


def random_real_estate_gacha():
    real_estate_gacha = random.randint(1, 3)

    if real_estate_gacha == 1:
        return BEACH_HOUSE
    elif real_estate_gacha == 2:
        return APARTMENT_COMPLEX
    elif real_estate_gacha == 3:
        return SHOPPING_MALL


random_business_1 = random_business_gacha()
random_business_2 = random_business_gacha()


def start_business(player):
    global random_business_1, random_business_2
    while True:
        print("You have the following businesses:", get_businesses(player))
        print("You have decided to start a business.")
        print_level(player)
        print_money(player)
        print("You can start a:")

        if random_business_1 is not None:
            print("1. " + random_business_1)
        if random_business_2 is not None:
            print("2. " + random_business_2)
        print("3. Back")

        choice = input("What would you like to do? ")

        if choice == "1" and random_business_1 is not None:
            if get_level(player) >= 1 and get_money(player) >= 100:
                print("You have started a " + random_business_1 + ".")
                add_business(player, random_business_1)
                random_business_1 = None
                increase_level(player)
                decrease_money(player, 100)
                break
            else:
                print("You are not a high enough level.")
        elif choice == "2" and random_business_2 is not None:
            if get_level(player) >= 1 and get_money(player) >= 100:
                print("You have started a " + random_business_2 + ".")
                add_business(player, random_business_2)
                random_business_2 = None
                increase_level(player)
                decrease_money(player, 100)
                break
            else:
                print("You are not a high enough level.")
        elif choice == "3":
            break


random_stocks_1 = random_stocks_gacha()
random_stocks_2 = random_stocks_gacha()


def invest_in_stocks(player):
    global random_stocks_1, random_stocks_2
    while True:
        print("You have the following stocks:", get_stock(player))
        print("You have decided to invest in stocks.")
        print_level(player)
        print_money(player)
        print("You can invest in:")

        if random_stocks_1 is not None:
            print("1. " + random_stocks_1)
        if random_stocks_2 is not None:
            print("2. " + random_stocks_2)
        print("3. Back")

        choice = input("What would you like to do? ")

        if choice == "1" and random_stocks_1 is not None:
            if get_level(player) >= 1 and get_money(player) >= 100:
                print("You have invested in " + random_stocks_1 + ".")
                add_stock(player, random_stocks_1)
                random_stocks_1 = None
                increase_level(player)
                decrease_money(player, 100)
                break
            else:
                print("You are not a high enough level.")
        elif choice == "2" and random_stocks_2 is not None:
            if get_level(player) >= 1 and get_money(player) >= 100:
                print("You have invested in " + random_stocks_2 + ".")
                add_stock(player, random_stocks_2)
                random_stocks_2 = None
                increase_level(player)
                decrease_money(player, 100)
                break
            else:
                print("You are not a high enough level.")
        elif choice == "3":
            break


random_real_estate_1 = random_real_estate_gacha()
random_real_estate_2 = random_real_estate_gacha()


def invest_in_real_estate(player):
    global random_real_estate_1, random_real_estate_2
    while True:
        print("You have the following real estate:", get_real_estate(player))
        print("You have decided to invest in real estate.")
        print_level(player)
        print_money(player)
        print("You can invest in:")

        if random_real_estate_1 is not None:
            print("1. " + random_real_estate_1)
        if random_real_estate_2 is not None:
            print("2. " + random_real_estate_2)
        print("3. Back")

        choice = input("What would you like to do? ")

        if choice == "1" and random_real_estate_1 is not None:
            if get_level(player) >= 1 and get_money(player) >= 100:
                print("You have invested in " + random_real_estate_1 + ".")
                add_real_estate(player, random_real_estate_1)
                random_real_estate_1 = None
                increase_level(player)
                decrease_money(player, 100)
                break
            else:
                print("You are not a high enough level.")
        elif choice == "2" and random_real_estate_2 is not None:
            if get_level(player) >= 1 and get_money(player) >= 100:
                print("You have invested in " + random_real_estate_2 + ".")
                add_real_estate(player, random_real_estate_2)
                random_real_estate_2 = None
                increase_level(player)
                decrease_money(player, 100)
                break
            else:
                print("You are not a high enough level.")
        elif choice == "3":
            break


def charity(player):
    while True:
        get_level(player)
        print("1. Donate $100 to charity")
        print("2. Donate $500 to charity")
        print("3. Donate $1000 to charity")
        print("4. Back")

        choice = input("What would you like to do? ")

        if choice == "1":
            if get_money(player) < 100:
                print("You do not have enough money.")
                continue
            decrease_money(player, 100)
            print("You have donated $100 to charity. You gain 1 level.")
            increase_level(player)
        elif choice == "2":
            if get_money(player) < 500:
                print("You do not have enough money.")
                continue
            decrease_money(player, 500)
            print("You have donated $500 to charity. You gain 5 levels.")
            for _ in range(5):
                increase_level(player)

        elif choice == "3":
            if get_money(player) < 1000:
                print("You do not have enough money.")
                continue
            decrease_money(player, 1000)
            print("You have donated $1000 to charity. You gain 10 levels.")
            for _ in range(10):
                increase_level(player)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def explore_opportunities(player):
    while True:
        print("1. Start a business")
        print("2. Invest in stocks")
        print("3. Invest in real estate")
        print("4. Back")

        choice = input("What would you like to do? ")

        if choice == "1":
            start_business(player)
        elif choice == "2":
            invest_in_stocks(player)
        elif choice == "3":
            invest_in_real_estate(player)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def random_end_of_day_event(player):
    end_of_day_event = random.randint(1, 11)

    if end_of_day_event == 1:
        print("You have found a $100 bill on the ground.")
        increase_money(player, 100)
    elif end_of_day_event == 2:
        print("You have found a $500 bill on the ground.")
        increase_money(player, 500)
    elif end_of_day_event == 3:
        print("You have found a $1000 bill on the ground.")
        increase_money(player, 1000)
    elif end_of_day_event == 4:
        print("You have found a $5000 bill on the ground.")
        increase_money(player, 5000)
    elif end_of_day_event == 5:
        print("You wet your pants. You lose $100.")
        decrease_money(player, 100)
    elif end_of_day_event == 6:
        print("A galactic alien has come to Earth and has given you $1000.")
        increase_money(player, 1000)
    elif end_of_day_event == 7:
        print("You have been robbed. You lose $1000.")
        decrease_money(player, 1000)
    elif end_of_day_event == 8:
        print("You have been robbed. You lose $5000.")
        decrease_money(player, 5000)
    elif end_of_day_event == 9:
        print("Avatar Aang has come to Earth and has robbed you. You lose $1000.")
        decrease_money(player, 1000)
    elif end_of_day_event == 10:
        print("A succubus has sucked your essence. You lose 1 level.")
        decrease_level(player)
    elif end_of_day_event == 11:
        print("You have killed a succubus. You gain 1 level.")
        increase_level(player)


def menu():
    player = 1

    print("Multiplayer ? (y/N)")
    choice = input("What would you like to do? ")

    global multiplayer
    if choice == "y" or choice == "Y":
        multiplayer = True
        print("You have chosen multiplayer.")
    else:
        multiplayer = False
        print("You have chosen singleplayer.")

    if multiplayer:
        player = random.randint(1, 2)

    while True:
        if multiplayer:
            print(player)
            player = 2 if player == 1 else 1
        print("-- Player " + str(player) + "'s turn.")

        print_level(player)
        print_money(player)

        print("1. Explore opportunities")
        print("2. Charity")
        print("3. Next day (skip)")
        print("4. Status")
        print("q. Quit the game")

        choice = input("What would you like to do? ")

        if choice == "1":
            explore_opportunities(player)
        elif choice == "2":
            charity(player)
        elif choice == "3":
            # Make current player lose or earn money/level randomly
            random_end_of_day_event(player)
            # Update businesses and stocks next day
            global random_business_1, random_business_2
            random_business_1 = random_business_gacha()
            random_business_2 = random_business_gacha()

            global random_stocks_1, random_stocks_2
            random_stocks_1 = random_stocks_gacha()
            random_stocks_2 = random_stocks_gacha()

            global random_real_estate_1, random_real_estate_2
            random_real_estate_1 = random_real_estate_gacha()
            random_real_estate_2 = random_real_estate_gacha()

            # end of game check
            if get_level(1) <= 0:
                print("Player 2 has won.")
                break
            elif get_level(2) <= 0:
                print("Player 1 has won.")
                break
        elif choice == "4":
            if multiplayer:
                print("Player 1:")
                print_money(1)
                print("Player 2:")
                print_money(2)
            else:
                print_money(player)

            if multiplayer:
                print("-Player 1:")
                print_level(1)
                print("-Player 2:")
                print_level(2)
            else:
                print_level(player)
        elif choice == "q":
            break


def main():
    print(
        "In the city of Prospera, you will embark on a journey to become the richest person in the city."
    )
    menu()


main()
