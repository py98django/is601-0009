

from django.urls import path
from .views import  AboutView, HomeView ,  PropertyListView, PropertyDetailView , PropertyCreateView, add_listing



app_name = "listing"


urlpatterns = [

    # path('', views.Home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('listings/', PropertyListView.as_view(), name='listings'),
    path('listing/<int:id>/', PropertyDetailView.as_view(), name='listing-detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('add-listing/', add_listing, name='add-listing'), 
]
