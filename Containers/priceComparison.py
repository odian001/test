import mariadb
import sys


def get_ingredient_prices(cur, id):
	query = f"SELECT StoreID, CurrentPrice FROM PriceData WHERE IngredientID={id}"
	cur.execute(query)
	return cur.fetchall()
	
def get_best_store_price(cur, ingredients):
	stores = {}
	for ing_id in ingredients:
		price_info = get_ingredient_prices(cur, ing_id)
		for store_id, price in price_info:
			if not store_id in stores:
				stores[store_id] = 0.0
			stores[store_id] += price
	
	best_store = -1
	best_price = 1000000000.0 # Arbitrary large value
	for store_id in stores:
		price = stores[store_id]
		cur.execute(f"SELECT StoreName FROM GroceryStore WHERE StoreID={store_id}")
		store_name = cur.fetchone()[0]
		print(f"Store: {store_name} (${price})")
		if price < best_price:
			best_store = store_id
			best_price = price
	
	return (best_store, best_price)

def get_best_mix(cur, ingredients):
	stores = {}
	for ing_id in ingredients:
		price_info = get_ingredient_prices(cur, ing_id)
		best_store = -1
		best_price = 1000000000.0 # Arbitrary large value
		for store_id, price in price_info:
			if not store_id in stores:
				stores[store_id] = []
			if price < best_price:
				best_store = store_id
				best_price = price
		
		stores[best_store] += [ing_id]
	
	return stores

# Set up database connection
try:
    conn = mariadb.connect(
        user="root",
        password="Quackblack75!",
        host="localhost",
        port=3306,
        database="DoughSaverDB"
    )
except mariadb.Error as e:
	print(f"Error connecting to MariaDB Platform: {e}")
	sys.exit(1)

cur = conn.cursor()
print("Connection successful\n")

# First, find the best single store to shop at
print("Finding best store for the following recipe:")
recipe = [1, 2, 3, 4, 5] # Placeholder for user data
for ing_id in recipe:
	cur.execute(f"SELECT IngredientName FROM Ingredient WHERE IngredientID={ing_id}")
	print(cur.fetchone()[0])
	
print("")

best_deal = get_best_store_price(cur, recipe)
best_store = best_deal[0]
best_price = best_deal[1]
cur.execute(f"SELECT StoreName FROM GroceryStore WHERE StoreID={best_store}")
store_name = cur.fetchone()[0]

print(f"\nBest store: {store_name} (${best_price})")

# Next, find the best mix of stores
print("\nFinding best mix...\n")
best_mix = get_best_mix(cur, recipe)
best_mix_price = 0.0
for store_id in best_mix:
	ingredients = best_mix[store_id]
	if not ingredients:
		continue
	cur.execute(f"SELECT StoreName FROM GroceryStore WHERE StoreID={store_id}")
	store_name = cur.fetchone()[0]
	print(store_name)
	for id in ingredients:
		cur.execute(f"SELECT IngredientName FROM Ingredient WHERE IngredientID={id}")
		ing_name = cur.fetchone()[0]
		print(f"--{ing_name}")
		cur.execute(f"SELECT CurrentPrice FROM PriceData WHERE StoreID={store_id} AND IngredientID={id}")
		best_mix_price += cur.fetchone()[0]

print(f"Best mix price: ${best_mix_price}")
conn.close();