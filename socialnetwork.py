class User:
    # Define the fields and methods for your object here.
    def __init__(self, name):
            self.name = name
            self.age = 0
            self.adult = False
            self.friends = []
    def add_friends(self, friend):
            self.friends.append(friend)
    def change_age(self, age):
            self.age = age
            if int(self.age)>18:
                self.adult = True

class Network:
    def __init__(self, community):
            self.name = community
            self.users = []
    def newuser(self, name,age):
            new_user=User(name)
            new_user.change_age(age)
            self.users.append(new_user)


def main():
    while 3>1:   #no significance, I just needed a forever loop
        newnetwork = Network("new net")
        A = input("type A to create a new user, or B to see current users")
        if A=="A":
            name = input("what is your name?")
            age = input("how old are you?")
            newnetwork.newuser(name, age)
            friends = input("who do you works with now?")
            profile = name, age, friends
        elif A=="B":
            print(newnetwork.users)
        elif A=="exit":
            break
        else:
            print("Ok thanks but that's not an option. Please try again. ")


    # Define the program flow for your user interface here.

# Runs your program.
if __name__ == '__main__':
    main()
