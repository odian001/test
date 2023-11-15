from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import StoreSelectionForm
from django.utils.safestring import mark_safe 
from django.contrib import messages
from doughsaverapp.models import *
from django.urls import reverse

def index(request):
    if request.method == "POST":
        username = request.POST["uname"]
        password = request.POST["psw"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.success(request, mark_safe("Welcome, you have successfully logged in!<br>"))
            return redirect('index') #uses name ='index' from urls.py
        else:
            # Return an 'invalid login' error message.
            messages.success(request, mark_safe("Incorrect username or password, please try again.<br>"))
            return redirect('index')
    else:
        return render(request, 'index.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, mark_safe("You were successfully logged out.<br>"))
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
            messages.success(request, mark_safe("You were successfully registered.<br>"))
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'accountcreation.html', {'form': form})

def store_selection(request):
    if request.method == 'POST':
        form = StoreSelectionForm(request.POST)
        if form.is_valid():
            selection = form.save()
            selection.user = request.user
            selection.save()
            form.save_m2m()
            # Redirect or do something after saving
            return redirect('store_selection')
    else:
        form = StoreSelectionForm()
    
    return render(request, 'store_selection.html', {'form': form})

#def view_selected_stores(request):
    #user_selection = UserStoreSelection.objects.get(user=request.user)
    #selected_stores = user_selection.stores.all()
    #return render(request, 'store_selection.html', {'selected_stores': selected_stores})

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

def item_search(request):
    search_query = request.GET.get('search_query', '')
    items = []

    if search_query:
            items = PriceData.objects.filter(IngredientID__IngredientName__icontains=search_query).values(
            'IngredientID',
            'IngredientID__IngredientName',
            'CurrentPrice',
            'StoreID__StoreName'
            )

    return render(request, 'search.html', {'search_query': search_query, 'items': items})
    
def ingredient_detail(request, IngredientID):
    ingredient = get_object_or_404(Ingredient, pk=IngredientID)
    return render(request, 'ingredient_detail.html', {'ingredient': ingredient})