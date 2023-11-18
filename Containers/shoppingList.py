import mysql.connector

db_config = {
    "host": "localhost",  
    "user": "root",
    "password": "1qaz!QAZ",
    "database": "DoughSaverDB",
}

def display_ingredients(cursor):
    try:
        # Execute a query to retrieve all ingredients
        query = "SELECT * FROM Ingredient"
        cursor.execute(query)

        # Fetch all rows
        IngredientName = cursor.fetchall()

        # Display the list of ingredients
        print("\nAvailable Ingredients:")
        for Ingredient in IngredientName:
            print(f"{Ingredient[0]}. {Ingredient[1]}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def create_shopping_list(cursor, selected_IngredientID):
    try:
        # Fetch the details of selected ingredients
        selected_ingredients = []
        for ingredient_id in selected_IngredientID:
            query = f"SELECT * FROM Ingredient WHERE IngredientID = {ingredient_id}"
            cursor.execute(query)
            ingredient = cursor.fetchone()
            selected_ingredients.append(ingredient)

        # Display the shopping list
        print("\nShopping List:")
        for ingredient in selected_ingredients:
            print(f"{ingredient[1]}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    try:
        # Establish a database connection
        connection = mysql.connector.connect(**db_config)

        # Check if the connection was successful
        if connection.is_connected():
            print("Successfully connected to the database!")

            # Create a cursor to execute SQL queries
            cursor = connection.cursor()

            # Display available ingredients
            display_ingredients(cursor)

            # Simulate user selecting ingredient IDs
            selected_ingredient_ids = [1, 3, 6]

            # Create and display the shopping list
            create_shopping_list(cursor, selected_ingredient_ids)

    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")

    finally:
        # Close the cursor and connection when done
        if 'connection' in locals():
            cursor.close()
            connection.close()
            print("Connection closed.")
