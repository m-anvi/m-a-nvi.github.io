import random

rnumber = [random.randint(10, 99) for x in range (100)]

mult_five = []
mult_three = []
for number in rnumber:
    if number%5==0:
        mult_five.append(number)
    elif number%3==0:
        mult_three.append(number)
print(mult_five)
print(mult_three)

print(sum(mult_five+mult_three))



############################################################
#level three
prime_numbers = []

for number in rnumber:

for number in range(2, (rnumber-1)):
    if rnumber%number == 0
