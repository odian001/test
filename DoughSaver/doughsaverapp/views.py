from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from .forms import StoreSelectionForm
from django.utils.safestring import mark_safe 
from django.contrib import messages
from doughsaverapp.models import *
from django.urls import reverse
from django.db import connection
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
from django.conf import settings
from django.contrib.auth.decorators import login_required


def get_ingredient_prices(ing_id, store_id):
    price_data = PriceData.objects.get(IngredientID_id=ing_id, StoreID=store_id)
    price = price_data.CurrentPrice

    return (price)
    
def get_best_store(shopping_list):
    best_store=None
    best_price=None
    stores = GroceryStore.objects.filter(StoreId__range=(1, 5))
    for store in stores:
        store_price=0.00
        for ing in shopping_list:
            store_price += get_ingredient_prices(ing.Ingredient_id, store.StoreId)
        if best_store == None:
            best_store = store
            best_price = store_price
        elif store_price < best_price:
            best_store = store
            best_price = store_price
    
    return (best_store)




@login_required
def target_price_ingredient(request):
    if request.method == 'POST':
        user_id = request.user.id
        ingredient_id = request.POST.get('ingredient_id')
        target_price = request.POST.get('target_price')
        
        ingredient_collection = IngredientCollection.objects.get(UserID=user_id, IngredientID=ingredient_id)
        ingredient_collection.TargetPrice = target_price
        ingredient_collection.save()

        return redirect('user_ingredients')

    # Handle GET request or other cases
    return render(request, 'user_ingredients.html')
    
def target_price_recipe(request):
    if request.method == 'POST':
        user_id = request.user.id
        recipe_id = request.POST.get('recipe_id')
        target_price = request.POST.get('target_price')
        
        recipe_collection = RecipeCollection.objects.get(UserID=user_id, RecipeID=recipe_id)
        recipe_collection.TargetPrice = target_price
        recipe_collection.save()

        return redirect('user_recipes')

    # Handle GET request or other cases
    return render(request, 'user_recipes.html')
    

def user_ingredients(request):
    date_user = AuthUser.objects.get(id=request.user.id)
    if request.method == 'POST':
        selecteddate = request.POST.get('selecteddate')
        if selecteddate:
            date_user.selecteddate = selecteddate
            date_user.save()
            return redirect(request.path) 
    # Retrieve the currently logged-in user and their selected date
    user = request.user
    selected_date = date_user.selecteddate
    
    # Retrieve the ingredients associated with the user
    ingredient_collections = IngredientCollection.objects.filter(UserID=user.id)
    user_ingredients = Ingredient.objects.filter(ingredientcollection__UserID=user.id)
    
    below_price = IngredientCollection.objects.none()
    
    for item in ingredient_collections:
        best_price = get_best_price(selected_date, item.IngredientID_id)
        if best_price is not None and best_price < item.TargetPrice:
            below_price |= IngredientCollection.objects.filter(DjangoID=item.DjangoID)
    # Pass the data to the template
    return render(request, 'user_ingredients.html', {'user_ingredients': user_ingredients, 'ingredient_collections': ingredient_collections, 'below_price': below_price, 'date_user': date_user})
    
def get_best_price(date, ingredient_id):
    best_price = None
    stores = GroceryStore.objects.all()

    for store in stores:
        price_history = PriceHistory.objects.filter(
            IngredientID=ingredient_id,
            StoreID=store.StoreId,
            UpdateTimestamp__lt=date
        ).order_by('-UpdateTimestamp')[:1]

        if price_history:
            if best_price is None:
                best_price = price_history[0].HistoricalPrice
            elif price_history[0].HistoricalPrice < best_price:
                best_price = price_history[0].HistoricalPrice
    return best_price
    
@login_required
def user_recipes(request):
    # Retrieve the currently logged-in user
    user = request.user

    # Retrieve the ingredients associated with the user
    recipe_collections = RecipeCollection.objects.filter(UserID=user.id)   
    user_recipes = Recipe.objects.filter(recipecollection__UserID=user.id).values('RecipeID', 'RecipeName').distinct()


    # Pass the data to the template
    return render(request, 'user_recipes.html', {'user_recipes': user_recipes, 'recipe_collections': recipe_collections})


