import sqlite3
import pandas as pd
import sqlalchemy as db
connection = sqlite3.connect('users.db')
connection = sqlite3.connect('favorites.db')
cursor = connection.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS users (email TEXT UNIQUE, name TEXT, password TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS favorites (email TEXT, name TEXT, outfit TEXT)")

def save_to_fav(email, name, outfit_data):
    connection = sqlite3.connect('favorites.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS favorites (email TEXT, name TEXT, outfit TEXT)")
    
    cursor.execute("INSERT INTO favorites (email, name, outfit) VALUES (?, ?, ?)", (email, name, outfit_data))
    
    connection.commit()
    cursor.close()
    connection.close()


def view_favs(email):
    connection = sqlite3.connect('favorites.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS favorites (email TEXT, name TEXT, outfit TEXT)")
    cursor.execute("SELECT * FROM favorites WHERE email=?", (email,))
    favorite_outfits = cursor.fetchall()
    if favorite_outfits:
        print("Here are your favorite outfits: ")
        for row in favorite_outfits:
            print(row)
    else: 
        print("No outfits added to favorites")


    cursor.close()
    connection.close()


def create_new_user(email, name, password):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (email TEXT UNIQUE, name TEXT, password TEXT)")
    
    try: 
        cursor.execute("INSERT INTO users (email, name, password) VALUES (?, ?, ?)", (email, name, password)) 
        print(f"User '{name}' created successfully.")
        connection.commit()
        return True
    except sqlite3.IntegrityError: 
        print(f"User '{email}' already exists.")
        return False
    finally: 
        cursor.close()
        connection.close()


def authentication(email, password):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (email TEXT UNIQUE, name TEXT, password TEXT)")
    cursor.execute("SELECT email FROM users")
    
    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password)) 
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    if user: 
        print("Authenticated successfully")
        return True
    else: 
        print("Authentication failed")
        return False



#if __name__ == "__main__":
#   print(create_new_user("anna@gmail.com", "anna", "hello"))
#   print(authentication("anna@gmail.com", "hello"))
#   print(save_to_fav("anna@gmail.com", "anna", "shirt"))
#   print(view_favs("anna@gmail.com"))