grocery_prices = {
    "Apples": 3.5,
    "Bananas": 1.2,
    "Milk": 2.5,
    "Bread": 2.0,
    "Eggs": 4.0
}

grocery_quantities = {
    "Apples": 2,
    "Bananas": 6,
    "Milk": 1,
    "Bread": 1,
    "Eggs": 12
}

def compute_total_cost(prices, quantities) :
    t_cost = 0

    for item in prices.keys() :
        if item in quantities.keys() :
            t_cost += prices[item] * quantities[item]
    
    return t_cost

print(compute_total_cost(grocery_prices, grocery_quantities))