from predictor import get_dog_recommendations

def get_input(prompt, min_val, max_val):
    while True:
        try:
            val = float(input(prompt))
            if min_val <= val <= max_val:
                return val
            print(f"Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def start_quiz():
    print("\n" + "="*40)
    print("      🐶 THE ULTIMATE DOG MATCHMAKER 🐶")
    print("="*40)
    print("Answer the following questions to find your perfect breed!\n")

    # --- GENERAL TRAITS (Questions 1-11) ---
    f = get_input("1. How friendly should the dog be? (1: Very Reserved - 10: Social Butterfly): ", 1, 10)
    l = get_input("2. Expected lifespan in years? (e.g., 5 to 15): ", 5, 15)
    s = get_input("3. General size preference? (1 :'Toy', 7: 'Giant'): ", 1, 7)
    g = get_input("4. How much time can you spend on grooming? (1: Low - 4: High): ", 1,4)
    e = get_input("5. Daily exercise you can provide? (Hours per day): ", 0, 5)
    c = get_input("6. How important is it that they are good with children? (0-4): ", 0, 4)
    i = get_input("7. Desired intelligence level? (1: Smart - 10: Einsetien): ", 1, 10)
    sh =get_input("8. Tolerance for shedding? (1: No hair - 4: Thick hair): ", 1, 4)
    h = get_input("9. Tolerance for health issue risk? (1: Low risk - 3: I don't mind): ", 1, 3)
    w = get_input("10. Preferred weight of the dog in kg? (e.g., 1 to 80): ", 1, 80)
    dt = get_input("11. How much patience do you have for training? (1: Expert only - 10: Very Easy): ", 1, 10)

    # --- DOG GROUP (Question 12-15 bundled) ---
    print("\n12. Which 'vibe' or category of dog do you prefer?")
    groups = ["Herding", "Hound", "Non-Sporting", "Sporting", "Standard", "Terrier", "Toy", "Working"]
    for idx, name in enumerate(groups, 1):
        print(f"{idx}: {name}")
    
    group_choice = int(get_input("Choice (1-8): ", 1, 8))
    
    # Initialize all group variables to 0
    herd = houn = NS = S = stand = terr = toy = work = 0
    
    # Set the selected group to 1
    if group_choice == 1: herd = 1
    elif group_choice == 2: houn = 1
    elif group_choice == 3: NS = 1
    elif group_choice == 4: S = 1
    elif group_choice == 5: stand = 1
    elif group_choice == 6: terr = 1
    elif group_choice == 7: toy = 1
    elif group_choice == 8: work = 1

    # --- EXECUTE PREDICTION ---
    print("\nCalculating your matches...")
    
    top_dogs = get_dog_recommendations(f, l, s, g, e, c, i, sh, h, w, dt, 
                                       herd, houn, NS, S, stand, terr, toy, work)

    print("\n" + "⭐" * 40)
    print("         YOUR TOP 3 DOG MATCHES")
    print(" " + "⭐" * 40)
    for rank, name in enumerate(top_dogs, 1):
        print(f"  {rank}. {name.upper()}")
    print("="*40 + "\n")

if __name__ == "__main__":
    start_quiz()