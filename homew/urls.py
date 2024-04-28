from django.urls import path
from homew.views import date_now

urlpatterns = [
    path('', date_now),
]