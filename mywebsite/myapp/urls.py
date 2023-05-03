from django.urls import path
from .views import Homepage, About, Contact

urlpatterns = [
    path("", Homepage, name='home'),
    path('about', About, name='about'),
    path('contact', Contact, name='contact')
]