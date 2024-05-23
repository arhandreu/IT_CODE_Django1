from django.urls import path
from homew.views import (HomePage, DetailCategory, SearchMagazine,
                         About, ClientAPIView, ClientModelView)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('clientMV', ClientModelView, basename='clientMV')

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('category/<int:pk>/', DetailCategory.as_view(), name='category'),
    path('magazine/', SearchMagazine.as_view(), name='magazine'),
    path('about/', About.as_view(), name='about'),
    path('clientAV/', ClientAPIView.as_view(), name='clientAV')
]

urlpatterns += router.urls
