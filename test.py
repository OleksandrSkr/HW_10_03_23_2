# 1) Context menu : a) All products b) Buy product c) Registration d) Auth e) Balance q) Quit
#  product - manufacturer , label , price , date

# Dict -> object
# {
#    "key" : "value"
# }

# a)  All products - print all products into the console
# []

# b) cart -> history of user shopping

# user = { "login" , "password" , "money" , "money_transfer"}
# c)  - register / auth
# q)  - quit
# buy car
# money_transfer

# e) Balance

# b)  Buy product -> if money enough -> buy car -> - money

from datetime import date

def is_exit():
    result = input("Do you wanna quit ? y/n : ")
    return result.lower()

def registration (login , password , balance = 0):
    return {
        "login" : login,
        "password" : password,
        "balance": balance
    }

def show_products (list_of_products):
    for product in list_of_products:
        print("\n")
        print("***********************" + product['label'] + "***********************\n")

        for key , value in product.items() :
            if key == "date":
                print(key + " ====> " + str(value))
                continue

            print(key + " ====> " + value)

def auth (login,array_of_users) :
    for user in array_of_users :
        if login in user['login'] :

            password = input("Enter your account's password : ")

            if password == user['password'] :
                return [user , True]

            else :
                print("Incorrect password")

        else:
            print("Incorrect login")

def get_balance (account) :
    print("[USER_BALANCE]", account['balance'], "Y.E.")

def money_transfer (account) :
    card_number = input("Enter your card number : ")

    card_date = input("Enter your card date : ")

    card_cvv = input("Enter your card cvv : ")

    # card number must consist of 15 symbols
    # card date must includes "/"
    # card_cvv must consist of 3 symbols

    # if error => print error into the console

    money = input("How much money do you want to send? : ")

    account['balance'] = int(account['balance']) + int(money)
    print(f"Congratulations now your balance is : {str(account['balance'])} y.e")

def buy_car (target , list_of_products) :
    for product in list_of_products:
        if target.lower() == product['label'].lower():
            sliced_price = product['price'].find("y")
            if int(current_user['balance']) > int(product['price'][:sliced_price - 1]):
                current_user['balance'] = current_user['balance'] - int(product['price'][:sliced_price - 1])
            else:
                print("You don't have enough money, top up your balance")

    print(f"After you bought the car there is left {str(current_user['balance'])} on your balance")

products = [
    {
        "manufacturer" : "Czech Republic",
        "label" : "Skoda",
        "price" : "30000 y.e",
        "date" : date(2023,11,1),
        "category" : "sedan"
    },
    {
        "manufacturer": "Italy",
        "label": "Fiat",
        "price": "20000 y.e",
        "date": date(2021, 6, 1),
        "category" : "sedan"
    },
    {
        "manufacturer": "Germany",
        "label": "BMW",
        "price": "10000 y.e",
        "date": date(2002, 8, 1),
        "category" : "crossover"
    },
    {
        "manufacturer": "Germany",
        "label": "MB",
        "price": "20000 y.e",
        "date": date(2012, 12, 2),
        "category" : "sedan"
    },
    {
        "manufacturer": "Germany",
        "label": "VW",
        "price": "10000 y.e",
        "date": date(2011, 12, 2),
        "category" : "truck"
    },
    {
        "manufacturer": "Italy",
        "label": "Alfa Romeo",
        "price": "10000 y.e",
        "date": date(2021, 6, 12),
        "category" : "crossover"
    },
]

is_running = True

is_registred = False

users = [
    {
        "login" : "admin",
        "password" : "admin",
        "balance" : "1200"
    }
]

current_user = {}

while is_running :
    user_choose = input("""
        a) Show products 
        b) Buy product 
        c) Register
        d) Auth
        e) Balance
        q) Quit
        
    Answer : """).lower()

    if user_choose == "a" :
        show_products(products)

    elif user_choose == "b":
        show_products(products)

        prefer_car = input("Choose car that you want buy")

        buy_car(prefer_car ,products)

    elif user_choose == "c":
        login = input("Enter login that you want to use continuously : ")
        password = input("Enter your password : ")

        user = registration(login ,password)

        users.append(user)
        print(users)

    elif user_choose == "d":
        login = input("Enter your account's login : ")

        result = auth(login  ,users)
        current_user , is_registred = result
        print(current_user)
        print(is_registred)

    elif user_choose == "e":

        if not is_registred :
            print("Error!")
            continue

        user_choose = input("""
            1) Look at bill
            2) Transfer by card 
        """)

        if user_choose == "1" :

            if is_registred == True :
                get_balance(current_user)

            else :
                print("You should to have an account to look at balance")

        elif  user_choose == "2":
            money_transfer(current_user)

    elif user_choose == "q":
        result = is_exit()

        if result == "y" :
            is_running = False
