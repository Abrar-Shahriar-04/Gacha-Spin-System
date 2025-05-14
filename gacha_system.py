import random

# Define the rewards pool
common_rewards = [
  "Gun crate of AK47", "Gun crate of Scar", "Gun crate of Famas", "Gun crate of AWM",
  "Gun crate of MP40", "Gun crate of P90", "Gun crate of M1887", "Gun crate of M82B",
  "Gun crate of G18", "Gun crate of USP", "Gun crate of M4A1", "Gun crate of M14", "Gun crate of Groza", "Gun crate of XM8", "Gun crate of G36", "Gun crate of Plasma", "Gun crate of M24"
]

rare_rewards = [
  "✪ AWM permanent skin", "✪ PARAFAL permanent skin", "✪ M1887 permanent skin", "✪ Thompson permanent skin", "✪ AK47 permanent skin"
]

grand_prize = ["✹ ✹ ✹ ✹ ✹ Exclusive Samurai Bundle ✹ ✹ ✹ ✹ ✹"]

# Function to simulate a single spin
def spin():
    rand_num = random.randint(1, 100)

    if rand_num <= 90:
        # 90% chance for a common reward
        return random.choice(common_rewards)
    elif rand_num <= 99:
        # 9% chance for a rare reward
        return random.choice(rare_rewards)
    else:
        # 1% chance for the grand prize
        return random.choice(grand_prize)

# Function to ask user to top up diamonds when they run out
def prompt_topup(diamonds):
    print("\nYou have run out of diamonds!")
    topup = int(input("How many diamonds would you like to top up? "))
    diamonds += topup
    print(f"\nYou topped up {topup} diamonds. Your new balance is {diamonds} diamonds.")
    return diamonds

# Function to run the spin system
def spin_system():
    diamonds = 1000  # Starting diamonds
    print(f"Welcome to the Gacha Spin System! You have {diamonds} diamonds.")

    while True:
        # Ask user for spin type if they have diamonds
        if diamonds >= 20:
            choice = input(f"\nYou have {diamonds} diamonds left.\n"
                           "1. Spin 1 time (20 diamonds)\n"
                           "2. Spin 10 times (200 diamonds) + 1 extra spin free!\n"
                           "3. Top up diamonds\n"
                           "4. Exit\nChoose an option (1/2/3/4): ")

            if choice == "1":
                if diamonds >= 20:
                    diamonds -= 20
                    print("\nYou spun 1 time and got: " + spin())
                else:
                    print("\nNot enough diamonds for 1 spin.")

            elif choice == "2":
                if diamonds >= 200:
                    diamonds -= 200
                    print("\nYou spun 10 times and got:")
                    for i in range(11):  # 10 spins + 1 free
                        print(f"{i+1}. {spin()}")
                else:
                    print("\nNot enough diamonds for 10 spins.")

            elif choice == "3":
                topup = int(input("How many diamonds would you like to top up? "))
                diamonds += topup
                print(f"\nYou topped up {topup} diamonds. Your new balance is {diamonds} diamonds.")

            elif choice == "4":
                print("\nThanks for playing! See you next time!")
                break

            else:
                print("\nInvalid choice. Please choose again.")

        else:
            # If the player doesn't have enough diamonds
            diamonds = prompt_topup(diamonds)

# Run the spin system
if __name__ == "__main__":
  spin_system()
