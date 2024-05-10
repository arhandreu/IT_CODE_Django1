from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse
from .models import Furniture, Category


def index(request):
    list_furniture = Furniture.objects.all()
    list_categories = Category.objects.annotate(num_furniture=Count('furniture'))
    context = {"furniture": list_furniture,
               "title": "Список мебели",
               "categories": list_categories, }

    return render(request, "homew/index.html", context)


def get_category(request, pk):
    list_furniture = Furniture.objects.filter(category=pk)
    list_categories = Category.objects.annotate(num_furniture=Count('furniture'))
    category = Category.objects.get(pk=pk)
    context = {"furniture": list_furniture,
               "title": "Список мебели",
               "categories": list_categories,
               "category": category, }

    return render(request, "homew/category.html", context)
