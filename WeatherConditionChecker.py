## Assignment 1 - Part One
## Weather Condition Checker

## Your Code goes here. 
weather = input("How is the weather currently").lower()

#weather reccomendations/conditions
if weather == "sunny":
    print("It's sunny. Enjoy the sunshine!")
elif weather == "cloudy":
    print("It's cloudy. It might stay dry, but be prepared for changes.")
elif weather == "rainy":
    print("It's rainy. You might want to carry an umbrella with you.")
elif weather == "snowy": 
    print("It's snowy. Be cautious while driving and dress warmly.")
#if it isnt a weather function within 
else: 
    print("I'm sorry, I don't have a specific recommendation")