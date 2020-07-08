from django.urls import path

urlpatterns = [

    path('', include('weather.urls')),

]