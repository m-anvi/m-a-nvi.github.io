new_dict = dict()
new_dict = {}
#print(new_dict)

ingredients1 = {"strawberry ice cream" : "0.5 gallons" , "fine graham cracker crumbs":"1.5 cups" ,
"melted butter":"6 tablespoons", "sugar":"0.25 cups + 2 tablespoons", "storebought cheesecake":"1",
"strawberries":"1 pint", "lemon":"0.5 juiced"}

instructions = ["1. set ice cream out for 30 minutes to melt meanwhile mix together graham crumbs, butter, and suger then press the mixture into the botttom of the pan",
"1. cut the strawberries into smaller pieces and put them into the pan", "3. Break the cheescakes into chunks then put them inside the pan",
"4. pour in the melted strawberry ice cream into the pan","5. pour in the lemon juice and mix everything together",
"6. proceed to put the pan into the freezer for 1 hour or until it hardens"]



for steps in instructions:
    print(steps)

start = input("do you want the recipe or do you want the ingredients?")

if start=="recipe"

print("do you need a reminder?")
choice = input("answer yes or no:")
if choice=="yes":
    step = input("what step do you need?")
    print(instructions[int(step)])
    quantity = input("what ingredient are you on?")
    print(ingredients1[quantity])
