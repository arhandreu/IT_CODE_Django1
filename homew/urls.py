from django.urls import path
from homew.views import HomePage, DetailCategory, SearchMagazine, About

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('category/<int:pk>/', DetailCategory.as_view(), name='category'),
    path('magazine/', SearchMagazine.as_view(), name='magazine'),
    path('about/', About.as_view(), name='about'),
]
