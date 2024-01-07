from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Cryptocurrency
from pycoingecko import CoinGeckoAPI
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Cryptoapp.form import SignUpForm
import logging
from django.http import HttpResponse



def home(request):
    unique_symbols = Cryptocurrency.objects.values('symbol').distinct()



    #checking to see if the user is logging in
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        #Authenticate

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in ")
            return redirect('home')
        else:
            messages.success(request,"There was an error while logging in! Please try again!")
            return redirect('home')
    else:
        
    
    # Fetch the latest data for each unique symbol
        cryptocurrencies = []
        for symbol in unique_symbols:
            latest_crypto = Cryptocurrency.objects.filter(symbol=symbol['symbol']).order_by('-timestamp').first()
            if latest_crypto:
                cryptocurrencies.append(latest_crypto)

        return render(request, 'home.html', {'cryptocurrencies': cryptocurrencies})

    
    
def register_users(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have successfully registered here!")
            return redirect('home')
        
    else: 
        form=SignUpForm() 
        return render(request,'register.html' ,{'form':form})
    return render(request,'register.html' ,{'form':form})    


def get_cryptocurrency_data():
    cg = CoinGeckoAPI()
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': False,
    }
    response = cg.get_coins_markets(**params)  
    data = response.json()
    return data



def display_cryptocurrencies(request):
    
    unique_symbols = Cryptocurrency.objects.values('symbol').distinct()

    # Fetch the latest data for each unique symbol
    cryptocurrencies = []
    for symbol in unique_symbols:
        latest_crypto = Cryptocurrency.objects.filter(symbol=symbol['symbol']).order_by('-timestamp').first()
        if latest_crypto:
            cryptocurrencies.append(latest_crypto)

    return render(request, 'cryptoprice.html', {'cryptocurrencies': cryptocurrencies})





from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cryptocurrency

def store_the_data(request, symbol):
    if request.method == 'POST':
        latest_crypto = Cryptocurrency.objects.filter(symbol=symbol).order_by('-timestamp').first()

        if latest_crypto:
            latest_crypto.save()
            messages.success(request, "Saved successfully")
        else:
            messages.warning(request, "No data available for the specified symbol")
        
        return redirect('home')  # Replace 'your_redirect_url' with the actual URL you want to redirect to

    return render(request, 'store_data.html', {'symbol': symbol})


    
def get_historical_data(symbol):
    symbol = symbol.strip().lower()
    cg = CoinGeckoAPI()
    ohlc = cg.get_coin_ohlc_by_id(id = symbol, vs_currency ="usd", days = "1")
    print (ohlc) 
    return ohlc



def get_chart_data(request, symbol):
    try:
         
        data = get_historical_data(symbol)
        return JsonResponse({"data": data})
    except Exception as e:
        logging.error(f"Error in get_chart_data: {str(e)}")
        return JsonResponse({"error": "Internal Server Error"}, status=500)



def logout_users(request):
    logout(request)
    messages.success(request,"You have logged out..")
    return redirect('home')
        