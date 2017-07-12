#defining variables

start = '''
you face two doors, only lit by their contents glowing beneath the crack.
you know this is a dream, but you can't shake the feeling that it's real.
do you go through the left door, with a constant steady beam of light, or through the right door, with light hues of color dancing softly?
'''

ending = '''
thanks for playing.
'''

D1 = '''
it's bright. you are overwhelmed by the heavy, toxic scent of disinfectant. it's clinical, like a doctors office.
will you keep going and walk on, or exit the room?
'''

D2 = '''
it's colorful. vibrant, blinding at first, but the lights fade into fluid bodies.
you can't be sure, the colors all look the same yet they contrast so severely.
so much is changing before you that you can't hear yourself think. you start going numb.
will you keep walking through, or exit the room?
'''

D3 = '''
the colors are infinite. you fall into pinks, roll into blues, stumble amongst oranges.
your heart inflates with hope and happiness and warmth but it's so close to bursting and breaking the spell.
will you keep going, or exit the room?
'''

D5 = '''
you're surrounded by numbers. you can't see them but you feel them.
all at once, you feel horrible inadequate. primative. naive. dumb.
you have entered the left brain.
'''


#game code

print(start)


print("Type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left":
    print(D1)
    print("type 'walk' to keep going. type 'retreat' to leave.")
    user_input = input()
    if user_input == "walk":
        print(D5)
        print(ending)
    elif user_input == "retreat":
        print(ending)
    else:
         print("type 'walk' or 'retreat'")

elif user_input == "right":
    print(D2)
    print("Type 'walk' to keep going, type 'exit' to leave.") # finished the story writing what happens
    user_input = input()
    if user_input == "walk":
        print(D2)
        print("type 'walk' to keep going. type 'exit' to leave.")
        user_input = input()
        if user_input == "walk":
            print(D3)
            print(ending)
        elif user_input == "exit":
            print("You wake up. You feel nothing.")
            print(ending)
    elif user_input == "exit":
        print("You wake up. You feel nothing.")
        print(ending)
