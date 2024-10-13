import random
import game_data
import art


def compare(value1, value2):
    if value1 > value2:
        return "option1_followers"
    elif value2 > value1:
        return "option2_followers"
    elif value2 == value1:
        return 0


print(art.logo)
game_over = False
score = 0
option1 = random.choice(game_data.data)
option2 = random.choice(game_data.data)

while not game_over:
    option1_followers = option1["follower_count"]
    option2_followers = option2["follower_count"]
    more_followers = compare(option1_followers, option2_followers)
    print(f"A: {option1["name"], option1["description"], option1["country"]}")
    print(art.vs)
    print(f"B: {option2["name"], option2["description"], option2["country"]}")
    user_choice = input("Who has more follower? A or B\n").lower()

    if user_choice == "a" and more_followers == "option1_followers":
        print("You are right!")
        score += 1
        print(score)
        option1 = option1
        option2 = random.choice(game_data.data)

    elif user_choice == "b" and more_followers == "option2_followers":
        print("You are right!")
        score += 1
        print(score)
        option1 = option2
        option2 = random.choice(game_data.data)

    elif (user_choice == "a" and more_followers == "option2_followers") or (
            user_choice == "b" and more_followers == "option1_followers"):
        print("You are wrong!")
        game_over = True
    elif more_followers == 0:
        print("Opps both have same no. of followers, error its on us !")

print(f"Your final score: {score}")
print(option1)
print(option2)