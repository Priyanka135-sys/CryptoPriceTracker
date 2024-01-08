# tracker/urls.py
from django.urls import path
from Cryptoapp import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    
    path('chart/<str:symbol>/', views.get_chart_data, name='get_chart_data'),
    path('storedata/<str:symbol>/', views.store_the_data, name='store_data'),
    path('register/',views.register_users,name='register'),
    path('logout/',views.logout_users,name='logout'),
    path('viewdata/',views.display_cryptocurrencies,name='display_data'),
    
    
]
