# menu = {"popcorn":20,
#         "apple":10,
#         "banana":10,
#         "toffee":5}

# cart =[]
# total =0

# print("-----Our Menu-----")
# for item, price in menu.items():
#     print(f"{item:10}: ${price:.2f}")

# print("----------------")

# while True:
#     food = input("Select an item (q to quit): ").lower()
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)

# for food in cart:
#     total += menu.get(food)
#     print(food , end=" ")

# print()
# print(f"Your total is: {total:.2f}")

#Random number guess

# import random

# low =1
# high = 100
# num = random.randint(1,100)

# while True:
#     guess = input("Enter the guess number (999 to quit): ")
#     if guess == 999:
#         break
#     elif guess == num:
#         print("🤑")
#     else:
#         print("🥹")

grades = [45,80,96,72,49,60,52]

grades = [grade for grade in grades if grade>=60]
print(grades)
    