# Define three functions fun(), disp() and msg(). Store them in a list and call them one by one in a loop

def fun() :
    print("This is fun() function")

def disp() :
    print("This is disp() function")

def msg() :
    print("This is msg() function")

list = [fun, disp, msg]

for function in list :
    function()