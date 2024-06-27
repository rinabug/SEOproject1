import re
from weatherAPI import fetch_weather
from gptapi import recomendation
from sql import save_to_fav, view_favs, authentication, create_new_user
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
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

def main():
    while True:
        print("Weather-Based Outfit Recommender")
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
                    while True:
                        email = input("Enter your email address: ")
                        if is_valid_email(email):
                            break
                        else:
                            if email == '':
                                break
                            else:
                                print("Invalid email. Please try again!")
                    username = input("Enter your name: ")
                    password = input("Enter your passowrd: ")
                    if authentication(email, password):
                        save_to_fav(email, username, rec)
                        print("Outfit saved to favorites.")
                    else: 
                        create = input("User not found! Would you like to create a new account? ( y / n )? ")
                        if create.lower() == 'y':
                            while True:
                                email = input("Enter your email address: ")
                                if is_valid_email(email):
                                    break
                                else:
                                    print("Invalid email. Please try again!")
                            username = input("Enter your username: ")
                            password = input("Enter your passowrd: ")
                            if create_new_user(email, username, password): 
                                save_to_fav(email, username, rec)
                                print("Account created successfully and outfit saved to favorites.")
                            else: 
                                print("Failed to create new account. Please try again!")
                        elif create == 'n': 
                            continue
                        else : 
                            print("Returning to main menu")
                elif save.lower() == 'n':
                    continue 
                else: 
                    print ("Invalid input. Please try again ")

        elif choice == '2':
            while True:
                email = input("Enter your email address: ")
                if is_valid_email(email):
                    break
                else:
                    if email == '':
                        break
                    else:
                        print("Invalid email. Please try again!")

            password = input("Enter your passowrd: ")

            if authentication(email, password):
                view_favs(email)
            else: 
                print("User not found. Get outfit recomendation and Create a new account.")

        elif choice == '3':
            print("Thank you for using Weather-Based Outfit Recommender")
            break
        else:
            print("Invalid. Please enter a valid option (1-3).")
        
        print() #print newline

if __name__ == "__main__":
    main()