# Smart Pantry AI Assistant

This project is a localized domestic workflow utility designed to handle kitchen inventory limitations and optimize daily meal planning. It helps reduce household food waste by matching available pantry ingredients to structured recipes.

## Project Structure

* **app.py**: Core Python routing engine that runs a lookup search on user-inputted ingredient strings using an internal dictionary database.
* **database.py**: Relational storage engine built with SQLite3 that manages persistent data schemas, sets up tables, seeds records, and handles secure query flows.

## Core Workflows

1. **Inventory Management**: Saves recipes, prep timelines, and cooking instructions cleanly inside database tables.
2. **Dynamic Querying**: Employs parameterized SQL lookup filters to search for recipes based on string matching of ingredients.
3. **Data Display**: Prints data points cleanly in structured column formats for easy terminal debugging.

## How to Run

1. Clone the project folder.
2. Run the setup command in your workspace terminal:
   python database.py
3. To execute the lookup search logic, run:
   python app.py
