import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "1qaz!QAZ",
    "database": "DoughSaverDB",
}

def display_ingredients(cursor):
    try:
        query = "SELECT * FROM Ingredient"
        cursor.execute(query)
        ingredients = cursor.fetchall()

        print("\nAvailable Ingredients with Prices:")
        for ingredient in ingredients:
            print(f"{ingredient[0]}. {ingredient[1]} - Prices:")
            prices = get_ingredient_prices(cursor, ingredient[0])
            if prices:
                for price in prices:
                    print(f"   Store ID: {price[0]}, Price: ${price[1]}")
            else:
                print("   No prices available.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def get_ingredient_prices(cur, id):
    query = f"SELECT StoreID, CurrentPrice FROM PriceData WHERE IngredientID={id}"
    cur.execute(query)
    return cur.fetchall()



def track_ingredients(cursor, selected_ingredient_ids, savings_percentage):
    try:
        total_amount = 0
        tracked_items = []

        for ingredient_id in selected_ingredient_ids:
            query = f"SELECT * FROM Ingredient WHERE IngredientID = {ingredient_id}"
            cursor.execute(query)
            ingredient = cursor.fetchone()

            if ingredient is not None:
                prices = get_ingredient_prices(cursor, ingredient_id)
                if prices:
                    tracked_items.append((ingredient[1], prices[0][1]))  # Store tracked items and prices
                else:
                    print(f"Prices for Ingredient with ID {ingredient_id} not found.")
            else:
                print(f"Ingredient with ID {ingredient_id} not found.")

        print("\nTracked Items with Prices:")
        for item, price in tracked_items:
            print(f"{item} - Price: ${price}")

        for _, price in tracked_items:
            total_amount += price  # Sum up prices for each tracked item

        if total_amount >= savings_percentage:
            print(f"\nTotal amount reached {savings_percentage}% savings: ${total_amount}. You've reached your goal!")
        else:
            print(f"\nTotal amount is ${total_amount}. You need ${savings_percentage - total_amount} more to reach {savings_percentage}% savings.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    try:
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            print("Successfully connected to the database!")
            cursor = connection.cursor()

            selected_ingredient_ids = [1, 3, 6]
            user_savings_percentage = 20

            track_ingredients(cursor, selected_ingredient_ids, user_savings_percentage)

    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")

    finally:
        if 'connection' in locals():
            cursor.close()
            connection.close()
            print("Connection closed.")
