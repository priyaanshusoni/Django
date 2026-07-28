from django.urls import path
from views import Home


urlpatterns = [
  
    path('', Home, name='Home'),        # root path
    path('app1/', Home, name='Home'),   # /app1/ path
]