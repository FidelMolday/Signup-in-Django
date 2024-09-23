from django.urls import path,include
from .views import authView,home

urlpatterns = [
 path('',home, name='home'),   
 path('signup/',authView, name='authview'),   
 path("account/", include("django.contrib.auth.urls")),
]
