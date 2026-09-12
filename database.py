import sqlite3

db_file = "smart_pantry.db"

def init_database():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS recipes")
    cursor.execute("""
        CREATE TABLE recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key_name TEXT UNIQUE,
            dish_name TEXT,
            prep_time TEXT,
            instructions TEXT
        )
    """)
    conn.commit()
    conn.close()

def seed_recipes():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    mock_data = [
        ("rice_curd", "Curd Rice (Tadka Dahi Bhaat)", "10 mins", "Mash leftover rice. Mix in fresh whisked curd and salt. Heat oil in a pan, crackle mustard seeds, and sauté onions. Pour tempering over rice and serve cold."),
        ("potato_tomato", "Quick Aloo Tomato Sabzi", "15 mins", "Chop potatoes and tomatoes. Heat oil, add spices, and sauté onions. Cook tomatoes down into a paste. Add potato cubes and a splash of water, cover and simmer."),
        ("leftover_fry", "Resourceful Leftover Stir-Fry", "8 mins", "Chop available ingredients uniformly. Heat oil in a skillet and bloom available spices. Sauté everything on medium heat until fully cooked.")
    ]
    
    for row in mock_data:
        try:
            cursor.execute(
                "INSERT INTO recipes (key_name, dish_name, prep_time, instructions) VALUES (?, ?, ?, ?)",
                row
            )
        except sqlite3.IntegrityError:
            pass
            
    conn.commit()
    conn.close()

def query_recipe_by_ingredient(user_input):
    search = user_input.lower()
    
    if "rice" in search or "curd" in search:
        target_key = "rice_curd"
    elif "potato" in search or "tomato" in search:
        target_key = "potato_tomato"
    else:
        target_key = "leftover_fry"
        
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT dish_name, prep_time, instructions FROM recipes WHERE key_name = ?", 
        (target_key,)
    )
    result = cursor.fetchone()
    conn.close()
    
    if result:
        print("DATABASE MATCH FOUND:")
        print("Dish:", result[0])
        print("Time:", result[1])
        print("Steps:", result[2])
    else:
        print("No matching recipe in database.")

init_database()
seed_recipes()

test_pantry = "I have leftover rice, onions, and curd"
query_recipe_by_ingredient(test_pantry)
