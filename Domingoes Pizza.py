import csv
from datetime import datetime


# Order class that prompts user and creates order

def OrderMain():
    temp=0
    descList=[]
    pizzaList=[]

    print("""
        Hello, welcome to the DominGoes Pizza!
            Make your choice and enjoy your meal!
                 """)
    baseDict = {"Margherita": 1, "Classic": 2, 'Thicc': 3, "Gluten Free": 4}

    toppDict = {"Olives": 1, "Mushrooms": 2, "Parmiggiani": 3, 'Pepperoni': 4,
                "Onion": 5, 'Corn': 6, "Basil": 7, "Broccoli":8, "No Topping":9}

    print("Here's the base materials you can choose from:")
    for a in baseDict.keys():
        print(str(baseDict.get(a))+f" {a}")

    while True:
        baseType=int(input("Please choose dough type:"))

        match baseType:
            case 1:
                pizzaAttain=Margherita()
                pType="Margherita"
                break
            case 2:
                pizzaAttain=Classic()
                pType="Classic"
                break
            case 3:
                pizzaAttain=Thicc()
                pType="Thicc"
                break
            case 4:
                pizzaAttain=GlutenFree()
                pType="GlutenFree"
                break
            case _:
                print("Invalid input.")
        continue            # location of continue is vital since it can put the program in deadlock. If put 2 indents in, for example.

    print("And now the toppings...")
    for a in toppDict.keys():
        print(str(toppDict.get(a))+f" {a}")



    while True:
        toppType = int(input("Please choose toppings:"))
        match toppType:
            case 1:
                toppAttain=decOlive()
                tType="Olives"
                break
            case 2:
                toppAttain=decMushroom()
                tType="Mushrooms"
                break
            case 3:
                toppAttain=decParmiggiani()
                tType="Parmiggiani"
                break
            case 4:
                toppAttain=decPepperoni()
                tType="Pepperoni"
                break
            case 5:
                toppAttain=decOnion()
                tType="Onion"
                break
            case 6:
                toppAttain=decCorn()
                tType="Corn"
                break
            case 7:
                toppAttain=decBasil()
                tType="Basil"
                break
            case 8:
                toppAttain=decBrocco()
                tType="Broccoli"
                break
            case 9:
                toppAttain=decNoThx()
                tType="Toppingless"
                break
            case _:
                print("Invalid input. Try Again:")
        continue

    placeOrder=allTogether(pizzaAttain, toppAttain)     # creating order with received inputs
    print(f"Your order: {pType} with {tType} that costs {placeOrder.get_cost()}")
    temp+=placeOrder.get_cost()
    descList.append(placeOrder.get_description())
    pizzaList.append([pType, tType])

    customerName=input("Your name:")
    customerLName=input("Your last name:")
    customerIDNo=input("Your ID Number:")
    customerCardNo=input("Your credit card number:")
    CardSecNo=input("3-digit security code behind your credit card:")


    # I gathered all the info as a list, just not to be overencumber the program with another loop

    csvRaw=[customerName, customerLName, customerIDNo, customerCardNo, CardSecNo, "{0} $".format(temp),
                        pizzaList, descList, datetime.now()]

    with open("orderCredentials.csv","a") as fOpt:
        clWriter=csv.writer(fOpt)
        clWriter.writerow(csvRaw)

# Pizza class and its inheritors

class Pizza:
    def get_description(self):
        return self.desc

    def get_cost(self):
        return self.price


class Margherita(Pizza):
    def __init__(self):
        self.price=40
        self.desc="Straight outta Napoli, nothing but tomatoes, Mozzarella and basil. "

class Classic(Pizza):
    def __init__(self):
        self.price=60
        self.desc="Your typical midnight munchie, top it off as you please."

class Thicc(Pizza):
    def __init__(self):
        self.price=50
        self.desc="Hate fries? Then more of that soft dough would do the trick."

class GlutenFree(Pizza):
    def __init__(self):
        self.price=75
        self.desc="Ideal for those who get respiratory paralysis upon contact with gluten."



# Decorator class and its inheritors

class Decorator:
    def get_description(self):
        return self.desc

    def get_cost(self):
        return self.price

class decOlive(Decorator):
    def __init__(self):
        self.price=3
        self.desc="Either hate it or love it. Fresh fermented olives."

class decMushroom(Decorator):
    def __init__(self):
        self.price=2
        self.desc="A healthy alternative protein source for vegans. Not magic though."

class decParmiggiani(Decorator):
    def __init__(self):
        self.price=5
        self.desc="Takes 2 years to make, but 2 minutes to flake. One might add 2 of it"

class decPepperoni(Decorator):
    def __init__(self):
        self.price=4
        self.desc="Don't forget to eat the ones that fell off the slice. Yummy."

class decOnion(Decorator):
    def __init__(self):
        self.price=2
        self.desc="No it won't give you bad breath, cuz we bake it to death."

class decCorn(Decorator):
    def __init__(self):
        self.price=2
        self.desc="Little nuggets of sweetness, definitely an indispensable"

class decBasil(Decorator):
    def __init__(self):
        self.price=5
        self.desc="Smells so good. Taste? Meh."

class decBrocco(Decorator):
    def __init__(self):
        self.price=2
        self.desc="Unpopular opinion: These taste great in pizza. For real."

class decNoThx(Decorator):
    def __init__(self):
        self.price=0
        self.desc="Nah I'm good."



# An auxillary class to get decorator and pizza classes's attributes together

class allTogether:
    def __init__(self, pizza, topping):
        self.pizza = pizza
        self.decor= topping

    def get_description(self):
        return self.pizza.get_description() + self.decor.get_description()

    def get_cost(self):
        return self.pizza.get_cost() + self.decor.get_cost()



if __name__ == "__main__":
    OrderMain()
    print("Thanks for choosing us. You will have a notification when your order is on delivery. Bonne apetit!")