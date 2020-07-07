age = input("Are you a cigarette addict older than 75 years old? ").lower()
age_bool = age == "yes"

chronic = input("Do you have a severe chronic disease? ").lower()
chronic_bool = chronic == "yes"

immune = input("Is your immune system too weak? ").lower()
immune_bool = immune == "yes"

if (age != "yes" and age != "no") or (chronic != "yes" and chronic != "no") or (immune != "yes" and immune != "no"):

    print("Please enter only 'yes or no'")

elif age_bool or chronic_bool or immune_bool:

    print("You are in risky group")

else:

    print("You are not in risky group")
