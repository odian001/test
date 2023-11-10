from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils.safestring import mark_safe 
from django.contrib import messages
from .forms import StoreSelectionForm
from doughsaverapp.models import *


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
    template = loader.get_template('accountcreation.html')
    return HttpResponse(template.render())

#def store_selection(request):
    if request.method == 'POST':
        form = StoreSelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.save()
            form.save_m2m()
            # Redirect or do something after saving
            return redirect('view_selected_stores')
    else:
        form = StoreSelectionForm()
    
    return render(request, 'store_selection.html', {'form': form}) 
    
#def view_selected_stores(request):
    user_selection = UserStoreSelection.objects.get(user=request.user)
    selected_stores = user_selection.stores.all()
    return render(request, 'store_selection.html', {'selected_stores': selected_stores})

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