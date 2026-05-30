import random
win = {
    "rock":"scissor",
    "paper":"rock",
    "scissor":"paper"
}
while True:
    re = random.choice(["rock","paper","scissor"])
    y = input("r p s which you want to choice?")
    print(f"You:{y} | Computer{re}")
    if y == re:
        print("Tie")
    elif win[y] == re:
        print("you win")
        break
    else:
        print("you lose")
        break