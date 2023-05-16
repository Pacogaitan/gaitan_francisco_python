fruits = {"banana" : 1.35, "apple" : 0.8, "pear" : 0.85, "orange": 0.7}
fruitinput = input("What fruit do you want? ")
q = int(input("How many kilos do you need? "))
fruitinput = fruitinput.lower()
try:
    print(f'Total for {fruitinput}s will be $',fruits[fruitinput]*q)
except KeyError:
    print(f"We don't have that fruit")
'''
try:
for x in fruits:
    if x == fruitinput:
        print(x)
        print(f"Total would be $",fruits[fruitinput]*q)
except KeyError:
    #print("sorry")
    #print(f"Sorry we don't have" + fruitinput)
'''