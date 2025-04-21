def give_time(hour) :
    for i in range(1, 23) :
        if hour >= 12 :
            print(f"{hour - 12} : {i} PM")
        elif hour == 3 :
            print(f"{hour} : {i} midnight")
        elif 0 <= hour < 12 :
            print(f"{hour - 24} : {i} AM")
        else :
            print("Invalid Input")
hour = int(input("Enter the hour : "))
give_time(hour)