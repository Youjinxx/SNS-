from django.urls import URLPattern, path
from .views import *

app_name = "accounts"

urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    
]