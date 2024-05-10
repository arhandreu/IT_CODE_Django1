from django.urls import path
from homew.views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:pk>/', get_category, name='category'),
]