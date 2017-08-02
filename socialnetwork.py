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
    def __newuser__(self, name,age):
            new_user=User(name)
            new_user.change_age(age)
            self.user.append(new_user)


def main():
    newnetwork = Network("new net")
    A = input("type A to create a new user")
    if A=="A":
        name = input("what is your name?")
        age = input("how old are you?")
        if int(age) > 18:
                self.adult = True
        friends = input("who do you work with now?")
        profile = name, age, friends
        print(profile)
    else:
        print("Ok thanks but that's not an A so goodbye.")


    # Define the program flow for your user interface here.

# Runs your program.
if __name__ == '__main__':
    main()
