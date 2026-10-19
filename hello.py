from datetime import date

name = input("What's your name? ")
days_left = (date(2029, 6, 3) - date.today()).days

print(f"Hi {name}, Welcome to Day 1.")
print(f"{days_left} days left until graduation. Let's build.")
