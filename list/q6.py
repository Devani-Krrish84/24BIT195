temprature = [10, -20, -289, 100]

def fahrenheit_to_celcius(temp) :
    celcius = []
    for i in temp :
        celcius.append((i - 32) * 5/9)
    return celcius

print(fahrenheit_to_celcius(temprature))