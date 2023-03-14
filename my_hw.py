print("Grocery store 'ATB'")

def is_exit():
    result = input("Do you wanna quit ? y/n : ")
    return result.lower()

def registration (login , password , balance):
    return {
        "login" : login,
        "password" : password,
        "balance": balance
    }

def show_products (list_of_products):
    for product in list_of_products:
        print("\n")
        for key , value in product.items():
            print(key + "       " + value)

def auth (login , array_of_users) :
    for user in array_of_users :
        if login in user['login'] :
#            print("hi user")

            password = input("Enter your account's password : ")

            if password == user['password'] :
                return [user , True]

            else :
                print("Incorrect password")

        else:
            print("Incorrect login")

def get_balance (account) :
    print("[USER_BALANCE]", account['balance'], "UAN")

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

def buy_food (target , list_of_products) :
    for product in list_of_products:
        if target.lower() == product['label'].lower():
            sliced_price = product['price'].find("U")
            if float(current_user['balance']) > float(product['price'][:sliced_price - 1]):
                current_user['balance'] = float(current_user['balance']) - float(product['price'][:sliced_price - 1])
                current_user_food.append(prefer_food)
            else:
                print("You don't have enough money, top up your balance")

    print(f"You have left {str(current_user['balance'])} on your balance")

products = [
    {
        "label" : "coca_cola", 
        "price" : "50 UAH"
    },
    {
        "label" : "fanta", 
        "price" : "45 UAH"
    },
    {
        "label" : "sprit", 
        "price" : "40 UAH"
    },
    {
        "label" : "bread", 
        "price" : "30 UAH"
    },
    {
        "label" : "potato", 
        "price" : "10 UAH"
    },
    {
        "label" : "carrot", 
        "price" : "25 UAH"
    },
    {
        "label" : "cabbage", 
        "price" : "35 UAH"
    },
    {
        "label" : "beet", 
        "price" : "35 UAN"
    },
    {
        "label" : "cabbage", 
        "price" : "35 UAH"
    },
    {
        "label" : "bananas", 
        "price" : "39 UAH"
    },
    {
        "label" : "apples", 
        "price" : "17.50 UAH"
    }
    ] 

user_name = input("Hi, what's your name : ")
print(user_name + " choose what you want?")

is_running = True

is_registred = False

users = [
#    {
#        "login" : "admin",
#        "password" : "admin",
#        "balance" : "1200"
#    }
]

current_user = {}

current_user_food = []


while is_running :
    user_choose = input("""
        a) I want to get acquainted with the assortment of the store 
        b) I want to shop in your store 
        c) I want to register
        d) I want to autorisation
        e) I want to know how much money I have
        q) I want to leave your store
        
    I want : """).lower()

    if user_choose == "a" :
        show_products(products)

    elif user_choose == "b":
        if not is_registred :
            print("Only registered customers can make purchases in the store! Please register or autorisation ")
            continue

        show_products(products)

        prefer_food = input("Choose car that you want buy : ")

        buy_food(prefer_food ,products)

#        current_user_food.append(prefer_food)
        print(current_user_food)

    elif user_choose == "c":
        login = input("Enter login that you want to use continuously : ")
        password = input("Enter your password : ")
        balance = input("How much money do you want to send? : ")

        user = registration(login ,password, balance)

        users.append(user)
        print(users)

    elif user_choose == "d":
     
        login = input("Enter your account's login : ")

        result = auth(login  , users)
        current_user , is_registred = result
        print(current_user)
        print(is_registred)

    elif user_choose == "e":

        if not is_registred :
            print(user_name + ", please register!")
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
