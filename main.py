import re
from weatherAPI import fetch_weather
from gptapi import recomendation
from sql import save_to_fav, view_favs, authentication, create_new_user
"""
#Prompts:
    #1. Get Outfit Reccomendation:
        #Ask user for location, data is fetched and sent to Chatgpt api
        #Gives option to user to add outfit to favorites(stores in table/sql, asks for user's name & password)
            #If user's name, promt them to enter password and if it matches it will add favorite outfit. It no match, try again.
            #If user's name already exits, and if user doesn't know password, have user enter something else to prompt them to go back.
    #2. View Favorite Outfits:
        #shows table of favorite outifts with location(asks for users name & password and only outputs that users info)
        #Once user enters name, iterate through sql database to find user's name and if it matches up ask for password and then show info.

    #3. Exit
    """

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None


def login(current_user, email_address):
    print("Welcome to Weather Wear!")

    while True:
        print("1. Returning User")
        print("2. New User")
        print("3. Stop")
        choose = input("Choose one of the options above: ")

        if choose == '1':
            while True:
                email = input("Enter your email address: ")
                if is_valid_email(email):
                    username = input("Enter your name: ")
                    password = input("Enter your passowrd: ")
                    if authentication(email, username, password):
                        current_user = username
                        email_address = email
                        print(f"Welcome back, {current_user}!")
                        return current_user, email_address
                    else:
                        print("Invalid email, name or password. Please try again!")
                else:
                    print("Invalid email format. Please try again!")

        elif choose == '2':
            create = input("Would you like to create a new account? ( y / n )? ")
            if create.lower() == 'y':
                while True:
                    email = input("Enter your email address: ")
                    if is_valid_email(email):
                        username = input("Enter your name: ")
                        password = input("Enter your passowrd: ")
                        create_new_user(email, username,password)
                        current_user = username
                        email_address = email
                        print(f"Account created for {current_user}!")
                        return current_user, email_address
                    else:
                        print("Invalid email. Please try again!")
            else:
                break

        elif choose == '3':
            break

        else:
             print("Invalid. Please enter a valid option (1-3).")

    return current_user, email_address

def main():
    current_user = None
    email_address = None
    current_user, email_address  = login(current_user, email_address)

    while True:
        print("\nWeather-Based Outfit Recommender")
        print("1. Get Outfit Reccomendation")
        print("2. View Favorite Outfits")
        print("3. Exit ")
        choice = input("Choose one of the options above: ")

        if choice == '1':
            #enter location
            weather_data = fetch_weather(input("what city are you in? "))

            if weather_data :
                rec = recomendation(weather_data)
                print(rec)

                save = input("Would you like to save this outfit to your favorites? ( y / n ): ")
                if save.lower() == 'y':
                    save_to_fav(email_address, current_user, rec)
                    print("Outfit saved to favorites.")
                elif save.lower() == 'n':
                    continue 
                else: 
                    print ("Invalid input. Please try again ")

        elif choice == '2':
            favorite_outfits = view_favs(email_address)
            print("Here are your favorite outfits: ")
            if favorite_outfits:
                for i, j in enumerate(favorite_outfits, start=1):
                    outfit_recommendation = j[0]  # Extracting the recommendation string from the tuple
                    print(f"\nFavorite #{i}:")
                    print(outfit_recommendation)
                    print("-" * 40)
            else:
                print("No favorite outfits found.")

        elif choice == '3':
            print("Thank you for using Weather-Wear!")
            break
        else:
            print("Invalid. Please enter a valid option (1-3).")
        
        print() #print newline

if __name__ == "__main__":
    main()
