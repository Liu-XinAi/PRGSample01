def calculate_cookie_score(ingredients):
    score = 0
    for item in ingredients:
        item = item.lower().strip()
        if item == "sugar":
            score += 5
        elif item == "butter":
            score += 4
        elif item == "chocolate chips":
            score += 3
        elif item == "flour":
            score -= 2
        else:
            score += 1
    return score

def process_cookie_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    for line in lines:
        if "," in line:
            parts = line.strip().split(",")
            name = parts[0].strip()
            ingredients = [item.strip() for item in parts[1:]]
            score = calculate_cookie_score(ingredients)

            print(f"Cookie: {name}")
            print(f"Score: {score}")

            if score < 5:
                print("This cookie is a disaster!")
            elif 5 <= score <= 14:
                print("This cookie is mediocore, but we're not judging.")
            else:
                print("This cookie deserves a gold medal.")

while True:
    answer = input("Would you like to score some cookies? (Type 'Stop' to quit, 'Yes' to start): ")

    if answer.lower() == "stop":
        print("Goodbye!")
        break
    elif answer.lower() == "yes":
        process_cookie_file("ingredients.txt")
    else:
        print("Invalid input. Please type 'Yes' or 'Stop'.")