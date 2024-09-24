import random

strength = 100
level = 1
while True:
    e = "🦍", "🔥", "🦧", "⚔"
    print("🦍\n💪Strength:", strength, "⚡️\n🩸Level:", level, "❤️")
    attack = input("Write (attack): ")
    bot = "win", "lose"
    if attack == "attack":
        bot = random.choice(bot)
        if bot == "win":
            print(e[0], e[3], e[2])
            print("You win", e[1])
            strength += 100
            level += 1
        else:
            print(e[0], e[3], e[2])
            print("You lose\nTry again")
    else:
        print("You stopped the game")
        break
