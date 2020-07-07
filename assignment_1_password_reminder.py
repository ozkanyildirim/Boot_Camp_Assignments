my_name = "Ozkan"

users_name = input("Your name please: ").title()

if users_name == my_name:

    print(f"Hallo {users_name}! The password is: claruswayE2167")

elif (i in list(users_name) for i in ["ö", "ü", "ı", "ş", "ğ", "ç"]):

    print(f"Hallo {users_name}! Avoid using characters except [A-Z] [a-z]")

else:

    print(f"Hallo {users_name}! See you later.")
