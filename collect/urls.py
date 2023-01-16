from django.urls import path
from collect import views

app_name = 'collect'

urlpatterns = [
    path('candle', views.candle),
]