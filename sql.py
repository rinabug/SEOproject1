import sqlite3
import pandas as pd
import sqlalchemy as db
connection = sqlite3.connect('users.db')
connection = sqlite3.connect('favorites.db')
cursor = connection.cursor()

# Connect to SQLite database (will create if not exists)
#connection = sqlite3.connect('favorites.db')
#cursor = connection.cursor()

# Execute a query
#cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")

# Insert data
#cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('Alice', 30))
#cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('Bob', 25))

cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT UNIQUE, password TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS favorites (username TEXT, outfit TEXT)")

def save_to_fav(username, outfit_data):
    connection = sqlite3.connect('favorites.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS favorites (username TEXT, outfit TEXT)")
    
    cursor.execute("INSERT INTO favorites (username, outfit) VALUES (?, ?)", (username, outfit_data))

    connection.commit()
    cursor.close()
    connection.close()


def view_favs(username):
    connection = sqlite3.connect('favorites.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS favorites (username TEXT, outfit TEXT)")
    cursor.execute("SELECT * FROM favorites WHERE username=?", (username,))
    favorite_outfits = cursor.fetchall()
    if favorite_outfits:
        print("Here are your favorite outfits: ")
        for row in favorite_outfits:
            print(row)
    else: 
        print("No outfits added to favorites")


    cursor.close()
    connection.close()


def create_new_user(username, password):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT UNIQUE, password TEXT)")
    
    try: 
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password)) 
        print(f"User '{username}' created successfully.")
        return True
    except sqlite3.IntegrityError: 
        print(f"User '{username}' already exists.")
        return False
    
    connection.commit()
    cursor.close()
    connection.close()


def authentication(username, password):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT UNIQUE, password TEXT)")
    cursor.execute("SELECT username FROM users")
    
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password)) 
    user = cursor.fetchone()

    if user: 
        print("Authenticated successfully")
        return True
    else: 
        print("Authentication failed")
        return False
    
    cursor.close()
    connection.close()



#if __name__ == "__main__":
"""create_new_user("anna", "hello")
authentication("anna", "hello")
save_to_fav("anna", "shirt")
view_favs("anna")"""




# Commit changes and close
"""connection.commit()
cursor.close()
connection.close()"""







"""# Select data
cursor.execute("SELECT username FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

print()"""

"""CREATE DATABASE IF NOT EXISTS favorites_collection;

CREATE TABLE user_info ( 
    username VARCHAR(255) default NULL,
    password VARCHAR(255) default NULL,
) AUTO_INCREMENT=1;*/

CREATE DATABASE IF NOT EXISTS guitars_collection;

CREATE TABLE catalog ( 
    id INT(8) UNSIGNED NOT NULL auto_increment,
    name VARCHAR(255) default NULL,
    manufacture_year YEAR(4) default NULL,
    brand VARCHAR(255) default NULL,
    PRIMARY KEY (id)
) AUTO_INCREMENT=1;"""