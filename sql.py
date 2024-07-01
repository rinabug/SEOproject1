import sqlite3
#import pandas as pd
#import sqlalchemy as db
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
    cursor.execute("SELECT outfit FROM favorites WHERE email=?", (email,))
    favorite_outfits = cursor.fetchall()
    cursor.close()
    connection.close()
    return favorite_outfits


def create_new_user(email, name, password):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (email TEXT UNIQUE, name TEXT, password TEXT)")
    
    try: 
        cursor.execute("INSERT INTO users (email, name, password) VALUES (?, ?, ?)", (email, name.lower(), password)) 
        print(f"User '{name}' created successfully.")
        connection.commit()
        return True
    except sqlite3.IntegrityError: 
        print(f"User '{email}' already exists.")
        return False
    finally: 
        cursor.close()
        connection.close()


def authentication(email, name, password):
    email = email.strip()
    name = name.strip().lower()
    password = password.strip()

    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (email TEXT UNIQUE, name TEXT, password TEXT)")
    cursor.execute("SELECT email FROM users")
    
    cursor.execute("SELECT * FROM users WHERE email=? AND name=? AND password=?", (email, name, password)) 
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
