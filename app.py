recipes_db = {
    "rice_curd": {
        "name": "Curd Rice (Tadka Dahi Bhaat)",
        "time": "10 mins",
        "steps": [
            "Mash leftover cooked rice slightly in a bowl.",
            "Mix in fresh whisked curd (yogurt) with a pinch of salt.",
            "Heat oil in a small pan, crackle mustard seeds, and sauté onions.",
            "Pour the tempered onions/seeds over the rice mix and serve cold."
        ]
    },
    "potato_tomato": {
        "name": "Quick Aloo Tomato Sabzi",
        "time": "15 mins",
        "steps": [
            "Chop potatoes and tomatoes into small cubes.",
            "Heat oil in a pan, add tempering spices, and sauté onions.",
            "Cook tomatoes down until they soften into a thick paste.",
            "Add potato cubes, a splash of water, cover and simmer until soft."
        ]
    },
    "leftover_fry": {
        "name": "Resourceful Leftover Stir-Fry",
        "time": "8 mins",
        "steps": [
            "Chop whatever ingredients are available into uniform pieces.",
            "Heat oil in a skillet and bloom available spices.",
            "Sauté everything together on medium heat until fully cooked."
        ]
    }
}

def find_recipe(pantry_str):
    search_txt = pantry_str.lower()
    
    print("Checking pantry data...")
    print("Items:", pantry_str)
    print()
    
    if "rice" in search_txt or "curd" in search_txt:
        selected_key = "rice_curd"
    elif "potato" in search_txt or "tomato" in search_txt:
        selected_key = "potato_tomato"
    else:
        selected_key = "leftover_fry"
        
    recipe = recipes_db[selected_key]
    
    print("Dish:", recipe["name"])
    print("Time Required:", recipe["time"])
    print("\nInstructions:")
    
    count = 1
    for step in recipe["steps"]:
        print(f"{count}. {step}")
        count += 1

test_items = "Leftover rice, 2 onions, curd, and some mustard seeds"
find_recipe(test_items)
