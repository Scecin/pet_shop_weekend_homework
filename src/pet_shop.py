# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, money):
    pet_shop["admin"]["total_cash"] = get_total_cash(pet_shop) + money

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, number):
    pet_shop["admin"]["pets_sold"] = get_pets_sold(pet_shop) + number

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, pet_breed):
    new_list_pets = []
    
    for pet in pet_shop["pets"]:
        if pet["breed"]== pet_breed:
            new_list_pets.append(pet)

    return new_list_pets
    
def find_pet_by_name(pet_shop, pet_name):
    found_dog = None
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            found_dog = pet
    return found_dog

def remove_pet_by_name(pet_shop, pet_name):
    found_dog = find_pet_by_name(pet_shop, pet_name)
    pet_shop["pets"].remove(found_dog)   

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] = get_customer_cash(customer) - cash

def get_customer_pet_count(customer):
    return len(customer["pets"])
    
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

#Optional
def customer_can_afford_pet(customer, new_pet):
    if get_customer_cash(customer) >= new_pet["price"]:
        return True
    else:
        return False

#'integration' tests
def  sell_pet_to_customer(pet_shop, pet, customer):
    #Check if customer have the money and if the pet exists
    if customer_can_afford_pet(customer, pet) and find_pet_by_name(pet_shop, pet["name"]):
        #Add new pet in customer pets information.
        add_pet_to_customer(customer, pet)
        #increase pet_shold.
        increase_pets_sold(pet_shop, 1)
        # #Substract pet price in customer cash.
        remove_customer_cash(customer, pet["price"])
        #Add pet price in pet_shop toltal_cash.
        add_or_remove_cash(pet_shop, pet["price"])
