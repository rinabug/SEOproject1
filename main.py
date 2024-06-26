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
                save = input("would you like to save this outfit to your favorites? ( y / n ): ")
                if save == 'y':
                    username = input("Enter your username: ")
                    password = input("Enter your passowrd: ")
                    if authentication(username, password) == True:
                        save_to_fav(username, rec)
                    elif authentication(username, password) == False: 
                        create = input("Username or password is incorrect. Would you like to create a new account? ( y / n )? ")
                        if create == 'y':
                            username = input("Enter your username: ")
                            password = input("Enter your passowrd: ")
                            new_user = create_new_user(username, password) 

                            if  new_user == True: 
                                print("Saved to favorites")
                                create_new_user(username, password)
                                save_to_fav(username, rec)
                            elif  new_user == False: 
                                username = input("Create new username: ")
                                password = input("Create new passowrd: ")
                                create_new_user(username, password)
                                save_to_fav(username, rec)
                                print("Account created successfullt and outfit saved to favorites")
                            else: 
                                continue
                            
                        elif create == 'n': 
                            continue
                        else : 
                            print("Invalid please try again")
                    else:
                        print("Failed to save outfit please try again")
                elif save == 'n':
                    continue 
                else: 
                    print ("invalid username, try again: ")

        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your passowrd: ")
            check = authentication(username, password)
            if  check == True:
                view_favs(username)
            elif check == False: 
                print("Username not found, get outfit recomendation and create a new account.")
            else: 
                print("viewing outfit failed, please try again")
        elif choice == '3':
            print("Thank you for using Weather-Based Outfit Recommender")
            break
        else:
            print("Invalid. Please try again!")

main()