def get_price_history(ingredient_id):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT StoreID, UpdateTimestamp, HistoricalPrice
            FROM PriceHistory
            WHERE IngredientID = %s
              AND UpdateTimestamp BETWEEN '2022-11-01' AND '2024-01-01'
            ORDER BY UpdateTimestamp;
            """,
            [ingredient_id]
        )
        rows = cursor.fetchall()
    return rows

def plot_price_history(ingredient_name, price_history, plot_save_path):
    # Create a dictionary to store data for each store
    store_data = {}

    for row in price_history:
        store_id, timestamp, price = row

        # Convert timestamps to datetime objects
        timestamp = pd.to_datetime(timestamp)

        # If the store_id is not in the dictionary, create a new entry
        if store_id not in store_data:
            store_data[store_id] = {'timestamps': [], 'prices': [], 'label': f'Store {store_id}'}

        # Append data to the corresponding store entry
        store_data[store_id]['timestamps'].append(timestamp)
        store_data[store_id]['prices'].append(price)

    # Retrieve store names from the database
    store_names = {store.StoreId: store.StoreName for store in GroceryStore.objects.all()}

    # Create the plot
    fig, ax = plt.subplots(figsize=(14, 8))

    for store_id, data in store_data.items():
        # Use store names in the legend
        store_name = store_names.get(store_id, f'Store {store_id}')

        # Combine timestamps and prices into a DataFrame
        df = pd.DataFrame({'timestamps': data['timestamps'], 'prices': data['prices']})
        df.set_index('timestamps', inplace=True)

        # Resample data to fill in missing timestamps with the last known price
        df_resampled = df.resample('D').fillna(method='ffill')
        

        # Handle any remaining NaN values after forward fill
        df_resampled['prices'].fillna(method='bfill', inplace=True)

        # Ensure there are no NaN values in the DataFrame
        df_resampled.dropna(subset=['prices'], inplace=True)


        # Extend the last known price to cover the entire year
        last_known_price = df_resampled['prices'].iloc[-1]
        end_of_year = pd.to_datetime(f'2024-01-01')
        
        # Create a new DataFrame for the end of the year with the last known price
        df_end_of_year = pd.DataFrame({'prices': [last_known_price]}, index=[end_of_year])
        
        # Extend the first known price to cover the entire year
        first_known_price = df_resampled['prices'].iloc[0]
        start_of_year = pd.to_datetime(f'2022-11-01')
        
        # Create a new DataFrame for the start of the year with the first known price
        df_start_of_year = pd.DataFrame({'prices': [first_known_price]}, index=[start_of_year])

        # Concatenate the DataFrames to combine the original data and start-of-year data
        df_resampled = pd.concat([df_start_of_year, df_resampled])

        # Concatenate the DataFrames to combine the original data and end-of-year data
        df_resampled = pd.concat([df_resampled, df_end_of_year])

        # Plot the data
        ax.plot(df_resampled.index, df_resampled['prices'], label=store_name)

    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(DateFormatter('%m-%Y'))
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.set_title(f'Price History for {ingredient_name}')
    ax.legend()
    # Rotate x-axis labels vertically
    plt.xticks(rotation='vertical')
    # Add a grid
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

    # Save the plot as an image
    plt.savefig(plot_save_path)
    plt.close()  # Close the plot to free up resources

def ingredient_price_history(request, ingredient_id):
    # Get the ingredient name from the Ingredient table
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT IngredientName FROM Ingredient WHERE IngredientID = %s",
            [ingredient_id]
        )
        ingredient_name = cursor.fetchone()[0]

    # Get the price history for the current ingredient
    price_history = get_price_history(ingredient_id)

    # Define the path to save the Matplotlib plot image
    plot_save_path = f"media/plots/{ingredient_id}_price_history.png"

    # Plot the price history and save the image
    plot_price_history(ingredient_name, price_history, plot_save_path)

    # Pass the image file path to the template
    context = {
        'ingredient_name': ingredient_name,
        'plot_image_path': plot_save_path,
    }

    # Render the template
    return render(request, 'price_history/ingredient_price_history.html', context)

def index(request):
    if request.method == "POST":
        username = request.POST["uname"]
        password = request.POST["psw"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('index')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, mark_safe("Incorrect username or password, please try again.<br>"))
            return redirect('index')
    else:
        return render(request, 'index.html', {})
    
def logout_user(request):
    logout(request)
    return redirect('index')

def accountcreation(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'accountcreation.html', {'form': form})

def store_selection(request):
    if request.method == 'POST':
        selected_store_ids = request.POST.getlist('store_ids')
        user_id = request.user.id
        StoreCollection.objects.filter(UserID=user_id).delete()
        for store_id in selected_store_ids:
            StoreCollection.objects.create(UserID_id=user_id, StoreID_id=store_id)
    
        return redirect('shopping_lists')

    user_id = request.user.id
    selected_stores = StoreCollection.objects.filter(UserID=user_id).values_list('StoreID', flat=True)
    grocery_stores = GroceryStore.objects.filter(StoreId__range=(1, 5))

    return render(request, 'store_selection.html', {'grocery_stores': grocery_stores, 'selected_stores': selected_stores})
    
def get_best_mix(shopping_list):

    stores = GroceryStore.objects.filter(StoreId__range=(1, 5))
    # Dictionary to store the lowest ingredient price for each store
    best_mix_stores = {}
    lowest_prices = {ing.Ingredient_id: float('inf') for ing in shopping_list}
    for ing in shopping_list:
        for store in stores:
            ingredient_price = get_ingredient_prices(ing.Ingredient_id, store.StoreId)
            # Update the lowest price for this store if the new price is lower
            if ingredient_price < lowest_prices[ing.Ingredient_id]:
                lowest_prices[ing.Ingredient_id] = ingredient_price
                best_mix_stores[ing.Ingredient_id] = store.StoreId
    # Find stores with the lowest ingredient price
    #best_mix_stores = [store for store, price in lowest_prices.items() if price != float('inf')]

    return (best_mix_stores)
    
def shopping_lists(request, list_id=None, algorithm=None):
    user_id = AuthUser.objects.get(id=request.user.id)
    total_cost=0.00

    if request.method == "POST":
        shopping_list_name = request.POST.get('shopping_list_name').strip()

        if not shopping_list_name:
            messages.error(request, mark_safe(f"Shopping list name cannot be empty or contain only whitespaces<br>"))
        else:
            ShoppingListNames.objects.create(ListName=shopping_list_name, UserID=user_id)
            messages.success(request, mark_safe(f"New shopping list created with Name: {shopping_list_name}<br>"))

    #get user shopping lists
    UserListID = ShoppingListNames.objects.filter(UserID=user_id)
    
    shopping_list_names = request.session.get('created_list_name', [])
    if list_id != None:
        selected_list=ShoppingListNames.objects.get(ListID=list_id )
        shopping_list_items=ShoppingList.objects.filter(ListID=list_id)
        current_prices=PriceData.objects.none()
        for item in shopping_list_items:
            current_prices|=PriceData.objects.filter(IngredientID=item.Ingredient_id)
        best_store=None
        best_mix_stores=None
        savings_percent=None
        if algorithm == "beststore":
            current_prices=PriceData.objects.none()
            best_store = get_best_store(shopping_list_items)
            for item in shopping_list_items:
                current_prices|=PriceData.objects.filter(IngredientID=item.Ingredient_id, StoreID=best_store.StoreId)
                total_cost+=PriceData.objects.get(IngredientID=item.Ingredient_id, StoreID=best_store.StoreId).CurrentPrice*ShoppingList.objects.get(ListID=list_id, Ingredient_id=item.Ingredient_id).Quantity
        elif algorithm == "bestmix":
            best_mix_stores = get_best_mix(shopping_list_items)
            for ingredient_id, store_id in best_mix_stores.items():
                total_cost+=PriceData.objects.get(IngredientID=ingredient_id, StoreID=store_id).CurrentPrice*ShoppingList.objects.get(ListID=list_id, Ingredient_id=ingredient_id).Quantity

        grocery_stores = GroceryStore.objects.filter(StoreId__range=(1, 5))

        return render(request, 'shopping_lists.html', {'UserListID': UserListID,
        'selected_list_id': list_id, 'session_list': shopping_list_names, 'best_mix_stores': best_mix_stores,
        'selected_list': selected_list, 'shopping_list_items': shopping_list_items, 'total_cost': total_cost,
        'current_prices': current_prices, 'best_store': best_store, 'savings_percent': savings_percent, 'grocery_stores': grocery_stores})

    return render(request, 'shopping_lists.html', {'UserListID': UserListID, 'selected_list_id': list_id, 'session_list': shopping_list_names,})

def price_comparison_options(request):
    if request.method == 'POST':
        #save the checkbox values in a list
        selected_price_options = request.POST.getlist('pricing_options')
        #If more than one price option is selected, error (Please choose one option)
        if len(selected_price_options) > 1:
            messages.error(request, mark_safe("Please choose only one price comparison option.<br><br>"))
            return redirect('price_comparison_options')
        else:
            #check which pricing option it is
            #call another function to get/pass stores and shopping list to correct pricing algorithm 
            #redirect to cost breakdown?
            return redirect('price_comparison_options')
        
    user_id = request.user.id
    user_stores = StoreCollection.objects.filter(UserID=user_id).values('StoreID')
    return render(request, 'price_comparison.html', {'user_stores': user_stores})

def view_selected_stores(request):
    user_id = request.user.id
    user_lists = ShoppingList.objects.filter(shoppinglistcollection__UserID=user_id).values('ListID', 'ListName','Ingredient', 'StoreID','Quantity').distinct()
    user_stores = GroceryStore.objects.filter(storecollection__UserID=user_id).values('StoreName', 'Address').distinct()
    return render(request, 'view_stores.html', {'user_stores': user_stores, 'user_lists': user_lists})

class PriceDataListView(ListView):
    model = PriceData
    template_name = 'price_data_list.html'
    context_object_name = 'price_data_list'

def ingredient_list(request):
    ingredients = Ingredient.objects.all()  # Query all Ingredient objects
    context = {'ingredients': ingredients}
    return render(request, 'ingredient_list.html', context)
    
def current_prices(request):
    # Retrieve PriceData objects along with related GroceryStore and Ingredient
    price_data_list = PriceData.objects.select_related('store', 'ingredient').all()
    context = {'price_data_list': price_data_list}
    return render(request, 'current_prices.html', context)

def price_history_list(request):
    price_history_list = PriceHistory.objects.all()
    context = {'price_history_list': price_history_list}
    return render(request, 'price_history_list.html', context)

def ingredient_search(request):
        
    if request.method == 'POST':
        # Get data from the form
        shopping_list_id = request.POST.get('shoppingList')
        quantity = request.POST.get('quantity')
        ingredient_id = request.POST.get('ingredient_id')
        store_id = request.POST.get('store_id')
        
        grocery_store = GroceryStore.objects.get(StoreId=store_id)
        ingredient = Ingredient.objects.get(IngredientID=ingredient_id)

        # Check if the entry already exists
        if not ShoppingList.objects.filter(
            ListID=shopping_list_id,
            Ingredient=ingredient,
            StoreID=grocery_store,
            Quantity=quantity
            ).exists():
            # If it doesn't exist, create a new entry
            ShoppingList.objects.create(
                ListID=shopping_list_id,
                Ingredient=ingredient,
                StoreID=grocery_store,
                Quantity=quantity
            )
            return redirect('ingredient_search')
        else:
            messages.error(request, mark_safe(f"<br><br>This item already exists in your shopping list.<br><br>"))
            return redirect('ingredient_search')


    # Redirect to a the ingredient search
        #return redirect('ingredient_search')  

    # Retrieve the user id
    user = request.user.id

    # Retrieve shopping lists for the user
    shopping_lists = ShoppingListNames.objects.filter(UserID=user)

    # Retrieve the search variable
    search_query = request.GET.get('search_query', '')

    # Get all the items in the database
    items = PriceData.objects.all()

    # Fetch stores associated with the current user
    user_stores = StoreCollection.objects.filter(UserID=user).values_list('StoreID', flat=True)

    if user_stores:
        # If user has collected stores, filter by stores when there's a search query
        if search_query:
            items = items.filter(
                IngredientID__IngredientName__icontains=search_query,
                StoreID__in=user_stores
            )
        # If the user has collected stores but not searched
        else:
            items = items.filter(StoreID__in=user_stores)
    elif search_query:
        # If no stores collected but there's a search query, filter by search query only
        items = items.filter(IngredientID__IngredientName__icontains=search_query)

    # Fetch the values for the filtered items
    items = items.values(
        'IngredientID',
        'IngredientID__IngredientName',
        'CurrentPrice',
        'StoreID',
        'StoreID__StoreName'
    )
    # Process items to select only one of each name
    unique_items = {}
    for item in items:
        ingredient_name = item['IngredientID__IngredientName']
        if ingredient_name not in unique_items:
            unique_items[ingredient_name] = item

    # Turn it back into a list
    unique_items = list(unique_items.values())

    return render(request, 'ingredient_search.html', {'ingredient_search_query': search_query, 'items': unique_items,'shopping_lists': shopping_lists})
    
def get_current_prices(ingredient_id):
    current_prices = PriceData.objects.filter(IngredientID=ingredient_id)
    return current_prices
    
def ingredient_detail(request, IngredientID):

    # Get the ingredient object or return a 404 error if not found
    ingredient = get_object_or_404(Ingredient, pk=IngredientID)

    # Get the price history for the current ingredient
    price_history = get_price_history(IngredientID)
    
    # Get the current prices for the current ingredient
    current_prices = get_current_prices(IngredientID)
    
    # Define the path to save the Matplotlib plot image
    plot_save_path = f"media/plots/{IngredientID}_price_history.png"

    # Plot the price history and save the image
    plot_price_history(ingredient.IngredientName, price_history, plot_save_path)

    # Pass the image file path to the template
    context = {
        'ingredient': ingredient,
        'current_prices': current_prices,
        'plot_image_path': plot_save_path,
        'media_url': settings.MEDIA_URL, 

    }

    # Render the template
    return render(request, 'ingredient_detail.html', context)

def recipe_search(request):
        user = request.user.id
        shopping_lists = ShoppingListNames.objects.filter(UserID=user)

        if request.method == 'POST':
            recipe_id = request.POST.get('RecipeID')
            shopping_list_id = request.POST.get('shoppingList')
            recipes = Recipe.objects.filter(RecipeID=recipe_id)  # Get all matching recipes

            user_stores = StoreCollection.objects.filter(UserID=user).values_list('StoreID', flat=True)
            # Then iterate through the queryset
            for recipe in recipes:
                ingredient = recipe.Ingredient
                quantity = recipe.Quantity
                    # Assuming you have a way to retrieve/store associations between stores and ingredients
                    # associated_store = Some logic to retrieve the store for this ingredient
            
            #Trying to Solve issue of duplicate entries of the same item
            #  shopping_item = ShoppingList.objects.filter(ListID=shopping_list_id, Ingredient=ingredient).first()
            # if shopping_item:
                #        shopping_item.Quantity += recipe.Quantity
                #           shopping_item.save()
                #else:
                
                # Filter StoreCollection for stores that have this ingredient and are user's stores
                store_with_ingredient = PriceData.objects.filter(StoreID__in=user_stores, IngredientID=ingredient).first()
                if store_with_ingredient:
                    # If a store with the ingredient is found, create a ShoppingList entry
                    ShoppingList.objects.create(
                        ListID=shopping_list_id,
                        Ingredient=ingredient,
                        Quantity=quantity,
                        StoreID=store_with_ingredient.StoreID  
                    )

            return redirect('recipe_search') 
        
        search_query = request.GET.get('search_query', '')
        recipes = []

        if search_query:
                recipes = Recipe.objects.filter(RecipeName__icontains=search_query).values(
                        'RecipeID',
                        'RecipeName'
                )
        distinct_recipes = {}

        for recipe in recipes:
            recipe_id = recipe['RecipeID']
            if recipe_id not in distinct_recipes:
                distinct_recipes[recipe_id] = recipe

            # Use only the distinct recipes
            recipes = list(distinct_recipes.values())

        return render(request, 'recipe_search.html', {'search_query': search_query, 'recipes': recipes,'shopping_lists': shopping_lists})

    
def shopping_list_detail(request, list_id):
    # Retrieve the shopping list items for the given list ID
    shopping_list_items = ShoppingList.objects.filter(ListID=list_id)

    # Pass the data to the template
    return render(request, 'shopping_list_detail.html', {'shopping_list_items': shopping_list_items})

def recipe_detail(request, RecipeID):
        
    recipe_items = Recipe.objects.filter(RecipeID=RecipeID)
        
    # Pass the data to the template
    return render(request, 'recipe_detail.html', {'recipe_items': recipe_items})

@login_required
def track_item(request):
    if request.method == 'POST':
        # Get the ingredient_id from the form data
        ingredient_id = request.POST.get('ingredient_id')

        # Retrieve the currently logged-in user
        user = request.user.id

        # Add the entry to the IngredientCollection table
        IngredientCollection.objects.get_or_create(UserID_id=user, IngredientID_id=ingredient_id)

    # Redirect back to the user_ingredients page
    return redirect('user_ingredients')

@login_required
def untrack_item(request):
    if request.method == 'POST':
        # Get the ingredient_id from the form data
        ingredient_id = request.POST.get('ingredient_id')

        # Retrieve the currently logged-in user
        user = request.user

        # Remove the entry from the IngredientCollection table
        IngredientCollection.objects.filter(UserID=user.id, IngredientID=ingredient_id).delete()

    # Redirect back to the user_ingredients page
    return redirect('user_ingredients')
    
@login_required
def track_recipe(request):
    if request.method == 'POST':
        # Get the recipe_id from the form data
        recipe_id = request.POST.get('recipe_id')

        # Retrieve the currently logged-in user
        user = request.user.id

        # Add the entry to the RecipeCollection table
        RecipeCollection.objects.get_or_create(UserID_id=user, RecipeID_id=recipe_id)

    # Redirect back to the user_recipes page
    return redirect('user_recipes')

@login_required
def untrack_recipe(request):
    if request.method == 'POST':
        # Get the recipe_id from the form data
        recipe_id = request.POST.get('recipe_id')

        # Retrieve the currently logged-in user
        user = request.user

        # Remove the entry from the IngredientCollection table
        RecipeCollection.objects.filter(UserID=user.id, RecipeID=recipe_id).delete()

    # Redirect back to the user_recipes page
    return redirect('user_recipes')
    
def shopping_list_names(request):
    # Replace 'your_user_id' with the actual user ID or retrieve it from the request
    user = request.user 

    # Retrieve shopping lists for the user
    shopping_lists = ShoppingListNames.objects.filter(UserID=user.id)

    return render(request, 'ingredient_search.html', {'shopping_lists': shopping_lists})

def remove_item_from_list(request):
    if request.method == 'POST':
        # Get the form data
        ingredient_id = request.POST.get('ingredient_id')
        list_id = request.POST.get('list_id')


        # Remove the entry from the IngredientCollection table
        ShoppingList.objects.filter(ListID=list_id, Ingredient_id=ingredient_id).delete()

    return redirect(f'/shopping_lists/{list_id}/')

def remove_shopping_list(request):
    if request.method == 'POST':
        # Get the form data
        #ingredient_id = request.POST.get('ingredient_id')
        list_id = request.POST.get('list_id')
        #Items = list(ShoppingList.objects.filter(ListID=list_id))
        #numItems = len(Items)

        ShoppingList.objects.filter(ListID=list_id).delete()
        ShoppingListNames.objects.filter(ListID=list_id).delete()

    return redirect(f'/shopping_lists')
    
def settings_page(request):
    date_user = AuthUser.objects.get(id=request.user.id)
    if request.method == 'POST':
        selecteddate = request.POST.get('selecteddate')
        if selecteddate:
            date_user.selecteddate = selecteddate
            date_user.save()
            return redirect('settings_page') 



    return render(request, 'settings.html', { 'date_user': date_user})
   
